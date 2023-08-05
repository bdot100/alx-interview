#!/usr/bin/python3
"""
Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""


from collections import deque


def canUnlockAll(boxes):
    """This function determines if all the
    boxes can be opened."""
    n = len(boxes)
    visited = set()
    queue = deque([0])  # Start with the first box (index 0) in the queue.

    while queue:
        currentBox = queue.popleft()  # Get the current box from the front of the queue.
        visited.add(currentBox)      # Mark the current box as visited.

        for key in boxes[currentBox]:
            if key not in visited:
                queue.append(key)  # Add the box unlocked by the current key to the queue.

    # If we have visited all the boxes (n boxes in total), return True; otherwise, return False.
    return len(visited) == n

