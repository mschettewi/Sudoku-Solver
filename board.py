from copy import deepcopy


class Board:
    def __init__(self, entries):
        self.board = entries

    # ================================
    # ||5 |3 |  ||  |7 |  ||  |  |  ||
    # ||6 |  |  ||1 |9 |5 ||  |  |  ||
    # ||  |9 |8 ||  |  |  ||  |6 |  ||
    # ================================
    # ||8 |  |  ||  |6 |  ||  |  |3 ||
    # ||4 |  |  ||8 |  |3 ||  |  |1 ||
    # ||7 |  |  ||  |2 |  ||  |  |6 ||
    # ================================
    # ||  |6 |  ||  |  |  ||2 |8 |  ||
    # ||  |  |  ||4 |1 |9 ||  |  |5 ||
    # ||  |  |  ||  |8 |  ||  |7 |9 ||
    # ================================
    def print_board(self):
        for i in range(0, len(self.board)):
            if (i == 0):
                print("================================")
            for j, val in enumerate(self.board[i]):
                print_pipe = [1, 2, 4, 5, 7, 8]
                if (j == 0):
                    print("||", end="")
                if (j in print_pipe):
                    print("|", end="")
                if (j % 3 == 0 and j != 0):
                    print("||", end="")
                if (val == -1):
                    print("  ", end="")
                else:
                    print(str(val) + " ", end="")
            if ((i + 1) % 3 == 0):
                print("||\n================================")
            else:
                print("||")
        print("\n")

    # adds to board
    def add(self, i, j, value):
        self.board[j][i] = value

    # returns if list of numbers is unique
    def unique(self, nums):
        nums = sorted(nums)
        last = 0
        for i in range(0, len(nums) - 1):
            if (nums[i] == nums[i + 1] and nums[i] != last and nums[i] != -1):
                return False
            last = nums[i]
        return True

    # returns if the board is valid
    def is_valid_board(self):
        # checking boxes
        ranges = [(0, 3), (3, 6), (6, 9)]
        for range1 in ranges:
            for range2 in ranges:
                square_numbers = []
                for square in self.board[range1[0]:range1[1]]:
                    square_numbers += square[range2[0]:range2[1]]
                if (not self.unique(square_numbers)):
                    return False

        # checking horizontals
        for row in self.board:
            if (not self.unique(row)):
                return False

        # checks verticals
        for i in range(0, 9):
            if (not self.unique([row[i] for row in self.board])):
                return False

        return True

    # returns if board is full
    def is_full(self):
        for x in self.board:
            for y in x:
                if (y == -1):
                    return False
        return True

    def next_spot(self):
        if (self.is_full()):
            return []
        found = False
        for y, row in enumerate(self.board):
            if (not found):
                for x, val in enumerate(row):
                    if (val == -1):
                        return x, y
        return -1, -1

    def solve(self):
        print(self.is_valid_board())
        while (True):
            if (not self.is_valid_board()):
                return None
            if (self.is_full()):
                return self.board
            x, y = self.next_spot()
            for i in range(1, 10):
                self.add(x, y, i)
                self.print_board()
                if (self.is_valid_board()):
                    this = self.solve()
                    if (this is not None):
                        this.print_board()
                        return this
                self.add(x, y, -1)


class Constraint(Board):
    def __init__(self, entries):
        self.board = entries
        self.backtracking = False
        possible = [[[num for num in range(1, 10)] for i in range(9)]
                    for j in range(9)]
        self.possible = possible
        self.reduce()

    def assign_one_possible(self):
        changed = False
        for i in range(0, len(self.possible)):
            for j in range(0, len(self.possible)):
                if (len(self.possible[i][j]) == 1):
                    self.add(j, i, self.possible[i][j][0])
                    self.possible[i][j] = []
                    changed = True
        return changed

    def reduce(self):
        possible = self.possible
        ranges = [range(0, 3), range(3, 6), range(6, 9)]
        for i, row in enumerate(self.board):
            for j, num in enumerate(row):
                if (num != -1):
                    possible[i][j] = []

                    # rows
                    for r in range(0, 9):
                        if (num in possible[i][r]):
                            possible[i][r].remove(num)

                    # columns
                    for r in range(0, 9):
                        if (num in possible[r][j]):
                            possible[r][j].remove(num)

                    # boxes
                    for x_range in ranges:
                        if (i in x_range):
                            break
                    for y_range in ranges:
                        if (j in y_range):
                            break
                    for x_check in x_range:
                        for y_check in y_range:
                            if (num in possible[x_check][y_check]):
                                possible[x_check][y_check].remove(num)
        self.possible = possible

    def backtracking_recursive(self):
        if (not self.is_valid_board()):
            return None
        if (self.is_full()):
            return self
        x, y = self.next_spot()
        for i in self.possible[y][x]:
            self.add(x, y, i)
            if (self.is_valid_board()):
                this = self.backtracking_recursive()
                if (this):
                    return this
            self.add(x, y, -1)
        return None

    def solve(self):
        while (self.assign_one_possible()):
            self.reduce()
            # TODO: add twins...
        if (not self.is_full() and self.is_valid_board()):
            self.backtracking = True
            self.backtracking_recursive()