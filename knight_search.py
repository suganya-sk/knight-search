import logging
logging.basicConfig(level=logging.CRITICAL)

class KnightSearch:
    """
    A search in which the neighbour of a cell is reached only through moves of a knight in a chess board.
    A knight moves in the shape of an L, two squares one way, one square the other.
    """

    def __init__(self, goal, board):
        self.goal = goal
        self.board = board
        self.found_goal = False
        self._so_far = ''


    def _inside_board(self, r_index, c_index):
        """
        Checks if the cell with the position passed is inside the board
        :param r_index: row index of cell
        :param c_index: column index of cell
        :return: bool
        """
        return 0 <= r_index < len(self.board) and 0 <= c_index < len(self.board[0])


    def _search_from(self, r_index, c_index, so_far):
        """
        Searches for a path to goal from the position passed
        :param r_index: row index of cell
        :param c_index: column index of cell
        :param so_far: part of goal traced so far
        :return: path reaching goal from cell passed; returns an empty list if no such path exists
        """
        path = []
        # have we reached the goal with this move?
        item = self.board[r_index][c_index]
        cur_str = so_far + item
        logging.debug(cur_str)
        if self.goal.startswith(cur_str):
            path.append([r_index, c_index])
        else:
            return path
        if cur_str == self.goal:
            self.found_goal = True
            return path

        i = r_index
        j = c_index

        # explore cell above
        logging.debug(' exploring cell above..')
        i = r_index - 1
        if self._inside_board(i, j):
            # move 2 steps right
            j = c_index + 2
            if self._inside_board(i, j):
                res = self._search_from(i, j, cur_str)
                if res:
                    path.extend(res)
                    return path
            # move 2 steps left
            j = c_index - 2
            if self._inside_board(i, j):
                res = self._search_from(i, j, cur_str)
                if res:
                    path.extend(res)
                    return path
            i -= 1
            j = c_index
            if self._inside_board(i, j):
                # move 1 step right
                j = c_index + 1
                if self._inside_board(i, j):
                    res = self._search_from(i, j, cur_str)
                    if res:
                        path.extend(res)
                        return path
                # move 1 step left
                j = c_index - 1
                if self._inside_board(i, j):
                    res = self._search_from(i, j, cur_str)
                    if res:
                        path.extend(res)
                        return path

        # explore cell below
        logging.debug(' exploring cell below..')
        i = r_index + 1
        if self._inside_board(i, j):
            # move 2 steps right
            j = c_index + 2
            if self._inside_board(i, j):
                res = self._search_from(i, j, cur_str)
                if res:
                    path.extend(res)
                    return path
            # move 2 steps left
            j = c_index - 2
            if self._inside_board(i, j):
                res = self._search_from(i, j, cur_str)
                if res:
                    path.extend(res)
                    return path
            i += 1
            j = c_index
            if self._inside_board(i, j):
                # move 1 step right
                j = c_index + 1
                if self._inside_board(i, j):
                    res = self._search_from(i, j, cur_str)
                    if res:
                        path.extend(res)
                        return path
                # move 1 step left
                j = c_index - 1
                if self._inside_board(i, j):
                    res = self._search_from(i, j, cur_str)
                    if res:
                        path.extend(res)
                        return path

        i = r_index

        # explore cell to the left
        logging.debug(' exploring cell to the left..')
        j = c_index - 1
        if self._inside_board(i, j):
            # move 2 steps above
            i = r_index - 2
            if self._inside_board(i, j):
                res = self._search_from(i, j, cur_str)
                if res:
                    path.extend(res)
                    return path
            # move 2 steps below
            i = r_index + 2
            if self._inside_board(i, j):
                res = self._search_from(i, j, cur_str)
                if res:
                    path.extend(res)
                    return path
            i = r_index
            j -= 1
            if self._inside_board(i, j):
                # move 1 step above
                i = r_index - 1
                if self._inside_board(i, j):
                    res = self._search_from(i, j, cur_str)
                    if res:
                        path.extend(res)
                        return path
                # move 1 step below
                i = r_index + 1
                if self._inside_board(i, j):
                    res = self._search_from(i, j, cur_str)
                    if res:
                        path.extend(res)
                        return path

        # explore cell to the right
        logging.debug(' exploring cell to the right..')
        j = c_index + 1
        if self._inside_board(i, j):
            # move 2 steps above
            i = r_index - 2
            if self._inside_board(i, j):
                res = self._search_from(i, j, cur_str)
                if res:
                    path.extend(res)
                    return path
            # move 2 steps below
            i = r_index + 2
            if self._inside_board(i, j):
                res = self._search_from(i, j, cur_str)
                if res:
                    path.extend(res)
                    return path
            i = r_index
            j += 1
            if self._inside_board(i, j):
                # move 1 step above
                i = r_index - 1
                if self._inside_board(i, j):
                    res = self._search_from(i, j, cur_str)
                    if res:
                        path.extend(res)
                        return path
                # move 1 step below
                i = r_index + 1
                if self._inside_board(i, j):
                    res = self._search_from(i, j, cur_str)
                    if res:
                        path.extend(res)
                        return path
        return []


    def start(self):
        """
        Start search for goal in board using Knight search
        :return:
        """
        logging.debug("Starting")
        path = []
        for r_index, row in enumerate(self.board):
            for c_index, item in enumerate(row):
                if item == self.goal[0]:
                    logging.debug("Found a 'p' at - " + str(r_index) + ", " + str(c_index))
                    path = self._search_from(r_index, c_index, self._so_far)
                    if self.found_goal:
                        print('Found path - ', str(path))
                        return
