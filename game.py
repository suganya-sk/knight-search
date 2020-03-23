from knight_search import KnightSearch

board = [['u', 'l', 'e', 'z', 'z', 'p', 'e'],
         ['p', 'l', 'u', 's', 'z', 'u', 'z'],
         ['z', 'p', 'u', 'l', 'l', 'z', 'p'],
         ['p', 'u', 's', 'u', 'p', 'e', 'e'],
         ['u', 'e', 'u', 'u', 'l', 'u', 's'],
         ['z', 'p', 'l', 'p', 's', 'p', 'u'],
         ['s', 'p', 'z', 's', 'z', 'e', 'z']
         ]
goal = 'puzzles'
game = KnightSearch(goal, board)
game.start()
