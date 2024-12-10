from typing import List

def retrieve_input() -> List[List[str]]:
    input: List[List[str]] = []
    with open('day_4/data/input.txt') as file:
        for line in file.readlines():
            input.append([char for char in line if char != '\n'])

    return input

def get_xmas_found_count(input: List[List[str]]) -> int:

    directions = [
        [(0,1),(0,2),(0,3)],
        [(-1,1),(-2,2),(-3,3)],
        [(-1,0),(-2,0),(-3,0)],
        [(-1,-1),(-2,-2),(-3,-3)],
        [(0,-1),(0,-2),(0,-3)],
        [(1,-1),(2,-2),(3,-3)],
        [(1,0),(2,0),(3,0)],
        [(1,1),(2,2),(3,3)],
    ]
    word_dict = {
        0: 'M',
        1: 'A',
        2: 'S',
    }
    xmas_found_count = 0
    for x, x_value in enumerate(input):
        for y, _ in enumerate(x_value):
            if not input[x][y] == 'X':
                continue

            for direction in directions:
                skip_direction = False
                for i, movement in enumerate(direction):
                    new_x = x + movement[0]
                    new_y = y + movement[1]
                    if (new_x < 0 or new_x >= len(x_value) or
                        new_y < 0 or new_y >= len(input)):
                        skip_direction = True
                        break

                    if word_dict[i] != input[new_x][new_y]:
                        skip_direction = True
                        break

                if not skip_direction:
                    xmas_found_count += 1

    return xmas_found_count


def main():
    input = retrieve_input()
    xmas_found_count = get_xmas_found_count(input)
    print(xmas_found_count)

if __name__ == '__main__':
    main()