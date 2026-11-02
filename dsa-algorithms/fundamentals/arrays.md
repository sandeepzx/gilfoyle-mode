# Arrays — Fundamentals

## 1. Array Traversal

### What is Array Traversal?

Array traversal is the process of visiting elements in an array one by one to access, inspect, search, calculate or modify data.

In Python, arrays are commonly represented using lists.

### Types of Traversal

**1. Direct traversal**

Visits each element directly. Useful when only the element value is required.

```python
nums = [10, 20, 30]

for num in nums:
    print(num)
```

**2. Index-based traversal**

Uses the index to access elements. Useful when position matters or elements need to be modified.

```python
for i in range(len(nums)):
    print(i, nums[i])
```

**3. Traversal using enumerate**

Provides both index and value.

```python
for i, num in enumerate(nums):
    print(i, num)
```

**4. Reverse traversal**

Visits elements from the end towards the beginning.

```python
for num in reversed(nums):
    print(num)
```

Alternatively, using indices:

```python
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])
```

**5. Conditional traversal**

Processes elements only when they satisfy a condition.

```python
for num in nums:
    if num > 15:
        print(num)
```

### Single-pass Traversal

A single-pass traversal processes an array in one iteration.

We maintain variables that store the information we need rather than traversing the array multiple times.

Example: Maintaining minimum and maximum.

```python
nums = [8, 3, 12, 5, 20]

minimum = maximum = nums[0]

for num in nums:
    minimum = min(minimum, num)
    maximum = max(maximum, num)
```

**Complexity:**
- Time: O(n)
- Auxiliary space: O(1)

### Nested Traversal

Nested traversal uses one loop inside another.

Common applications:
- Comparing every pair of elements.
- Generating combinations.
- Matrix traversal.

Example: Comparing every pair.

```python
nums = [10, 20, 30]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])
```

For two nested loops that each execute n times:

- Time: O(n²)

For a matrix with r rows and c columns:

- Time: O(r × c)

### Important Considerations

- Python lists use zero-based indexing.
- For a list of length n, valid positive indices are 0 to n-1.
- Negative indexing accesses elements from the end.
- Accessing an invalid index raises `IndexError`.
- Always consider empty arrays and single-element arrays.

---

## 2. Two Pointers

### What is Two Pointers?

Two Pointers is an algorithmic technique that uses two position variables to traverse or track elements in a data structure.

Instead of repeatedly searching or comparing elements, we move pointers according to the problem's conditions.

### Types of Two Pointers

#### A. Opposite-direction Pointers

One pointer starts at the beginning, and another starts at the end. They move towards each other.

Example: Pointer initialization and movement.

```python
nums = [1, 2, 3, 4, 5]

left = 0
right = len(nums) - 1

while left < right:
    print(nums[left], nums[right])

    left += 1
    right -= 1
```

Common applications:
- Pair-sum problems in sorted arrays.
- Palindrome checking.
- Reversing arrays.
- Finding pairs that satisfy certain conditions.

**Important:** Sorted order often makes pointer movement predictable and allows us to eliminate unnecessary possibilities.

Typical complexity:
- Time: O(n)
- Auxiliary space: O(1)

#### B. Same-direction Pointers

Both pointers move from left to right, but perform different roles.

- Read pointer: examines elements.
- Write pointer: identifies where the next valid element should be placed.

Example: Basic read/write pointer movement.

```python
nums = [10, 20, 30, 40]

write = 0

for read in range(len(nums)):
    if nums[read] > 20:
        nums[write] = nums[read]
        write += 1
```

Common applications:
- Removing duplicates.
- Removing specific elements.
- Moving zeroes.
- In-place array modification.

Typical complexity:
- Time: O(n)
- Auxiliary space: O(1)

#### C. Fast and Slow Pointers

Both pointers move in the same direction but at different speeds.

Commonly:
- Slow pointer moves one step.
- Fast pointer moves two steps.

Example: Tracking positions.

```python
slow = 0
fast = 0

while fast + 1 < len(nums):
    slow += 1
    fast += 2
```

This demonstrates the movement concept for an array. Fast and slow pointers are especially important in linked lists.

Common applications:
- Finding the middle of a linked list.
- Detecting cycles.
- Identifying repeated states in certain problems.

### When to Recognize Two Pointers

Look for:
- Sorted arrays.
- Pair comparisons.
- Elements at opposite ends.
- In-place modifications.
- Removing duplicates.
- Finding middle positions or detecting cycles.

### Important Considerations

Two Pointers is not automatically suitable for every array problem. Pointer movement must be justified by the properties of the data and the problem's conditions.

---

## 3. Sliding Window

### What is Sliding Window?

Sliding Window is a technique for processing a contiguous section of an array or string.

A window represents the current range of elements being considered.

Instead of recalculating information for every possible range, we maintain the current window and update it as it moves.

### Types of Sliding Window

#### A. Fixed-size Window

The window has a predefined size k.

At every movement:
- Add the new element entering the window.
- Remove the old element leaving the window.
- Update the required result.

Example: Updating a running window sum.

```python
nums = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(nums[:k])

for right in range(k, len(nums)):
    window_sum += nums[right]
    window_sum -= nums[right - k]
```

Common applications:
- Maximum sum of a subarray of size k.
- Average of every subarray of size k.
- Maximum number of vowels in a substring of length k.

Typical complexity:
- Time: O(n)
- Auxiliary space: O(1)

#### B. Variable-size Window

The window size changes depending on a condition.

General structure:

```python
left = 0

for right in range(len(nums)):

    # Include the new element in the window

    while window_is_invalid:
        # Remove the leftmost element
        left += 1

    # Update the answer
```

Common applications:
- Longest substring without repeating characters.
- Longest subarray with at most k distinct elements.
- Shortest valid subarray under suitable constraints.

Typical complexity:
- Time: O(n), when each pointer moves forward at most n times.
- Auxiliary space: Depends on the information maintained inside the window.

### Frequency Dictionary with Sliding Window

A dictionary can maintain the frequency of elements inside the current window.

Example: Adding and removing frequencies.

```python
window = {}

# Add an element
num = 5
window[num] = window.get(num, 0) + 1

# Remove an element
window[num] -= 1

if window[num] == 0:
    del window[num]
```

It helps track:
- How many times each element appears.
- The number of distinct elements.
- Whether the window satisfies a condition.

The number of dictionary keys represents the number of distinct elements currently in the window.

### When to Recognize Sliding Window

Look for:
- Contiguous subarrays or substrings.
- Fixed-length ranges.
- Longest or shortest valid ranges.
- Maximum or minimum values within ranges.
- Conditions involving distinct elements or frequencies.

### Important Limitation

The standard variable-size sliding window for sum-based problems often relies on non-negative numbers.

With negative numbers, expanding or shrinking the window may not change the sum predictably.

Therefore, not every subarray-sum problem can be solved using ordinary Sliding Window.

---

## 4. Prefix Sums

### What is a Prefix Sum?

A prefix sum is a cumulative sum of array elements from the beginning up to a particular index.

Example:

```python
nums = [2, 4, 1, 5, 3]
```

Prefix sums:

```python
prefix = [2, 6, 7, 12, 15]
```

Each position stores the sum of all elements up to that position.

### Building Prefix Sums

A common approach is to use a leading zero:

```python
prefix = [0]

for num in nums:
    prefix.append(prefix[-1] + num)
```

Result:

```python
[0, 2, 6, 7, 12, 15]
```

The leading zero simplifies range-sum calculations.

### Range Sum Queries

To calculate the sum of elements between indices `l` and `r`, inclusive:

```python
range_sum = prefix[r + 1] - prefix[l]
```

Example:

```python
nums = [2, 4, 1, 5, 3]
```

Find the sum from index 1 to index 3:

```python
prefix = [0, 2, 6, 7, 12, 15]

prefix[4] - prefix[1]
# 12 - 2 = 10
```

The corresponding subarray is `[4, 1, 5]`.

### Prefix Sum + Hash Map

Prefix sums are useful for subarray problems, especially when negative numbers are present.

For a subarray with sum `k`:

\[
current\_sum - previous\_prefix = k
\]

Rearranging:

\[
previous\_prefix = current\_sum - k
\]

We can use a dictionary to remember previously encountered prefix sums.

For counting subarrays, store the frequency of each prefix sum.

```python
prefix_count = {0: 1}

current_sum = 0
count = 0

for num in nums:
    current_sum += num

    required = current_sum - k
    count += prefix_count.get(required, 0)

    prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
```

The initial `{0: 1}` represents the empty prefix and allows subarrays beginning at index zero to be counted.

This technique is used in LeetCode #560 — Subarray Sum Equals K.

### Two-Dimensional Prefix Sums

Prefix sums can also be applied to matrices to calculate rectangular region sums efficiently.

The recurrence is:

\[
P[i][j] = A[i][j] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]
\]

The overlapping top-left region is subtracted because it was counted twice.

### Complexity

| Operation | Complexity |
|---|---|
| Build prefix sums | O(n) |
| One range-sum query | O(1) |
| q range-sum queries | O(n + q) |
| Prefix sum + hash map traversal | O(n) expected |
| Auxiliary space | O(n) |

### Important Points

- Prefix sums work with positive, zero and negative numbers.
- Repeated prefix sums are possible.
- Use a frequency dictionary when counting subarrays.
- If the original array changes, the existing prefix sums become invalid.
- Frequent updates and range queries may require Fenwick Trees or Segment Trees.

---

## 5. Kadane's Algorithm

### What is Kadane's Algorithm?

Kadane's Algorithm finds the maximum sum of a non-empty contiguous subarray in linear time.

Example:

```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

The maximum-sum subarray is:

```python
[4, -1, 2, 1]
```

Maximum sum = `6`.

### Core Idea

At every element, we have two choices:

1. Continue the previous subarray.
2. Start a new subarray from the current element.

We choose whichever produces the larger sum.

\[
current = \max(num,\ current + num)
\]

### Two Important Variables

- `current_sum`: Maximum subarray sum ending at the current position.
- `max_sum`: Maximum subarray sum found anywhere so far.

Initialization:

```python
current_sum = nums[0]
max_sum = nums[0]
```

Update:

```python
current_sum = max(nums[i], current_sum + nums[i])
max_sum = max(max_sum, current_sum)
```

### Why Not Initialize with Zero?

Consider:

```python
nums = [-5, -2, -8]
```

The answer is `-2`, not `0`.

The problem requires a non-empty subarray. Initializing with the first element handles this correctly.

### Finding the Actual Subarray

If a problem asks for the subarray itself, maintain its starting and ending indices.

Track:

- `start`: Start of the current candidate.
- `best_start`: Start of the best subarray.
- `best_end`: End of the best subarray.

Whenever a new maximum is found, save the boundaries.

Python slicing can retrieve the result:

```python
nums[best_start:best_end + 1]
```

### Complexity

- Time: O(n)
- Auxiliary space: O(1)

### Important Points

- The subarray must be contiguous.
- The algorithm works with negative numbers.
- A non-empty subarray must be considered.
- Kadane's Algorithm optimizes the maximum sum, not necessarily the length or number of subarrays.

---

## 6. In-place Modification

### What is In-place Modification?

In-place modification means modifying the original array directly instead of creating another array proportional to the input size.

The main objective is to reduce auxiliary space.

### Read and Write Pointers

A common technique uses two pointers:

- `read`: Examines each element.
- `write`: Tracks where the next valid element should be placed.

Example: Move non-negative elements to the beginning.

```python
nums = [3, -1, 5, -2, 8]

write = 0

for read in range(len(nums)):
    if nums[read] >= 0:
        nums[write] = nums[read]
        write += 1
```

After execution:

```python
nums = [3, 5, 8, -2, 8]
```

The meaningful portion is:

```python
nums[:write]
# [3, 5, 8]
```

The unused portion may contain old or duplicated values.

### Common In-place Techniques

1. **Read and write pointers**
   - Remove duplicates.
   - Remove specific elements.
   - Move zeroes.
   - Filter elements.

2. **Opposite-direction pointers**
   - Reverse an array.
   - Rearrange elements.
   - Swap elements from both ends.

3. **Cyclic rearrangement**
   - Rotate arrays.
   - Reposition elements according to their indices.

### Complexity

| Operation | Time | Auxiliary Space |
|---|---:|---:|
| Modify every element | O(n) | O(1) |
| Reverse an array | O(n) | O(1) |
| Filter using read/write pointers | O(n) | O(1) |
| Create a separate filtered list | O(n) | O(n) |

### Important Points

- In-place algorithms generally aim for O(1) auxiliary space.
- Avoid overwriting elements before reading them.
- Some problems require preserving the original order; others don't.
- Some problems expect only the first `k` elements to contain the valid result.
- In Python, `nums[:]` creates a copy, while `nums[:] = values` replaces the original list contents.

---

## 7. Matrix Traversal

### What is a Matrix?

A matrix is a two-dimensional collection of elements arranged in rows and columns.

Python represents matrices commonly using nested lists.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Access an element:

```python
matrix[row][column]
```

For example:

```python
matrix[1][2]  # 6
```

### Matrix Dimensions

For a matrix with `r` rows and `c` columns:

```python
rows = len(matrix)
cols = len(matrix[0])
```

Total elements:

\[
r \times c
\]

A matrix doesn't have to be square.

For an empty matrix, check whether it contains rows before accessing `matrix[0]`.

### Row-wise Traversal

Visit every element from left to right, then move to the next row.

```python
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        print(matrix[row][col])
```

Time complexity: O(r × c).

### Column-wise Traversal

Visit every row in one column before moving to the next column.

```python
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        print(matrix[row][col])
```

Time complexity: O(r × c).

### Primary Diagonal

In a square matrix, the primary diagonal has equal row and column indices.

```python
for i in range(len(matrix)):
    print(matrix[i][i])
```

### Secondary Diagonal

For a square matrix of size `n`:

\[
col = n - 1 - row
\]

```python
n = len(matrix)

for row in range(n):
    print(matrix[row][n - 1 - row])
```

### Boundary Traversal

Boundary traversal visits the outermost elements of a matrix.

It can be implemented by traversing the top, right, bottom and left boundaries while avoiding duplicate corners.

### Spiral Traversal

Spiral traversal visits matrix elements in a spiral pattern.

Maintain four boundaries:

- `top`
- `bottom`
- `left`
- `right`

After traversing a boundary, move it inward. Continue until the boundaries cross.

### Complexity

| Operation | Complexity |
|---|---|
| Access one element | O(1) |
| Traverse all elements | O(r × c) |
| Search every element | O(r × c) |
| Create another matrix | O(r × c) space |

For a square matrix with `n` rows and `n` columns:

\[
O(n \times n) = O(n^2)
\]

---

## 8. Intervals

### What is an Interval?

An interval represents a continuous range between two boundaries, usually represented as `[start, end]`.

Example:

```python
intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18]
]
```

Intervals are common in scheduling, calendar events, bookings and range-based problems.

### Overlapping Intervals

Two inclusive intervals overlap when they share at least one point.

For intervals `[a, b]` and `[c, d]`, the overlap condition is:

\[
a \leq d \quad \text{and} \quad c \leq b
\]

If this condition is false, they don't overlap.

For example:

```text
[1, 5] and [3, 7]
```

Their shared range is `[3, 5]`.

### Sorting Intervals

Most interval problems become easier after sorting by start time.

```python
intervals.sort(key=lambda x: x[0])
```

Sorting allows us to process intervals from left to right.

Typical sorting complexity: O(n log n).

### Merging Overlapping Intervals

Consider:

```python
intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18]
]
```

The first two intervals overlap, so they can be combined.

Result:

```python
merged = [
    [1, 6],
    [8, 10],
    [15, 18]
]
```

The merged boundaries are:

\[
new\_start = \min(start_1, start_2)
\]

\[
new\_end = \max(end_1, end_2)
\]

Merging preserves the combined coverage while simplifying the representation.

### Common Interval Patterns

- Merge overlapping intervals.
- Insert a new interval into existing intervals.
- Detect overlapping meetings.
- Find the minimum number of meeting rooms.
- Remove overlapping intervals.

### Complexity

For the usual sorting-and-processing approach:

- Sorting: O(n log n)
- Traversal: O(n)
- Total time: O(n log n)
- Output space: O(n) in the worst case.

### Important Points

- Intervals represent ranges, not necessarily array subarrays.
- Sorting by start time is a common first step.
- Check whether endpoints are inclusive or exclusive.
- Merging combines coverage; it doesn't simply delete information.

---

# 9. Pattern Comparison and Relationships

## Array Traversal vs Two Pointers vs Sliding Window

| Pattern | Main idea | Typical use |
|---|---|---|
| Array Traversal | Visit elements | Search, calculate, inspect |
| Two Pointers | Maintain two positions | Pair search, reversal, rearrangement |
| Sliding Window | Maintain a contiguous range | Longest/shortest valid subarray or substring |

Important relationship:

- Sliding Window commonly uses two pointers.
- Not every Two Pointers problem is a Sliding Window problem.
- Traversal is the foundation used by both.

## Two Pointers vs Prefix Sum

| Two Pointers | Prefix Sum |
|---|---|
| Moves positions through the array | Stores cumulative totals |
| Often works with sorted data or a specific movement property | Useful for repeated range-sum calculations |
| Can use O(1) auxiliary space | Usually uses O(n) auxiliary space |
| Often processes elements dynamically | Preprocesses cumulative information |

## Sliding Window vs Prefix Sum

Both can solve some subarray problems, but they work differently.

| Sliding Window | Prefix Sum |
|---|---|
| Maintains a changing range | Stores cumulative sums |
| Often depends on a monotonic condition | Works with negative numbers too |
| Can use O(1) or additional space | Usually O(n) preprocessing space |
| Useful for many longest/shortest window problems | Useful for range sums and subarray-sum relationships |

**Important:** Ordinary variable-size sliding-window sum techniques generally rely on non-negative values. Negative values break the monotonic behaviour needed for simple expansion and shrinking.

## Prefix Sum vs Kadane's Algorithm

| Prefix Sum | Kadane's Algorithm |
|---|---|
| Tracks cumulative sums | Tracks the best subarray ending at the current position |
| Useful for range queries and subarray-sum problems | Specifically finds maximum-sum contiguous subarrays |
| Usually O(n) extra space | O(1) auxiliary space |

Both use cumulative information, but their objectives differ.

## Two Pointers vs In-place Modification

These concepts are closely related.

Read/write pointers and opposite-direction pointers are common ways to modify arrays in place.

However:

- Two Pointers is a pointer-management technique.
- In-place Modification is an objective or constraint about modifying the original data.

An in-place algorithm doesn't always need two pointers.

## Matrix Traversal vs Normal Array Traversal

| One-dimensional array | Matrix |
|---|---|
| One index | Two indices |
| `nums[i]` | `matrix[row][col]` |
| O(n) full traversal | O(r × c) full traversal |
| One-dimensional position | Row and column position |

## Intervals vs Subarrays

| Subarray | Interval |
|---|---|
| Contiguous elements from an array | A continuous range between boundaries |
| Uses array indices | Usually uses start and end values |
| Example: `nums[1:4]` | Example: `[2, 6]` |
| Common patterns: Sliding Window, Prefix Sum, Kadane | Common patterns: Sorting, Merging, Overlap detection |

---

# 10. Important Relationships to Remember

1. **Traversal is fundamental:** Most array algorithms require some form of traversal.
2. **Two Pointers reduce unnecessary work:** Instead of repeatedly searching, maintain positions and move them based on a valid property.
3. **Sliding Window is a specialised Two Pointers technique:** It maintains a contiguous range.
4. **Prefix Sum avoids repeated addition:** Precompute cumulative information to answer range queries efficiently.
5. **Prefix Sum + Hash Map solves many subarray-sum problems:** Store previous cumulative sums and their frequencies.
6. **Kadane's Algorithm optimises a particular subarray objective:** It finds the maximum-sum contiguous subarray.
7. **In-place modification controls extra memory:** Read/write pointers are a common implementation.
8. **Matrix traversal extends array traversal into two dimensions.**
9. **Sorting simplifies interval problems:** It makes overlap detection and merging easier.
10. **A pattern is not a solution by itself:** Always check constraints, ordering, contiguity, allowed memory and required output.

---

# 11. Complexity Quick Reference

| Technique | Typical Time | Typical Auxiliary Space |
|---|---:|---:|
| Array traversal | O(n) | O(1) |
| Nested pair traversal | O(n²) | O(1) |
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(1) or O(k) |
| Prefix Sum construction | O(n) | O(n) |
| Prefix Sum range query | O(1) | O(1) per query |
| Prefix Sum + Hash Map | O(n) expected | O(n) |
| Kadane's Algorithm | O(n) | O(1) |
| In-place modification | O(n) | O(1) |
| Matrix traversal | O(r × c) | O(1) |
| Interval sorting and merging | O(n log n) | O(n) output space |

*Complexities are typical for the described implementations; actual complexity depends on the problem and implementation.*

---
