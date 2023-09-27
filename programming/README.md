# Arrays

## Two Sum: Find indices that add up to a target.
Input: [2, 7, 11, 15], target=9
Output: [0, 1]

## Maximum Subarray: Find the largest sum of a contiguous subarray.
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6

## Contains Duplicate: Check if the array contains duplicates within k distance.
Input: [1, 2, 3, 1], k=3
Output: True

## Product Except Self: Calculate an output array such that output[i] is equal to the product of all the elements of the array except arr[i].
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]

## Rotate Array: Rotate the array to the right by k steps.
Input: [1, 2, 3, 4, 5, 6, 7], k=3
Output: [5, 6, 7, 1, 2, 3, 4]

# Dynamic Programming
## Climbing Stairs: Count ways to climb n stairs.

Input: n=2
Output: 2

## Coin Change: Find the minimum number of coins that you need to make up an amount n.

Input: coins = [1, 2, 5], amount = 11
Output: 3

## House Robber: Find the maximum amount you can rob tonight without alerting the police.

Input: [1, 2, 3, 1]
Output: 4

## Longest Increasing Subsequence: Length of longest increasing subsequence.

Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4

## Unique Paths: A robot is located at the top-left corner of a m x n grid. How many unique paths are there?

Input: m=3, n=7
Output: 28

# Linked Lists

## Reverse Linked List: Reverse a linked list.

Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1

## Middle of Linked List: Find the middle node of a linked list.

Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 3

## Remove Nth Node From End: Remove the n-th node from the end.

Input: 1 -> 2 -> 3 -> 4 -> 5, n=2
Output: 1 -> 2 -> 3 -> 5

## Merge Two Sorted Lists: Merge two sorted linked lists.

Input: 1 -> 3 -> 5 and 2 -> 4 -> 6
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6

##  Cycle in Linked List: Detect a cycle in a linked list.

Input: 3 -> 2 -> 0 -> -4 -> 2 (Last node points back to the second node)
Output: True

# Trees
##  Maximum Depth of Binary Tree: Find the maximum depth of the binary tree.

Input: [3, 9, 20, null, null, 15, 7] (Binary Tree)
Output: 3

##  Balanced Binary Tree: Determine if the binary tree is balanced.

Input: [3, 9, 20, null, null, 15, 7] (Binary Tree)
Output: True
## Invert Binary Tree: Invert a binary tree.

Input: [4, 2, 7, 1, 3, 6, 9] (Binary Tree)
Output: [4, 7, 2, 9, 6, 3, 1]
## Binary Tree Level Order Traversal: Return the level order traversal of the binary tree nodes' values.

Input: [3, 9, 20, null, null, 15, 7] (Binary Tree)
Output: [[3], [9, 20], [15, 7]]
## Lowest Common Ancestor: Find the lowest common ancestor of two given nodes in the binary tree.

Input: [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p=5, q=1 (Binary Tree)
Output: 3
# Graphs

## Clone Graph: Clone a graph with n nodes.

Input: Graph with [[2, 4], [1, 3], [2, 4], [1, 3]] as neighbors for each node.
Output: Cloned graph.

## Number of Islands: Count the number of islands in a 2D grid.

Input: [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
Output: 1

## Topological Sort: Perform a topological sort on a directed graph.

Input: Graph with edges [[0, 1], [0, 2], [1, 3], [1, 4]]
Output: [0, 2, 1, 4, 3]

## Course Schedule: Check if it's possible to finish all courses given the prerequisites.

Input: numCourses=2, prerequisites=[[1, 0]]
Output: True

## Shortest Path in Binary Matrix: Find the shortest path in a grid.

Input: [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
Output: 4