# Count Number of Teams

## Intuition

For each index `j`, compute two values:
1. `lt_left` = The number of indices `i` (`< j`) such that `rating[i] < rating[j]`
1. `gt_right` = The number of indices `k` (`> j`) such that `rating[j] < rating[k]`

Use these to find the number of teams with `j` in the middle for ascending and descending ratings *separately*.

## Approach

Consider a team with their indices represented by `(i, j, k)` in that order. Their ratings could be one of two tyeps:
1. `rating[i] < rating[j] < rating[k]` - Ascending Ratings
1. `rating[i] > rating[j] > rating[k]` - Descending Ratings

Suppose for each index `j` we had two pieces of information:
1. `lt_left` = The number of indices `i` (`< j`) such that `rating[i] < rating[j]`
1. `gt_right` = The number of indices `k` (`> j`) such that `rating[j] < rating[k]`

`lt_left` is the number of soldiers with rating less than soldier `j`'s, to the left of `j`. Similarly, `gt_right` is the number of soldiers with rating greater than soldier `j`'s. For the Ascending Ratings case, we can pair up any of the `lt_left` soldiers on the left with any of the `gt_right` soldiers on the right to form a valid team. This gives us:

```python
teams_asc = lt_left * gt_right
```

The number of soldiers to the left of index `j` is simply `j`. So `gt_left = j - lt_left` gives us the number of soldiers to the left of `j` with rating **greater than** soldier `j`'s. Similarly, the number of soldiers to the right of `j` with rating **less than** soldier `j`'s is `lt_right = (N - 1 - j) - gt_right`. This gives us:

```python
gt_left = j - lt_left
lt_right = (N - 1 - j) - gt_right
teams_desc = gt_left * lt_right
```

Adding both of these cases to the total number of teams, we end up with:

```python
teams += teams_asc + teams_desc
```

## Complexity

- Time Complexity: `O(N^2)`
- Time Complexity: `O(1)`
