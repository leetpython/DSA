# Gas Station

## Intuition

Use two passes:
1. Check if it's even possible to go around the circle with fuel >= 0 remaining
1. (If yes) Assume you start at station `0`. Loop through the stations and keep a running count of your fuel surplus. If it becomes negative at station `i`, choose to start instead from station `i+1`.

## Approach

The only number we care about is your fuel surplus i.e. the gas you will have after the combination of refueling + traveling to the next station. In other words, `surplus = gas[i] - cost[i]`.

To determine if it's even possible to make a round trip, simply add up the surpluses after each station, and check if it is >= 0. If yes, then it's possible to start from some station without ever running out of fuel mid-journey. But we still need to determine which station to start from.

Let's say you have chosen to start from some station `start`, and you have `x` amount of fuel surplus when you reach station `i`. If your surplus is negative, that means it's impossible to make a round-trip if you start at station `start`. So, we can simply set `start = i+1` instead. In this manner, we keep updating our starting position until we reach the end of our stations' list. We know a round-trip is possible, so `start` will never be `>= N`.

## Complexity

- Time Complexity: `O(N)`
- Space Complexity: `O(1)`
