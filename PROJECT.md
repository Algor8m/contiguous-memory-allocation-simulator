# Contiguous Memory Allocation Simulator

## 1. Project Overview

The Contiguous Memory Allocation Simulator is an Operating Systems project that demonstrates how processes are allocated to available memory blocks using different contiguous memory allocation strategies.

The simulator implements three classical memory allocation algorithms:

- First Fit
- Best Fit
- Worst Fit

The application provides a graphical interface where users can enter memory block sizes and process sizes, select an allocation algorithm, and observe the resulting memory allocation.

---

## 2. Objective

The main objective of this project is to simulate and understand contiguous memory allocation techniques used in Operating Systems.

The simulator allows users to:

- Define memory blocks.
- Define processes with different memory requirements.
- Allocate processes using different allocation strategies.
- Identify allocated and unallocated processes.
- View remaining memory in each block.
- Compare the behavior of First Fit, Best Fit, and Worst Fit.

---

## 3. Inputs

The simulator accepts two main inputs.

### Memory Block Sizes

The available memory is divided into blocks.

Example:

```text
100, 500, 200, 300, 600
```

This represents:

```text
B1 = 100 KB
B2 = 500 KB
B3 = 200 KB
B4 = 300 KB
B5 = 600 KB
```

### Process Sizes

Each process requires a certain amount of memory.

Example:

```text
212, 417, 112, 426
```

This represents:

```text
P1 = 212 KB
P2 = 417 KB
P3 = 112 KB
P4 = 426 KB
```

---

## 4. Outputs

The simulator produces:

- Process allocation information.
- Allocated memory block for each process.
- Unallocated processes.
- Remaining memory in each block.
- Used memory.
- Memory utilization.
- Memory visualization.
- Comparison of all three algorithms.
- Process allocation comparison chart.
- Memory utilization comparison chart.

---

## 5. Algorithms

### 5.1 First Fit

First Fit searches the memory blocks from the beginning and allocates a process to the first block that is large enough.

#### Basic Procedure

1. Start from the first memory block.
2. Check whether the block can accommodate the process.
3. If it can, allocate the process.
4. If it cannot, move to the next block.
5. Continue until a suitable block is found.
6. If no suitable block exists, the process remains unallocated.

---

### 5.2 Best Fit

Best Fit searches all available memory blocks and allocates the process to the smallest block that is large enough.

#### Basic Procedure

1. Examine all memory blocks.
2. Find blocks that can accommodate the process.
3. Select the smallest suitable block.
4. Allocate the process.
5. Update the remaining memory.
6. If no suitable block exists, the process remains unallocated.

---

### 5.3 Worst Fit

Worst Fit searches all available memory blocks and allocates the process to the largest available block that can accommodate it.

#### Basic Procedure

1. Examine all memory blocks.
2. Find blocks that can accommodate the process.
3. Select the largest suitable block.
4. Allocate the process.
5. Update the remaining memory.
6. If no suitable block exists, the process remains unallocated.

---

## 6. Example

### Input

```text
Memory Blocks:
100, 500, 200, 300, 600

Processes:
212, 417, 112, 426
```

### First Fit

```text
P1 → B2
P2 → B5
P3 → B2
P4 → Unallocated
```

Remaining memory:

```text
B1 = 100 KB
B2 = 176 KB
B3 = 200 KB
B4 = 300 KB
B5 = 183 KB
```

---

### Best Fit

```text
P1 → B4
P2 → B2
P3 → B3
P4 → B5
```

Remaining memory:

```text
B1 = 100 KB
B2 = 83 KB
B3 = 88 KB
B4 = 88 KB
B5 = 174 KB
```

---

### Worst Fit

```text
P1 → B5
P2 → B2
P3 → B5
P4 → Unallocated
```

Remaining memory:

```text
B1 = 100 KB
B2 = 83 KB
B3 = 200 KB
B4 = 300 KB
B5 = 276 KB
```

---

## 7. Project Architecture

The project consists of three main files:

```text
OsProject/
│
├── app.py
├── algorithms.py
└── requirements.txt
```

### app.py

Responsible for the graphical user interface.

Functions include:

- Accepting user input.
- Validating input.
- Selecting algorithms.
- Displaying allocation results.
- Displaying memory visualization.
- Displaying statistics.
- Displaying comparison charts.

### algorithms.py

Contains the implementation of:

```text
first_fit()
best_fit()
worst_fit()
```

The algorithms perform the actual memory allocation calculations.

### requirements.txt

Contains the Python dependency required by the application:

```text
streamlit
```

---

## 8. Technologies Used

- Python
- Streamlit
- HTML
- CSS

Python is used for the allocation algorithms and application logic.

Streamlit is used to create the graphical user interface.

HTML and CSS are used to customize the appearance of the interface.

---

## 9. Input Validation

The application validates user input before running the algorithms.

The following invalid inputs are rejected:

- Empty input.
- Non-numeric values.
- Extra commas.
- Zero values.
- Negative values.

For example:

```text
100,,300
```

is rejected because it contains an empty value.

Similarly:

```text
100,abc,300
```

is rejected because `abc` is not a number.

---

## 10. User Interface

The application provides:

### Memory Configuration

Users enter:

```text
Memory Block Sizes
Process Sizes
```

### Allocation Strategy

Users can select:

```text
First Fit
Best Fit
Worst Fit
Compare All Algorithms
```

### Results

The application displays:

- Process allocation table.
- Allocated processes.
- Unallocated processes.
- Used memory.
- Memory utilization.
- Memory block visualization.

---

## 11. Algorithm Comparison

When the user selects **Compare All Algorithms**, the application executes:

```text
First Fit
Best Fit
Worst Fit
```

The results are displayed together.

The comparison includes:

- Number of allocated processes.
- Number of unallocated processes.
- Remaining memory.
- Memory utilization.

The application also generates comparison charts.

---

## 12. How to Run the Project

### Step 1: Install Python

Make sure Python is installed on the system.

Check using:

```bash
python --version
```

### Step 2: Install Dependencies

Open a terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Run:

```bash
python -m streamlit run app.py
```

The application will open in the browser.

The default local address is:

```text
http://localhost:8501
```

---

## 13. Project Workflow

The overall workflow is:

```text
Start
  ↓
Enter Memory Blocks
  ↓
Enter Process Sizes
  ↓
Validate Input
  ↓
Select Allocation Algorithm
  ↓
Run Algorithm
  ↓
Allocate Processes
  ↓
Calculate Remaining Memory
  ↓
Display Results
  ↓
Display Memory Visualization
  ↓
Compare Algorithms
  ↓
End
```

---

## 14. Project Features

The simulator provides the following features:

- Interactive graphical interface.
- First Fit simulation.
- Best Fit simulation.
- Worst Fit simulation.
- Algorithm comparison.
- Process allocation table.
- Memory block visualization.
- Remaining memory calculation.
- Memory utilization calculation.
- Allocation statistics.
- Comparison charts.
- Input validation.
- Error handling.

---

## 15. Conclusion

The Contiguous Memory Allocation Simulator provides an interactive way to understand and visualize classical memory allocation strategies.

By allowing the same memory and process configuration to be tested with First Fit, Best Fit, and Worst Fit, the simulator demonstrates how different allocation strategies can produce different memory allocation results.

The project combines Operating Systems concepts with a Python-based graphical interface to create a practical memory management simulation.
