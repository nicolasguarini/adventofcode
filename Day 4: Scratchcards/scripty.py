def part_1():
    with open("input.txt") as my_file:
        cards = my_file.read().split('\n')

    total_points = 0

    for card in cards:
        card_id, numbers = card.split(": ")
        winning_numbers, my_numbers = numbers.split(" | ")

        winning_numbers = [n for n in winning_numbers.split()]
        my_numbers = [n for n in my_numbers.split()]
        
        card_score = 0
        for n in my_numbers:
            if n in winning_numbers:
                if card_score <= 0:
                    card_score = 1
                else:
                    card_score *= 2

        total_points += card_score

        print(f"{card_id} score: {card_score}")
    
    print(f"Day 4 (Part 1): {total_points}")

def part_2():
    pass

if __name__ == "__main__":
    part_1()
    part_2()