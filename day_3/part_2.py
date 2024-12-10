import re

def retrieve_memory() -> str:
    memory = ''
    with open('day_3/data/input.txt') as file:
        for line in file.readlines():
            memory += line

    return memory

def get_sum_of_multiplications(memory) -> int:

    sum = 0
    is_enabled = True
    
    for i, _ in enumerate(memory):
        try:
            # enable
            if (memory[i] == 'd' and memory[i+1] == 'o' and 
                memory[i+2] == '(' and memory[i+3] == ')'):
                is_enabled = True


            # disable
            if (memory[i] == 'd' and memory[i+1] == 'o' and 
                memory[i+2] == 'n' and memory[i+3] == "'" and
                memory[i+4] == 't' and memory[i+5] == '(' and
                memory[i+6] == ')'):
                is_enabled = False

            # mul()
            if (is_enabled and memory[i] == 'm' and memory[i+1] == 'u' and 
                memory[i+2] == 'l' and memory[i+3] == '('):

                skip = False
                left_number = ''
                i_relative = i+4
                while(memory[i_relative]!=','):
                    if not memory[i_relative].isnumeric():
                        skip = True
                        break
                    left_number += memory[i_relative]
                    i_relative+=1

                if skip:
                    continue

                right_number = ''
                i_relative += 1
                while(memory[i_relative]!=')'):
                    if not memory[i_relative].isnumeric():
                        skip = True
                        break
                    right_number += memory[i_relative]
                    i_relative+=1

                if skip:
                    continue

                sum += int(left_number) * int(right_number)

        except IndexError:
            break
    

    return sum


def main():
    memory = retrieve_memory()
    sum_of_multiplications = get_sum_of_multiplications(memory)

    print(sum_of_multiplications)


if __name__ == '__main__':
    main()