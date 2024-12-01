# Import Counter to help count occurrences of numbers efficiently
from collections import Counter

# Read input data and process in a single pass using zip and map
with open("input.txt", "r") as file:
    # For each line: split into two parts, convert both to integers, and create two lists
    # map(int, line.split()) converts both numbers to integers
    # zip(*...) unpacks the pairs into two separate lists
    left_list, right_list = zip(*(map(int, line.split()) for line in file))

# Part 1: Calculate differences between sorted lists
# zip() pairs up the numbers from both sorted lists
# [abs(r - l) for ...] creates a list of absolute differences between each pair
differences = [abs(r - l) for r, l in zip(sorted(right_list), sorted(left_list))]
# Sum all differences to get final result
print(f"Part 1: {sum(differences)}")  # 1765812

# Part 2: Calculate similarity score using Counter
# Counter creates a dictionary where keys are numbers and values are how often they appear
right_counts = Counter(right_list)
# For each number in left_list:
#   - right_counts[num] gets how many times that number appears in right_list
#   - multiply by num and sum all results
similarity_score = sum(num * right_counts[num] for num in left_list)
print(f"Part 2: {similarity_score}")  # 20520794
