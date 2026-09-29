import os
import streamlit as st
import pandas as pd

from algorithms import first_fit, best_fit, worst_fit

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Contiguous Memory Allocation Simulator",
    page_icon="💾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# COLOR PALETTE
# ============================================================

PRIMARY_RED = "#9E1B32"
HOVER_RED = "#7E1426"
DARK_TEXT = "#111111"
MUTED_TEXT = "#333333"
LIGHT_BG = "#F4F6F8"
CARD_BG = "#FFFFFF"
BORDER_COLOR = "#DDE2E5"

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* Completely hide Streamlit default top ribbon */
header[data-testid="stHeader"] {{
    display: none !important;
}}
#MainMenu, footer {{
    visibility: hidden;
}}

.stApp {{
    background-color: #F4F6F8;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}}
.block-container {{
    padding-top: 1rem !important;
    padding-bottom: 3.5rem;
    max-width: 1350px;
}}
.stApp p, .stApp span, .stApp label, .stApp div {{
    color: {DARK_TEXT};
}}
.header-card {{
    background-color: {CARD_BG};
    border: 1px solid {BORDER_COLOR};
    border-top: 4px solid {PRIMARY_RED};
    border-radius: 6px;
    padding: 22px 26px;
    margin-bottom: 16px;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
}}
.header-tag {{
    color: {PRIMARY_RED} !important;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 4px;
}}
.header-title {{
    color: {DARK_TEXT} !important;
    font-size: 28px;
    font-weight: 800;
    margin: 0;
}}
.header-desc {{
    color: {MUTED_TEXT} !important;
    font-size: 14px;
    margin-top: 6px;
    line-height: 1.5;
}}
.team-container {{
    background-color: #FFFFFF;
    border: 1px solid {BORDER_COLOR};
    border-radius: 6px;
    padding: 10px 16px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}}
.team-title {{
    font-weight: 700;
    font-size: 12.5px;
    color: {PRIMARY_RED} !important;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}}
.student-tag {{
    background-color: #F8F9FA;
    border: 1px solid {BORDER_COLOR};
    border-left: 3px solid {PRIMARY_RED};
    padding: 5px 12px;
    border-radius: 4px;
    font-size: 13px;
    font-weight: 600;
    color: {DARK_TEXT};
}}
.content-panel {{
    background-color: {CARD_BG};
    border: 1px solid {BORDER_COLOR};
    border-radius: 6px;
    padding: 20px;
    margin-top: 16px;
    margin-bottom: 20px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
}}
.section-title {{
    font-size: 18px;
    font-weight: 700;
    color: {DARK_TEXT} !important;
    border-left: 4px solid {PRIMARY_RED};
    padding-left: 10px;
    margin-bottom: 16px;
    margin-top: 20px;
    letter-spacing: 0.3px;
}}
div[data-testid="stTextInput"] label {{
    color: {DARK_TEXT} !important;
    font-weight: 600;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}
div[data-testid="stTextInput"] input {{
    color: {DARK_TEXT} !important;
    background-color: #FFFFFF !important;
    border: 1px solid #CCD2D8 !important;
    border-radius: 4px;
    padding: 8px 12px;
}}
div[data-testid="stTextInput"] input:focus {{
    border-color: {PRIMARY_RED} !important;
    box-shadow: 0 0 0 1px {PRIMARY_RED} !important;
}}
div.stButton > button {{
    background-color: {PRIMARY_RED} !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 4px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.8px !important;
    padding: 10px 16px !important;
    transition: 0.2s ease-in-out;
    width: 100%;
}}
div.stButton > button p {{
    color: #FFFFFF !important;
}}
div.stButton > button:hover {{
    background-color: {HOVER_RED} !important;
}}
div[data-testid="stMetric"] {{
    background-color: #FFFFFF;
    border: 1px solid {BORDER_COLOR};
    border-top: 3px solid {PRIMARY_RED};
    padding: 14px;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
}}
.styled-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0 24px 0;
    font-size: 14px;
    background-color: #FFFFFF;
    border: 1px solid {BORDER_COLOR};
    border-radius: 6px;
    overflow: hidden;
}}
.styled-table thead tr {{
    background-color: {PRIMARY_RED};
    color: #FFFFFF;
    text-align: left;
}}
.styled-table th {{
    padding: 12px 16px;
    color: #FFFFFF !important;
    font-weight: 600;
    font-size: 13px;
    letter-spacing: 0.5px;
}}
.styled-table td {{
    padding: 12px 16px;
    border-bottom: 1px solid {BORDER_COLOR};
    color: {DARK_TEXT};
}}
.styled-table tbody tr:nth-of-type(even) {{
    background-color: #F8F9FA;
}}
.styled-table tbody tr:last-of-type td {{
    border-bottom: none;
}}
.memory-block-card {{
    background-color: #FFFFFF;
    border: 1px solid {BORDER_COLOR};
    border-radius: 6px;
    overflow: hidden;
    margin-bottom: 12px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}}
.memory-block-header {{
    padding: 8px 12px;
    font-weight: 700;
    font-size: 13px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid {BORDER_COLOR};
}}
.block-occupied {{
    background-color: #FDF2F2;
    color: {PRIMARY_RED};
    border-left: 4px solid {PRIMARY_RED};
}}
.block-free {{
    background-color: #F8F9FA;
    color: {MUTED_TEXT};
    border-left: 4px solid #A0AEC0;
}}
.memory-block-body {{
    padding: 12px;
    font-size: 13px;
    line-height: 1.6;
    color: {DARK_TEXT};
}}
.trace-card {{
    background-color: #FFFFFF;
    border: 1px solid {BORDER_COLOR};
    border-left: 4px solid {PRIMARY_RED};
    border-radius: 6px;
    padding: 14px 18px;
    margin-bottom: 10px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}}
.trace-title {{
    font-weight: 700;
    font-size: 14px;
    color: {PRIMARY_RED};
    margin-bottom: 6px;
}}
.trace-step {{
    font-size: 13px;
    color: {DARK_TEXT};
    padding: 2px 0;
}}
</style>""",
    unsafe_allow_html=True,
)

# ============================================================
# COMPREHENSIVE THEORY & CONCEPTS MODAL DIALOG
# ============================================================

@st.dialog("Operating Systems — Memory Management Academic Guide", width="large")
def show_theory_dialog():
    st.subheader("1. Fundamental Concept: Contiguous Memory Allocation")
    st.write(
        "In **contiguous memory allocation**, each program must occupy a single continuous block of physical memory addresses. "
        "This project implements **Fixed Partitioning (Multiprogramming with a Fixed number of Tasks - MFT)**:"
    )
    st.markdown(
        "- **Predefined Partitions:** Memory is divided into static partitions of predefined sizes at system startup.\n"
        "- **Single Process Rule:** Each partition can hold at most **one process** at any given time. Any remaining space inside an occupied partition cannot be given to another job.\n"
        "- **Degree of Multiprogramming:** Directly limited by the total number of partitions configured."
    )
    st.divider()

    st.subheader("2. Fragmentation Formulations")
    st.write("**A. Internal Fragmentation:** Unused space trapped inside an occupied partition that cannot be used by any other process.")
    st.code("Internal Fragmentation = Partition_Size - Process_Size  (for Occupied Partition)", language="text")

    st.write("**B. External Fragmentation:** Total free memory available across unoccupied partitions when an unallocated process cannot run because no single partition is large enough.")
    st.code("External Fragmentation = sum(Unoccupied Partition Sizes)  [if unallocated processes exist]", language="text")

    st.write("**C. Memory Utilization Efficiency:**")
    st.code("Utilization (%) = (Total Allocated Processes Size / Total System Memory) * 100", language="text")
    st.divider()

    st.subheader("3. Allocation Strategies: Mechanics & Trade-offs")

    with st.container(border=True):
        st.markdown(f"#### :red[First Fit]")
        st.markdown(
            "- **Logic:** Scans partitions sequentially from the first block and allocates the process to the **very first partition** that is large enough.\n"
            "- **Time Complexity:** $O(n)$ in the worst case, but has the fastest average search time.\n"
            "- **Advantages:** Very fast allocation with minimal CPU overhead.\n"
            "- **Disadvantages:** Tends to accumulate small unusable fragments near the beginning of memory."
        )

    with st.container(border=True):
        st.markdown(f"#### :red[Best Fit]")
        st.markdown(
            "- **Logic:** Searches through all partitions and allocates the process to the **smallest partition** that can accommodate it.\n"
            "- **Time Complexity:** $O(n)$ always (must inspect every partition).\n"
            "- **Advantages:** Minimizes internal fragmentation within the chosen partition.\n"
            "- **Disadvantages:** Slower due to full list traversal; creates very small, scattered leftover fragments."
        )

    with st.container(border=True):
        st.markdown(f"#### :red[Worst Fit]")
        st.markdown(
            "- **Logic:** Searches all partitions and allocates the process into the **largest available partition**.\n"
            "- **Time Complexity:** $O(n)$ always (must inspect every partition).\n"
            "- **Advantages:** Leaves the largest possible leftover fragments, which may fit future incoming jobs.\n"
            "- **Disadvantages:** Quickly uses up the largest partitions, causing future large processes to fail."
        )

    st.write("")
    if st.button("Close Guide", use_container_width=True):
        st.rerun()

# ============================================================
# LOGO & HEADER BANNER
# ============================================================

logo_col, title_col = st.columns([1, 4])

with logo_col:
    if os.path.exists("nmims_logo.png"):
        st.image("nmims_logo.png", use_container_width=True)
    else:
        st.markdown(
            f'<div style="border: 2px dashed {BORDER_COLOR}; border-radius: 6px; padding: 25px; text-align: center; color: {MUTED_TEXT}; font-weight: bold; font-size: 12px;">nmims_logo.png</div>',
            unsafe_allow_html=True,
        )

with title_col:
    st.markdown(
        f'<div class="header-card" style="margin-bottom: 0;">'
        f'<div class="header-tag">Operating Systems | Unit 5 – Memory Management</div>'
        f'<h1 class="header-title">Contiguous Memory Allocation Simulator</h1>'
        f'<div class="header-desc">Simulate and evaluate partition-based contiguous memory strategies: '
        f'<b>First Fit</b>, <b>Best Fit</b>, and <b>Worst Fit</b>. Analyzes partition assignment, internal fragmentation, external fragmentation, and allocation efficiency.</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

st.write("")

# ============================================================
# DEVELOPER CREDITS
# ============================================================

st.markdown(
    '<div class="team-container">'
    '<span class="team-title">Developed By:</span>'
    '<div class="student-tag">Ritam Mahakur &nbsp;<b>(C001)</b></div>'
    '<div class="student-tag">Nandini Devnani &nbsp;<b>(C005)</b></div>'
    '<div class="student-tag">Sahasra &nbsp;<b>(C046)</b></div>'
    '</div>',
    unsafe_allow_html=True,
)

# ============================================================
# FULL-WIDTH THEORY BUTTON
# ============================================================

if st.button("📖 Click for Explanation", use_container_width=True):
    show_theory_dialog()

# ============================================================
# CONFIGURATION INPUT PANEL
# ============================================================

st.markdown('<div class="content-panel">', unsafe_allow_html=True)
st.markdown('<div class="section-title" style="margin-top: 0;">Configuration Parameters</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    block_input = st.text_input(
        "Memory Partition Sizes (KB)",
        value="100, 500, 200, 300, 600",
        help="Enter block capacities separated by commas.",
    )

with col2:
    process_input = st.text_input(
        "Incoming Process Sizes (KB)",
        value="212, 417, 112, 426",
        help="Enter incoming job sizes separated by commas.",
    )

st.markdown('<div class="section-title">Run Allocation Strategy</div>', unsafe_allow_html=True)

btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)

with btn_col1:
    if st.button("First Fit", use_container_width=True):
        st.session_state["active_algo"] = "First Fit"

with btn_col2:
    if st.button("Best Fit", use_container_width=True):
        st.session_state["active_algo"] = "Best Fit"

with btn_col3:
    if st.button("Worst Fit", use_container_width=True):
        st.session_state["active_algo"] = "Worst Fit"

with btn_col4:
    if st.button("Compare All", use_container_width=True):
        st.session_state["active_algo"] = "Compare All"

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# INPUT PARSER
# ============================================================

def parse_input(value):
    value = value.strip()
    if not value:
        raise ValueError("Input cannot be empty.")

    parts = value.split(",")
    for part in parts:
        if part.strip() == "":
            raise ValueError("Invalid format: extra or trailing comma detected.")

    try:
        numbers = [int(part.strip()) for part in parts]
    except ValueError:
        raise ValueError("Invalid input: values must be positive integers.")

    for number in numbers:
        if number <= 0:
            raise ValueError("Invalid size: all partition and process sizes must exceed 0 KB.")

    return numbers


def run_algorithm(func, blocks, processes):
    res = func(blocks, processes)
    if len(res) == 4:
        return res[0], res[1], res[2], res[3]
    elif len(res) == 3:
        return res[0], res[1], res[2], []
    else:
        return res[0], [False] * len(blocks), [0] * len(blocks), []

# ============================================================
# MEMORY VISUALIZER
# ============================================================

def display_memory(blocks, processes, allocation, occupied, internal_frag):
    st.markdown('<div class="section-title">Partition Memory Map</div>', unsafe_allow_html=True)

    cols_per_row = 4
    total_blocks = len(blocks)

    for row_start in range(0, total_blocks, cols_per_row):
        row_end = min(row_start + cols_per_row, total_blocks)
        cols = st.columns(cols_per_row)

        for col_idx, block_idx in enumerate(range(row_start, row_end)):
            allocated_proc = "None"
            process_size = 0

            for p_idx, b_idx in enumerate(allocation):
                if b_idx == block_idx:
                    allocated_proc = f"P{p_idx + 1}"
                    process_size = processes[p_idx]
                    break

            if occupied[block_idx]:
                header_class = "block-occupied"
                status_label = "OCCUPIED"
                frag_val = f"{internal_frag[block_idx]} KB"
            else:
                header_class = "block-free"
                status_label = "FREE"
                frag_val = "0 KB"

            card_html = (
                f'<div class="memory-block-card">'
                f'<div class="memory-block-header {header_class}">'
                f'<span>Partition {block_idx + 1}</span>'
                f'<span>{status_label}</span>'
                f'</div>'
                f'<div class="memory-block-body">'
                f'<b>Total Capacity:</b> {blocks[block_idx]} KB<br>'
                f'<b>Active Process:</b> {allocated_proc} ({process_size} KB)<br>'
                f'<b>Internal Frag.:</b> {frag_val}<br>'
                f'<b>Unused Space:</b> {blocks[block_idx] - process_size} KB'
                f'</div>'
                f'</div>'
            )
            with cols[col_idx]:
                st.markdown(card_html, unsafe_allow_html=True)

# ============================================================
# RESULTS RENDERER
# ============================================================

def display_results(name, blocks, processes, allocation, occupied, internal_frag, logs):
    st.markdown(f'<div class="section-title">{name} — Allocation Report</div>', unsafe_allow_html=True)

    table_rows = []
    for i in range(len(processes)):
        if allocation[i] != -1:
            blk_idx = allocation[i]
            block_name = f"Partition {blk_idx + 1}"
            status = "<span style='color: #2E7D32; font-weight:600;'>Allocated</span>"
            frag = f"{internal_frag[blk_idx]} KB"
        else:
            block_name = "-"
            status = "<span style='color: #C62828; font-weight:600;'>Unallocated</span>"
            frag = "-"

        table_rows.append(
            {
                "Process": f"<b>P{i + 1}</b>",
                "Required Memory": f"{processes[i]} KB",
                "Allocated Partition": block_name,
                "Status": status,
                "Internal Frag.": frag,
            }
        )

    df_report = pd.DataFrame(table_rows)
    table_html = df_report.to_html(classes="styled-table", index=False, escape=False)
    st.markdown(table_html, unsafe_allow_html=True)

    allocated_count = sum(1 for x in allocation if x != -1)
    unallocated_count = len(processes) - allocated_count
    total_memory = sum(blocks)
    total_allocated_proc_mem = sum(
        processes[i] for i, b in enumerate(allocation) if b != -1
    )
    total_internal_frag = sum(internal_frag)

    external_frag = (
        sum(blocks[i] for i in range(len(blocks)) if not occupied[i])
        if unallocated_count > 0
        else 0
    )

    utilization = (
        (total_allocated_proc_mem / total_memory) * 100 if total_memory > 0 else 0
    )

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Allocated", f"{allocated_count}/{len(processes)}")
    c2.metric("Unallocated", unallocated_count)
    c3.metric("Total Internal Frag.", f"{total_internal_frag} KB")
    c4.metric("External Frag.", f"{external_frag} KB")
    c5.metric("System Utilization", f"{utilization:.2f}%")

    if logs:
        st.markdown('<div class="section-title">Step-by-Step Allocation Trace</div>', unsafe_allow_html=True)
        for item in logs:
            steps_html = "".join([f'<div class="trace-step">• {s}</div>' for s in item["steps"]])
            trace_box = (
                f'<div class="trace-card">'
                f'<div class="trace-title">{item["process"]} ({item["size"]} KB) Allocation Trace:</div>'
                f'{steps_html}'
                f'</div>'
            )
            st.markdown(trace_box, unsafe_allow_html=True)

    display_memory(blocks, processes, allocation, occupied, internal_frag)

# ============================================================
# PERSISTENT EXECUTION LOGIC (VIA SESSION STATE)
# ============================================================

active_action = st.session_state.get("active_algo", None)

if active_action:
    try:
        blocks = parse_input(block_input)
        processes = parse_input(process_input)
    except ValueError as e:
        st.error(str(e))
        st.stop()

    algo_map = {
        "First Fit": first_fit,
        "Best Fit": best_fit,
        "Worst Fit": worst_fit,
    }

    if active_action in algo_map:
        alloc, occ, frag, logs = run_algorithm(algo_map[active_action], blocks, processes)
        display_results(active_action, blocks, processes, alloc, occ, frag, logs)
    elif active_action == "Compare All":
        st.markdown('<div class="section-title">Comparative Performance Analysis</div>', unsafe_allow_html=True)

        results = {}
        for name, func in algo_map.items():
            alloc, occ, frag, logs = run_algorithm(func, blocks, processes)
            results[name] = {"allocation": alloc, "occupied": occ, "internal_frag": frag, "logs": logs}

        comp_data = []
        algo_names = []
        allocated_list = []
        unallocated_list = []
        utilization_list = []
        total_mem = sum(blocks)
        total_processes = len(processes)

        for name, res in results.items():
            alloc = res["allocation"]
            occ = res["occupied"]
            frag = res["internal_frag"]

            allocated_count = sum(1 for x in alloc if x != -1)
            unallocated_count = len(processes) - allocated_count
            allocated_proc_mem = sum(
                processes[i] for i, b in enumerate(alloc) if b != -1
            )
            total_int_frag = sum(frag)
            ext_frag = (
                sum(blocks[i] for i in range(len(blocks)) if not occ[i])
                if unallocated_count > 0
                else 0
            )
            utilization = (
                (allocated_proc_mem / total_mem) * 100 if total_mem > 0 else 0
            )

            comp_data.append(
                {
                    "Algorithm": f"<b>{name}</b>",
                    "Allocated Processes": allocated_count,
                    "Unallocated Processes": unallocated_count,
                    "Internal Frag.": f"{total_int_frag} KB",
                    "External Frag.": f"{ext_frag} KB",
                    "Memory Utilization": f"<b>{utilization:.2f}%</b>",
                }
            )

            algo_names.append(name)
            allocated_list.append(allocated_count)
            unallocated_list.append(unallocated_count)
            utilization_list.append(round(utilization, 2))

        df_comp = pd.DataFrame(comp_data)
        st.markdown(df_comp.to_html(classes="styled-table", index=False, escape=False), unsafe_allow_html=True)

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.markdown(
                '<div style="background-color: #FFFFFF; border: 1px solid #DDE2E5; border-radius: 6px; padding: 18px 20px; margin-bottom: 16px;">'
                '<div style="font-size: 15px; font-weight: 700; color: #111111; margin-bottom: 14px;">Process Allocation Success Ratio</div>',
                unsafe_allow_html=True,
            )
            for name, alloc_c, unalloc_c in zip(algo_names, allocated_list, unallocated_list):
                col_n, col_p = st.columns([1, 2])
                with col_n:
                    st.markdown(f"**{name}**")
                    st.caption(f"{alloc_c} of {total_processes} Jobs Allocated")
                with col_p:
                    ratio = alloc_c / total_processes if total_processes > 0 else 0
                    st.progress(ratio)
            st.markdown("</div>", unsafe_allow_html=True)

        with chart_col2:
            st.markdown(
                '<div style="background-color: #FFFFFF; border: 1px solid #DDE2E5; border-radius: 6px; padding: 18px 20px; margin-bottom: 16px;">'
                '<div style="font-size: 15px; font-weight: 700; color: #111111; margin-bottom: 14px;">Memory Utilization Efficiency (%)</div>',
                unsafe_allow_html=True,
            )
            for name, util_val in zip(algo_names, utilization_list):
                col_n, col_p = st.columns([1, 2])
                with col_n:
                    st.markdown(f"**{name}**")
                    st.caption(f"{util_val:.2f}% System Utilization")
                with col_p:
                    ratio = min(max(util_val / 100.0, 0.0), 1.0)
                    st.progress(ratio)
            st.markdown("</div>", unsafe_allow_html=True)

        st.divider()
        st.markdown('<div class="section-title">Detailed Strategy Outputs</div>', unsafe_allow_html=True)

        for name, res in results.items():
            display_results(
                name,
                blocks,
                processes,
                res["allocation"],
                res["occupied"],
                res["internal_frag"],
                res["logs"],
            )
            st.divider()