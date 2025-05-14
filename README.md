
Section Number: 5

Section Name
Theory of Computation Practical Exam
Task Being Solved
This repository contains solutions to three tasks related to automata theory:

DFA for "101" Substring Detection: Implements a Deterministic Finite Automaton (DFA) to accept binary strings containing the substring "101".
CFG to GNF Conversion: Converts a Context-Free Grammar (CFG) into Greibach Normal Form (GNF), with a specific example generating strings over terminals 'a' and 'b'.
Turing Machine for Divisibility by 3: Implements a Turing Machine to check if a binary string represents a number divisible by 3.

Brief Instructions on How to Run and Test the Code for Each Section
1. DFA for "101" Substring Detection (dfa_101.py)

Description: This script implements a Deterministic Finite Automaton (DFA) to detect whether a binary string contains the substring "101". The DFA operates with four states: ( q_0 ) (start state), ( q_1 ), ( q_2 ), and ( q_3 ) (accepting state). It processes each character of the input string, transitioning between states based on the current state and input (0 or 1). The DFA reaches ( q_3 ) only when it encounters "101", accepting the string. The steps are: (1) Validate the input as a binary string, (2) Iterate through each character, updating the state (e.g., ( q_0 \xrightarrow{1} q_1 ), ( q_1 \xrightarrow{0} q_2 ), ( q_2 \xrightarrow{1} q_3 )), and (3) Return "Accepted" if the final state is ( q_3 ), otherwise "Rejected" with the ending state.
How to Run: Execute the script directly using Python:python dfa_101.py


Output: The script tests several binary strings (e.g., "1101", "0000") and prints results like "Accepted: Contains '101'" or "Rejected: Does not contain '101'ended in q0".
Testing: Unit tests are included in test_dfa_101.py. Run them with:python -m unittest test_dfa_101.py



2. CFG to GNF Conversion (cfg_to_gnf.py)

Description: This script transforms a Context-Free Grammar (CFG) into Greibach Normal Form (GNF), where all productions start with a terminal followed by zero or more non-terminals. It processes a sample CFG with variables S, B, C, and A, generating strings over terminals 'a' and 'b'. The steps are: (1) Check for and remove unit productions (e.g., ( A \to B )) and null productions (e.g., ( A \to \varepsilon )) by identifying nullable variables, (2) Convert to Chomsky Normal Form (CNF) by breaking long productions into pairs of non-terminals or terminals, (3) Rename non-terminals to ( A_i ) in ascending order, (4) Ensure productions follow ascending index order (e.g., ( A_i \to A_j X ) where ( i < j )), and (5) Remove left recursion by introducing new variables (e.g., ( A \to \beta A' ), ( A' \to \alpha A' \mid \varepsilon )) and ensuring GNF compliance. The script prints the CFG at each step and the final GNF.
How to Run: Execute the script directly using Python:python cfg_to_gnf.py


Output: The script outputs the CFG transformation process and the final GNF (e.g., "A1 -> b A3 | b A4") with ordered productions.
Testing: Unit tests are included in test_cfg_to_gnf.py. Run them with:python -m unittest test_cfg_to_gnf.py



3. Turing Machine for Divisibility by 3 (tm_divisible_by_3.py)

Description: This script implements a Turing Machine to determine if a binary string represents a number divisible by 3, using an implicit approach. It avoids explicit decimal conversion by tracking the remainder modulo 3. The steps are: (1) Validate the input as a binary string, (2) Initialize a remainder of 0, (3) For each bit, update the remainder using the formula ( (2 \times \text{current remainder} + \text{bit}) \mod 3 ) (simulating binary multiplication by 2 and addition), and (4) Return "Accepted" if the final remainder is 0, otherwise "Rejected". A commented-out explicit approach converts the binary string to decimal first and checks divisibility, but the implicit method is active. The script includes test cases to demonstrate functionality.
How to Run: Execute the script directly using Python:python tm_divisible_by_3.py


Output: The script tests binary strings (e.g., "0", "110") and prints results like "Binary: 110 -> Accepted: Divisible by 3" or "Binary: 11 -> Rejected: Not divisible by 3".
Testing: Unit tests are included in test_tm_divisible_by_3.py. Run them with:python -m unittest test_tm_divisible_by_3.py



