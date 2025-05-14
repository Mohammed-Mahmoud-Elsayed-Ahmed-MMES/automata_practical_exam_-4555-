# 1- Implicit approach

def turing_machine_divisible_by_3(binary_string):
    # Check if input is a valid binary string
    if not all(char in "01" for char in binary_string):
        return "Invalid input: Use only 0s and 1s"
    
    remainder = 0  # Start with remainder 0
    for bit in binary_string:
        bit = int(bit)  # Convert "0" or "1" to integer
        # Update remainder: (2 * current remainder + bit) % 3
        remainder = (2 * remainder + bit) % 3
    
    # If final remainder is 0, the number is divisible by 3
    if remainder == 0:
        return "Accepted: Divisible by 3"
    else:
        return "Rejected: Not divisible by 3"

# Test the Turing Machine
print("Testing Turing Machine for binary numbers divisible by 3:")
test_strings = ["0", "11", "110", "1001", "111"]
for s in test_strings:
    print(f"Binary: {s} -> {turing_machine_divisible_by_3(s)}")


# 2- Explicit approach

# def binary_to_decimal(binary_string):
#     # Check if input is a valid binary string
#     if not all(char in "01" for char in binary_string):
#         return "Invalid input: Use only 0s and 1s"
    
#     decimal = 0
#     for bit in binary_string:
#         decimal = decimal * 2 + int(bit)
#     return decimal

# def turing_machine_divisible_by_3(decimal_number):    
#     # If final remainder is 0, the number is divisible by 3
#     if decimal_number % 3 == 0:
#         return "Accepted: Divisible by 3"
#     else:
#         return "Rejected: Not divisible by 3"

# # Test the Turing Machine
# print("Testing Turing Machine for binary numbers divisible by 3:")
# test_strings = ["0", "11", "110", "1001", "111"]
# for s in test_strings:
#     # Convert binary string to decimal for clarity
#     decimal = binary_to_decimal(s)
#     print(f"Binary: {s} (Decimal: {decimal}) -> {turing_machine_divisible_by_3(decimal)}")