def part_1():
    with open("input.txt") as my_file:
        games = my_file.readlines()
    
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    id = 1
    id_sum = 0

    for game in games:
        is_valid = True
        grabs = game.split(': ')[1].split('; ')

        for grab in grabs:
            occurrences = grab.split(', ')

            for occurrence in occurrences:
                n, color = occurrence.split(' ')
                
                if bag[color.replace('\n', '')] < int(n):
                    is_valid = False
                    break

            if not is_valid:
                break

        if is_valid:
            id_sum += id
        id += 1
    
    print("Answer (Part 1): " + str(id_sum))

if __name__ == "__main__":
    part_1()
