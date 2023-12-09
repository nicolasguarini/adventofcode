def split_list(input_list):
    result = [[]]
    
    for item in input_list:
        if item == "":
            result.append([])
        else:
            result[-1].append(item)
    
    return result

def part_1():
    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()
    
    lines = split_list(lines)
    
    seeds = [int(s) for s in lines[0][0].split(': ')[1].split()]
    maps_lines = lines[1:]

    maps = []
    for line in maps_lines:
        numbers = line[1:]
        current_nums = []

        for n in numbers:
            current_nums.append([int(x) for x in n.split()])

        maps.append(current_nums)

    for j in range(len(seeds)):
        for map in maps:
            for dest_start, src_start, ran_len in map:
                if seeds[j] >= src_start and seeds[j] <= src_start + ran_len - 1:
                    if dest_start < src_start:
                        seeds[j] -= src_start - dest_start
                        break
                    else:
                        seeds[j] += dest_start - src_start
                        break

    print(f"Day 5 (Part 1): {min(seeds)}")

def get_seeds(seeds):
    return [j for i in range(0, len(seeds), 2) for j in range(seeds[i], seeds[i] + seeds[i + 1])]

def part_2():
    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()
    
    lines = split_list(lines)
    
    seeds = [int(s) for s in lines[0][0].split(': ')[1].split()]
    maps_lines = lines[1:]

    maps = []
    for line in maps_lines:
        numbers = line[1:]
        current_nums = []

        for n in numbers:
            current_nums.append([int(x) for x in n.split()])

        maps.append(current_nums)

    seeds = get_seeds(seeds)

    for j in range(len(seeds)):
        for map in maps:
            for dest_start, src_start, ran_len in map:
                if seeds[j] >= src_start and seeds[j] <= src_start + ran_len - 1:
                    if dest_start < src_start:
                        seeds[j] -= src_start - dest_start
                        break
                    else:
                        seeds[j] += dest_start - src_start
                        break

    print(f"Day 5 (Part 2): {min(seeds)}")

if __name__ == "__main__":
    part_1()
    part_2()
