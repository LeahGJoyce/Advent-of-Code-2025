DIAL_SIZE = 100


def parse_input(strings):
    """Accepts an array of strings and rotates the dial accordingly.

    Args:
        strings: A list of strings in format "L<number>" or "R<number>"

    Returns:
        The total number of times the dial lands on or passes zero.
    """

    start = 50  # dial starts at 50
    total_zero_events = 0
    
    for string in strings:
        direction = string[0]
        increment = int(string[1:])
        
        if direction == "L":
            # Count how many times we pass through or land on 0 going left
            # Going left from 'start' by 'increment' positions
            for _ in range(increment):
                start = (start - 1) % DIAL_SIZE
                if start == 0:
                    total_zero_events += 1
        elif direction == "R":
            # Count how many times we pass through or land on 0 going right
            # Going right from 'start' by 'increment' positions
            for _ in range(increment):
                start = (start + 1) % DIAL_SIZE
                if start == 0:
                    total_zero_events += 1
    
    return total_zero_events


def turn_right(start, increment):
    """Increment a number from start by increment, wrapping the dial."""
    return (start + increment) % DIAL_SIZE


def turn_left(start, increment):
    """Decrement a number from start by increment, wrapping the dial."""
    return (start - increment) % DIAL_SIZE


def main():
    """Read input text, split into lines, and print the result."""
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    total = parse_input(lines)
    print(total)


if __name__ == "__main__":
    main()
