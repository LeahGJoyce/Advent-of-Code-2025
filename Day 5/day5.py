def parse_input(data):
    """A list of ranges and a list of strings.

    Args:
        data: A list of strings from the input file and a list of ranges that may or may not contain the provided IDs

    Returns:
        How many of the ID's are contained within the provided ranges
    """
    # Split ranges and IDs by empty line
    ranges = []
    ids = []
    found_empty = False
    
    for line in data:
        if line.strip() == "":
            found_empty = True
        elif not found_empty:
            # Parse range (e.g., "3-5")
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            # Parse ID
            ids.append(int(line))
    
    # Count valid IDs (those contained in at least one range)
    valid_count = 0
    for id_val in ids:
        for start, end in ranges:
            if start <= id_val <= end:
                valid_count += 1
                break  # ID is valid, move to next ID
    
    return valid_count


def main():
    """Read input text, split into lines, and print the result."""
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    result = parse_input(lines)
    print(f"Valid IDs: {result}")


if __name__ == "__main__":
    main()
