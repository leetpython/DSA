# Indexes of Subarray Sum

## Intuition

Use two pointers from the start to create a flexible subarray window. If the window's sum is less than the target, expand it to the right, otherwise shrink it from the left.

```
arr = [10, 1, 3, 4, 7, 2], target = 13

left = 0, right = 1, sum = 10
[10] 1 3 4 7 2

left = 0, right = 2, sum = 11
[10 1] 3 4 7 2

left = 0, right = 3, sum = 14
[10 1 3] 4 7 2

left = 1, right = 3, sum = 4
10 [1 3] 4 7 2

left = 1, right = 4, sum = 8
10 [1 3 4] 7 2

left = 1, right = 5, sum = 15
10 [1 3 4 7] 2

left = 2, right = 5, sum = 14
10 1 [3 4 7] 2

left = 3, right = 5, sum = 11
10 1 3 [4 7] 2

left = 3, right = 6, sum = 13
10 1 3 [4 7 2]
```

## Approach

A few things to note:

- All numbers are non-negative. This means that expanding any subarray will always increase its sum, and shrinking it will always decrease its sum.
- If multiple valid subarrays exist, we want the leftmost. So we start both pointers from index `0`.

It is helpful to think of the brute-force approach first.

```python
for i in range(N):
    subarray_sum = 0
    for j in range(i, N):
        subarray_sum += arr[j]
        if subarray_sum == target:
            # SUCCESS!
```

This executes in `O(N^2)` time, with `O(1)` space. One obvious inefficiency is that even if we know that `sum(arr[i..j]) < target`, the brute-force approach will eventually reach `i+1` and check subarrays that start at it. But we know that `sum(arr[i+1..j]) < sum(arr[i..j])`, so we are wasting compute time.

We can solve this by using a window-like approach, where we have two variables `left` and `right` that represent the ends of the window.
1. If `sum(arr[left..right]) > target`, we can shrink the window by incrementing `left`.
1. If `sum(arr[left..right]) < target`, we can expand the window by incrementing `right`.

This is essentially the brute-force approach, but we save a LOT of time by skipping some subarrays. In fact, this executes in `O(N)` time, since `left` and `right` only go from `0` to `N` independently.

## Complexity

- Time Complexity: `O(N)`
- Space Complexity: `O(1)`
