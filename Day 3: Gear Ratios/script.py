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

def check_line(direction, lines, i, j, h=False):
    current_number = ''

    if not(i >= 0 and i < len(lines)):
        return current_number
    
    line = lines[i]
    
    if h and not line[j].isdigit():
        return current_number

    if i >= 0 and i < len(lines) and j >= 0 and j < len(line):
        if line[j].isdigit():
            current_number += line[j]
        
        if j > 0 and j < len(line):
            j += direction

            while j >= 0 and j < len(line) and line[j].isdigit():
                current_number += line[j]
                j += direction

    if direction == -1:
        current_number = current_number[::-1]

    return current_number

def get_gear_ratio(lines, i, j):
    nums = []
    
    usx = check_line(-1, lines, i-1, j)
    udx = check_line(1, lines, i-1, j)
    dx = check_line(1, lines, i, j+1, h=True)
    sx = check_line(-1, lines, i, j-1, h=True)
    bsx = check_line(-1, lines, i+1, j)
    bdx = check_line(1, lines, i+1, j)

    if i > 0:
        if not lines[i-1][j].isdigit():
            if usx:
                nums.append(int(usx))
            
            if udx:
                nums.append(int(udx))
        else:
            nums.append(int(usx+udx[1:]))
    
    if i < len(lines)-1:
        if not lines[i+1][j].isdigit():
            if bsx:
                nums.append(int(bsx))
            
            if bdx:
                nums.append(int(bdx))
        else:
            nums.append(int(bsx+bdx[1:]))
 
    if dx:
        nums.append(int(dx))
    
    if sx: 
        nums.append(int(sx))

    if len(nums) == 2:
        return nums[0] * nums[1]

    return 0

def part_2():
    with open("input.txt") as my_file:
        lines = my_file.read().split('\n')

    total_sum = 0
    for i, line in enumerate(lines):
        for j, character in enumerate(line):
            if character == '*':
                total_sum += get_gear_ratio(lines, i, j)
    
    print(f"Day 3 (Part 2): {total_sum}")

if __name__ == "__main__":
    part_1()
    part_2()
