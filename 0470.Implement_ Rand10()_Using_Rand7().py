# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def __init__(self):
        self.matrix = [
            [0, 1, 2, 3, 4, 5, 6],
            [7, 8, 9, 0, 1, 2, 3],
            [4, 5, 6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5, 6, 7],
            [8, 9, 0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9, 0, 1],
            [2, 3, 4, 5, 6, 7, 9],
        ]

    def rand10(self):
        row, col = rand7() - 1, rand7() - 1
        while row == 6 or row == 5 and col >= 5:
            row, col = rand7() - 1, rand7() - 1

        return self.matrix[row][col] + 1
