def dfa_101(binary_string):
    state = "q0"  # Start state
    for char in binary_string:
        if char not in "01":  # Check if input is valid binary
            return "Invalid input: Use only 0s and 1s"
        
        if state == "q0":
            if char == "1":
                state = "q1"
            # If char is "0", stay in q0
        elif state == "q1":
            if char == "0":
                state = "q2"
            else:  # char == "1"
                state = "q1"  # Stay in q1 if we see another 1
        elif state == "q2":
            if char == "1":
                state = "q3"  # Found "101", go to accepting state
            else:  # char == "0"
                state = "q0"  # Reset to start
        elif state == "q3":
            # Once we find "101", we stay in q3 (accepting state)
            pass

    # q3 is the accepting state
    if state == "q3":
        return "Accepted: Contains '101'"
    else:
        return f"Rejected: Does not contain '101'ended in {state}" 

# Test the DFA
print("Testing DFA for '101' substring:")
test_strings = ["1101", "0000", "1010", "111101", "010"]
for s in test_strings:
    print(f"String: {s} -> {dfa_101(s)}")
