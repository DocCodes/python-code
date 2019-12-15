#!/usr/bin/env python3
"""
Author   : Evan Elias Young
Date     : 2018-02-10
Revision : 2019-12-14
"""

import random
from typing import List


def randomize(steps: int = 20) -> List[str]:
    """Will generate a list of steps to randomize a cube.

    Args:
        steps (integer): The number of steps to list. Defaults to 20.

    Returns:
        array: The list of steps to randomize the cube.

    """
    moves: List[str] = ['R', 'L', 'B', 'D', 'F', 'U']
    que: List[str] = [random.choice(moves)]
    for i in range(steps):
        mv = que[-1]
        while mv == que[-1]:
            mv = random.choice(moves)
        que.append(mv)
    return que


if __name__ == '__main__':
    print('Hello Console!')

    print(' '.join(randomize()))
