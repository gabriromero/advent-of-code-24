import re

def retrieve_memory() -> str:
    memory = ''
    with open('day_3/data/input.txt') as file:
        for line in file.readlines():
            memory += line

    return memory

def get_sum_of_multiplications(memory) -> int:
    matches = re.findall(r"mul\((\d+),(\d+)\)", memory)

    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])

    return sum


def main():
    memory = retrieve_memory()
    sum_of_multiplications = get_sum_of_multiplications(memory)

    print(sum_of_multiplications)


if __name__ == '__main__':
    main()