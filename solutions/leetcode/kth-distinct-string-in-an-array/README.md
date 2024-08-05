# Kth Distinct String in an Array

## Intuition

Use a dictionary to count the frequency of each string, and then count each distinct string.

## Approach

Create a dictionary `freq` that maps each string of the array to its frequency.

Traverse the array, and check each element to see whether it is distinct. If so, then increment a counter to keep track of which distinct string that element is (first, second, etc.). If the counter is equal to `k`, return that string.

If the loop exits normally, that means there are fewer than `k` distinct strings, so return `""`.

## Complexity

- Time Complexity: `O(N)`
- Space Complexity: `O(N)`
