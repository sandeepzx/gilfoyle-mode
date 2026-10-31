## Big-O

### What is Big-O?
Big-O describes how the amount of work grows as input size n grows.

### Common complexities

O(1)       constant

O(log n)   repeatedly reduce the problem, first iteration n then n/2 then n/3.. like binary search

O(n)       go through n items in a loop

O(n log n) n work × log n levels

O(n²)      nested n work

## Problem 1 — Pair Sum

Brute force:
O(n²) time
O(1) extra space

Optimized using set:
O(n) average time
O(n) space

Key idea:
Use a set when we repeatedly need to check whether a value exists.

## Problem 2 — First Duplicate

Using set:
O(n) average time
O(n) space

Key idea:
Store previously seen values.

## Problem 3 — Two Sum

Using dict:
number → index

O(n) average time
O(n) space

Key idea:
Set → "Have I seen this?"
Dict → "What information do I have about this?"

