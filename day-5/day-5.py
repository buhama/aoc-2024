
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


for page in pages:
    all_rules_passed = True
    
    for rule in rules:
        first_number = int(rule.split('|')[0])
        second_number = int(rule.split('|')[1])

        first_num_position = find_position_of_number(first_number, page)
        second_num_position = find_position_of_number(second_number, page)

        if first_num_position == -1 or second_num_position == -1:
            continue
        elif first_num_position < second_num_position:
            continue
        else:
            all_rules_passed = False
            break

    if not all_rules_passed:
        continue
    else:
        total_middle_sum += find_middle_number(page)

print(total_middle_sum)