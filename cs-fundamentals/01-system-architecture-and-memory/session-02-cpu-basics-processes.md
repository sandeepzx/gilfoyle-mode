# Session 2: CPU Basics and Processes

## 1. CPU Basics

The CPU (Central Processing Unit) executes machine instructions. It fetches instructions, decodes them, and performs the required operations.

### Important CPU components

- **Registers:** Very small, fast storage locations inside the CPU that hold values needed for current execution.
- **Program Counter / Instruction Pointer:** Identifies the instruction the CPU should execute next. Exact behavior depends on the instruction and architecture.
- **CPU cache:** Stores copies of frequently or recently accessed memory data to reduce the time spent waiting for RAM.
- **CPU clock frequency:** The number of clock cycles per second, measured in hertz. A higher frequency does not automatically mean proportionally higher performance.

### Physical cores and logical CPUs

- **CPU package:** The physical processor installed in the computer.
- **Physical core:** A processing core within the CPU package.
- **Logical CPU:** An execution context exposed by the processor to the operating system. With SMT (Simultaneous Multithreading), one physical core can expose multiple logical CPUs.

My laptop:
- CPU package: 1
- Physical cores: 2
- Logical CPUs: 4

The two logical CPUs associated with one physical core share some execution resources. Therefore, four logical CPUs do not provide the same resources as four independent physical cores.

A computer's number of CPUs does not determine its purpose. It describes the processing hardware, not whether the machine is a server, desktop, or special-purpose system.

## 2. Processes

A **process** is a running instance of a program, managed by the operating system.

A process typically has:
- A process ID (PID)
- An execution state
- Its own virtual address space
- Resources and operating-system bookkeeping
- One or more threads

A program is a set of instructions stored as a file or other representation. A process is an executing instance of a program.

For example, running a Python script creates a process:

```bash
python3 script.py
```

The OS assigns the process an identifier, called its PID.

## 3. Threads

A **thread** is an execution path within a process. The operating system schedules threads to run on logical CPUs.

A process can have one or multiple threads.

Threads in the same process generally share:
- The process's address space and heap
- Global data
- Open resources such as file descriptors, subject to operating-system semantics

Each thread has its own execution state, including:
- Instruction pointer
- CPU registers
- Stack and stack pointer

Because threads share process memory, they can communicate through shared data. However, concurrent access to shared mutable data can cause race conditions unless appropriately synchronized.

### Process versus thread

| Process | Thread |
|---|---|
| Running instance of a program | Execution path within a process |
| Has its own virtual address space | Shares its process's address space |
| Can contain multiple threads | Belongs to a process |
| Process isolation generally separates memory spaces | Threads in one process can access shared memory |

## 4. Inspecting Threads on Ubuntu

A useful command is:

```bash
ps -T -p PID
```

Replace `PID` with the process ID you want to inspect.

For example, if the process ID is `6591`:

```bash
ps -T -p 6591
```

The output includes columns such as:

- `PID`: process ID
- `SPID`: thread ID on Linux
- `TTY`: controlling terminal
- `TIME`: accumulated CPU time
- `CMD`: command name

In the Python thread demonstration, the output showed four rows with the same PID and different SPIDs. This indicated four threads belonging to one process.

On Linux, the main thread's thread ID is normally the same as the process ID shown by `ps`.

**Important:** Four threads in a process do not necessarily execute simultaneously. Their execution depends on the number of available logical CPUs, scheduling, and resource availability.

## 5. Process States

A simplified process/thread state model includes:

### Ready (Runnable)
The task can run but is waiting for CPU time.

### Running
The task is currently executing on a logical CPU.

### Blocked (Waiting)
The task cannot currently proceed because it is waiting for an event, such as completion of an I/O operation.

For example, suppose a process requests data from a disk:

1. The process requests disk I/O.
2. It cannot continue until the required data is available.
3. The OS blocks the relevant task.
4. Another runnable task can use the CPU.
5. When the I/O completes, the waiting task can become runnable again.

The process does not need to keep consuming CPU time while waiting for slow I/O.

Real operating systems have more detailed state models than this simplified explanation.

## 6. Scheduling and Time Slices

The **scheduler** decides which runnable task should execute on a logical CPU.

When multiple tasks need CPU time, the OS can give them opportunities to run according to its scheduling policies.

A **time slice** is a period of CPU execution allocated to a task under a scheduling scheme.

When a timer interrupt occurs, the OS gets an opportunity to regain control and reconsider scheduling. A timer interrupt does not necessarily cause a context switch every time; the scheduler may decide that the current task should continue.

## 7. Context Switching

A **context switch** occurs when the CPU stops executing one task and starts executing another, preserving enough execution state so the previous task can resume later.

A simplified sequence:

1. Thread A is executing.
2. An event occurs, such as a timer interrupt or A blocking for I/O.
3. The OS takes control.
4. The relevant execution state of A is preserved.
5. The scheduler selects another runnable thread, B.
6. The CPU restores B's execution state and resumes B.

Context switches allow multiple tasks to share CPU resources.

### What execution state must be preserved?

The exact state depends on the processor architecture and operating system, but relevant state can include:

- Instruction pointer / program counter
- CPU registers
- Stack pointer
- Other architecture-specific execution state

The instruction pointer matters because the CPU must know where the thread should resume.

### What happens to the program's memory?

The OS does **not** normally save the entire contents of a process's RAM to a special file every time a context switch occurs.

Most of the process's memory remains in memory. The OS preserves the execution state required to pause and resume its threads.

Context switching has overhead: saving and restoring state takes work, and switching tasks can also affect cache and other hardware state.

## 8. Process Control Block (PCB)

A **Process Control Block (PCB)** is a textbook operating-system concept describing the data the OS maintains to manage a process.

Conceptually, it can include:
- Process ID
- Process state
- Scheduling information
- Memory-management information
- Resource and accounting information

The PCB is not necessarily one literal structure containing every detail. Linux uses several related kernel structures, including process-level and thread-level structures, to manage execution.

The PID identifies a process. Thread identifiers distinguish individual threads.

## 9. Concurrency and Parallelism

These terms are related but different.

### Concurrency
Multiple tasks make progress during overlapping periods. On one logical CPU, the OS can switch between tasks so they each make progress.

### Parallelism
Multiple tasks execute at the same time using different execution resources.

On my laptop, four runnable threads can potentially be scheduled across four logical CPUs. However, because two logical CPUs share each physical core's resources through SMT, the performance may differ from a machine with four physical cores.

## 10. Quick Reference

| Concept | Meaning |
|---|---|
| CPU package | Physical processor |
| Physical core | Processing core inside a CPU package |
| Logical CPU | Hardware execution context visible to the OS |
| Process | Running instance of a program |
| Thread | Execution path within a process |
| PID | Process identifier |
| TID / SPID | Thread identifier in the relevant Linux output |
| Ready | Able to run, waiting for CPU time |
| Running | Currently executing |
| Blocked | Waiting for an event |
| Scheduler | Selects runnable tasks for CPU execution |
| Time slice | Period of CPU execution allocated to a task |
| Context switch | Switching execution from one task to another while preserving its state |
| PCB | Conceptual OS bookkeeping structure for a process |

## 11. Key Mental Models

1. A program is not the same thing as a process: the program provides instructions; the process is an executing instance.
2. A process can contain multiple threads.
3. Threads in one process share memory but have their own execution state.
4. A blocked task can wait without continuously using the CPU.
5. A context switch preserves execution state; it does not normally copy the entire process memory to disk.
6. A timer interrupt gives the OS an opportunity to reconsider scheduling; it does not guarantee a context switch.
7. Multiple logical CPUs allow potential parallel execution, but logical CPUs sharing a physical core do not equal independent physical cores.
8. OS scheduling, process states, and context switching explain how a computer runs many applications even with limited CPU resources.

## Session Status

**Completed:** CPU basics, processes, threads, process states, scheduling, time slices, context switching, PCB, and logical CPUs.

