def get_neighbors(grid, row, col):
    """Get adjacent cells (all 8 neighbors including diagonals)."""
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:  # Skip the cell itself
                continue
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                neighbors.append((new_row, new_col))
    return neighbors


def count_adjacent_at_signs(grid, row, col):
    """Count how many neighbors are '@' symbols."""
    count = 0
    for nr, nc in get_neighbors(grid, row, col):
        if grid[nr][nc] == '@':
            count += 1
    return count


def parse_input(data):
    """Parse the input and solve the problem.

    Args:
        data: A list of strings from the input file

    Returns:
        The solution result
    """
    # Convert input to a 2D grid
    grid = [list(line.strip()) for line in data]
    
    result = 0
    
    # Count @ symbols that have fewer than 4 adjacent @ symbols
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                adjacent_count = count_adjacent_at_signs(grid, row, col)
                if adjacent_count < 4:
                    result += 1
    
    return result


def main():
    """Read input text, split into lines, and print the result."""
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    result = parse_input(lines)
    print(result)


if __name__ == "__main__":
    main()
