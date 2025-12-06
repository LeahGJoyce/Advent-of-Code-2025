def parse_input(lines):
    """
    Parse the input into a 2D map/grid.
    Returns a list of lists or 2D array.
    """
    grid = [list(line.strip()) for line in lines]
    return grid




def get_neighbors(grid, row, col):
    """Get adjacent cells (up, down, left, right) or all 8 neighbors."""
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # or add diagonals
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            neighbors.append((new_row, new_col))
    return neighbors


def count_adjacent(grid, row, col, target_char):
    """Count how many neighbors match a target character."""
    count = 0
    for nr, nc in get_neighbors(grid, row, col):
        if grid[nr][nc] == target_char:
            count += 1
    return count


def test_fewer_than_four_adjacent():
    """Test counting @ symbols with fewer than 4 adjacent @ symbols."""
    from day4 import count_adjacent_at_signs
    
    test_input = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@."
    ]
    
    grid = parse_input(test_input)
    count = 0
    
    # Count @ symbols with fewer than 4 adjacent @ symbols
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                adjacent_count = count_adjacent_at_signs(grid, row, col)
                if adjacent_count < 4:
                    count += 1
    
    assert count == 13, f"Expected 13, but got {count}"
    print(f"Test passed! Found {count} @ symbols with fewer than 4 adjacent @ symbols")


if __name__ == "__main__":
    test_fewer_than_four_adjacent()
