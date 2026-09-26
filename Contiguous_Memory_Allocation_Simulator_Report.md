# CONTIGUOUS MEMORY ALLOCATION SIMULATOR

## Operating Systems Mini Project Report

---

## 1. Introduction

Memory management is one of the fundamental responsibilities of an operating system. When processes need to be loaded into memory, the operating system must decide where each process should be placed while making effective use of the available memory.

This project implements a **Contiguous Memory Allocation Simulator** that demonstrates three classical memory allocation strategies:

- First Fit
- Best Fit
- Worst Fit

The simulator accepts memory block sizes and process sizes as input and shows how each process is allocated. It also displays unallocated processes, remaining memory, memory utilization, and a comparison of the three algorithms.

The project is implemented in Python with a Streamlit-based graphical user interface.

---

## 2. Problem Statement

The objective of this project is to develop a simulator that demonstrates how contiguous memory allocation algorithms assign processes to available memory blocks.

The simulator should:

- Accept memory block sizes as input.
- Accept process sizes as input.
- Allocate processes using First Fit, Best Fit, or Worst Fit.
- Identify processes that cannot be allocated.
- Calculate the remaining memory in each block.
- Display memory utilization.
- Compare the results of all three allocation algorithms.

---

## 3. Objectives

The main objectives of the project are:

1. To understand contiguous memory allocation.
2. To implement First Fit allocation.
3. To implement Best Fit allocation.
4. To implement Worst Fit allocation.
5. To visualize the allocation of processes into memory blocks.
6. To calculate remaining and used memory.
7. To compare the behavior of different allocation strategies.
8. To provide an interactive graphical interface for experimentation.

---

## 4. System Requirements

### Hardware Requirements

- Computer/Laptop
- Minimum 4 GB RAM
- Keyboard and mouse
- Display

### Software Requirements

- Windows/Linux/macOS
- Python 3.x
- Streamlit
- Web browser
- Visual Studio Code or another Python-compatible editor

---

## 5. Input and Output

### Inputs

The simulator accepts:

1. Memory block sizes in KB.
2. Process sizes in KB.
3. Allocation algorithm.

Example:

```text
Memory Blocks:
100, 500, 200, 300, 600

Processes:
212, 417, 112, 426
```

### Outputs

The simulator produces:

- Process allocation
- Allocated and unallocated processes
- Remaining memory in every block
- Used memory
- Memory utilization
- Memory visualization
- Algorithm comparison

---

## 6. System Flowchart

The overall flow of the simulator is:

```text
START
  |
  v
Enter Memory Block Sizes
  |
  v
Enter Process Sizes
  |
  v
Input Valid?
 /        \
NO        YES
 |          |
 v          v
Display     Select Allocation
Error       Algorithm
 |          |
 v          v
END      Run Algorithm
             |
             v
       Allocate Processes
             |
             v
      Calculate Remaining
          Memory
             |
             v
      Calculate Memory
         Utilization
             |
             v
      Display Allocation
          Results
             |
             v
      Display Memory
       Visualization
             |
             v
      Display Algorithm
         Comparison
             |
             v
            END
```

**Figure 1:** System flowchart of the Contiguous Memory Allocation Simulator.

The generated flowchart image is included separately as:

`contiguous_memory_allocation_flowchart.png`

---

## 7. Algorithms Used

### 7.1 First Fit

First Fit searches the memory blocks from the beginning and allocates a process to the first block that is large enough to contain it.

#### Procedure

1. Start from the first memory block.
2. Check whether the block can accommodate the process.
3. If sufficient space is available, allocate the process.
4. Reduce the remaining size of the selected block.
5. If the block is insufficient, continue to the next block.
6. If no suitable block is found, the process remains unallocated.

#### Pseudocode

```text
FOR each process:
    FOR each memory block:
        IF block is large enough:
            allocate process
            reduce remaining block size
            BREAK
```

---

### 7.2 Best Fit

Best Fit searches all available memory blocks and allocates the process to the smallest block that is large enough.

#### Procedure

1. Examine all memory blocks.
2. Identify blocks that can accommodate the process.
3. Select the smallest suitable block.
4. Allocate the process.
5. Reduce the remaining size of that block.
6. If no suitable block exists, leave the process unallocated.

#### Pseudocode

```text
FOR each process:
    Find the smallest block that can contain it
    IF such a block exists:
        allocate process
        reduce remaining block size
```

---

### 7.3 Worst Fit

Worst Fit searches the available memory blocks and allocates the process to the largest suitable block.

#### Procedure

1. Examine all memory blocks.
2. Identify blocks that can accommodate the process.
3. Select the largest suitable block.
4. Allocate the process.
5. Reduce the remaining size of that block.
6. If no suitable block exists, leave the process unallocated.

#### Pseudocode

```text
FOR each process:
    Find the largest block that can contain it
    IF such a block exists:
        allocate process
        reduce remaining block size
```

---

## 8. System Design

The project is divided into two main components.

### 8.1 Algorithm Module

File:

```text
algorithms.py
```

This module contains:

```text
first_fit()
best_fit()
worst_fit()
```

Each function receives:

```text
Memory blocks
Process sizes
```

and returns:

```text
Process allocation
Remaining memory
```

### 8.2 Graphical User Interface

File:

```text
app.py
```

The Streamlit application provides:

- Input fields
- Algorithm selection
- Simulation button
- Results tables
- Memory visualization
- Metrics
- Algorithm comparison charts
- Input validation and error messages

---

## 9. Project Structure

```text
OsProject/
│
├── app.py
├── algorithms.py
├── requirements.txt
├── README.md
├── PROJECT.md
└── contiguous_memory_allocation_flowchart.png
```

### File Description

| File | Purpose |
|---|---|
| `app.py` | Streamlit graphical interface and result display |
| `algorithms.py` | First Fit, Best Fit, and Worst Fit implementations |
| `requirements.txt` | Python dependency list |
| `README.md` | Project overview and setup information |
| `PROJECT.md` | Detailed project documentation |
| `contiguous_memory_allocation_flowchart.png` | System flowchart |

---

## 10. Implementation

The project uses Python for the implementation.

The core algorithm module contains three allocation functions.

### First Fit

```python
def first_fit(blocks, processes):
    memory = blocks.copy()
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(memory)):
            if memory[j] >= processes[i]:
                allocation[i] = j
                memory[j] -= processes[i]
                break

    return allocation, memory
```

### Best Fit

```python
def best_fit(blocks, processes):
    memory = blocks.copy()
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        best_index = -1

        for j in range(len(memory)):
            if memory[j] >= processes[i]:
                if best_index == -1 or memory[j] < memory[best_index]:
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            memory[best_index] -= processes[i]

    return allocation, memory
```

### Worst Fit

```python
def worst_fit(blocks, processes):
    memory = blocks.copy()
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        worst_index = -1

        for j in range(len(memory)):
            if memory[j] >= processes[i]:
                if worst_index == -1 or memory[j] > memory[worst_index]:
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            memory[worst_index] -= processes[i]

    return allocation, memory
```

---

## 11. User Interface

The graphical interface contains the following major sections:

### Header

Displays the project name and memory management simulation label.

### Memory Configuration

The user enters memory block sizes.

Example:

```text
100, 500, 200, 300, 600
```

### Process Configuration

The user enters process sizes.

Example:

```text
212, 417, 112, 426
```

### Allocation Strategy

The user can select:

- First Fit
- Best Fit
- Worst Fit
- Compare All Algorithms

### Results

The application displays:

- Process allocation table
- Number of allocated processes
- Number of unallocated processes
- Used memory
- Memory utilization
- Memory block visualization

---

## 12. Input Validation

The application validates user input before running an algorithm.

The following conditions are handled:

### Empty Input

```text
Input cannot be empty.
```

### Non-numeric Input

Example:

```text
100, 500, abc, 300
```

The application displays an error instead of terminating.

### Negative or Zero Values

Example:

```text
100, 500, -200, 300
```

Values must be greater than zero.

### Extra Commas

Example:

```text
100, 500,, 300
```

The application detects the invalid input.

---

## 13. Test Case

The following test data was used:

```text
Memory Blocks:
100, 500, 200, 300, 600

Processes:
212, 417, 112, 426
```

Total memory:

```text
1700 KB
```

Total process memory:

```text
1167 KB
```

---

## 14. Results

### 14.1 First Fit

Process allocation:

| Process | Size | Block |
|---|---:|---|
| P1 | 212 KB | B2 |
| P2 | 417 KB | B5 |
| P3 | 112 KB | B2 |
| P4 | 426 KB | Unallocated |

Remaining memory:

```text
B1 = 100 KB
B2 = 176 KB
B3 = 200 KB
B4 = 300 KB
B5 = 183 KB
```

Allocated processes:

```text
3
```

Unallocated processes:

```text
1
```

---

### 14.2 Best Fit

Process allocation:

| Process | Size | Block |
|---|---:|---|
| P1 | 212 KB | B4 |
| P2 | 417 KB | B2 |
| P3 | 112 KB | B3 |
| P4 | 426 KB | B5 |

Remaining memory:

```text
B1 = 100 KB
B2 = 83 KB
B3 = 88 KB
B4 = 88 KB
B5 = 174 KB
```

Allocated processes:

```text
4
```

Unallocated processes:

```text
0
```

---

### 14.3 Worst Fit

Process allocation:

| Process | Size | Block |
|---|---:|---|
| P1 | 212 KB | B5 |
| P2 | 417 KB | B2 |
| P3 | 112 KB | B5 |
| P4 | 426 KB | Unallocated |

Remaining memory:

```text
B1 = 100 KB
B2 = 83 KB
B3 = 200 KB
B4 = 300 KB
B5 = 276 KB
```

Allocated processes:

```text
3
```

Unallocated processes:

```text
1
```

---

## 15. Algorithm Comparison

For the test case:

| Algorithm | Allocated Processes | Unallocated Processes |
|---|---:|---:|
| First Fit | 3 | 1 |
| Best Fit | 4 | 0 |
| Worst Fit | 3 | 1 |

The application presents this comparison through a table and graphical charts.

The purpose of the comparison is to demonstrate that different allocation strategies can produce different memory distributions for the same input.

The simulator does not assume that one strategy will produce the same result for every possible input; results depend on the memory block and process sizes provided.

---

## 16. Memory Utilization

Memory utilization is calculated using:

```text
Memory Utilization =
(Used Memory / Total Memory) × 100
```

For the example input:

```text
Total Memory = 1700 KB
Total Process Memory = 1167 KB
```

For Best Fit, all four processes are allocated, so:

```text
Used Memory = 1167 KB
```

and:

```text
Memory Utilization ≈ 68.65%
```

For First Fit and Worst Fit, the allocated processes occupy:

```text
741 KB
```

Therefore:

```text
Memory Utilization ≈ 43.59%
```

---

## 17. Advantages

- Simple and interactive interface.
- Demonstrates important operating-system memory allocation concepts.
- Supports three classical allocation algorithms.
- Allows custom memory and process inputs.
- Provides visual representation of memory blocks.
- Provides algorithm comparison.
- Includes input validation.
- Easy to run and modify.

---

## 18. Limitations

- The simulator models partition-based contiguous allocation and does not represent a complete operating-system memory manager.
- It does not simulate virtual memory.
- It does not simulate paging or segmentation.
- It does not model real hardware memory.
- Allocation results depend on the order of processes and memory blocks entered by the user.

---

## 19. Future Enhancements

Possible future improvements include:

- Adding more allocation algorithms.
- Adding internal/external fragmentation analysis.
- Adding animated allocation visualization.
- Adding memory deallocation.
- Adding process arrival and termination.
- Adding allocation history.
- Exporting simulation results to CSV or PDF.
- Adding more detailed performance statistics.

---

## 20. Conclusion

The Contiguous Memory Allocation Simulator demonstrates how First Fit, Best Fit, and Worst Fit algorithms allocate processes to memory blocks.

The project provides an interactive way to observe process allocation, remaining memory, memory utilization, and differences between allocation strategies.

Through this implementation, the project demonstrates practical application of operating-system memory management concepts using Python and a graphical user interface.

---

## 21. References

1. Operating Systems concepts and memory-management material provided as part of the course.
2. Python documentation.
3. Streamlit documentation.
