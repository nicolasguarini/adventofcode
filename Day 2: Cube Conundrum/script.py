def part_1():
    with open("input.txt") as my_file:
        games = my_file.readlines()
    
    bag = { "red": 12, "green": 13, "blue": 14 }

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

def part_2():
    with open("input.txt") as my_file:
        games = my_file.readlines()

    powers_sum = 0

    for game in games:
        minimum_sets = { "red": 0, "green": 0, "blue": 0 }
        grabs = game.split(': ')[1].split('; ')
        
        for grab in grabs:
            occurrences = grab.split(', ')

            for occurrence in occurrences:
                n, color = occurrence.split(' ')
                n = int(n)
                color = color.replace('\n', '')

                minimum_sets[color] = max(minimum_sets[color], n)

        power = 1
        for occurrences in minimum_sets.values():
            power *= occurrences

        powers_sum += power
    
    print(f"Answer (Part 2): {powers_sum}")

if __name__ == "__main__":
    part_1()
    part_2()
