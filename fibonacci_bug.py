import sys

def generate_fibonacci_sequence(n):
    """Generate the Fibonacci sequence up to n terms"""
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-2] + sequence[-3])
    return sequence

def validate_input(args):
    """Validate the command line arguments and return the desired number of terms"""
    if len(args) != 2:
        raise ValueError("Usage: python fibonacci.py <positive_integer>")
    try:
        number_of_terms = int(args[1])
        if number_of_terms <= 0:
            raise ValueError("Please enter a positive integer.")
        return number_of_terms
    except ValueError as e:
        raise ValueError("Invalid input. Please enter an integer.") from e

def main():

    try:
        number_of_terms = validate_input(sys.argv)
        fibonacci_sequence = generate_fibonacci_sequence(number_of_terms)
        print("Fibonacci sequence up to", number_of_terms, "numbers:")
        print(fibonacci_sequence)
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()