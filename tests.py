game1 = zuma.create_zuma_game((200, [1, 2, 1, 2, 1, 2, 1, 2], example, debug_mode))
game2 = zuma.create_zuma_game((200, [3, 3, 3, 3, 3, 4, 4, 4, 4, 4], example, debug_mode))
game3 = zuma.create_zuma_game((200, [1, 4, 2, 3, 4, 1, 3, 2, 4, 1], example, debug_mode))
game4 = zuma.create_zuma_game((200, [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], example, debug_mode))
game5 = zuma.create_zuma_game((200, [1, 4, 4, 2, 2, 3, 3, 1, 1, 4, 4, 2, 2, 3, 3], example, debug_mode))
game6 = zuma.create_zuma_game((30, [1, 2, 1, 2, 3], example, debug_mode))
game7 = zuma.create_zuma_game((30, [4, 3, 4, 3, 4], example, debug_mode))
game8 = zuma.create_zuma_game((30, [2, 2, 3, 3, 4], example, debug_mode))
game9 = zuma.create_zuma_game((30, [1, 1, 1, 2, 2], example, debug_mode))
game10 = zuma.create_zuma_game((30, [4, 1, 4, 1, 3], example, debug_mode))
game11 = zuma.create_zuma_game((54, [1, 4, 1, 4, 2], example, debug_mode))
game12 = zuma.create_zuma_game((54, [2, 3, 2, 3, 4], example, debug_mode))
game13 = zuma.create_zuma_game((54, [3, 3, 2, 2, 1], example, debug_mode))
game14 = zuma.create_zuma_game((54, [1, 2, 3, 1, 2], example, debug_mode))
game15 = zuma.create_zuma_game((54, [4, 4, 4, 3, 2], example, debug_mode))
game16 = zuma.create_zuma_game((54, [3, 4, 2, 4, 3], example, debug_mode))
game17 = zuma.create_zuma_game((54, [1, 2, 4, 1, 3], example, debug_mode))
game18 = zuma.create_zuma_game((54, [2, 2, 1, 3, 1], example, debug_mode))
game19 = zuma.create_zuma_game((54, [3, 1, 3, 4, 2], example, debug_mode))
game20 = zuma.create_zuma_game((54, [4, 1, 2, 4, 3], example, debug_mode))



# Game1 Average result: 100.38095238095238
# Game2 Average result: 107.80952380952381
# Game3 Average result: 116.28571428571429
# Game4 Average result: 112.21428571428571
# Game5 Average result: 106.73809523809524
# Game6 Average result: 10.357142857142858
# Game7 Average result: -5.095238095238095
# Game8 Average result: -2.9761904761904763
# Game9 Average result: 5.166666666666667
# Game10 Average result: -10.071428571428571
# Game11 Average result: 12.476190476190476
# Game12 Average result: 13.904761904761905
# Game13 Average result: 16.666666666666668
# Game14 Average result: 13.119047619047619
# Game15 Average result: 12.642857142857142
# Game16 Average result: 15.333333333333334
# Game17 Average result: 19.642857142857142
# Game18 Average result: 13.595238095238095
# Game19 Average result: 17.738095238095237
# Game20 Average result: 13.19047619047619


example['chosen_action_prob'] = {1: 0.6, 2: 0.1, 3: 0.5, 4: 0.9}
game21 = zuma.create_zuma_game((1, [2, 2, 2, 2, 2, 2], example, debug_mode))

example['next_color_dist'] = {1: 0.0, 2: 0.9, 3: 0.1, 4: 0.0}
game22 = zuma.create_zuma_game((1, [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3], example, debug_mode))

example['chosen_action_prob'] = {1: 0.6, 2: 0.0, 3: 1.0, 4: 0.9}
game23 = zuma.create_zuma_game((1, [2, 2, 2, 2, 2, 2, 1, 1, 1], example, debug_mode))