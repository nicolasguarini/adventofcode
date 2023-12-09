import math

def preprocess_nodes(nodes):
    d = {}
    for node in nodes:
        curr, l_r = node.split(' = ')
        left, right = l_r[1:-1].split(', ')
        
        d[curr] = (left, right)

    return d

def preprocess_instructions(instructions):
    return instructions.replace('L', '0').replace('R', '1')

def part_1():
    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()

    instructions, nodes = lines[0], lines[2:]
    
    nodes = preprocess_nodes(nodes)
    instructions = preprocess_instructions(instructions)

    current_node = 'AAA'
    steps = 0
    
    while True:
        for instruction in instructions:
            current_node = nodes[current_node][int(instruction)]
            steps += 1

            if current_node == 'ZZZ':
                break

        if current_node == 'ZZZ':
            break

    print(f"Day 8 (Part 1): {steps}")

def get_starting_nodes(node_keys):
    return [key for key in node_keys if key[-1] == 'A']

def all_nodes_finished(nodes):
    return all(node[-1] == 'Z' for node in nodes)

def part_2_naive(): # you will wait millions of hours :)
    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()

    instructions, nodes = lines[0], lines[2:]
    nodes = preprocess_nodes(nodes)
    instructions = preprocess_instructions(instructions)
    current_nodes = get_starting_nodes(nodes.keys())

    print(current_nodes)

    steps = 0
    while not all_nodes_finished(current_nodes):
        for instruction in instructions:
            current_nodes = [nodes[node][int(instruction)] for node in current_nodes]
            steps += 1
        
    print(current_nodes)
    print(f"Day 8 (Part 2): {steps}")

def part_2_lcm():
    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()

    instructions, nodes = lines[0], lines[2:]
    nodes = preprocess_nodes(nodes)
    instructions = preprocess_instructions(instructions)
    starting_nodes = get_starting_nodes(nodes.keys())

    counts = []
    for next_node in starting_nodes:
        steps = 0
        i = 0

        while not next_node.endswith("Z"):
            if i >= len(instructions):
                i = 0

            cur_node = nodes[next_node]
            next_node = cur_node[int(instructions[i])]

            steps += 1
            i += 1

        counts.append(steps)

    result = math.lcm(*counts)
    
    print(f"Day 8 (Part 2): {result}")
    
if __name__ == "__main__":
    part_1()
    part_2_lcm()
