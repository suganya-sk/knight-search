
class KnightSearch:

    def __init__(self, goal, board):
        self.goal = goal
        self.board = board
        self.found_goal = False
        self._so_far = ''


    def _search_from(self, r_index, c_index):
        return None


    def start(self):
        while not self.found_goal:
            for r_index, row in enumerate(self.board):
                for c_index, item in enumerate(row):
                    if item == self.goal[0]:
                        self._so_far = self.goal[0]
                        path = self._search_from(r_index, c_index)
                        if path:
                            print('Found path - %s', str(path))
                            self.found_goal = True

############################################################################

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
