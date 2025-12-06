def parse_input(data):
    """Separate each line of input into a string.

    Args:
        data: A list of strings from the input file

    Returns:
        A list of strings, separated by newlines
    """
    return data


def find_largest_12_digit_number(number_sets):
    """Find the largest 12-digit number possible from the provided digits.
    
    Args:
        number_sets: A list of strings, each containing digits
        
    Returns:
        The largest 12-digit number that can be formed by selecting 12 digits
        from all concatenated strings while maintaining their original order.
    """
    # Concatenate all digits from all number sets
    all_digits = ''.join(number_sets)
    
    # Use a greedy approach to select the 12 largest digits while maintaining order
    # We need to select 12 digits from n digits, so we can skip at most n-12 digits
    max_skips = len(all_digits) - 12
    selected = []
    start_idx = 0
    
    for _ in range(12):
        # Find the largest digit in the remaining searchable range
        # We can skip at most max_skips digits
        end_idx = len(all_digits) - (12 - len(selected) - 1)
        largest_digit = max(all_digits[start_idx:end_idx])
        pos = all_digits.index(largest_digit, start_idx)
        selected.append(largest_digit)
        start_idx = pos + 1
    
    # Convert to integer
    largest_12_digit_num = int(''.join(selected))
    
    return largest_12_digit_num


def main():
    """Read input text, split into lines, and print the result."""
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    result = parse_input(lines)
    
    # Sum the largest 12-digit numbers from each line
    total = 0
    for line in result:
        num = find_largest_12_digit_number([line])
        total += num
    
    print(total)


if __name__ == "__main__":
    main()
