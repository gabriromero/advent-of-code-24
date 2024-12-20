from typing import List, Tuple

def retrieve_numbers_from_input() -> Tuple[List[int], List[int]]:
    left_numbers: List[int] = []
    right_numbers: List[int] = []

    with open('day_1/data/input.txt') as file:
        for line in file.readlines():
            line_numbers: List[str] = line.split()
            left_numbers.append(int(line_numbers[0]))
            right_numbers.append(int(line_numbers[1]))

    return (left_numbers, right_numbers)


def get_total_distance(left_numbers: List[int], right_numbers: List[int]) -> int:

    left_numbers.sort()
    right_numbers.sort()
    
    sum = 0
    for i in range(len(left_numbers)):
        sum += abs(left_numbers[i] - right_numbers[i])

    return sum

def main():
    left_numbers, right_numbers = retrieve_numbers_from_input()

    total_distance = get_total_distance(left_numbers, right_numbers)

    print(total_distance)

if __name__ == "__main__":
    main()