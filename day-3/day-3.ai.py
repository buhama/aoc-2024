import re

# Function to extract numbers from a valid `mul` pattern and calculate the product
def get_numbers_from_pattern(match):
    """
    Extracts two numbers from a match in the format mul(X,Y), where X and Y are integers.
    Returns the product of the two numbers.
    """
    number_pattern = r"\d+"  # Matches one or more digits
    numbers = re.findall(number_pattern, match)  # Find all numbers in the string
    num1, num2 = map(int, numbers)  # Convert the numbers to integers
    return num1 * num2  # Return their product

def calculate_total_sum(file_path):
    """
    Reads a file, processes instructions (mul, don't(), do()), and calculates the sum of valid enabled `mul` instructions.
    """
    # Regular expression to match valid `mul(X,Y)` patterns
    pattern = r"mul\(\d+,\d+\)"
    
    # Initial states
    total_sum = 0  # To store the final sum of enabled `mul` results
    is_enabled = True  # At the beginning, mul instructions are enabled

    # Read the entire file content
    with open(file_path, "r") as file:
        memory = file.read()  # Read the entire corrupted memory into a string

    # Split the content by "don't()" and "do()" to handle enable/disable logic
    sections = re.split(r"(don't\(\)|do\(\))", memory)

    for section in sections:
        if section == "don't()":
            is_enabled = False  # Disable future mul instructions
        elif section == "do()":
            is_enabled = True  # Enable future mul instructions
        else:
            if is_enabled:  # Only process `mul` instructions if enabled
                matches = re.findall(pattern, section)  # Find all valid `mul` patterns
                for match in matches:
                    total_sum += get_numbers_from_pattern(match)  # Add the product to the total sum

    return total_sum  # Return the final calculated sum

# Main program
if __name__ == "__main__":
    # Path to the input file
    input_file = "input.txt"
    # Calculate and print the total sum of valid multiplications
    result = calculate_total_sum(input_file)
    print("The total sum of valid multiplications is:", result)
