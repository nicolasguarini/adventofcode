def part_1():
    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()
    
    race_durations, race_records = lines
    race_durations = [int(x) for x in race_durations.split(':')[1].strip().split()]
    race_records = [int(x) for x in race_records.split(':')[1].strip().split()]

    races = zip(race_durations, race_records)
    result = 1

    for i, (duration, record) in enumerate(races):
        cont_win_ways = 0
        for ms_pressed in range(1, duration):
            remaining_ms = duration - ms_pressed
            mm_moved = ms_pressed * remaining_ms

            if mm_moved > record:
                cont_win_ways += 1

        print(f"Race {i}: {cont_win_ways} ways")
        result *= cont_win_ways

    print(f"Day 6 (Part 1): {result}")

def part_2():
    with open("input.txt") as my_file:
        lines = my_file.read().splitlines()
    
    race_duration, race_record = lines
    race_duration = int(''.join(race_duration.split(':')[1].strip().split()))
    race_record = int(''.join(race_record.split(':')[1].strip().split()))

    cont_win_ways = 0
    for ms_pressed in range(1, race_duration):
        remaining_ms = race_duration - ms_pressed
        mm_moved = ms_pressed * remaining_ms

        if mm_moved > race_record:
            cont_win_ways += 1

    print(f"Day 6 (Part 2): {cont_win_ways}")

if __name__ == "__main__":
    part_1()
    part_2()
