#!/usr/bin/python3
"""
Defines a function that determines if a box containing
a list of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """This function determines if all the
    boxes can be opened."""
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
