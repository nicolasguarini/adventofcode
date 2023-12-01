def part_1():
    with open("./input.txt") as my_file:
        lines = my_file.readlines()

    total_sum = 0
    for line in lines:
        line_digits = []

        for character in line:
            if character.isdigit():
                line_digits.append(character)
        
        total_sum += int(line_digits[0] + line_digits[-1])

    print("Answer (Part 1): " + str(total_sum))

def part_2():
    pass

if __name__ == "__main__": 
    part_1()
    part_2()