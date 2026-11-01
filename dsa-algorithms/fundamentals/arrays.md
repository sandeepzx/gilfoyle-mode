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

## 4. Pattern Comparison

| Technique | Main idea | Common use |
|---|---|---|
| Array Traversal | Visit elements systematically | Search, counting, aggregation |
| Two Pointers | Maintain two positions | Pair search, modification |
| Sliding Window | Maintain a contiguous range | Subarray and substring problems |

### Important Relationship

Sliding Window is closely related to Two Pointers.

A variable-size sliding window commonly uses two pointers:
- Left pointer defines the beginning.
- Right pointer defines the end.

However, not every Two Pointers problem is a Sliding Window problem.

---

## Progress

- [x] Array Traversal
- [x] Two Pointers
- [x] Sliding Window
- [ ] Prefix Sums
- [ ] Kadane's Algorithm
- [ ] In-place Modification
- [ ] Matrix Traversal
- [ ] Intervals

**Note:** These are theory notes. LeetCode problem solutions, approaches, code and individual problem learnings will be maintained separately in the Problems section.