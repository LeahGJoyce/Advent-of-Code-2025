def parse_input(data):
    """Parse the input and solve the math problems.
    
    Parses vertically arranged math problems where numbers are stacked
    vertically and operators are on the bottom row.
    
    Example:
        123 328 51 64 
        45 64 387 23 
        6 98 215 314
        * + * +
    
    Returns a list of results for each column (ignoring alignment).

    Args:
        data: A list of strings from the input file

    Returns:
        A list of results from each column's math operation
    """
    if not data or len(data) < 2:
        return []
    
    # Extract operators from the last row
    operators_row = data[-1]
    operators = [char for char in operators_row if char in ['*', '+']]
    
    if not operators:
        return []
    
    # Extract numbers from the rows above
    number_rows = data[:-1]
    
    # Extract all numbers from each row
    all_numbers = []
    for row in number_rows:
        numbers = []
        num_str = ""
        for char in row:
            if char.isdigit():
                num_str += char
            else:
                if num_str:
                    numbers.append(int(num_str))
                    num_str = ""
        if num_str:
            numbers.append(int(num_str))
        all_numbers.append(numbers)
    
    # Calculate result for each column
    results = []
    num_columns = len(operators)
    
    for col in range(num_columns):
        numbers = [all_numbers[row][col] for row in range(len(all_numbers))]
        operator = operators[col]
        
        result = numbers[0]
        for num in numbers[1:]:
            if operator == '*':
                result *= num
            elif operator == '+':
                result += num
        results.append(result)
    
    return results


def main():
    """Read input text, split into lines, and print the result."""
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    results = parse_input(lines)
    
    # Print individual results
    for i, result in enumerate(results):
        print(f"Column {i+1}: {result}")
    
    # Print grand total
    grand_total = sum(results)
    print(f"\nGrand Total: {grand_total}")


if __name__ == "__main__":
    main()
