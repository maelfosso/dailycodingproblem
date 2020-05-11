#!/usr/bin/env python3

# This problem was asked by Google.
# Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.
# For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:
#     5
#    / \
#   3   7
#  / \   \
# 2   4   8

class Tree:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def display(self):

    if not self.left is None:
      self.left.display()

    if not self.right is None:
      self.right.display()

    print(f"{self.value}\t")

def reconstruct(postorder):
  
  if (len(postorder) == 0 or postorder is None):
    return None

  if len(postorder) == 1:
    return Tree(postorder[0])

  root_value = postorder[-1]
  root = Tree(root_value)

  arr = postorder[:-1]
  i = 0
  while i < len(arr) and arr[i] <= root_value:
    i += 1

  left_tree = reconstruct(arr[:i])
  right_tree = reconstruct(arr[i:])

  root.left = left_tree
  root.right = right_tree

  return root


# reconstruct([2, 4, 3, 8, 7, 5])