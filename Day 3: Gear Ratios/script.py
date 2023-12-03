def is_valid_char(char):
    return char != '.' and not char.isdigit()

def check_adjacents(lines, i, start, end):
    if end < len(lines[0]) - 1 and is_valid_char(lines[i][end + 1]):
        return True
    
    if start > 0 and is_valid_char(lines[i][start - 1]):
        return True
    
    if i > 0:
        for idx in range(start, end + 1):
            if is_valid_char(lines[i - 1][idx]):
                return True
        
        if start > 0 and is_valid_char(lines[i - 1][start - 1]):
            return True
        
        if end < len(lines[0]) - 1 and is_valid_char(lines[i - 1][end + 1]):
            return True
    
    if i < len(lines) - 1:
        for idx in range(start, end + 1):
            if is_valid_char(lines[i + 1][idx]):
                return True

        if start > 0 and is_valid_char(lines[i + 1][start - 1]):
            return True
        
        if end < len(lines[0]) - 1 and is_valid_char(lines[i + 1][end + 1]):
            return True

    return False

def part_1():
    with open("input.txt") as my_file:
        lines = my_file.read().split('\n')

    def process_number(i, start, end, current_number):
        if check_adjacents(lines=lines, i=i, start=start, end=end):
            return int(current_number)
        else:
            return 0

    total_sum = 0
    for i, line in enumerate(lines):
        if not line:
            continue

        scanning_number = False
        start_number = -1
        current_number = ''

        for j, character in enumerate(line):
            if character.isdigit():
                if not scanning_number:
                    scanning_number = True
                    start_number = j
                current_number += character
            elif scanning_number:
                total_sum += process_number(i, start_number, j - 1, current_number)
                scanning_number = False
                current_number = ''

        if scanning_number:
            total_sum += process_number(i, start_number, len(line) - 1, current_number)

    print(f"Day 3 (Part 1): {total_sum}")

def part_2():
    #TODO
    pass

if __name__ == "__main__":
    part_1()
    part_2()