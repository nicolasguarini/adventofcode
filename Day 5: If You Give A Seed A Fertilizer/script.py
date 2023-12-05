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

    print(f"Seeds: {str(seeds)}")
    for i, map in enumerate(maps, start=1):
        d = {}
        for dest_start, src_start, ran_len in map:
            range_src = range(src_start, src_start + ran_len)
            range_dest = range(dest_start, dest_start + ran_len)

            d.update(zip(range_src, range_dest))

        for j, n in enumerate(seeds):
            if n in d:
                seeds[j] = d[n]
        
        print(f"Seeds (map {i}): {str(seeds)}")

    print(f"Day 5 (Part 1): {min(seeds)}")

if __name__ == "__main__":
    part_1()