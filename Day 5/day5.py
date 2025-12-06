def get_all_valid_ids(data):
    """Get count of all possible valid IDs from the provided ranges.

    Args:
        data: A list of strings from the input file with ranges

    Returns:
        Count of all unique IDs contained within the provided ranges
    """
    ranges = []
    found_empty = False
    
    for line in data:
        if line.strip() == "":
            found_empty = True
        elif not found_empty:
            # Parse range (e.g., "3-5")
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            break  # Stop once we hit the IDs section
    
    if not ranges:
        return 0
    
    # Sort ranges by start position
    ranges.sort()
    
    # Merge overlapping ranges and count unique IDs
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            # Overlapping or adjacent ranges, merge them
            merged[-1] = (last_start, max(last_end, end))
        else:
            # Non-overlapping range
            merged.append((start, end))
    
    # Count total unique IDs from merged ranges
    valid_count = 0
    for start, end in merged:
        valid_count += (end - start + 1)
    
    return valid_count


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
    
    all_valid_count = get_all_valid_ids(lines)
    print(f"All possible valid IDs: {all_valid_count}")


if __name__ == "__main__":
    main()
