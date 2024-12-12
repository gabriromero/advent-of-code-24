from typing import List

def retrieve_input() -> List[List[str]]:
    input: List[List[str]] = []
    with open('day_4/data/input.txt') as file:
        for line in file.readlines():
            input.append([char for char in line if char != '\n'])

    return input

def get_letter_by_position(x: str, y: str, input) -> str:
    if (x < 0 or x >= len(input[0]) or
        y < 0 or y >= len(input)):
        return ''
    
    return input[x][y]


def get_xmas_found_count(input: List[List[str]]) -> int:

    xmas_found_count = 0
    for x, x_value in enumerate(input):
        for y, _ in enumerate(x_value):
            if not input[x][y] == 'A':
                continue

            if set(
                [
                    get_letter_by_position(x+1,y+1,input),
                    get_letter_by_position(x-1,y-1,input)
                ]
            ) == {'M','S'} and (
                set(
                [
                    get_letter_by_position(x-1,y+1,input),
                    get_letter_by_position(x+1,y-1,input)
                ]
            )
            ) == {'M','S'}:
                xmas_found_count += 1

    return xmas_found_count


def main():
    input = retrieve_input()
    xmas_found_count = get_xmas_found_count(input)
    print(xmas_found_count)

if __name__ == '__main__':
    main()