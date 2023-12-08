def get_card_occ(hand):
    card_occ = {}

    for card in hand:
        if card in card_occ:
            card_occ[card] += 1
        else:
            card_occ[card] = 1

    return card_occ

def card_rank(card):
    card_strength = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

    return card_strength[card]

def hand_type(hand):
    if len(set(hand)) == 1:
        return 7  # Five of a kind
    elif len(set(hand)) == 2:
        counts = [hand.count(card) for card in set(hand)]
        if 4 in counts:
            return 6  # Four of a kind
        else:
            return 5  # Full house
    elif len(set(hand)) == 3:
        counts = [hand.count(card) for card in set(hand)]
        if 3 in counts:
            return 4  # Three of a kind
        else:
            return 2  # Two pair
    elif len(set(hand)) == 4:
        return 1  # One pair
    else:
        return 0  # High card
    
def compare_hands(hand1, hand2):
    type1, type2 = hand_type(hand1), hand_type(hand2)
    if type1 < type2:
        return -1
    elif type1 > type2:
        return 1

    for card1, card2 in zip(hand1, hand2):
        rank1, rank2 = card_rank(card1), card_rank(card2)
        if rank1 < rank2:
            return -1
        elif rank1 > rank2:
            return 1
        
    return 0

def custom_sort(hands):
    # Implementazione dell'algoritmo di ordinamento personalizzato
    for i in range(len(hands)):
        for j in range(i + 1, len(hands)):
            comparison_result = compare_hands(hands[i][0], hands[j][0])
            if comparison_result == 1:
                hands[i], hands[j] = hands[j], hands[i]

def part_1():
    with open("example.txt") as my_file:
        lines = my_file.read().splitlines()
    
    hands = [tuple(line.split()) for line in lines]
    custom_sort(hands)
    
    total_winning = 0
    for idx, (hand, bid) in enumerate(hands, start=1):
        total_winning += int(bid) * idx
    
    print(f"Day 7 (Part 1): {total_winning}")


if __name__ == "__main__": 
    part_1() # 6592
