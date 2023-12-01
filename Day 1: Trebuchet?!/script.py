import re

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
    spelled_digits = {
        "one": "1",
        "two": "2", 
        "three": "3", 
        "four": "4",
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
    }

    with open("./input.txt") as my_file:
        lines = my_file.readlines()

    total_sum = 0
    for line in lines:
        line_digits = {}

        for (index, character) in enumerate(line):
            if character.isdigit():
                line_digits[index] = character

        for (spelled_digit, digit) in spelled_digits.items():
            pattern = re.compile(spelled_digit)
            matches = [match.start(0) for match in re.finditer(pattern, line)]
            for match in matches:
                line_digits[match] = digit

        sorted_line_digits = list(dict(sorted(line_digits.items())).values())
        total_sum += int(sorted_line_digits[0] + sorted_line_digits[-1])

    print("Answer 1 (Part 2): " + str(total_sum))

if __name__ == "__main__": 
    part_1()
    part_2()
    