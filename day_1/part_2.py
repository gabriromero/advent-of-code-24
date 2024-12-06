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


def get_numbers_by_freq(numbers: List[int]) -> int:
    freq = {}
    for number in numbers:
        if number not in freq:
            freq[number] = 1
        else:
            freq[number] += 1

    return freq

def get_similarity_score(left_numbers: List[int], right_numbers_by_freq: dict) -> int:

    sum = 0
    for number in left_numbers:
        if number in right_numbers_by_freq:
            sum += number * right_numbers_by_freq[number]

    return sum

def main():
    left_numbers, right_numbers = retrieve_numbers_from_input()

    right_numbers_by_freq = get_numbers_by_freq(right_numbers)

    similarity_score = get_similarity_score(left_numbers, right_numbers_by_freq)

    print(similarity_score)

if __name__ == "__main__":
    main()