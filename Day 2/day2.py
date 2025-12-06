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
    """Find IDs made entirely of repeating patterns

    Args:
       range_str: A string in format "11-22"

    Returns:
        A list of IDs that are made entirely of a repeating pattern.
    """
    start, end = map(int, range_str.split("-"))
    ids_with_repeats = []
    
    for num in range(start, end + 1):
        num_str = str(num)
        length = len(num_str)
        # Check all possible pattern lengths
        for pattern_len in range(1, length // 2 + 1):
            if length % pattern_len == 0:
                pattern = num_str[:pattern_len]
                if pattern * (length // pattern_len) == num_str:
                    ids_with_repeats.append(num)
                    break
    
    return ids_with_repeats

def main():
    """Read input text, split into ranges, find invalid ID's in each range, add them together, print the result."""
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    ranges = parse_input(lines)
    total = 0
    for range_str in ranges:
        invalid_ids = find_ids_in_range(range_str)
        total += sum(invalid_ids)
    
    print(f"Sum of all invalid IDs: {total}")


if __name__ == "__main__":
    main()
