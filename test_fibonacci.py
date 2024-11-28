import sys
import unittest
from unittest.mock import patch

# Import the functions to test
from fib2 import generate_fibonacci_sequence, validate_input

class TestFibonacciSequence(unittest.TestCase):

    def test_generate_fibonacci_sequence(self):
        # Test the generate_fibonacci_sequence function
        self.assertEqual(generate_fibonacci_sequence(1), [0])
        self.assertEqual(generate_fibonacci_sequence(2), [0, 1])
        self.assertEqual(generate_fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(generate_fibonacci_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_validate_input(self):
        # Test the validate_input function
        with self.assertRaises(ValueError):
            validate_input([])
        with self.assertRaises(ValueError):
            validate_input(["fibonacci.py", "not_an_integer"])
        with self.assertRaises(ValueError):
            validate_input(["fibonacci.py", "0"])
        with self.assertRaises(ValueError):
            validate_input(["fibonacci.py", "-1"])
        self.assertEqual(validate_input(["fibonacci.py", "1"]), 1)
        self.assertEqual(validate_input(["fibonacci.py", "10"]), 10)

    def test_generate_fibonacci_sequence_for_5(self):
        # Test the generate_fibonacci_sequence function for the number 5
        self.assertEqual(generate_fibonacci_sequence(5), [0, 1, 1, 2, 3])

    @patch('sys.exit')
    def test_main(self, mock_exit):
        # Test the main function
        with patch.object(sys, 'argv', ["fibonacci.py", "10"]):
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_with("Fibonacci sequence up to", 10, "numbers:")
                mock_print.assert_called_with([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

        with patch.object(sys, 'argv', ["fibonacci.py", "not_an_integer"]):
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_with("Invalid input. Please enter an integer.")

        with patch.object(sys, 'argv', ["fibonacci.py"]):
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_with("Usage: python fibonacci.py <positive_integer>")

if __name__ == "__main__":
    unittest.main()