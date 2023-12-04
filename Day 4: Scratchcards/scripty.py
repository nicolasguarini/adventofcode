def read_cards(filename="input.txt"):
    with open(filename) as file:
        return file.read().split('\n')

def calculate_score(winning_numbers, my_numbers):
    score = 0
    for num in my_numbers:
        if num in winning_numbers:
            score = max(1, score * 2)
    return score

def part_1():
    cards = read_cards()

    total_points = 0
    for card in cards:
        _, numbers = card.split(": ")
        winning_numbers, my_numbers = map(str.split, numbers.split(" | "))
        
        total_points += calculate_score(winning_numbers, my_numbers)

    print(f"Day 4 (Part 1): {total_points}")

def part_2():
    cards = read_cards()
    scratchcards = {i + 1: 1 for i in range(len(cards))}

    for id, card in enumerate(cards, start=1):
        _, numbers = card.split(": ")
        winning_numbers, my_numbers = map(str.split, numbers.split(" | "))

        matches = sum(num in winning_numbers for num in my_numbers)
        for i in range(id + 1, id + 1 + matches):
            scratchcards[i] += scratchcards[id]

    print(f"Day 4 (Part 2): {sum(scratchcards.values())}")

if __name__ == "__main__":
    part_1()
    part_2()
