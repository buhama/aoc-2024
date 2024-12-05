
from typing import List

rules = []
pages = []
adding_rules = True

def find_position_of_number(number, page):
    for index, page_number in enumerate(page):
        if page_number == number:
            return index
    return -1

def find_middle_number(page):
    return page[len(page) // 2]

def fix_page(page: List[int], first_number, second_number, first_num_position, second_num_position, rule):
    new_page = page.copy()
    new_page.pop(first_num_position)
    new_page.insert(second_num_position, first_number)
    
    return new_page


with open("input.txt", "r") as file:
    for line in file:
        if line.strip() == "":
            adding_rules = False
        elif adding_rules:
            rules.append(line.strip())
        else:
            numbers = line.strip().split(',')
            int_numbers = [int(x) for x in numbers]
            pages.append(int_numbers)


total_middle_sum = 0
total_middle_sum_fixed = 0
new_fixed_pages = []

def rules_passed(page, rules):
    new_page = page.copy()
    all_rules_passed = True
    
    while True:
        rules_failed = False
        for rule in rules:
            first_number = int(rule.split('|')[0])
            second_number = int(rule.split('|')[1])

            first_num_position = find_position_of_number(first_number, new_page)
            second_num_position = find_position_of_number(second_number, new_page)

            if first_num_position == -1 or second_num_position == -1:
                continue
            elif first_num_position < second_num_position:
                continue
            else:
                new_page = fix_page(new_page, first_number, second_number, first_num_position, second_num_position, rule)
                all_rules_passed = False
                rules_failed = True
                break
                
        if not rules_failed:
            break
            
    if not all_rules_passed:
        new_fixed_pages.append(new_page)
    
    return all_rules_passed


for page in pages:
    all_rules_passed = rules_passed(page, rules)

    if not all_rules_passed:
        continue
    else:
        total_middle_sum += find_middle_number(page)


for page in new_fixed_pages:
    total_middle_sum_fixed += find_middle_number(page)

print('Total middle sum', total_middle_sum)
print('Total middle sum fixed', total_middle_sum_fixed)