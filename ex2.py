import zuma
import copy
import random

id = ["313591935"]

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
    def _finished_game(model, line):
        """
        Rewards or punishes for any leftovers in the line
        """
        reward = 0
        if len(line) == 0:
            reward += model['finished_reward']
        else:
            for k, v in model['color_not_finished_punishment'].items():
                num_of_ball = line.count(k)
                reward -= num_of_ball * v

        return reward

    def get_expected_reward(self, model, ball, action, steps_left):
        self.copy_game.submit_next_action(action)
        if steps_left - 1 == 0:
            line = self.copy_game.get_current_state()[0]
            return self._finished_game(model, line)


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
        color_not_finished_punishment = model['color_not_finished_punishment']
        finished_reward = model['finished_reward']

        state = self.original_game.get_current_state()
        line = state[0]
        ball = state[1]
        step = state[2]
        max_steps = state[3]

        rewards = [self.get_expected_reward(model, ball, a, max_steps - step) for a in range(-1, len(line) + 1)]
        print(rewards)
        return rewards.index(max(rewards)) - 1
        # return random.choice([i for i in range(-1, len(self.original_game.get_current_state()[0]) + 1)])
