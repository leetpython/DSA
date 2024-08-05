# Reverse Linked List

## Intuition

Traverse the linked list node by node, and reverse the previous link (to the current head) every iteration.

```
 None     A  → B → C → None
(prev)  (curr)

None ←   A       B    → C → None
       (prev)  (curr)

None ← A ←   B       C    → None
           (prev)  (curr)

None ← A ← B ←   C      None
               (prev)  (curr)
```

## Approach

There are two important variables:

1. `curr`
   A reference to the current node, which will always be the head of a subset of the original linked list.
1. `prev`
   A reference to the node just before the current node (in the original linked list). This will always be the head of a subset of the reversed linked list.

At each iteration, we transform `prev → curr` into `prev ← curr` and update the variables accordingly.

1. Suppose we start some iteration with `prev = A → None` and `curr = B → C → None`.
1. In the next iteration, we transform this into `prev = B → A → None` and `curr = C → None`.
1. In the next iteration, we transform this into `prev = C → B → A → None` and `curr = None`
1. `prev` now represents the head of the reversed linked list.

## Complexity

- Time Complexity: `O(N)`
- Space Complexity: `O(1)` because we simply maintain two variables
