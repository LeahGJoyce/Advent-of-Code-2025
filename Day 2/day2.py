def parse_input(data):
    """Read in text file and return as list of strings.

    Args:
       filename: The input file name

    Returns:
        A list of input ranges. ["11-22", "33-44", ...]
    """
    ranges = []
    for line in data:
        # Split by comma and filter out empty strings
        line_ranges = [r.strip() for r in line.split(",") if r.strip()]
        ranges.extend(line_ranges)
    return ranges

def find_ids_in_range(range_str):
    """Find invalid ID's in range using regex

    Args:
       range_str: A string in format "11-22"

    Returns:
        A list of invalid ID's in the given range.
    """
    start, end = map(int, range_str.split("-"))
    invalid_ids = []
    
    for num in range(start, end + 1):
        num_str = str(num)
        # Check if the number is a sequence repeated exactly twice
        length = len(num_str)
        if length % 2 == 0:
            mid = length // 2
            if num_str[:mid] == num_str[mid:]:
                invalid_ids.append(num)
    
    return invalid_ids

def main():
    """Read input text, split into ranges, find invalid ID's in each range, add them together, print the result."""
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    result = parse_input(lines)
    print(result)


if __name__ == "__main__":
    main()
