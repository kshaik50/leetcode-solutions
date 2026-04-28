# 1. Two Sum

| Field | Details |
| --- | --- |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| LeetCode | [Two Sum](https://leetcode.com/problems/two-sum/) |

## Approach

Use a hash map to remember numbers already seen and their indices. For each number, compute the value needed to reach the target. If that needed value is already in the map, the answer has been found.

## Algorithm

1. Create an empty dictionary from number to index.
2. For each number in the array, compute `target - num`.
3. If the complement is already in the dictionary, return both indices.
4. Otherwise, store the current number and index.

## Complexity

| Type | Complexity |
| --- | --- |
| Time | `O(n)` |
| Space | `O(n)` |

## Solution

- [Python](solution.py)

