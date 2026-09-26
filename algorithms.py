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