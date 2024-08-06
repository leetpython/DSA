# Longest Substring Without Repeating Characters

## Intuition

Think of the subarray as a window, and use a dictionary that maps each character found with its latest position in the string.

If a character has been found **and** its latest position is within the window, shrink the window from the left. Otherwise, keep expanding the window to the right.

## Approach

This is similar to _Sliding Window_ problems, with one optimization: since each character must be unique within the window, we can use a dictionary to store the index of the character (instead of its frequency).

There are two important variables:

1. `position_map`
   While traversing the string, this dictionary maps every character found till that point to its index till that point.
1. `window_start`
   The index at which the subarray (window) starts. To check whether a character exists within the window, we simply check if `position_map[character] >= window_start`.

Use Python's [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict) to ensure that every character's initial index is set to `-1`.

1. For each index `i`:
    1. The window's range is given by `[window_start, i-1]`.
    1. Let `c` be the character at position `i` that we are trying to add to the window.
    1. If `c` already exists within the window (`position_map[c] >= window_start`), we won't be able to add it again. So, we must shrink the window to the point where `c` doesn't exist in the window, which is simply `position_map[c] + 1`. So, we set `window_start = position_map[c] + 1`.
    1. Now, add `c` to the window with its new position: `position_map[c] = i`.
    1. The new window's range is given by `[window_start, i]`, and it contains no repeating characters.
    1. Update the final result with this window's length if it is greater.

## Complexity

- Time Complexity: `O(N)`
- Space Complexity: `O(N)` because in the worst case, every character is unique and needs space in the dictionary.
