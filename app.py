import streamlit as st

from algorithms import first_fit, best_fit, worst_fit


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Contiguous Memory Allocation Simulator",
    page_icon="💾",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# COLOR PALETTE
# ============================================================

RED = "#A91D22"
BLACK = "#000000"
GREY = "#7F7F7F"
DARK_GREY = "#333333"
LIGHT_GREY = "#F4F4F4"
WHITE = "#FFFFFF"
BORDER = "#D9D9D9"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
<style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {{
        background-color: {WHITE};
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }}

    /* Force normal text to remain visible */
    .stApp p,
    .stApp span,
    .stApp label {{
        color: {BLACK};
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: {BLACK} !important;
    }}


    /* ========================================================
       HEADER
       ======================================================== */

    .project-header {{
        background-color: {BLACK};
        padding: 18px 30px;
        border-radius: 10px;
        margin-bottom: 25px;
    }}

    .project-header-title {{
        color: {WHITE} !important;
        font-size: 28px;
        font-weight: 700;
        margin: 0;
    }}

    .project-header-subtitle {{
        color: #D0D0D0 !important;
        font-size: 14px;
        margin-top: 4px;
    }}


    /* ========================================================
       MAIN TITLE
       ======================================================== */

    .main-title {{
        text-align: center;
        color: {BLACK} !important;
        font-size: 38px;
        font-weight: 800;
        margin-top: 10px;
        margin-bottom: 5px;
    }}

    .title-line {{
        width: 90px;
        height: 4px;
        background-color: {RED};
        margin: 10px auto 12px auto;
        border-radius: 5px;
    }}

    .subtitle {{
        text-align: center;
        color: {GREY} !important;
        font-size: 16px;
        margin-bottom: 35px;
    }}


    /* ========================================================
       SECTION TITLES
       ======================================================== */

    .section-title {{
        color: {BLACK} !important;
        font-size: 23px;
        font-weight: 700;
        border-left: 5px solid {RED};
        padding-left: 12px;
        margin-top: 25px;
        margin-bottom: 15px;
    }}


    /* ========================================================
       INFORMATION CARD
       ======================================================== */

    .info-card {{
        background-color: {LIGHT_GREY};
        border: 1px solid {BORDER};
        border-left: 5px solid {RED};
        border-radius: 8px;
        padding: 18px;
        margin-top: 20px;
        margin-bottom: 20px;
    }}

    .info-card-title {{
        color: {BLACK} !important;
        font-weight: 700;
        font-size: 17px;
        margin-bottom: 8px;
    }}

    .info-card-text {{
        color: {DARK_GREY} !important;
        font-size: 14px;
        line-height: 1.6;
    }}


    /* ========================================================
       TEXT INPUT
       ======================================================== */

    div[data-testid="stTextInput"] label {{
        color: {BLACK} !important;
        font-weight: 600;
    }}

    div[data-testid="stTextInput"] input {{
        color: {BLACK} !important;
        background-color: {WHITE} !important;
        border: 1px solid {BORDER};
        border-radius: 7px;
    }}

    div[data-testid="stTextInput"] input::placeholder {{
        color: {GREY} !important;
    }}

    div[data-testid="stTextInput"] input:focus {{
        border-color: {RED};
        box-shadow: 0 0 0 1px {RED};
    }}


    /* ========================================================
       SELECT BOX
       ======================================================== */

    div[data-testid="stSelectbox"] label {{
        color: {BLACK} !important;
        font-weight: 600;
    }}

    div[data-testid="stSelectbox"] div {{
        color: {BLACK};
    }}


    /* ========================================================
       BUTTON
       ======================================================== */

    div.stButton > button {{
        background-color: {RED};
        color: {WHITE} !important;
        border: none;
        border-radius: 7px;
        font-weight: 700;
        padding: 10px 24px;
        transition: 0.2s;
    }}

    div.stButton > button p {{
        color: {WHITE} !important;
    }}

    div.stButton > button:hover {{
        background-color: #8F181D;
        color: {WHITE} !important;
    }}

    div.stButton > button:hover p {{
        color: {WHITE} !important;
    }}


    /* ========================================================
       MEMORY BLOCK
       ======================================================== */

    .memory-block {{
        background-color: {LIGHT_GREY};
        border: 2px solid {BORDER};
        border-top: 5px solid {RED};
        border-radius: 10px;
        padding: 16px;
        text-align: center;
        min-height: 280px;
        margin-bottom: 10px;
        color: {BLACK} !important;
    }}

    .memory-block h3 {{
        color: {RED} !important;
        margin-top: 0;
        margin-bottom: 8px;
    }}

    .memory-block b {{
        color: {BLACK} !important;
    }}

    .memory-block hr {{
        border: none;
        border-top: 1px solid {BORDER};
    }}


    /* ========================================================
       METRICS
       ======================================================== */

    div[data-testid="stMetric"] {{
        background-color: {LIGHT_GREY};
        border-left: 4px solid {RED};
        padding: 15px;
        border-radius: 7px;
    }}

    div[data-testid="stMetric"] label {{
        color: {GREY} !important;
    }}

    div[data-testid="stMetric"] [data-testid="stMetricValue"] {{
        color: {BLACK} !important;
    }}

    div[data-testid="stMetric"] [data-testid="stMetricLabel"] {{
        color: {GREY} !important;
    }}


    /* ========================================================
       TABLE
       ======================================================== */

    table {{
        color: {BLACK} !important;
    }}

    thead tr th {{
        background-color: {BLACK} !important;
        color: {WHITE} !important;
    }}

    tbody tr td {{
        color: {BLACK} !important;
        background-color: {WHITE} !important;
    }}

    tbody tr:nth-child(even) td {{
        background-color: {LIGHT_GREY} !important;
    }}


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {{
        text-align: center;
        color: {GREY} !important;
        font-size: 13px;
        padding-top: 30px;
        margin-top: 40px;
        border-top: 1px solid {BORDER};
    }}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="project-header">
        <div class="project-header-title">
            Operating Systems Mini Project
        </div>
        <div class="project-header-subtitle">
            Memory Management Simulation
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MAIN TITLE
# ============================================================

st.markdown(
    '<div class="main-title">'
    'Contiguous Memory Allocation Simulator'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title-line"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Simulation and comparison of First Fit, Best Fit, and Worst Fit allocation strategies'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.markdown(
    '<div class="info-card">'
    '<div class="info-card-title">About the Simulator</div>'
    '<div class="info-card-text">'
    'This simulator demonstrates contiguous memory allocation '
    'using three classical allocation strategies: First Fit, '
    'Best Fit, and Worst Fit. Enter memory block sizes and '
    'process sizes to observe process allocation, remaining '
    'memory, memory utilization, and algorithm comparison.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MEMORY CONFIGURATION
# ============================================================

st.markdown(
    '<div class="section-title">Memory Configuration</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    block_input = st.text_input(
        "Memory Block Sizes (KB)",
        value="100, 500, 200, 300, 600",
        help="Enter memory block sizes separated by commas."
    )

with col2:

    process_input = st.text_input(
        "Process Sizes (KB)",
        value="212, 417, 112, 426",
        help="Enter process sizes separated by commas."
    )


# ============================================================
# ALGORITHM SELECTION
# ============================================================

st.markdown(
    '<div class="section-title">Allocation Strategy</div>',
    unsafe_allow_html=True
)

algorithm = st.selectbox(
    "Select Allocation Algorithm",
    [
        "First Fit",
        "Best Fit",
        "Worst Fit",
        "Compare All Algorithms"
    ]
)


# ============================================================
# INPUT PARSER AND VALIDATION
# ============================================================

def parse_input(value):

    value = value.strip()

    # Empty input
    if not value:

        raise ValueError(
            "Input cannot be empty."
        )

    # Split by comma
    parts = value.split(",")

    # Detect extra commas
    for part in parts:

        if part.strip() == "":

            raise ValueError(
                "Invalid input: extra comma detected."
            )

    # Convert values to integers
    try:

        numbers = [
            int(part.strip())
            for part in parts
        ]

    except ValueError:

        raise ValueError(
            "Invalid input: only numbers are allowed."
        )

    # Reject zero and negative values
    for number in numbers:

        if number <= 0:

            raise ValueError(
                "Invalid input: all values must be greater than 0."
            )

    return numbers


# ============================================================
# MEMORY VISUALIZATION
# ============================================================

def display_memory(
    blocks,
    processes,
    allocation,
    remaining
):

    st.subheader("Memory Visualization")

    columns = st.columns(len(blocks))

    for i in range(len(blocks)):

        allocated_processes = []

        for process_index, block_index in enumerate(allocation):

            if block_index == i:

                allocated_processes.append(
                    f"P{process_index + 1} "
                    f"({processes[process_index]} KB)"
                )

        used = blocks[i] - remaining[i]

        process_text = "<br>".join(
            allocated_processes
        )

        if not process_text:

            process_text = "No process allocated"

        html = f"""
<div class="memory-block">
<h3>B{i + 1}</h3>
<hr>
<b>Total:</b> {blocks[i]} KB
<br><br>
<b>Allocated:</b>
<br>
{process_text}
<br><br>
<b>Used:</b> {used} KB
<br>
<b>Remaining:</b> {remaining[i]} KB
</div>
"""

        with columns[i]:

            st.markdown(
                html,
                unsafe_allow_html=True
            )


# ============================================================
# RESULT DISPLAY
# ============================================================

def display_results(
    name,
    blocks,
    processes,
    allocation,
    remaining
):

    st.header(name)

    # --------------------------------------------------------
    # PROCESS ALLOCATION TABLE
    # --------------------------------------------------------

    st.subheader("Process Allocation")

    table_data = []

    for i in range(len(processes)):

        if allocation[i] != -1:

            block_name = f"B{allocation[i] + 1}"
            status = "Allocated"

        else:

            block_name = "-"
            status = "Unallocated"

        table_data.append(
            {
                "Process": f"P{i + 1}",
                "Size (KB)": processes[i],
                "Allocated Block": block_name,
                "Status": status
            }
        )

    st.table(table_data)

    # --------------------------------------------------------
    # STATISTICS
    # --------------------------------------------------------

    allocated_count = sum(
        1
        for x in allocation
        if x != -1
    )

    unallocated_count = (
        len(processes)
        - allocated_count
    )

    total_memory = sum(blocks)

    remaining_memory = sum(remaining)

    used_memory = (
        total_memory
        - remaining_memory
    )

    utilization = (
        used_memory
        / total_memory
    ) * 100

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Allocated Processes",
            allocated_count
        )

    with col2:

        st.metric(
            "Unallocated Processes",
            unallocated_count
        )

    with col3:

        st.metric(
            "Used Memory",
            f"{used_memory} KB"
        )

    with col4:

        st.metric(
            "Memory Utilization",
            f"{utilization:.2f}%"
        )

    # --------------------------------------------------------
    # MEMORY VISUALIZATION
    # --------------------------------------------------------

    display_memory(
        blocks,
        processes,
        allocation,
        remaining
    )


# ============================================================
# RUN SIMULATION
# ============================================================

if st.button(
    "Run Simulation",
    type="primary",
    width="stretch"
):

    # --------------------------------------------------------
    # VALIDATE INPUTS
    # --------------------------------------------------------

    try:

        blocks = parse_input(
            block_input
        )

        processes = parse_input(
            process_input
        )

    except ValueError as e:

        st.error(
            str(e)
        )

        st.stop()

    # ========================================================
    # FIRST FIT
    # ========================================================

    if algorithm == "First Fit":

        allocation, remaining = first_fit(
            blocks,
            processes
        )

        display_results(
            "First Fit",
            blocks,
            processes,
            allocation,
            remaining
        )

    # ========================================================
    # BEST FIT
    # ========================================================

    elif algorithm == "Best Fit":

        allocation, remaining = best_fit(
            blocks,
            processes
        )

        display_results(
            "Best Fit",
            blocks,
            processes,
            allocation,
            remaining
        )

    # ========================================================
    # WORST FIT
    # ========================================================

    elif algorithm == "Worst Fit":

        allocation, remaining = worst_fit(
            blocks,
            processes
        )

        display_results(
            "Worst Fit",
            blocks,
            processes,
            allocation,
            remaining
        )

    # ========================================================
    # COMPARE ALL ALGORITHMS
    # ========================================================

    else:

        results = {}

        # ----------------------------------------------------
        # RUN ALL THREE ALGORITHMS
        # ----------------------------------------------------

        for name, function in [
            ("First Fit", first_fit),
            ("Best Fit", best_fit),
            ("Worst Fit", worst_fit)
        ]:

            allocation, remaining = function(
                blocks,
                processes
            )

            results[name] = {
                "allocation": allocation,
                "remaining": remaining
            }

        # ----------------------------------------------------
        # COMPARISON TABLE
        # ----------------------------------------------------

        st.header("Algorithm Comparison")

        comparison_data = []

        for name in [
            "First Fit",
            "Best Fit",
            "Worst Fit"
        ]:

            allocation = results[name]["allocation"]

            remaining = results[name]["remaining"]

            allocated_count = sum(
                1
                for x in allocation
                if x != -1
            )

            unallocated_count = (
                len(processes)
                - allocated_count
            )

            remaining_memory = sum(
                remaining
            )

            comparison_data.append(
                {
                    "Algorithm": name,
                    "Allocated Processes":
                        allocated_count,
                    "Unallocated Processes":
                        unallocated_count,
                    "Remaining Memory (KB)":
                        remaining_memory
                }
            )

        st.table(
            comparison_data
        )

        # ----------------------------------------------------
        # PROCESS ALLOCATION COMPARISON
        # ----------------------------------------------------

        st.subheader(
            "Process Allocation Comparison"
        )

        chart_data = []

        for name in [
            "First Fit",
            "Best Fit",
            "Worst Fit"
        ]:

            allocation = results[name]["allocation"]

            allocated_count = sum(
                1
                for x in allocation
                if x != -1
            )

            unallocated_count = (
                len(processes)
                - allocated_count
            )

            chart_data.append(
                {
                    "Algorithm": name,
                    "Allocated": allocated_count,
                    "Unallocated": unallocated_count
                }
            )

        st.bar_chart(
            chart_data,
            x="Algorithm",
            y=[
                "Allocated",
                "Unallocated"
            ]
        )

        # ----------------------------------------------------
        # MEMORY UTILIZATION COMPARISON
        # ----------------------------------------------------

        st.subheader(
            "Memory Utilization Comparison"
        )

        utilization_data = []

        total_memory = sum(blocks)

        for name in [
            "First Fit",
            "Best Fit",
            "Worst Fit"
        ]:

            remaining = results[name]["remaining"]

            remaining_memory = sum(
                remaining
            )

            used_memory = (
                total_memory
                - remaining_memory
            )

            utilization = (
                used_memory
                / total_memory
            ) * 100

            utilization_data.append(
                {
                    "Algorithm": name,
                    "Memory Utilization (%)":
                        round(utilization, 2)
                }
            )

        st.bar_chart(
            utilization_data,
            x="Algorithm",
            y="Memory Utilization (%)"
        )

        # ====================================================
        # DETAILED RESULTS
        # ====================================================

        st.header("Detailed Results")

        # ----------------------------------------------------
        # FIRST FIT
        # ----------------------------------------------------

        allocation = results[
            "First Fit"
        ]["allocation"]

        remaining = results[
            "First Fit"
        ]["remaining"]

        display_results(
            "First Fit",
            blocks,
            processes,
            allocation,
            remaining
        )

        st.divider()

        # ----------------------------------------------------
        # BEST FIT
        # ----------------------------------------------------

        allocation = results[
            "Best Fit"
        ]["allocation"]

        remaining = results[
            "Best Fit"
        ]["remaining"]

        display_results(
            "Best Fit",
            blocks,
            processes,
            allocation,
            remaining
        )

        st.divider()

        # ----------------------------------------------------
        # WORST FIT
        # ----------------------------------------------------

        allocation = results[
            "Worst Fit"
        ]["allocation"]

        remaining = results[
            "Worst Fit"
        ]["remaining"]

        display_results(
            "Worst Fit",
            blocks,
            processes,
            allocation,
            remaining
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer">'
    'Contiguous Memory Allocation Simulator | '
    'Operating Systems Mini Project'
    '</div>',
    unsafe_allow_html=True
)