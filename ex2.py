import zuma
import copy
import random
import re

ids = ["313591935"]

V_table = {}


class Controller:
    """This class is a controller for a Zuma game."""

    def __init__(self, game: zuma.Game):
        """Initialize controller for given game model.
        This method MUST terminate within the specified timeout.
        """
        self.original_game = game
        self.copy_game = copy.deepcopy(game)

    @staticmethod
    def _remove_group(model, line, ball, reward=0):
        """
        removes groups of balls according to their pop probability.
        :param line: list (sequence of balls to check for pops)
        :param ball: scalar (index of ball insertion)
        :param reward: scalar (reward of current insertion)
        :return: list (updated sequence of balls), scalar (reward of insertion)
        """
        burstable = re.finditer(r'1{3,}|2{3,}|3{3,}|4{3,}', ''.join([str(i) for i in line]))
        new_reward = reward
        new_line = line.copy()
        for group in burstable:
            if ball in range(group.span()[0], group.span()[1]):
                new_reward += model['color_pop_prob'][line[group.start()]] * (model['color_pop_reward']['3_pop'][line[group.start()]] +
                                (group.span()[1] - group.span()[0] - 3) *
                                model['color_pop_reward']['extra_pop'][line[group.start()]]) \
                              - (1-model['color_pop_prob'][line[group.start()]]) * model['color_not_finished_punishment'][line[group.start()]]
                new_line = line[:group.span()[0]] + line[group.span()[1]:]
                break
        if new_reward != reward:
            new_line, new_reward = Controller._remove_group(model, new_line, ball, new_reward)
        return new_line, new_reward

    @staticmethod
    def _finished_game(model, line):
        reward = 0.
        if len(line) == 0:
            reward += model['finished_reward']
        else:
            for k, v in model['color_not_finished_punishment'].items():
                num_of_ball = line.count(k)
                reward -= num_of_ball * v

        return reward

    def get_expected_reward(self, model, line, ball, action, steps_left):
        # self.copy_game.submit_next_action(action)
        # reward = self.copy_game.get_current_reward()
        # print(f'reward {reward}, line {self.copy_game.get_current_state()[0]}')
        # line = self.copy_game.get_current_state()[0]
        line = line.copy()
        if action != -1:
            line.insert(action, ball)
        line, pop_reward = self._remove_group(model, line, ball)
        return self._finished_game(model, line) + pop_reward

        # self.copy_game = copy.deepcopy(self.original_game)
        # return reward


    def choose_next_action(self):
        """Choose next action for Zuma given the current state of the game.
        """
        # find out what Q(s,a) brings us the greatest expected value

        # start with thinking that:
        # 1. popping is deterministic
        # 2. next ball is uniformly chosen
        # 3. don't know how many rounds until stop

        # need to:
        # 1. detect popping behavior
        # 2. because the model is known can choose the optimal action always using the Bellman equation
        model = self.original_game.get_model()
        chosen_action_prob = model['chosen_action_prob']
        next_color_dist = model['next_color_dist']
        color_pop_reward = model['next_color_dist'] # 3_pop extra_pop
        # color_not_finished_punishment = model['color_not_finished_punishment']
        # finished_reward = model['finished_reward']

        state = self.original_game.get_current_state()
        line = state[0]
        ball = state[1]
        step = state[2]
        max_steps = state[3]

        # TODO: should decide between skipping or adding for pop possibilities
        rewards = [self.get_expected_reward(model, line, ball, a, max_steps - step) for a in range(-1, len(line) + 1)]
        weighted_rewards = [chosen_action_prob[ball] * rewards[i] + (1-chosen_action_prob[ball]) * (1 / (len(rewards)-1)) * sum(rewards[:i] + rewards[i+1:]) for i, r in enumerate(rewards)]
        print(f'step {step}, ball: {ball}, rewards: {[f"{num:.2f}" for num in weighted_rewards]} picked: {weighted_rewards.index(max(weighted_rewards))-1}')
        return weighted_rewards.index(max(weighted_rewards))-1
        # return len(rewards) - list(reversed(rewards)).index(max(rewards)) - 1
        # return random.choice([i for i in range(-1, len(self.original_game.get_current_state()[0]) + 1)])
