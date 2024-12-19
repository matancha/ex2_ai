import random
def create_example(seed=42):
    example_dict = {
        'chosen_action_prob': dict(),
        'next_color_dist': dict(),
        'color_pop_prob': dict(),
        'color_pop_reward': {'3_pop': dict(),
                             'extra_pop': dict()},
        'color_not_finished_punishment': dict(),
        'finished_reward': 150,
        'seed': 42}
    random.seed(seed)
    steps = random.randint(1, 200)
    line = random.choices(range(1, 5), k=random.randint(5, 50))
    for k in ['chosen_action_prob', 'color_pop_prob']:
        for c in range(1, 5):
            example_dict[k][c] = random.random()
    prob_sum = 1
    for c in range(1, 4):
        r_num = random.uniform(0, prob_sum)
        example_dict['next_color_dist'][c] = r_num
        prob_sum -= r_num
    example_dict['next_color_dist'][4] = prob_sum
    for c in range(1, 5):
        example_dict['color_pop_reward']['3_pop'][c] = random.randint(0, 10)
        example_dict['color_pop_reward']['extra_pop'][c] = random.randint(0, 10)
        example_dict['color_not_finished_punishment'][c] = random.randint(0, 10)
    example_dict['finished_reward'] = random.randint(50, 300)
    example_dict['seed'] = seed
    return [steps, line, example_dict]
