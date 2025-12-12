from dayX import parse_input


def test_vertical_math_problems():
    """Test parsing and evaluating vertical math problems."""
    # Vertical format:
    # 123 328  51 64 
    #  45 64  387 23 
    #   6 98  215 314
    # *   +   *   +  
    
    input_data = [
        "123 328  51 64",
        " 45 64  387 23",
        "  6 98  215 314",
        "*   +   *   +"
    ]
    
    result = parse_input(input_data)
    
    # Expected results from vertical arrangement:
    # 123 * 45 * 6 = 33210
    # 328 + 64 + 98 = 490
    # 51 * 387 * 215 = 4243455
    # 64 + 23 + 314 = 401
    expected = [33210, 490, 4243455, 401]
    
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Test passed! Result: {result}")


def test_single_column():
    """Test a single column of vertical math."""
    input_data = [
        "123",
        " 45",
        "  6",
        "*"
    ]
    
    result = parse_input(input_data)
    expected = [33210]  # 123 * 45 * 6
    
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Single column test passed! Result: {result}")


def test_addition_column():
    """Test addition column."""
    input_data = [
        "328",
        " 64",
        " 98",
        "+"
    ]
    
    result = parse_input(input_data)
    expected = [490]  # 328 + 64 + 98
    
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Addition column test passed! Result: {result}")


def test_multiplication_column():
    """Test multiplication column."""
    input_data = [
        "51",
        "387",
        "215",
        "*"
    ]
    
    result = parse_input(input_data)
    expected = [4243455]  # 51 * 387 * 215
    
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Multiplication column test passed! Result: {result}")


def test_grand_total():
    """Test the grand total of all math problem answers."""
    input_data = [
        "123 328  51 64",
        " 45 64  387 23",
        "  6 98  215 314",
        "*   +   *   +"
    ]
    
    result = parse_input(input_data)
    
    # Individual answers: 33210, 490, 4243455, 401
    # Grand total: 33210 + 490 + 4243455 + 401 = 4277556
    grand_total = sum(result)
    expected_total = 4277556
    
    assert grand_total == expected_total, f"Expected {expected_total}, got {grand_total}"
    print(f"Grand total test passed! Result: {grand_total}")


test_cases = [
    {
        "name": "Vertical Math Problems",
        "input": [
            "123 328  51 64",
            " 45 64  387 23",
            "  6 98  215 314",
            "*   +   *   +"
        ],
        "output": [33210, 490, 4243455, 401],
    },
    {
        "name": "Single Multiplication Column",
        "input": [
            "123",
            " 45",
            "  6",
            "*"
        ],
        "output": [33210],
    },
    {
        "name": "Single Addition Column",
        "input": [
            "328",
            " 64",
            " 98",
            "+"
        ],
        "output": [490],
    },
]


if __name__ == "__main__":
    test_vertical_math_problems()
    test_single_column()
    test_addition_column()
    test_multiplication_column()
    test_grand_total()
    print("\nAll tests passed!")
