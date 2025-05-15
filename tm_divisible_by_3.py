def turing_machine_divisible_by_3(binary_string):
    """
    Implements a Turing Machine to check if a binary string represents a number
    divisible by 3 using an implicit approach. The algorithm tracks the remainder
    modulo 3 without converting to decimal, simulating the TM's state transitions.
    The steps are: (1) Validate the input, (2) Initialize remainder to 0, (3) Update
    remainder as (2 * current remainder + bit) % 3 for each bit, and (4) Accept if
    the final remainder is 0.

    Args:
        binary_string (str): The input binary string to check.

    Returns:
        str: Result message indicating "Accepted: Divisible by 3" or
             "Rejected: Not divisible by 3".
    """
    # Validate that the input contains only binary digits (0 or 1)
    if not all(char in "01" for char in binary_string):
        return "Invalid input: Use only 0s and 1s"
    
    remainder = 0  # Initialize remainder to 0, representing the TM's initial state
    for bit in binary_string:
        bit = int(bit)  # Convert the character '0' or '1' to an integer
        # Update remainder: Multiply current remainder by 2 (left shift) and add the bit,
        # then take modulo 3 to simulate TM state transitions
        remainder = (2 * remainder + bit) % 3
    
    # Check the final remainder to determine divisibility by 3
    if remainder == 0:
        return "Accepted: Divisible by 3"
    else:
        return "Rejected: Not divisible by 3"

# Example usage with test cases
if __name__ == "__main__":
    print("Testing Turing Machine for binary numbers divisible by 3:")
    test_strings = ["0", "11", "110", "1001", "111"]
    for s in test_strings:
        print(f"Binary: {s} -> {turing_machine_divisible_by_3(s)}")

# Commented-out explicit approach for reference
# def binary_to_decimal(binary_string):
#     """
#     Converts a binary string to its decimal equivalent (for explicit approach).
#     """
#     if not all(char in "01" for char in binary_string):
#         return "Invalid input: Use only 0s and 1s"
#     decimal = 0
#     for bit in binary_string:
#         decimal = decimal * 2 + int(bit)
#     return decimal
#
# def turing_machine_divisible_by_3(decimal_number):
#     """
#     Checks divisibility by 3 using the decimal number (explicit approach).
#     """
#     if decimal_number % 3 == 0:
#         return "Accepted: Divisible by 3"
#     else:
#         return "Rejected: Not divisible by 3"
#
# # Test the explicit approach
# if __name__ == "__main__":
#     print("Testing Turing Machine for binary numbers divisible by 3 (Explicit):")
#     test_strings = ["0", "11", "110", "1001", "111"]
#     for s in test_strings:
#         decimal = binary_to_decimal(s)
#         print(f"Binary: {s} (Decimal: {decimal}) -> {turing_machine_divisible_by_3(decimal)}")
