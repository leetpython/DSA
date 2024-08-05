# Number of Senior Citizens

## Intuition

Extract the age component from each citizen's details, and increment a counter if the age is above 60.

## Approach

In Python, this is how you can extract the different components of a citizen's details:

```python
phone = detail[0:10]
gender = detail[10:11]
age = detail[11:13]
seat = detail[13:15]
```

For each citizen's details, extract their age, convert it to an integer using `int()` and increment a counter if the age is above 60.

## Complexity

- Time Complexity: `O(N)`
- Space Complexity: `O(1)`
