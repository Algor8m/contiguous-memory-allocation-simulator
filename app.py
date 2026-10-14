import os
import streamlit as st
import pandas as pd

from algorithms import first_fit, best_fit, worst_fit

# ============================================================
# page configuration
# ============================================================

st.set_page_config(
    page_title="Contiguous Memory Allocation Simulator",
    page_icon="💾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# color palette
# ============================================================

PRIMARY_RED = "#9E1B32"
HOVER_RED = "#7E1426"
DARK_TEXT = "#111111"
MUTED_TEXT = "#333333"
LIGHT_BG = "#F4F6F8"
CARD_BG = "#FFFFFF"
BORDER_COLOR = "#DDE2E5"

# ============================================================
# custom css
# ============================================================

st.markdown(
    f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

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
    padding-bottom: 2rem;
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
    margin-bottom: 14px;
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
.content-panel {{
    background-color: {CARD_BG};
    border: 1px solid {BORDER_COLOR};
    border-radius: 6px;
    padding: 20px;
    margin-top: 14px;
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

/* centered styled table */
.styled-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0 24px 0;
    font-size: 14px;
    background-color: #FFFFFF;
    border: 1px solid {BORDER_COLOR};
    border-radius: 8px;
    overflow: hidden;
}}
.styled-table thead tr {{
    background-color: {PRIMARY_RED};
    color: #FFFFFF;
}}
.styled-table th {{
    padding: 12px 16px;
    color: #FFFFFF !important;
    font-weight: 600;
    font-size: 13px;
    letter-spacing: 0.5px;
    text-align: center !important;
}}
.styled-table td {{
    padding: 12px 16px;
    border-bottom: 1px solid {BORDER_COLOR};
    color: {DARK_TEXT};
    text-align: center !important;
}}
.styled-table tbody tr:nth-of-type(even) {{
    background-color: #F8F9FA;
}}
.styled-table tbody tr:last-of-type td {{
    border-bottom: none;
}}

/* dual bars layout */
.bar-label {{
    font-size: 13px;
    font-weight: 700;
    color: {DARK_TEXT};
    margin: 12px 0 6px 0;
}}
.visual-bar-wrap {{
    display: flex;
    width: 100%;
    height: 44px;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid {BORDER_COLOR};
    background-color: #EAEDF1;
    margin-bottom: 14px;
}}
.bar-seg {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    padding: 0 4px;
    font-weight: 600;
    font-size: 11px;
    border-right: 1px solid #FFFFFF;
}}
.seg-proc {{
    background: #9E1B32;
    color: #FFFFFF !important;
}}
.seg-int-frag {{
    background: #E07A5F;
    color: #FFFFFF !important;
}}
.seg-ext-frag {{
    background: #3D5A80;
    color: #FFFFFF !important;
}}
.seg-free-ok {{
    background: #CBD5E1;
    color: #334155 !important;
}}
.seg-neutral {{
    background: #E2E8F0;
    color: #64748B !important;
}}

/* partition block cards */
.memory-block-card {{
    background-color: #FFFFFF;
    border: 1px solid {BORDER_COLOR};
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 14px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.04);
}}
.memory-block-header {{
    padding: 10px 14px;
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
    background-color: #F8FAFC;
    color: #475569;
    border-left: 4px solid #94A3B8;
}}
.status-pill {{
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 12px;
    font-weight: 700;
    letter-spacing: 0.4px;
}}
.status-pill-occupied {{
    background-color: #FCE8E8;
    color: {PRIMARY_RED};
}}
.status-pill-free {{
    background-color: #E2E8F0;
    color: #475569;
}}
.memory-block-body {{
    padding: 14px;
    font-size: 13px;
    line-height: 1.6;
    color: {DARK_TEXT};
}}
.detail-row {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 6px;
    font-size: 12px;
}}
.detail-label {{
    color: #64748B;
    font-weight: 500;
}}
.detail-value {{
    font-weight: 700;
    color: {DARK_TEXT};
}}

/* metric cards */
.metric-box-custom {{
    background-color: #FFFFFF;
    border: 1px solid {BORDER_COLOR};
    border-top: 3px solid {PRIMARY_RED};
    padding: 14px 16px;
    border-radius: 6px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
    min-height: 110px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
.metric-box-title {{
    font-size: 13px;
    font-weight: 600;
    color: #475569;
    margin-bottom: 6px;
}}
.metric-box-value {{
    font-size: 24px;
    font-weight: 800;
    color: #111111;
    line-height: 1.1;
    margin-bottom: 8px;
}}
.metric-box-calc {{
    font-size: 11px;
    color: #64748B;
    background-color: #F8FAFC;
    padding: 4px 6px;
    border-radius: 4px;
    border: 1px dashed #CBD5E1;
    word-break: break-word;
}}

/* persistent light expander styling */
div[data-testid="stExpander"] {{
    background-color: #FFFFFF !important;
    border: 1px solid {BORDER_COLOR} !important;
    border-radius: 6px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03) !important;
}}
div[data-testid="stExpander"] details {{
    background-color: #FFFFFF !important;
}}
div[data-testid="stExpander"] summary {{
    background-color: #FFFFFF !important;
    color: #111111 !important;
}}
div[data-testid="stExpander"] summary:hover {{
    background-color: #F8F9FA !important;
    color: {PRIMARY_RED} !important;
}}
div[data-testid="stExpander"] summary svg {{
    fill: #111111 !important;
}}
div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {{
    background-color: #FFFFFF !important;
    border-top: 1px solid {BORDER_COLOR} !important;
    padding-top: 12px !important;
}}

.trace-card {{
    background-color: #FFFFFF;
    border: 1px solid {BORDER_COLOR};
    border-left: 4px solid {PRIMARY_RED};
    border-radius: 6px;
    padding: 12px 16px;
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

div[data-testid="stDialog"] div[role="dialog"] {{
    background-color: #FFFFFF !important;
    border: 1px solid {BORDER_COLOR} !important;
    border-top: 5px solid {PRIMARY_RED} !important;
    border-radius: 8px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15) !important;
}}
div[data-testid="stDialog"] div[role="dialog"] * {{
    color: {DARK_TEXT} !important;
}}
div[data-testid="stDialog"] div[role="dialog"] h1,
div[data-testid="stDialog"] div[role="dialog"] h2,
div[data-testid="stDialog"] div[role="dialog"] h3,
div[data-testid="stDialog"] div[role="dialog"] h4 {{
    color: {PRIMARY_RED} !important;
    font-weight: 700 !important;
}}
div[data-testid="stDialog"] div[role="dialog"] pre,
div[data-testid="stDialog"] div[role="dialog"] code {{
    background-color: #F8F9FA !important;
    color: {DARK_TEXT} !important;
    border: 1px solid {BORDER_COLOR} !important;
}}
div[data-testid="stDialog"] div[role="dialog"] div[data-testid="stVerticalBlockBorderWrapper"] {{
    background-color: #FFFFFF !important;
    border: 1px solid {BORDER_COLOR} !important;
    border-left: 4px solid {PRIMARY_RED} !important;
    border-radius: 6px !important;
}}
div[data-testid="stDialog"] button {{
    background-color: {PRIMARY_RED} !important;
}}
div[data-testid="stDialog"] button * {{
    color: #FFFFFF !important;
}}

.footer-watermark {{
    text-align: center;
    padding-top: 35px;
    padding-bottom: 10px;
    font-size: 13px;
    color: #666666 !important;
}}
.footer-watermark a {{
    color: {PRIMARY_RED} !important;
    text-decoration: none;
    font-weight: 700;
}}
.footer-watermark a:hover {{
    text-decoration: underline;
}}
</style>""",
    unsafe_allow_html=True,
)

# ============================================================
# theory & concepts modal dialog
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
    st.code("Internal Fragmentation = Partition_Size - Process_Size  for Occupied Partition", language="text")

    st.write("**B. External Fragmentation:** Total free memory available across unoccupied partitions when an unallocated process cannot run because no single partition is large enough.")
    st.code("External Fragmentation = sum(Unoccupied Partition Sizes)  if unallocated processes exist", language="text")

    st.write("**C. Memory Utilization Efficiency:**")
    st.code("Utilization % = (Total Allocated Processes Size / Total System Memory) * 100", language="text")
    st.divider()

    st.subheader("3. Allocation Strategies: Mechanics & Trade-offs")

    with st.container(border=True):
        st.markdown("#### First Fit")
        st.markdown(
            "- **Logic:** Scans partitions sequentially from the first block and allocates the process to the **very first partition** that is large enough.\n"
            "- **Time Complexity:** O(n) in the worst case, but has the fastest average search time.\n"
            "- **Advantages:** Very fast allocation with minimal CPU overhead.\n"
            "- **Disadvantages:** Tends to accumulate small unusable fragments near the beginning of memory."
        )

    with st.container(border=True):
        st.markdown("#### Best Fit")
        st.markdown(
            "- **Logic:** Searches through all partitions and allocates the process to the **smallest partition** that can accommodate it.\n"
            "- **Time Complexity:** O(n) always.\n"
            "- **Advantages:** Minimizes internal fragmentation within the chosen partition.\n"
            "- **Disadvantages:** Slower due to full list traversal; creates very small, scattered leftover fragments."
        )

    with st.container(border=True):
        st.markdown("#### Worst Fit")
        st.markdown(
            "- **Logic:** Searches all partitions and allocates the process into the **largest available partition**.\n"
            "- **Time Complexity:** O(n) always.\n"
            "- **Advantages:** Leaves the largest possible leftover fragments, which may fit future incoming jobs.\n"
            "- **Disadvantages:** Quickly uses up the largest partitions, causing future large processes to fail."
        )

    st.write("")
    if st.button("Close Guide", use_container_width=True):
        st.rerun()

# ============================================================
# logo & header banner
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
        f'<div class="header-tag">Operating Systems</div>'
        f'<h1 class="header-title">Contiguous Memory Allocation Simulator</h1>'
        f'<div class="header-desc">Simulate and evaluate partition-based contiguous memory strategies: '
        f'<b>First Fit</b>, <b>Best Fit</b>, and <b>Worst Fit</b>. Analyzes partition assignment, internal fragmentation, external fragmentation, and allocation efficiency.</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

st.write("")

# ============================================================
# full-width theory button
# ============================================================

if st.button("📖 Click for Explanation", use_container_width=True):
    show_theory_dialog()

# ============================================================
# configuration input panel
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
# input parser
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
# physical memory map visualizer: 2 clean stacked bars
# ============================================================

def display_memory(blocks, processes, allocation, occupied, internal_frag):
    st.markdown('<div class="section-title">Physical Partition Memory Map</div>', unsafe_allow_html=True)

    total_mem = sum(blocks)
    unallocated_count = sum(1 for x in allocation if x == -1)

    # 1. internal fragmentation map
    st.markdown('<div class="bar-label">1. Internal Fragmentation Breakdown (Active RAM vs Wasted Trapped Space)</div>', unsafe_allow_html=True)
    int_bar_html = '<div class="visual-bar-wrap">'
    for idx, capacity in enumerate(blocks):
        width_pct = max((capacity / total_mem) * 100, 6.0)
        is_occ = occupied[idx]

        if is_occ:
            proc_id = None
            proc_sz = 0
            for p_idx, b_idx in enumerate(allocation):
                if b_idx == idx:
                    proc_id = p_idx + 1
                    proc_sz = processes[p_idx]
                    break
            
            frag_sz = internal_frag[idx]
            proc_w = (proc_sz / total_mem) * 100
            frag_w = (frag_sz / total_mem) * 100

            int_bar_html += f'<div class="bar-seg seg-proc" style="width: {proc_w:.2f}%;" title="Partition {idx + 1}: Process {proc_id} ({proc_sz} KB)">'
            int_bar_html += f'<span>P{proc_id}</span>'
            int_bar_html += f'<span style="font-size: 9px;">{proc_sz} KB</span>'
            int_bar_html += '</div>'

            if frag_sz > 0:
                int_bar_html += f'<div class="bar-seg seg-int-frag" style="width: {frag_w:.2f}%;" title="Partition {idx + 1}: Internal Waste ({frag_sz} KB)">'
                int_bar_html += f'<span>Int. Waste</span>'
                int_bar_html += f'<span style="font-size: 9px;">{frag_sz} KB</span>'
                int_bar_html += '</div>'
        else:
            int_bar_html += f'<div class="bar-seg seg-neutral" style="width: {width_pct:.2f}%;" title="Partition {idx + 1}: Unallocated ({capacity} KB)">'
            int_bar_html += f'<span>Partition {idx + 1}</span>'
            int_bar_html += f'<span style="font-size: 9px;">{capacity} KB (Free)</span>'
            int_bar_html += '</div>'
    int_bar_html += '</div>'
    st.markdown(int_bar_html, unsafe_allow_html=True)

    # 2. external fragmentation map
    st.markdown('<div class="bar-label">2. External Fragmentation Breakdown (Free Partitions Blocked by Fragmented Memory)</div>', unsafe_allow_html=True)
    ext_bar_html = '<div class="visual-bar-wrap">'
    for idx, capacity in enumerate(blocks):
        width_pct = max((capacity / total_mem) * 100, 6.0)
        is_occ = occupied[idx]

        if is_occ:
            ext_bar_html += f'<div class="bar-seg seg-neutral" style="width: {width_pct:.2f}%; opacity: 0.6;" title="Partition {idx + 1}: Occupied ({capacity} KB)">'
            ext_bar_html += f'<span>Partition {idx + 1}</span>'
            ext_bar_html += f'<span style="font-size: 9px;">In Use</span>'
            ext_bar_html += '</div>'
        else:
            if unallocated_count > 0:
                ext_bar_html += f'<div class="bar-seg seg-ext-frag" style="width: {width_pct:.2f}%;" title="Partition {idx + 1}: External Frag ({capacity} KB)">'
                ext_bar_html += f'<span>Ext. Frag</span>'
                ext_bar_html += f'<span style="font-size: 9px;">{capacity} KB</span>'
                ext_bar_html += '</div>'
            else:
                ext_bar_html += f'<div class="bar-seg seg-free-ok" style="width: {width_pct:.2f}%;" title="Partition {idx + 1}: Free Space ({capacity} KB)">'
                ext_bar_html += f'<span>Partition {idx + 1}</span>'
                ext_bar_html += f'<span style="font-size: 9px;">{capacity} KB Free</span>'
                ext_bar_html += '</div>'
    ext_bar_html += '</div>'
    st.markdown(ext_bar_html, unsafe_allow_html=True)

    # partition block cards
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
                    allocated_proc = f"Process {p_idx + 1}"
                    process_size = processes[p_idx]
                    break

            is_occ = occupied[block_idx]
            cap = blocks[block_idx]
            frag_val = internal_frag[block_idx] if is_occ else 0
            
            if is_occ:
                header_class = "block-occupied"
                pill_class = "status-pill-occupied"
                status_text = "IN USE"
            else:
                header_class = "block-free"
                pill_class = "status-pill-free"
                status_text = "AVAILABLE"

            card_html = f"""
            <div class="memory-block-card">
                <div class="memory-block-header {header_class}">
                    <span>Partition {block_idx + 1}</span>
                    <span class="status-pill {pill_class}">{status_text}</span>
                </div>
                <div class="memory-block-body">
                    <div class="detail-row">
                        <span class="detail-label">Total Size:</span>
                        <span class="detail-value">{cap} KB</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Assigned Job:</span>
                        <span class="detail-value">{allocated_proc}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Process Memory:</span>
                        <span class="detail-value">{process_size} KB</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label" style="color: #E07A5F;">Internal Frag.:</span>
                        <span class="detail-value" style="color: #E07A5F;">{frag_val} KB</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Free Leftover:</span>
                        <span class="detail-value">{cap - process_size} KB</span>
                    </div>
                </div>
            </div>
            """
            with cols[col_idx]:
                st.markdown(card_html, unsafe_allow_html=True)

# ============================================================
# results renderer
# ============================================================

def display_results(name, blocks, processes, allocation, occupied, internal_frag, logs):
    st.markdown(f'<div class="section-title">{name} — Allocation Report</div>', unsafe_allow_html=True)

    # 1. centered allocation table
    table_rows = []
    for i in range(len(processes)):
        if allocation[i] != -1:
            blk_idx = allocation[i]
            block_name = f"<span style='font-weight: 600; color: #111111;'>Partition {blk_idx + 1}</span>"
            status = "<span style='background-color: #E8F5E9; color: #2E7D32; font-weight: 700; padding: 4px 10px; border-radius: 12px; font-size: 12px;'>Allocated</span>"
            frag = f"<span style='font-weight: 600;'>{internal_frag[blk_idx]} KB</span>"
        else:
            block_name = "<span style='color: #888888;'>None</span>"
            status = "<span style='background-color: #FFEBEE; color: #C62828; font-weight: 700; padding: 4px 10px; border-radius: 12px; font-size: 12px;'>Unallocated</span>"
            frag = "<span style='color: #888888;'>—</span>"

        table_rows.append(
            {
                "Process": f"<b>Process {i + 1}</b>",
                "Required Memory": f"{processes[i]} KB",
                "Allocated Partition": block_name,
                "Status": status,
                "Internal Frag.": frag,
            }
        )

    df_report = pd.DataFrame(table_rows)
    table_html = df_report.to_html(classes="styled-table", index=False, escape=False)
    st.markdown(table_html, unsafe_allow_html=True)

    # 2. step-by-step decision trace log
    if logs:
        with st.expander(f"🔍 Step-by-Step Allocation Decision Trace ({name})", expanded=False):
            for item in logs:
                steps_html = "".join([f'<div class="trace-step">• {s}</div>' for s in item["steps"]])
                trace_box = (
                    f'<div class="trace-card">'
                    f'<div class="trace-title">{item["process"]} ({item["size"]} KB) Allocation Trace:</div>'
                    f'{steps_html}'
                    f'</div>'
                )
                st.markdown(trace_box, unsafe_allow_html=True)

    # 3. physical partition memory map
    display_memory(blocks, processes, allocation, occupied, internal_frag)

    # 4. metric summary cards with live calculation formulas
    allocated_count = sum(1 for x in allocation if x != -1)
    unallocated_count = len(processes) - allocated_count
    total_memory = sum(blocks)
    total_allocated_proc_mem = sum(
        processes[i] for i, b in enumerate(allocation) if b != -1
    )
    total_internal_frag = sum(internal_frag)

    free_blocks = [blocks[i] for i in range(len(blocks)) if not occupied[i]]
    external_frag = sum(free_blocks) if unallocated_count > 0 else 0

    utilization = (
        (total_allocated_proc_mem / total_memory) * 100 if total_memory > 0 else 0
    )

    alloc_calc = f"{allocated_count} assigned of {len(processes)} total"
    unalloc_calc = f"{len(processes)} - {allocated_count} = {unallocated_count}"

    active_frags = [f"{internal_frag[i]}" for i in range(len(blocks)) if occupied[i] and internal_frag[i] > 0]
    if active_frags:
        int_calc = " + ".join(active_frags) + f" = {total_internal_frag} KB"
    else:
        int_calc = "no internal fragmentation"

    if unallocated_count > 0 and free_blocks:
        ext_calc = " + ".join(str(b) for b in free_blocks) + f" = {external_frag} KB"
    elif unallocated_count == 0:
        ext_calc = "all processes placed = 0 KB"
    else:
        ext_calc = "no free blocks = 0 KB"

    util_calc = f"{total_allocated_proc_mem} / {total_memory} × 100"

    st.write("")
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.markdown(f"""
        <div class="metric-box-custom">
            <div class="metric-box-title">Allocated</div>
            <div class="metric-box-value">{allocated_count}/{len(processes)}</div>
            <div class="metric-box-calc">{alloc_calc}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-box-custom">
            <div class="metric-box-title">Unallocated</div>
            <div class="metric-box-value">{unallocated_count}</div>
            <div class="metric-box-calc">{unalloc_calc}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-box-custom">
            <div class="metric-box-title">Total Internal Frag.</div>
            <div class="metric-box-value">{total_internal_frag} KB</div>
            <div class="metric-box-calc">{int_calc}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="metric-box-custom">
            <div class="metric-box-title">External Frag.</div>
            <div class="metric-box-value">{external_frag} KB</div>
            <div class="metric-box-calc">{ext_calc}</div>
        </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown(f"""
        <div class="metric-box-custom">
            <div class="metric-box-title">System Utilization</div>
            <div class="metric-box-value">{utilization:.2f}%</div>
            <div class="metric-box-calc">{util_calc}</div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# persistent execution logic
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
                    "Allocated Processes": f"{allocated_count}/{total_processes}",
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

# ============================================================
# watermark footer
# ============================================================

st.markdown(
    """
    <div class="footer-watermark">
        <a href="https://www.linkedin.com/in/ritammahakur" target="_blank">Algor8m</a>
    </div>
    """,
    unsafe_allow_html=True,
)