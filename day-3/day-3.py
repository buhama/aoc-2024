import re

pattern = r"mul\(\d+,\d+\)"

def get_numbers_from_pattern(match):
    number_pattern = r"\d+"
    numbers = re.findall(number_pattern, match)
    num1, num2 = map(int, numbers)

    print(num1, num2)

    return num1 * num2

total_sum = 0
full_line = ""

with open("input.txt", "r") as file:
    combined_line = ""
    for line in file:
        combined_line += line

    split_by_dont = combined_line.split("don't()")
    for index, split in enumerate(split_by_dont):
        if index == 0:
            full_line += split
        else:
            split_by_do = split.split("do()")
            for index_do, split_by_do in enumerate(split_by_do):
                if index_do == 0: # the content between don't() and do()
                    continue
                else:
                    full_line += split_by_do
                

    matches = re.findall(pattern, full_line)
    total_sum += sum(get_numbers_from_pattern(match) for match in matches)

print(total_sum)
