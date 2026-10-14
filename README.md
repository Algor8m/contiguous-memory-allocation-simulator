# Contiguous Memory Allocation Simulator

A Python-based interactive simulator for demonstrating **contiguous memory allocation** in Operating Systems using the **First Fit, Best Fit, and Worst Fit** algorithms.

The application provides a Streamlit web interface where users can configure memory blocks and process sizes, execute allocation strategies, visualize memory utilization, analyze fragmentation, and compare algorithm performance.

## Features

- **Memory Allocation Algorithms**
  - First Fit
  - Best Fit
  - Worst Fit
- **Custom Inputs:** Configure memory block sizes and process sizes.
- **Allocation Results:** View process allocation status and unallocated processes.
- **Fragmentation Analysis:** Calculate internal and external fragmentation.
- **Memory Utilization:** Analyze allocated memory, remaining memory, and utilization percentage.
- **Memory Visualization:** View a proportional RAM strip with distinct partition and process indicators.
- **Partition Details:** Examine partition usage through individual cards and progress bars.
- **Decision Trace:** Follow step-by-step allocation decisions for each algorithm.
- **Algorithm Comparison:** Compare the results of all three allocation strategies.
- **Academic Reference Guide:** Review key concepts related to Operating Systems memory management.
- **Input Validation:** Handle empty inputs, non-numeric values, zero and negative values, and malformed comma-separated inputs.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Streamlit | Interactive web interface |
| Pandas | Tabular data processing and presentation |
| Git | Version control |
| GitHub | Source code hosting |

## Project Structure

```text
contiguous-memory-allocation-simulator/
│
├── app.py
├── algorithms.py
├── requirements.txt
├── README.md
├── PROJECT.md
├── Contiguous_Memory_Allocation_Simulator_Final_Report.docx
├── Contiguous_Memory_Allocation_Simulator_Presentation.pptx
├── Contiguous_Memory_Allocation_Simulator_Report.md
└── contiguous_memory_allocation_flowchart.png
```

### File Descriptions

- `app.py` — Implements the Streamlit application interface, input handling, result presentation, and visualization.
- `algorithms.py` — Contains the memory allocation algorithms and their associated logic.
- `requirements.txt` — Lists the Python dependencies required to run the application.
- `PROJECT.md` — Provides detailed project documentation.
- `Contiguous_Memory_Allocation_Simulator_Final_Report.docx` — Contains the final project report.
- `Contiguous_Memory_Allocation_Simulator_Presentation.pptx` — Contains the project presentation.
- `Contiguous_Memory_Allocation_Simulator_Report.md` — Provides the project report in Markdown format.
- `contiguous_memory_allocation_flowchart.png` — Illustrates the system workflow.

## How It Works

The simulator accepts three primary inputs:

1. Memory block sizes
2. Process sizes
3. Memory allocation algorithm

It processes the inputs using the selected allocation strategy and presents the allocation results, remaining memory, fragmentation metrics, utilization statistics, and a visual representation of memory.

### Example Input

**Memory Blocks**
```text
100, 500, 200, 300, 600
```

**Processes**
```text
212, 417, 112, 426
```

### Outputs

The simulator displays:

- Process-to-block allocation details
- Allocated and unallocated process counts
- Remaining memory in each block
- Used and remaining memory
- Internal and external fragmentation metrics
- Memory utilization percentage
- Visual memory map
- Step-by-step allocation trace
- Comparative results for all three algorithms

## Allocation Algorithms

### 1. First Fit

First Fit searches the available memory blocks in their original order and allocates a process to the first block that satisfies its memory requirement.

**Approach:**
1. Traverse the memory blocks from the beginning.
2. Find the first suitable block.
3. Allocate the process if the block can accommodate it.
4. Continue with the next process.

**Advantage:** Simple and generally fast because the search stops at the first suitable block.

### 2. Best Fit

Best Fit selects the smallest available block that can accommodate the process.

**Approach:**
1. Examine all suitable memory blocks.
2. Identify the smallest block that satisfies the process requirement.
3. Allocate the process to that block.
4. Continue with the next process.

**Advantage:** Attempts to minimize the unused space within the selected block.

### 3. Worst Fit

Worst Fit selects the largest available block that can accommodate the process.

**Approach:**
1. Examine the available memory blocks.
2. Identify the largest suitable block.
3. Allocate the process to that block.
4. Continue with the next process.

**Advantage:** Attempts to leave relatively large unused memory regions for future allocations.

## Installation

### Prerequisites

Ensure that the following are installed:

- Python 3
- pip
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/Algor8m/contiguous-memory-allocation-simulator.git
```

### Step 2: Navigate to the Project Directory

```bash
cd contiguous-memory-allocation-simulator
```

### Step 3: Create a Virtual Environment (Optional)

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python -m streamlit run app.py
```

The application will start locally, and Streamlit will provide a URL to access the interactive interface in your web browser.

## Example Test Case

**Memory Blocks**
```text
100, 500, 200, 300, 600
```

**Processes**
```text
212, 417, 112, 426
```

The simulator evaluates these inputs using each allocation algorithm and displays the resulting allocation map, process statuses, fragmentation metrics, and memory utilization.

Results may differ depending on the allocation rules implemented, including whether allocated blocks can accommodate multiple processes and how remaining memory is tracked.

## Input Validation

The application validates user inputs to prevent invalid data from disrupting execution.

Supported validation scenarios include:

- Empty input fields
- Non-numeric values
- Zero-sized values
- Negative values
- Extra commas or malformed comma-separated input

**Example of invalid input:**
```text
100, 500,, 300
```

The application displays an appropriate validation message instead of terminating unexpectedly.

## Memory Management Concepts

### Internal Fragmentation

Internal fragmentation refers to memory allocated to a process that remains unused within its assigned partition.

### External Fragmentation

External fragmentation occurs when available memory is distributed across separate free regions, preventing a process from being allocated despite sufficient total free memory.

### Memory Utilization

Memory utilization represents the proportion of total memory currently in use.

A common calculation is:

\[
\text{Memory Utilization (\%)} =
\frac{\text{Used Memory}}{\text{Total Memory}} \times 100
\]

The precise fragmentation and utilization calculations depend on the simulator's allocation model and implementation.

## Documentation

The repository includes the following supporting resources:

- `PROJECT.md` — Detailed project documentation
- `Contiguous_Memory_Allocation_Simulator_Final_Report.docx` — Final project report
- `Contiguous_Memory_Allocation_Simulator_Presentation.pptx` — Project presentation
- `Contiguous_Memory_Allocation_Simulator_Report.md` — Markdown report
- `contiguous_memory_allocation_flowchart.png` — System flowchart

## Project Objective

The objective of this project is to demonstrate and compare contiguous memory allocation strategies used in Operating Systems.

The simulator provides an interactive learning environment for understanding how allocation decisions affect process placement, memory utilization, fragmentation, and the availability of memory for subsequent processes.

## Academic Context

This project was developed as an academic **Operating Systems mini project**. It combines algorithm implementation, interactive visualization, input validation, and comparative analysis to support practical learning of memory management concepts.

## License

This project was developed for academic purposes. No separate open-source license is specified in this repository.

---

**Repository:** [contiguous-memory-allocation-simulator](https://github.com/Algor8m/contiguous-memory-allocation-simulator)