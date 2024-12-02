safe_levels = 0

def is_safe_part_1(line_numbers): # 639
    order = 'none'
    if int(line_numbers[0]) < int(line_numbers[1]):
        order = 'ascending'
    elif int(line_numbers[0]) > int(line_numbers[1]):
        order = 'descending'

    for index, number in enumerate(line_numbers):
        if (int(index) + 1) >= len(line_numbers):
            break
        difference = int(line_numbers[int(index) + 1]) - int(number)
        if abs(difference) < 1 or abs(difference) > 3:
            return False
        if difference < 0:
            if order == 'ascending':
                return False
        elif difference > 0:
            if order == 'descending':
                return False
    return True

def check_after_removing(line_numbers, index):
    numbers_after_removing_index = line_numbers.copy()
    numbers_after_removing_index.pop(index)
    
    if (is_safe_part_2(numbers_after_removing_index, False)):
        return True
    
    if index < len(line_numbers):
        numbers_after_removing_index_plus_one = line_numbers.copy()
        numbers_after_removing_index_plus_one.pop(index + 1)
        if (is_safe_part_2(numbers_after_removing_index_plus_one, False)):
            return True
    
    if index >= 0:
        numbers_after_removing_index_minus_one = line_numbers.copy()
        numbers_after_removing_index_minus_one.pop(index - 1)
        if (is_safe_part_2(numbers_after_removing_index_minus_one, False)):
            return True
    return False

def is_safe_part_2(line_numbers, allow_removing_numbers=False): # 674
    order = 'none'
    if int(line_numbers[0]) < int(line_numbers[1]):
        order = 'ascending'
    elif int(line_numbers[0]) > int(line_numbers[1]):
        order = 'descending'

    for index, number in enumerate(line_numbers):
        if (int(index) + 1) >= len(line_numbers):
            break
        difference = int(line_numbers[int(index) + 1]) - int(number)
        
        if abs(difference) < 1 or abs(difference) > 3:
            if allow_removing_numbers:
                return check_after_removing(line_numbers, index)
            else:
                return False
        if difference < 0:
            if order == 'ascending':
                if allow_removing_numbers:
                    return check_after_removing(line_numbers, index)
                else:
                    return False
        elif difference > 0:
            if order == 'descending':
                if allow_removing_numbers:
                    return check_after_removing(line_numbers, index)
                else:
                    return False
    return True

with open("input.txt", "r") as file:
    for line in file:
        line_numbers = line.split()

        if is_safe_part_2(line_numbers, False):
            safe_levels += 1

print(f"\nFinal safe levels: {safe_levels}")
