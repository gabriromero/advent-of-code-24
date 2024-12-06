from typing import List, Tuple

def insert_in_ordered_list(list: List[int], number: int):
    low = 0
    high = len(list)

    while low != high:
        mid = (low+high) // 2
        if list[mid] < number:
            low = mid + 1
        else:
            high = mid

    list.insert(low, number)

def retrieve_numbers_from_input() -> Tuple[List[int], List[int]]:
    left_numbers: List[int] = []
    right_numbers: List[int] = []

    with open('day_1/inputs/input_part_1.txt') as file:
        for line in file.readlines():
            line_numbers: List[str] = line.split()
            insert_in_ordered_list(left_numbers, int(line_numbers[0]))
            insert_in_ordered_list(right_numbers, int(line_numbers[1]))

    return (left_numbers, right_numbers)


def main():
    left_numbers, right_numbers = retrieve_numbers_from_input()
    
    sum = 0
    for i in range(len(left_numbers)):
        sum += abs(left_numbers[i] - right_numbers[i])

    print(sum)

if __name__ == "__main__":
    main()