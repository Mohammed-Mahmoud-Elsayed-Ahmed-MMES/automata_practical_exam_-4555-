def dfa_101(binary_string):
    """
    Implements a Deterministic Finite Automaton (DFA) to detect if a binary string
    contains the substring "101". The DFA has four states: q0 (start), q1, q2, and
    q3 (accepting state). It transitions based on input (0 or 1) and accepts only
    if it ends in state q3, indicating "101" was found.

    Args:
        binary_string (str): The input string to check, expected to contain only 0s and 1s.

    Returns:
        str: Result message indicating acceptance ("Accepted: Contains '101'") or rejection
             ("Rejected: Does not contain '101'ended in {state}") with the final state.
    """
    state = "q0"  # Initialize to the start state q0
    for char in binary_string:
        # Validate that the input contains only binary digits (0 or 1)
        if char not in "01":
            return "Invalid input: Use only 0s and 1s"
        
        # State transition logic based on current state and input
        if state == "q0":
            if char == "1":  # Transition to q1 on seeing '1'
                state = "q1"
            # If char is '0', remain in q0 (implicit transition)
        elif state == "q1":
            if char == "0":  # Transition to q2 on seeing '0' after '1'
                state = "q2"
            else:  # char == "1", stay in q1 (e.g., "11" keeps us in q1)
                state = "q1"
        elif state == "q2":
            if char == "1":  # Transition to q3 (accepting state) on seeing '1' after '10'
                state = "q3"
            else:  # char == "0", reset to q0 (e.g., "100" resets)
                state = "q0"
        elif state == "q3":
            # Once "101" is detected, stay in q3 regardless of further input
            pass

    # Check the final state to determine acceptance
    if state == "q3":
        return "Accepted: Contains '101'"
    else:
        return f"Rejected: Does not contain '101'ended in {state}"

# Example usage with test cases
if __name__ == "__main__":
    print("Testing DFA for '101' substring:")
    test_strings = ["1101", "0000", "1010", "111101", "010"]
    for s in test_strings:
        print(f"String: {s} -> {dfa_101(s)}")
