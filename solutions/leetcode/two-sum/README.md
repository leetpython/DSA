# Two Sum

## Intuition

Use a dictionary to check in `O(1)` time if `target - x` exists for any element `x`.

## Approach

In the brute force approach, we take every single pair of elements in the array, and check if they add up to `target`.
This is `O(N^2)` in time complexity.

We can observe that for any element `x` of the array, we simply need to find another element `target-x` in the array. The **`Dictionary`** data structure is perfect for this, because it allows searching in `O(1)` time.

1. Let `hashmap` be a dictionary which will map an element to its index (duplicates can be ignored)
1. For every element `x` at index `i` of the array:
    1. Calculate its complement: `complement = target - x`.
    1. Check if the complement already exists in `hashmap`:
        1. If so, return their indices: `return [i, hashmap[complement]]`

    1. Add this element to the dictionary: `hashmap[x] = i`

**Note**: We add the element to the dictionary *after* searching it, because if `target == x + x`, the element would be paired up with itself.

## Complexity

- Time complexity: `O(N)` (to loop over every element of the array)
- Additional Space complexity: `O(N)` (to create the hashmap)
