import zuma
import ex2
import random
import numpy as np
import pandas as pd
import copy

examples = [
    {
        'chosen_action_prob': {1: 0.6, 2: 0.7, 3: 0.5, 4: 0.9},
        'next_color_dist': {1: 0.25, 2: 0.25, 3: 0.25, 4: 0.25},
        'color_pop_prob': {1: 0.6, 2: 0.7, 3: 0.4, 4: 0.9},
        'color_pop_reward': {'3_pop': {1: 3, 2: 1, 3: 2, 4: 2},
                             'extra_pop': {1: 1, 2: 2, 3: 3, 4: 1}},
        'color_not_finished_punishment': {1: 2, 2: 3, 3: 5, 4: 1},
        'finished_reward': 100,
    },

    {
        'chosen_action_prob': {1: 0.6, 2: 0.7, 3: 0.5, 4: 0.9},
        'next_color_dist': {1: 0.1, 2: 0.6, 3: 0.15, 4: 0.15},
        'color_pop_prob': {1: 0.6, 2: 0.7, 3: 0.4, 4: 0.9},
        'color_pop_reward': {'3_pop': {1: 3, 2: 1, 3: 2, 4: 2},
                             'extra_pop': {1: 1, 2: 2, 3: 3, 4: 1}},
        'color_not_finished_punishment': {1: 2, 2: 3, 3: 5, 4: 1},
        'finished_reward': 150,
    },

    {
        'chosen_action_prob': {1: 1, 2: 1, 3: 1, 4: 1},
        'next_color_dist': {1: 0.2, 2: 0.2, 3: 0.5, 4: 0.1},
        'color_pop_prob': {1: 0.6, 2: 0.7, 3: 0.4, 4: 0.9},
        'color_pop_reward': {'3_pop': {1: 3, 2: 1, 3: 2, 4: 2},
                             'extra_pop': {1: 1, 2: 2, 3: 3, 4: 1}},
        'color_not_finished_punishment': {1: 2, 2: 3, 3: 5, 4: 1},
        'finished_reward': 50,
    },

    {
        'chosen_action_prob': {1: 0.6, 2: 0.7, 3: 0.5, 4: 0.9},
        'next_color_dist': {1: 0.1, 2: 0.6, 3: 0.15, 4: 0.15},
        'color_pop_prob': {1: 0.6, 2: 0.7, 3: 0.4, 4: 0.9},
        'color_pop_reward': {'3_pop': {1: 2, 2: 3, 3: 9, 4: 7},
                             'extra_pop': {1: 1, 2: 2, 3: 3, 4: 1}},
        'color_not_finished_punishment': {1: 2, 2: 3, 3: 5, 4: 1},
        'finished_reward': 120,
    },

    {
        'chosen_action_prob': {1: 0.5, 2: 0.7, 3: 0.1, 4: 0.9},
        'next_color_dist': {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4},
        'color_pop_prob': {1: 0.6, 2: 0.9, 3: 0.5, 4: 0.9},
        'color_pop_reward': {'3_pop': {1: 2, 2: 3, 3: 9, 4: 7},
                             'extra_pop': {1: 1, 2: 2, 3: 3, 4: 1}},
        'color_not_finished_punishment': {1: 3, 2: 5, 3: 2, 4: 1},
        'finished_reward': 300,
    },
]

seeds = [42, 123, 789, 1001, 33, 4, 55, 76, 88, 5, 66, 70]

num_of_steps = [50, 100, 200]


initial_lines = [
[1, 2, 3, 3, 3, 4, 2, 1, 2, 3, 4, 4],
[1,2,4],
[2, 2, 2, 3, 3, 3],
[2, 2, 2, 2, 3, 3, 3, 3, 3, 1,1],
[4, 4, 4, 4],
[3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3],
[1, 2, 3, 3, 3, 4, 2, 1, 2, 3, 4, 4, 1, 2, 3, 3, 3, 4, 2, 1, 2, 3, 4, 4],
[1, 1, 2, 2, 3, 3, 4,4,4,4,3, 3, 2, 2, 1, 1]]


def run_tests():
    num_runs = len(seeds)
    results = []
    for initial_line in initial_lines:
        for example_num, example_original in enumerate(examples):
            for steps in num_of_steps:
                rewards = []
                for seed in seeds:
                    example = copy.deepcopy(example_original)
                    example['seed'] = seed
                    game = zuma.create_zuma_game((steps, initial_line.copy(), example, False))
                    policy = ex2.Controller(game)
                    for _ in range(game.get_current_state()[3]):
                        game.submit_next_action(policy.choose_next_action())
                    rewards.append(game.get_current_reward())

                avg_reward = np.mean(rewards)
                max_reward = np.max(rewards)
                results.append({
                    'initial_line': str(initial_line),
                    'example': example_num + 1,
                    'steps': steps,
                    'avg_reward': avg_reward,
                    'max_reward': max_reward
                })
    return pd.DataFrame(results)

results_df = run_tests()

print(results_df)

results_df.to_csv("zuma_results.csv", index=False)
