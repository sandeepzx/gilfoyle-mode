## Set

```python
seen = set()
```

* Stores unique values.
* `x in seen` → O(1) average
* `seen.add(x)` → O(1) average

Use when we need to quickly check:

> "Have I seen this?"

Empty `{}` is a `dict`, not a set.

## Dict / Hash Map

```python
seen = {}
```

Stores:

```text
key → value
```

Example:

```python
seen = {5: 2}
```

Means `5` is associated with index `2`.

Use when we need:

> "What information do I have about this?"

## Main Lesson

```text
Repeated search → set/dict → faster lookup
```
