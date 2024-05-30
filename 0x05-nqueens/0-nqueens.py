#!/usr/bin/python3

"""This module contains a function that solves the N queens puzzle"""

import sys


def is_safe(board, row, col):
    # Check if the current position is safe to place a queen
    for i in range(row):
        if board[i] == col or \
           board[i] == col - (row - i) or \
           board[i] == col + (row - i):
            return False
    return True


def solve_n_queens(n, board=[], row=0):
    if row == n:
        # Base case: all queens have been placed
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            # Place a queen at the current position
            board.append(col)
            solve_n_queens(n, board, row + 1)
            # Backtrack: remove the queen at the current position
            board.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(n)
