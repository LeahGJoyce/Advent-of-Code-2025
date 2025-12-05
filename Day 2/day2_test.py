from day2 import parse_input, find_ids_in_range


def test_parse_input():
    """Test the parse_input function with sample data."""
    input_data = [
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,",
        "1698522-1698528,446443-446449,38593856-38593862,565653-565659,",
        "824824821-824824827,2121212118-2121212124",
    ]

    result = parse_input(input_data)
    expected = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Test parse_input passed! Result: {result}")


def test_find_ids_in_range():
    """Test the find_ids_in_range function with sample data."""
    test_cases = [
        {
            "name": "11-22",
            "input": "11-22",
            "output": [11, 22],
        },
        {
            "name": "95-115",
            "input": "95-115",
            "output": [99],
        },
        {
            "name": "998-1012",
            "input": "998-1012",
            "output": [1010],
        },
        {
            "name": "1188511880-1188511890",
            "input": "1188511880-1188511890",
            "output": [1188511885],
        },
        {
            "name": "222220-222224",
            "input": "222220-222224",
            "output": [222222],
        },
        {
            "name": "1698522-1698528",
            "input": "1698522-1698528",
            "output": [],
        },
        {
            "name": "446443-446449",
            "input": "446443-446449",
            "output": [446446],
        },
        {
            "name": "38593856-38593862",
            "input": "38593856-38593862",
            "output": [38593859],
        },
        {
            "name": "565653-565659",
            "input": "565653-565659",
            "output": [],
        },
        {
            "name": "824824821-824824827",
            "input": "824824821-824824827",
            "output": [],
        },
        {
            "name": "2121212118-2121212124",
            "input": "2121212118-2121212124",
            "output": [],
        },
    ]

    for test_case in test_cases:
        result = find_ids_in_range(test_case["input"])
        expected = test_case["output"]
        assert result == expected, f"Test '{test_case['name']}' failed: Expected {expected}, got {result}"
        print(f"Test '{test_case['name']}' passed!")


def test_sum_all_outputs():
    """Test that sums all outputs from the test range."""
    test_cases = [
        {
            "name": "11-22",
            "input": "11-22",
            "output": [11, 22],
        },
        {
            "name": "95-115",
            "input": "95-115",
            "output": [99],
        },
        {
            "name": "998-1012",
            "input": "998-1012",
            "output": [1010],
        },
        {
            "name": "1188511880-1188511890",
            "input": "1188511880-1188511890",
            "output": [1188511885],
        },
        {
            "name": "222220-222224",
            "input": "222220-222224",
            "output": [222222],
        },
        {
            "name": "1698522-1698528",
            "input": "1698522-1698528",
            "output": [],
        },
        {
            "name": "446443-446449",
            "input": "446443-446449",
            "output": [446446],
        },
        {
            "name": "38593856-38593862",
            "input": "38593856-38593862",
            "output": [38593859],
        },
        {
            "name": "565653-565659",
            "input": "565653-565659",
            "output": [],
        },
        {
            "name": "824824821-824824827",
            "input": "824824821-824824827",
            "output": [],
        },
        {
            "name": "2121212118-2121212124",
            "input": "2121212118-2121212124",
            "output": [],
        },
    ]

    total = sum(sum(test_case["output"]) for test_case in test_cases)
    print(f"Sum of all outputs: {total}")
    assert total == 1227775554, f"Expected sum to be 1,227,775,554, got {total}"
    print("Test sum_all_outputs passed!")


if __name__ == "__main__":
    test_parse_input()
    test_find_ids_in_range()
    test_sum_all_outputs()
