def parse_input(data):
    """Parse the input and solve the problem.

    Args:
        data: A list of strings from the input file

    Returns:
        The number of times the line splits
    """
    # Find the starting point 'S'
    start_row = None
    start_col = None
    for i, line in enumerate(data):
        if 'S' in line:
            start_row = i
            start_col = line.index('S')
            break
    
    if start_row is None:
        return 0
    
    # Track all beams as (row, col)
    # Beams always travel downward
    beams = {(start_row, start_col)}
    visited = set()
    split_count = 0
    
    while beams:
        new_beams = set()
        
        for row, col in beams:
            # Move downward
            new_row = row + 1
            
            # Check bounds
            if new_row >= len(data):
                continue
            
            # Check if out of bounds horizontally
            if col < 0 or col >= len(data[0]):
                continue
            
            # Check if we've been at this position before
            if (new_row, col) in visited:
                continue
            visited.add((new_row, col))
            
            # Check what's at this position
            if data[new_row][col] == '^':
                # Hit a splitter - split into left and right beams
                split_count += 1
                # Left beam
                if col - 1 >= 0:
                    new_beams.add((new_row, col - 1))
                # Right beam
                if col + 1 < len(data[0]):
                    new_beams.add((new_row, col + 1))
            else:
                # Continue downward with same beam
                new_beams.add((new_row, col))
        
        beams = new_beams
    
    return split_count


def main():
    """Read input text, split into lines, and print the result."""
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    result = parse_input(lines)
    print(result)


if __name__ == "__main__":
    main()
