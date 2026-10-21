
# Session 1 — Memory, Stack and Heap

## 1. What Is Memory?

When a program runs, it needs memory to store data and keep track of what it is doing.

For example:

```python
x = 10
name = "Sandeep"
numbers = [10, 20, 30]
```

The program needs to represent the integer `10`, the string `"Sandeep"`, and the list containing three integers.

Memory is made up of locations that can be addressed. At a low level, data is represented using bits (0s and 1s). Programs and the operating system manage access to that data.

### Memory addresses

A memory address identifies a location in memory.

Think of memory like a collection of numbered storage locations. A program can use addresses to locate the data it needs.

However, in a modern operating system, programs normally use **virtual memory addresses**. The operating system and hardware translate these addresses to physical RAM locations when needed.

---

## 2. What Happens When a Program Runs?

A program stored on disk is not the same as a running program.

When you execute a program, the operating system creates a process and provides it with a virtual address space.

The process's memory contains different regions for different purposes, including:

- Code and program instructions.
- Global and static data.
- Stack memory.
- Heap memory.
- Other regions used by the operating system and runtime.

The exact arrangement depends on the operating system, programming language, and implementation.

For this session, we focus on the stack and heap.

---

## 3. Stack Memory

The stack is a memory region commonly used to manage function calls.

When a function is called, the program needs to remember information such as:

- Which function is executing.
- Its local execution state.
- Where to return after the function finishes.
- Other information required by the calling convention and runtime.

This information is commonly organized into a **stack frame** for each active function call.

### Example

```python
def greet():
    message = "Hello"
    print(message)

greet()
```

Conceptually, when `greet()` is called, a new function-call frame becomes active.

When the function finishes, its frame is removed from the active call stack.

This is why ordinary function calls can be managed efficiently.

### Nested function calls

```python
def first():
    second()

def second():
    print("Inside second")

first()
```

The execution order is:

1. `first()` is called.
2. `first()` calls `second()`.
3. `second()` executes.
4. `second()` returns to `first()`.
5. `first()` finishes.

The stack follows a last-in, first-out (LIFO) pattern: the most recently called function normally returns first.

### Important note about Python

Python is a high-level language. Its variables and objects are managed by the Python runtime.

Do not assume that every Python local variable is simply a value stored directly on the machine stack. In CPython, for example, local variables commonly hold references to Python objects, while the interpreter manages function execution.

---

## 4. Heap Memory

The heap is memory used for dynamic allocation.

In Python, objects such as lists, dictionaries, instances of classes, and integers are managed by the Python runtime. In CPython, these objects are generally allocated in memory managed by its allocator, commonly associated with the heap.

Example:

```python
numbers = [10, 20, 30]
```

Conceptually:

- `numbers` is a name bound to a list object.
- The list object contains references to its elements.
- The Python runtime manages the object's memory.

The variable name and the object it refers to are different concepts.

This distinction is essential for understanding Python references.

---

## 5. Variables and References in Python

Consider:

```python
x = 10
y = x
```

A useful mental model is:

- An integer object representing `10` exists.
- The name `x` is bound to that object.
- The assignment `y = x` binds `y` to the same object.

Conceptually:

```text
x ──┐
    ├──> Integer object: 10
y ──┘
```

Python assignment does not automatically create a new copy of the object. It binds a name to an object.

### Reassigning a variable

```python
x = 10
y = x

x = 20
```

Now `x` is bound to the integer object representing `20`, while `y` remains bound to the object representing `10`.

Conceptually:

```text
x ─────> Integer object: 20

y ─────> Integer object: 10
```

The assignment `x = 20` does not modify the integer object `10`. It rebinds the name `x`.

Integers are immutable in Python, meaning their values cannot be changed in place.

### Using the variables

```python
x = 10
y = x
x = 20
z = x + y
```

The result is:

```python
x  # 20
y  # 10
z  # 30
```

The addition evaluates to `30`, and `z` is bound to the resulting integer object.

**Key idea:** A variable name is not the object itself. A name refers to an object.

---

## 6. Stack vs Heap

| Stack | Heap |
|---|---|
| Commonly manages active function calls | Commonly stores dynamically allocated objects |
| Uses stack frames to track execution | Holds objects whose lifetimes are managed by the runtime |
| Function-call frames are normally removed when calls return | Objects can outlive the function that created them |
| Has a limited amount of available space | Has limits determined by the process, runtime, and system |

These are general concepts, not absolute rules for every language or runtime.

In particular, Python does not follow the simple rule that all variables live on the stack and all objects live on the heap in exactly the same way as C.

---

## 7. What Happens When a Function Returns?

Consider:

```python
def create_number():
    value = 100
    return value

result = create_number()
```

Conceptually:

1. `create_number()` is called.
2. A function-call frame becomes active.
3. `value` is bound to the integer object representing `100`.
4. The function returns the object.
5. The function's execution frame is no longer active.
6. `result` is bound to the returned object.

The function's local name `value` no longer exists as a local name in an active call frame, but the returned object remains accessible through `result`.

This illustrates an important distinction:

**A function's local variable can disappear while the object it referred to continues to exist.**

The object's lifetime depends on whether it remains reachable and on the memory-management rules of the runtime.

---

## 8. Object Lifetime and Garbage Collection

Python manages object memory automatically.

In CPython, two important mechanisms are:

### Reference counting

CPython keeps track of references to objects. When an object's reference count reaches zero, the object can generally be deallocated immediately.

### Garbage collection

Reference counting alone cannot reclaim every unreachable object. For example, two objects might refer to each other even though neither is reachable from the running program.

Python's cyclic garbage collector can detect and collect certain groups of unreachable objects.

You generally do not need to manually free ordinary Python objects, unlike dynamically allocated memory in languages such as C.

However, automatic memory management does not mean that memory usage can never grow unnecessarily. Keeping references to objects that are no longer needed can still cause memory leaks at the application level.

---

## 9. Virtual Memory vs Physical Memory

### Physical memory (RAM)

The actual hardware memory installed in the computer.

### Virtual memory

The address space a process uses. Each process normally operates with its own virtual address space, isolated from those of other processes.

The operating system and memory-management hardware translate virtual addresses into physical locations or handle cases where the memory is not currently resident in RAM.

Benefits include:

- Process isolation.
- Protection between processes.
- A convenient address space for each process.
- Flexible memory allocation and management.

Virtual memory is not simply another name for RAM, and it does not mean that every virtual address corresponds to a permanently occupied physical RAM location.

---

## 10. Final Mental Model

When a program runs:

1. The operating system creates a process and gives it a virtual address space.
2. The process has memory regions for different purposes.
3. The stack helps manage active function calls.
4. The heap and runtime allocators support dynamic object allocation.
5. Python names are bound to objects; assignment does not necessarily copy an object.
6. Reassigning a name changes what it refers to, not necessarily the object it previously referred to.
7. Objects can remain alive after a function returns if they are still referenced.
8. Python manages object lifetimes automatically, using mechanisms such as reference counting and garbage collection in CPython.

The most important concept from this session is:

**Names, references, and objects are different things. Understanding that distinction makes Python's behavior much easier to reason about.**
