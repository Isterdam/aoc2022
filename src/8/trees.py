import numpy as np
from itertools import takewhile

lines = open('in.txt').read().splitlines()
trees = np.array([list(map(int, [*line])) for line in lines])

def strict_max(x, l):
    return np.sum(l >= x) == 1 # only contains 1 element >= x

def visible_up(i, j):
    return strict_max(trees[i, j], trees[:i+1, j])

def visible_down(i, j):
    return strict_max(trees[i, j], trees[i:, j])

def visible_left(i, j):
    return strict_max(trees[i, j], trees[i, :j+1])

def visible_right(i, j):
    return strict_max(trees[i, j], trees[i, j:])

def tree_visible(i, j):
    return (visible_up(i, j) or visible_down(i, j) or
        visible_left(i, j) or visible_right(i, j)) 

width = trees.shape[0]
height = trees.shape[1]
visible = 2*width + 2*height - 4 # edges

for i in range(1, width-1):
    for j in range(1, height-1):
        if tree_visible(i, j):
            visible += 1

print(visible) # part 1

def scenic_score(i, j):
    tree = trees[i, j]
    def higher(y):
        return tree > y

    # if the tree isn't visible we can still see the blocking tree
    # from our point of view in the forest, hence +1
    up = 0 if visible_up(i, j) else 1
    down = 0 if visible_down(i, j) else 1
    left = 0 if visible_left(i, j) else 1
    right = 0 if visible_right(i, j) else 1

    up += len(list(takewhile(higher, trees[:i+1, j][:-1][::-1])))
    down += len(list(takewhile(higher, trees[i:, j][1:])))
    left += len(list(takewhile(higher, trees[i, :j+1][:-1][::-1])))
    right += len(list(takewhile(higher, trees[i, j:][1:])))

    return up * down * left * right

print(max([scenic_score(i, j) for i in range(1, width-1) for j in range(1, height-1)])) # part 2