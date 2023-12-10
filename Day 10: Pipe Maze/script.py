lefts = ["-", "F", "L"]
rights = ["-", "J", "7"]
downs = ["|", "L", "J"]
ups = ["|", "F", "7"]

def find_starting_coordinates(lines):
    n_rows = len(lines)
    n_cols = len(lines[0])

    for i in range(n_rows):
        for j in range(n_cols):
            if lines[i][j] == 'S':
                return (i,j)
    
    return (-1, -1)

def find_connected_pipes(lines, coord):
    i,j = coord
    connected_pipes = []

    if lines[i+1][j] in downs:
        connected_pipes.append((i+1, j))

    if lines[i][j+1] in rights:
        connected_pipes.append((i, j+1))
    
    if lines[i-1][j] in ups:
        connected_pipes.append((i-1, j))
    
    if lines[i][j-1] in lefts:
        connected_pipes.append((i, j-1))

    return connected_pipes

def find_next_pipe(lines, current_coord, previous_coord):
    ci, cj = current_coord
    pi, pj = previous_coord

    if lines[ci][cj] == "-":
        if pj > cj: # check left
            if lines[ci][cj-1] in lefts:
                return (ci, cj-1)
        else: # check right
            if lines[ci][cj+1] in rights:
                return (ci, cj+1)
            
    if lines[ci][cj] == "|":
        if pi < ci: # check down
            if lines[ci+1][cj] in downs:
                return (ci+1, cj)
        else: # check up
            if lines[ci-1][cj] in ups:
                return (ci-1, cj)
            
    if lines[ci][cj] == "L":
        if pi < ci: # check right
            if lines[ci][cj+1] in rights:
                return (ci, cj+1)
        else: # check up 
            if lines[ci-1][cj] in ups:
                return (ci-1, cj)
            
    if lines[ci][cj] == "J":
        if pi < ci: # check left
            if lines[ci][cj-1] in lefts:
                return (ci, cj-1)
        else: # check up
            if lines[ci-1][cj] in ups:
                return (ci-1, cj)
            
    if lines[ci][cj] == "7":
        if pi > ci: # check left
            if lines[ci][cj-1] in lefts:
                return (ci, cj-1)
        else: # check down
            if lines[ci+1][cj] in downs:
                return (ci+1, cj)
            
    if lines[ci][cj] == "F":
        if pi > ci: # check right
            if lines[ci][cj+1] in rights:
                return (ci, cj+1)
        else: # check down
            if lines[ci+1][cj] in downs:
                return (ci+1, cj)

    return (-1, -1)

def part_1():
    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()

    starting_coordinates = find_starting_coordinates(lines)
    connected_pipes = find_connected_pipes(lines, starting_coordinates)
    print(f"Starting: {starting_coordinates}")
    print(f"Runners: {connected_pipes}")

    prev_1 = starting_coordinates
    prev_2 = starting_coordinates
    runner_1, runner_2 = connected_pipes

    steps = 1
    while runner_1 != runner_2:
        temp = runner_1
        runner_1 = find_next_pipe(lines, runner_1, prev_1)
        prev_1 = temp

        temp = runner_2
        runner_2 = find_next_pipe(lines, runner_2, prev_2)
        prev_2 = temp

        steps += 1
    
    print(f"Day 10 (Part 1): {steps}")

part_1()