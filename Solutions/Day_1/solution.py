from typing import Tuple
from read_input import read_input_from_daynum
import re
# Part 1
def get_digit_from_line(line) -> str:
    for char in line:
        if char.isnumeric():
            return char

def part_1(input_lines):
    line_nums = []
    for line in input_lines:
        first = get_digit_from_line(line)
        second = get_digit_from_line(line[::-1])
        line_nums.append(int(f"{first}{second}"))
    return sum(line_nums)

# Part 2

NUMBER_MAP = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def get_num_from_str(number_str: str) -> str:
    return (
        str(NUMBER_MAP[number_str])
        if NUMBER_MAP.get(number_str)
        else number_str
    )

def part_2(input_lines):
    total = 0
    for line in input_lines:
        numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',line)
        for item in numbers:
            # Unjumble bound strings
            num = get_num_from_str(item)
            new_sub = item[0] + num + item[-1]
            line = re.sub(item,new_sub,line)
        numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        if len(numbers) == 1:
            number = get_num_from_str(numbers[0])
            value = int(number + number)
        else:
            front = get_num_from_str(numbers[0])
            back = get_num_from_str(numbers[-1])
            value = int(front + back)
        total += value
    return total

def main():
    input_lines = read_input_from_daynum(1, readlines=True)
    part_1_solution = part_1(input_lines)
    part_2_solution = part_2(input_lines)

if __name__ == "__main__":
    main()