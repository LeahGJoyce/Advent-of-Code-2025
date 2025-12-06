from day3 import find_largest_12_digit_number
from itertools import combinations


def find_largest_two_digit_number(number_sets):
    """Find the largest number made from two digits from each set without rearranging.
    
    Args:
        number_sets: A list of strings, each containing digits
        
    Returns:
        The largest number that can be formed by picking two digits from each set
        while preserving their original order within each set.
    """
    max_number = -1
    
    # Generate all combinations of two digit indices for each set
    def generate_candidates(sets, current_number_str, set_index):
        nonlocal max_number
        
        if set_index == len(sets):
            if current_number_str:
                max_number = max(max_number, int(current_number_str))
            return
        
        # Get all 2-digit combinations from current set (preserving order)
        current_set = sets[set_index]
        if len(current_set) < 2:
            return  # Skip sets with less than 2 digits
            
        for i, j in combinations(range(len(current_set)), 2):
            digits = current_set[i] + current_set[j]
            generate_candidates(sets, current_number_str + digits, set_index + 1)
    
    generate_candidates(number_sets, "", 0)
    return max_number if max_number != -1 else None


def test_largest_two_digit_number():
    """Test finding the largest number from two digits of each set."""
    # Test case: Advent of Code data - largest 12-digit numbers
    aoc_data = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]
    
    # Expected 12-digit numbers from each set
    expected_numbers = [987654321111, 811111111119, 434234234278, 888911112111]
    expected_sum = 3121910778619
    
    results = []
    total = 0
    for data in aoc_data:
        num = find_largest_12_digit_number([data])
        results.append(num)
        total += num
    
    print(f"Largest 12-digit numbers: {results}")
    print(f"Expected numbers: {expected_numbers}")
    print(f"Sum: {total}")
    print(f"Expected sum: {expected_sum}")
    print(f"Test passed: {total == expected_sum}")


test_cases = [
    {
        "name": "Simple Two Sets",
        "input": ["123", "456"],
        "output": None,
    },
    {
        "name": "Different Digit Counts",
        "input": ["12", "789"],
        "output": None,
    },
    {
        "name": "Advent of Code Data",
        "input": [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111"
        ],
        "output": None,
    },
]


if __name__ == "__main__":
    test_largest_two_digit_number()
