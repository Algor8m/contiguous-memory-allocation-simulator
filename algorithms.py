def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    occupied = [False] * len(blocks)
    internal_frag = [0] * len(blocks)
    logs = []

    for i in range(len(processes)):
        allocated = False
        step_logs = []
        for j in range(len(blocks)):
            if occupied[j]:
                step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) is already occupied.")
            elif blocks[j] < processes[i]:
                step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) is too small for P{i + 1} ({processes[i]} KB).")
            else:
                allocation[i] = j
                occupied[j] = True
                internal_frag[j] = blocks[j] - processes[i]
                step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) fits P{i + 1} ({processes[i]} KB). Allocated! Internal frag: {internal_frag[j]} KB.")
                allocated = True
                break

        if not allocated:
            step_logs.append(f"No available partition could accommodate P{i + 1} ({processes[i]} KB). Process remains unallocated.")

        logs.append({"process": f"P{i + 1}", "size": processes[i], "steps": step_logs})

    return allocation, occupied, internal_frag, logs


def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    occupied = [False] * len(blocks)
    internal_frag = [0] * len(blocks)
    logs = []

    for i in range(len(processes)):
        best_index = -1
        step_logs = []

        for j in range(len(blocks)):
            if occupied[j]:
                step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) is already occupied.")
            elif blocks[j] < processes[i]:
                step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) is too small for P{i + 1} ({processes[i]} KB).")
            else:
                if best_index == -1 or blocks[j] < blocks[best_index]:
                    best_index = j
                    step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) qualifies (new best candidate).")
                else:
                    step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) qualifies but is larger than Partition {best_index + 1} ({blocks[best_index]} KB).")

        if best_index != -1:
            allocation[i] = best_index
            occupied[best_index] = True
            internal_frag[best_index] = blocks[best_index] - processes[i]
            step_logs.append(f"Final Decision: Allocated P{i + 1} ({processes[i]} KB) to Partition {best_index + 1} ({blocks[best_index]} KB). Internal frag: {internal_frag[best_index]} KB.")
        else:
            step_logs.append(f"Final Decision: No suitable partition found for P{i + 1} ({processes[i]} KB). Process remains unallocated.")

        logs.append({"process": f"P{i + 1}", "size": processes[i], "steps": step_logs})

    return allocation, occupied, internal_frag, logs


def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    occupied = [False] * len(blocks)
    internal_frag = [0] * len(blocks)
    logs = []

    for i in range(len(processes)):
        worst_index = -1
        step_logs = []

        for j in range(len(blocks)):
            if occupied[j]:
                step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) is already occupied.")
            elif blocks[j] < processes[i]:
                step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) is too small for P{i + 1} ({processes[i]} KB).")
            else:
                if worst_index == -1 or blocks[j] > blocks[worst_index]:
                    worst_index = j
                    step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) qualifies (new largest candidate).")
                else:
                    step_logs.append(f"Partition {j + 1} ({blocks[j]} KB) qualifies but is smaller than Partition {worst_index + 1} ({blocks[worst_index]} KB).")

        if worst_index != -1:
            allocation[i] = worst_index
            occupied[worst_index] = True
            internal_frag[worst_index] = blocks[worst_index] - processes[i]
            step_logs.append(f"Final Decision: Allocated P{i + 1} ({processes[i]} KB) to Partition {worst_index + 1} ({blocks[worst_index]} KB). Internal frag: {internal_frag[worst_index]} KB.")
        else:
            step_logs.append(f"Final Decision: No suitable partition found for P{i + 1} ({processes[i]} KB). Process remains unallocated.")

        logs.append({"process": f"P{i + 1}", "size": processes[i], "steps": step_logs})

    return allocation, occupied, internal_frag, logs