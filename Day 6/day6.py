def parse_input(data):
    """Parse the input and solve the math problems.
    
    Numbers are written right-to-left in columns. Each column represents a single
    number, read top-to-bottom (most significant digit at top, least significant at bottom).
    Blank columns separate different problems.
    Operators are in the bottom row.
    
    Example:
        123 328  51 64
         45  64  387 23
          6  98  215 314
        *    +   *   +
    
    Read problems right-to-left (rightmost problem first).

    Args:
        data: A list of strings from the input file

    Returns:
        The grand total of all problem results
    """
    if not data or len(data) < 2:
        return 0
    
    # Pad all lines to same length
    max_len = max(len(line) for line in data) if data else 0
    lines = [line.ljust(max_len) for line in data]
    
    # Extract number rows (all but last)
    number_rows = lines[:-1]
    operator_row = lines[-1]
    
    # Find column groups (separated by blank columns)
    # A blank column has only spaces in number_rows
    blank_separated_groups = []
    in_group = False
    group_start = 0
    
    for col in range(max_len):
        # Check if this column is blank (all spaces in number rows)
        is_blank = all(col >= len(row) or row[col] == ' ' for row in number_rows)
        
        if not is_blank and not in_group:
            in_group = True
            group_start = col
        elif is_blank and in_group:
            in_group = False
            blank_separated_groups.append((group_start, col))
    
    if in_group:
        blank_separated_groups.append((group_start, max_len))
    
    # Now split each blank-separated group by operator positions
    column_groups = []
    operator_positions = []
    for col in range(max_len):
        if col < len(operator_row) and operator_row[col] in '*+':
            operator_positions.append(col)
    
    for group_start, group_end in blank_separated_groups:
        # Find operators in this group
        ops_in_group = [op for op in operator_positions if group_start <= op < group_end]
        
        if not ops_in_group:
            column_groups.append((group_start, group_end))
        else:
            # Create groups such that each group contains one operator
            prev_end = group_start
            for i, op_pos in enumerate(ops_in_group):
                # Group extends from prev_end to just after this operator
                # But we need to find where the next operator starts (or end of group)
                next_op_pos = ops_in_group[i + 1] if i + 1 < len(ops_in_group) else group_end
                column_groups.append((prev_end, next_op_pos))
                prev_end = next_op_pos
    
    # Process each column group, reading right-to-left
    results = []
    for group_start, group_end in reversed(column_groups):
        numbers = []
        operator = None
        
        # Extract numbers from columns in this group, left-to-right within the group
        for col in range(group_start, group_end):
            # Skip blank columns
            if all(col >= len(row) or row[col] == ' ' for row in number_rows):
                continue
            
            # Read this column top-to-bottom to get a number
            num_str = ""
            for row in number_rows:
                if col < len(row) and row[col].isdigit():
                    num_str += row[col]
            
            if num_str:
                numbers.append(int(num_str))
        
        # Find operator for this group
        for col in range(group_start, group_end):
            if col < len(operator_row) and operator_row[col] in '*+':
                operator = operator_row[col]
                break
        
        # Calculate result
        if numbers and operator:
            result = numbers[0]
            for num in numbers[1:]:
                if operator == '*':
                    result *= num
                elif operator == '+':
                    result += num
            results.append(result)
    
    # Return grand total
    return sum(results)


def main():
    """Read input text, split into lines, and print the result."""
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    grand_total = parse_input(lines)
    print(grand_total)


if __name__ == "__main__":
    main()
