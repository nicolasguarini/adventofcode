def get_sequences(numbers):
    sequences = [numbers]

    while(not all(n == 0 for n in sequences[-1])):
        new_line = []
        for i in range(len(sequences[-1])):
            if i < len(sequences[-1])-1:
                diff = sequences[-1][i+1]-sequences[-1][i]
                new_line.append(diff)
            else:
                break
        
        sequences.append(new_line)

    return sequences

def part_1():
    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()

    prediction_sum = 0
    for line in lines:
        numbers = [int(n) for n in line.split()]
        sequences = get_sequences(numbers)
        sequences = sequences[::-1]

        prediction = 0
        for i in range(1, len(sequences)):
            prediction += sequences[i][-1]

        print(prediction)
        prediction_sum += prediction

    print(f"Day 9 (Part 1): {prediction_sum}")
    
if __name__ == "__main__":
    part_1()