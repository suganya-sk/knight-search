import logging
logging.basicConfig(level=logging.DEBUG)

class KnightSearch:

    def __init__(self, goal, board):
        self.goal = goal
        self.board = board
        self.found_goal = False
        self._so_far = ''


    def _inside_board(self, r_index, c_index):
        return 0 <= r_index < len(self.board) and 0 <= c_index < len(self.board[0])


    def _search_from(self, r_index, c_index, so_far):
        # have we reached the goal with this move?
        item = self.board[r_index][c_index]
        cur_str = so_far + item
        logging.debug(cur_str)
        if self.goal.startswith(cur_str):
            print("Current string is - " + cur_str)
        else:
            return False
        if cur_str == self.goal:
            print("&&&&&&&&&&&&&&&&&&&&&&&&& Puzzles &&&&&&&&&&&&&&&&&&&&")
            return True

        i = r_index
        j = c_index

        # explore cell above
        i = r_index - 1
        if self._inside_board(i, j):
            # move 2 steps right
            j = c_index + 2
            if self._inside_board(i, j):
                if self._search_from(i, j, cur_str):
                    return True
            # move 2 steps left
            j = c_index - 2
            if self._inside_board(i, j):
                if self._search_from(i, j, cur_str):
                    return True
            # tmp_str = so_far + self.board[i][j]
            # if self.goal.startswith(tmp_str):
            #     return self._search_from(i, j, tmp_str)
            i -= 1
            if self._inside_board(i, j):
                # move 1 step right
                j = c_index + 1
                if self._inside_board(i, j):
                    if self._search_from(i, j, cur_str):
                        return True
                # tmp_str = so_far + self.board[i][j]
                # if self.goal.startswith(tmp_str):
                #     return self._search_from(i, j, tmp_str)
                # move 1 step left
                j = c_index - 1
                if self._inside_board(i, j):
                    if self._search_from(i, j, cur_str):
                        return True
                # tmp_str = so_far + self.board[i][j]
                # if self.goal.startswith(tmp_str):
                #     return self._search_from(i, j, tmp_str)

        # explore cell below
        i = r_index + 1
        if self._inside_board(i, j):
            # move 2 steps right
            j = c_index + 2
            if self._inside_board(i, j):
                if self._search_from(i, j, cur_str):
                    return True
            # tmp_str = so_far + self.board[i][j]
            # if self.goal.startswith(tmp_str):
            #     return self._search_from(i, j, tmp_str)
            # move 2 steps left
            j = c_index - 2
            if self._inside_board(i, j):
                if self._search_from(i, j, cur_str):
                    return True
            # tmp_str = so_far + self.board[i][j]
            # if self.goal.startswith(tmp_str):
            #     return self._search_from(i, j, tmp_str)
            i += 1
            if self._inside_board(i, j):
                # move 1 step right
                j = c_index + 1
                if self._inside_board(i, j):
                    if self._search_from(i, j, cur_str):
                        return True
                # tmp_str = so_far + self.board[i][j]
                # if self.goal.startswith(tmp_str):
                #     return self._search_from(i, j, tmp_str)
                # move 1 step left
                j = c_index - 1
                if self._inside_board(i, j):
                    if self._search_from(i, j, cur_str):
                        return True
                # tmp_str = so_far + self.board[i][j]
                # if self.goal.startswith(tmp_str):
                #     return self._search_from(i, j, tmp_str)

        i = r_index

        # explore cell to the left
        j = c_index - 1
        if self._inside_board(i, j):
            # move 2 steps above
            i = r_index - 2
            if self._inside_board(i, j):
                if self._search_from(i, j, cur_str):
                    return True
            # tmp_str = so_far + self.board[i][j]
            # if self.goal.startswith(tmp_str):
            #     return self._search_from(i, j, tmp_str)
            # move 2 steps below
            i = r_index + 2
            if self._inside_board(i, j):
                if self._search_from(i, j, cur_str):
                    return True
            # tmp_str = so_far + self.board[i][j]
            # if self.goal.startswith(tmp_str):
            #     return self._search_from(i, j, tmp_str)
            j -= 1
            if self._inside_board(i, j):
                # move 1 step right
                j = c_index + 1
                if self._inside_board(i, j):
                    if self._search_from(i, j, cur_str):
                        return True
                # tmp_str = so_far + self.board[i][j]
                # if self.goal.startswith(tmp_str):
                #     return self._search_from(i, j, tmp_str)
                # move 1 step left
                j = c_index - 1
                if self._inside_board(i, j):
                    if self._search_from(i, j, cur_str):
                        return True
                # tmp_str = so_far + self.board[i][j]
                # if self.goal.startswith(tmp_str):
                #     return self._search_from(i, j, tmp_str)

        # explore cell to the right
        j = c_index + 1
        if self._inside_board(i, j):
            # move 2 steps above
            i = r_index - 2
            if self._inside_board(i, j):
                if self._search_from(i, j, cur_str):
                    return True
            # tmp_str = so_far + self.board[i][j]
            # if self.goal.startswith(tmp_str):
            #     return self._search_from(i, j, tmp_str)
            # move 2 steps below
            i = r_index + 2
            if self._inside_board(i, j):
                if self._search_from(i, j, cur_str):
                    return True
            # tmp_str = so_far + self.board[i][j]
            # if self.goal.startswith(tmp_str):
            #     return self._search_from(i, j, tmp_str)
            j += 1
            if self._inside_board(i, j):
                # move 1 step right
                j = c_index + 1
                if self._inside_board(i, j):
                    if self._search_from(i, j, cur_str):
                        return True
                # tmp_str = so_far + self.board[i][j]
                # if self.goal.startswith(tmp_str):
                #     return self._search_from(i, j, tmp_str)
                # move 1 step left
                j = c_index - 1
                if self._inside_board(i, j):
                    if self._search_from(i, j, cur_str):
                        return True
                # tmp_str = so_far + self.board[i][j]
                # if self.goal.startswith(tmp_str):
                #     return self._search_from(i, j, tmp_str)

        return False


    def start(self):
        logging.debug("Starting")
        # while not self.found_goal:
        for r_index, row in enumerate(self.board):
            for c_index, item in enumerate(row):
                if self.found_goal:
                    break
                if item == self.goal[0]:
                    logging.debug("Found a 'p' at - " + str(r_index) + ", " + str(c_index))
                    path = self._search_from(r_index, c_index, self._so_far)
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
