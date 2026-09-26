# Contiguous Memory Allocation Simulator

A Python-based Operating Systems project that simulates contiguous memory allocation using First Fit, Best Fit, and Worst Fit algorithms.

## Features

- First Fit allocation
- Best Fit allocation
- Worst Fit allocation
- Compare all three algorithms
- Process allocation table
- Memory block visualization
- Remaining memory calculation
- Memory utilization calculation
- Allocation statistics
- Comparison charts
- Input validation and error handling
- Interactive Streamlit GUI

## Technologies

- Python
- Streamlit
- HTML
- CSS

## Project Structure

```text
OsProject/
│
├── app.py
├── algorithms.py
├── requirements.txt
├── PROJECT.md
└── README.md
```

### `app.py`

Contains the Streamlit graphical interface, input validation, result display, memory visualization, statistics, and algorithm comparison.

### `algorithms.py`

Contains the implementations of:

- `first_fit()`
- `best_fit()`
- `worst_fit()`

### `requirements.txt`

Contains the required Python dependency:

```text
streamlit
```

## Input

### Memory Block Sizes

Enter memory block sizes separated by commas.

Example:

```text
100, 500, 200, 300, 600
```

### Process Sizes

Enter process sizes separated by commas.

Example:

```text
212, 417, 112, 426
```

## Algorithms

### First Fit

Allocates each process to the first available memory block that is large enough.

### Best Fit

Allocates each process to the smallest available memory block that can accommodate it.

### Worst Fit

Allocates each process to the largest available memory block that can accommodate it.

## Example

Input:

```text
Memory Blocks:
100, 500, 200, 300, 600

Processes:
212, 417, 112, 426
```

Example allocation results:

```text
First Fit:
P1 → B2
P2 → B5
P3 → B2
P4 → Unallocated

Best Fit:
P1 → B4
P2 → B2
P3 → B3
P4 → B5

Worst Fit:
P1 → B5
P2 → B2
P3 → B5
P4 → Unallocated
```

## Installation

Make sure Python is installed:

```bash
python --version
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Run:

```bash
python -m streamlit run app.py
```

The application will open in the browser at:

```text
http://localhost:8501
```

## Input Validation

The application rejects:

- Empty input
- Non-numeric values
- Extra commas
- Zero values
- Negative values

Processes that cannot fit into any available memory block are displayed as **Unallocated**.

## Workflow

```text
Start
  ↓
Enter Memory Blocks
  ↓
Enter Process Sizes
  ↓
Validate Input
  ↓
Select Algorithm
  ↓
Run Simulation
  ↓
Allocate Processes
  ↓
Calculate Remaining Memory
  ↓
Display Results
  ↓
Display Visualization
  ↓
Compare Algorithms
  ↓
End
```

## Project Documentation

For detailed project documentation, algorithms, examples, workflow, and implementation details, see:

`PROJECT.md`

## License

This project is developed as an academic Operating Systems project.
