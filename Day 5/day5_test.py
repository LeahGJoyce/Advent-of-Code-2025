from day5 import parse_input, get_all_valid_ids


def test_parse_input():
    """Test the parse_input function with sample data."""
    input_data = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]

    result = parse_input(input_data)
    # Valid IDs: 5 (in 3-5), 11 (in 10-14), 17 (in 16-20 and 12-18)
    # Invalid IDs: 1, 8, 32
    expected = 3
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Test passed! Result: {result}")


def test_get_all_valid_ids():
    """Test the get_all_valid_ids function to count all possible valid IDs from ranges."""
    input_data = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]

    result = get_all_valid_ids(input_data)
    # Valid IDs from ranges: 3-5 (3), 10-14 (5), 16-20 (5), 12-18 (7)
    # Total possible: 14 unique IDs
    expected = 14
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Test passed! Result: {result}")


test_cases = [
    {
        "name": "Sample Test Case 1",
        "input": [
            "3-5",
            "10-14",
            "16-20",
            "12-18",
            "",
            "1",
            "5",
            "8",
            "11",
            "17",
            "32",
        ],
        "output": "3",
    },
]


if __name__ == "__main__":
    test_parse_input()
    test_get_all_valid_ids()
