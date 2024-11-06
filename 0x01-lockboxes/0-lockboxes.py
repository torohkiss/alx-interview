#!/usr/bin/python3
"""A method that determines if all the boxes can be opened"""

from collections import deque


def canUnlockAll(boxes):
    """Checks boxes for keys that can unlock them"""

    n = len(boxes)
    opened = set()
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        if current_box not in opened:
            opened.add(current_box)

            for key in boxes[current_box]:
                if key < n and key not in opened:
                    queue.append(key)
    return len(opened) == n
