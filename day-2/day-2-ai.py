from typing import List

def is_safe_part_1(numbers: List[str]) -> bool:
    # Convert all numbers to integers once at the start
    nums = [int(n) for n in numbers]
    
    # Determine if sequence is ascending or descending based on first two numbers
    is_ascending = nums[0] < nums[1]
    
    # Check each pair of adjacent numbers
    for i in range(len(nums) - 1):
        difference = nums[i + 1] - nums[i]
        
        # Rule 1: Difference must be between 1 and 3
        if not (1 <= abs(difference) <= 3):
            return False
            
        # Rule 2: Must maintain consistent direction
        if (is_ascending and difference < 0) or (not is_ascending and difference > 0):
            return False
            
    return True

def check_removals(numbers: List[int]) -> bool:
    """Try removing each number and its neighbors to find a valid sequence"""
    for i in range(len(numbers)):
        # Create three possible lists by removing current number and its neighbors
        candidates = [
            numbers[:i] + numbers[i+1:],  # Remove current number
            numbers[:i-1] + numbers[i:] if i > 0 else None,  # Remove previous number
            numbers[:i] + numbers[i+2:] if i < len(numbers)-1 else None  # Remove next number
        ]
        
        # Check each candidate list
        for candidate in candidates:
            if candidate and is_safe_part_2(candidate, False):
                return True
    return False

def is_safe_part_2(numbers: List[str], allow_removals: bool = False) -> bool:
    # Convert all numbers to integers once at the start
    nums = [int(n) for n in numbers]
    
    # Determine if sequence is ascending or descending based on first two numbers
    is_ascending = nums[0] < nums[1]
    
    # Check each pair of adjacent numbers
    for i in range(len(nums) - 1):
        difference = nums[i + 1] - nums[i]
        
        # Check if rules are violated
        rules_violated = (
            not (1 <= abs(difference) <= 3) or  # Difference rule
            (is_ascending and difference < 0) or  # Direction rule for ascending
            (not is_ascending and difference > 0)  # Direction rule for descending
        )
        
        if rules_violated:
            # If removals are allowed, try removing numbers to fix the sequence
            return check_removals(nums) if allow_removals else False
            
    return True

def main():
    safe_levels = 0
    
    # Using 'with' ensures file is properly closed after reading
    with open("input.txt", "r") as file:
        for line in file:
            numbers = line.split()
            
            # Part 2: Check if sequence is safe (without removals for this puzzle)
            if is_safe_part_2(numbers, False):
                safe_levels += 1
    
    print(f"\nFinal safe levels: {safe_levels}")

if __name__ == "__main__":
    main()
