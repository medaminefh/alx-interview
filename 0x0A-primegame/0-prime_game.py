#!/usr/bin/python3
"""
Prime game module
"""


def isWinner(x, nums):
    """Determines the winner of a prime game

    Args:
        x: number of rounds
        nums: list of numbers

    Returns:
        winner of the game
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for _ in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        remove_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def remove_multiples(l, x):
    """removes multiples of x from list l
    """
    for i in range(2, len(l)):
        try:
            l[i * x] = 0
        except (ValueError, IndexError):
            break
