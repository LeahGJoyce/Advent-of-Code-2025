from day5 import parse_input


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
