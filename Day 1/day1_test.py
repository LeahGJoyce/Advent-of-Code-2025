from day1 import parse_input


def test_parse_input():
    input_strings = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"
    ]

    result = parse_input(input_strings)
    # Expectation from sample: 6 times the dial lands on or passes through 0
    expected_total = 6
    assert result == expected_total, f"Expected {expected_total} total events, got {result}"
    print(f"Test passed! Total events: {result}.")

test_cases = [
    {
        "name": "AOC Input 1",
        "input": [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ],
        "output": "6",
    },
    {
        "name": "Right Increment smaller than DIAL_SIZE",
        "input": ["R10", "L10", "R10"],
        "output": "0",
    },
    {
        "name": "Right Increment larger than DIAL_SIZE",
        "input": ["R160", "L10", "R10"],
        "output": "3",
    },
    {
        "name": "Left Increment larger than DIAL_SIZE",
        "input": ["L160", "R10", "L10"],
        "output": "3",
    },
]

if __name__ == "__main__":
    test_parse_input()
