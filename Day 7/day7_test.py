from day7 import parse_input


def visualize_grid(input_data, result):
    """Visualize the grid with the beam paths."""
    print("\nVisualized Grid:")
    for i, line in enumerate(input_data):
        print(f"Row {i}: {line}")
    print(f"\nResult: {result} splits\n")


def test_parse_input():
    """Read each line from top to bottom, following the path of '^' characters."""
    input_data = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]

    result = parse_input(input_data)
    visualize_grid(input_data, result)
    expected = 21
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Test passed! Result: {result}")


def test_vertical_split():
    """Test a vertical line from S that splits when hitting ^ characters."""
    input_data = [
        "...S...",
        "...^...",
        "...^...",
        "...^...",
        "...^...",
        ".^...^.",
    ]
    
    result = parse_input(input_data)
    visualize_grid(input_data, result)
    # The line starts at S (row 0, col 3), goes downward and splits once at the first ^ (row 1)
    # Expected: 1 split
    expected = 1  # 1 split at row 1
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Vertical split test passed! Result: {result}")


test_cases = [
    {
        "name": "Sample Test Case 1",
        "input": [
            # TODO: Add sample data
        ],
        "output": "0",
    },
]


if __name__ == "__main__":
    test_parse_input()
    test_vertical_split()
