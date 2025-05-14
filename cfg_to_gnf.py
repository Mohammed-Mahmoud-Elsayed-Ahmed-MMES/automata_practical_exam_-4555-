# Helper function to print the CFG
def print_cfg(cfg, end="\n"):
    print("Current CFG:")
    for var in cfg:
        prods = cfg[var]
        prod_str = " | ".join(prods)
        print(f"{var} -> {prod_str}")
    print(end)

# Helper function to check if a string is a non-terminal (uppercase, matches a variable in cfg)
def is_non_terminal(symbol, cfg):
    if not symbol:
        return False
    return symbol in cfg

# Helper function to check if a string is a terminal (lowercase)
def is_terminal(symbol):
    if not symbol:
        return False
    for i in range(len(symbol)):
        if not (symbol[i] >= "a" and symbol[i] <= "z"):
            return False
    return True

# Step 1: Check and Remove Unit Productions or Null Productions
def step1_check_remove_unit_null(cfg):
    print("Step 1: Checking for unit productions or null productions...")
    
    # Check for unit and null productions
    has_unit_or_null = False
    for var, prods in cfg.items():
        for prod in prods:
            # Check for null production (ε represented as empty string "")
            if prod == "":
                has_unit_or_null = True
                print(f"Found null production: {var} -> ε")
            # Check for unit production (e.g., A -> B, where B is a non-terminal)
            elif prod in cfg:
                has_unit_or_null = True
                print(f"Found unit production: {var} -> {prod}")
    
    if not has_unit_or_null:
        print("No unit or null productions found.\n")
        return cfg
    
    print("Unit or null productions found. Resolving...")
    
    # First, find all nullable variables
    nullable = set()
    changed = True
    while changed:
        changed = False
        for var, prods in cfg.items():
            if var not in nullable and "" in prods:
                nullable.add(var)
                changed = True
                continue
            
            for prod in prods:
                if prod and all(symbol in nullable for symbol in prod):
                    if var not in nullable:
                        nullable.add(var)
                        changed = True
                        break
    
    # Remove null productions and substitute nullable variables
    new_cfg = {}
    for var, prods in cfg.items():
        new_prods = [p for p in prods if p != ""]
        
        # Add new productions for each nullable variable
        for prod in list(new_prods):
            for i, symbol in enumerate(prod):
                if symbol in nullable:
                    # Create new production without this nullable symbol
                    new_prod = prod[:i] + prod[i+1:]
                    if new_prod and new_prod not in new_prods:
                        new_prods.append(new_prod)
        
        new_cfg[var] = new_prods
    
    # Remove unit productions
    result_cfg = {}
    for var, prods in new_cfg.items():
        new_prods = []
        for prod in prods:
            if prod in new_cfg:  # Unit production
                new_prods.extend(new_cfg[prod])
            else:
                new_prods.append(prod)
        result_cfg[var] = new_prods
    
    print("Unit and null productions removed.")
    print_cfg(result_cfg)
    return result_cfg

# Step 2: Check and Convert to Chomsky Normal Form (CNF)
def step2_check_convert_to_cnf(cfg):
    print("Step 2: Checking if CFG is in Chomsky Normal Form (CNF)...")
    
    # Check if the grammar is already in CNF
    is_cnf = True
    for var, prods in cfg.items():
        for prod in prods:
            # Case 1: A -> a (one terminal)
            if len(prod) == 1 and prod.islower():
                continue
            # Case 2: A -> BC (two non-terminals)
            elif len(prod) == 2 and all(symbol in cfg for symbol in prod):
                continue
            else:
                is_cnf = False
                print(f"Production not in CNF: {var} -> {prod}")
    
    if is_cnf:
        print("CFG is already in CNF.\n")
        return cfg
    
    print("CFG is not in CNF. Converting to CNF...")
    
    # Step 1: Replace terminals in longer productions
    new_cfg = {}
    terminal_vars = {}
    var_counter = 1
    
    for var in cfg:
        new_cfg[var] = []
    
    for var, prods in cfg.items():
        for prod in prods:
            if len(prod) == 1 or (len(prod) == 2 and all(symbol in cfg for symbol in prod)):
                # Already in CNF format
                new_cfg[var].append(prod)
            else:
                # Need to convert
                new_prod = ""
                for symbol in prod:
                    if symbol.islower():  # Terminal
                        if symbol not in terminal_vars:
                            new_var = f"T{var_counter}"
                            var_counter += 1
                            terminal_vars[symbol] = new_var
                            new_cfg[new_var] = [symbol]
                        new_prod += terminal_vars[symbol]
                    else:
                        new_prod += symbol
                
                # Now break long productions
                if len(new_prod) <= 2:
                    new_cfg[var].append(new_prod)
                else:
                    # Break into binary rules
                    current_var = var
                    for i in range(len(new_prod) - 2):
                        next_var = f"X{var_counter}"
                        var_counter += 1
                        new_cfg[current_var].append(new_prod[i] + next_var)
                        new_cfg[next_var] = []
                        current_var = next_var
                    # Add the last rule
                    new_cfg[current_var].append(new_prod[-2:])
    
    print("Converted to CNF.")
    print_cfg(new_cfg)
    return new_cfg

# Step 3: Rename Non-Terminal Symbols to Ai in Ascending Order
def step3_rename_non_terminals(cfg):
    print("Step 3: Renaming non-terminal symbols to Ai in ascending order...")
    
    # Create a mapping for renaming
    rename_map = {}
    counter = 1
    
    # Start with the start symbol (usually S)
    start_symbol = next(iter(cfg))
    rename_map[start_symbol] = f"A{counter}"
    counter += 1
    
    # Process all other variables
    for var in cfg:
        if var != start_symbol and var not in rename_map:
            rename_map[var] = f"A{counter}"
            counter += 1
    
    # Create a new CFG with renamed variables
    new_cfg = {}
    for var, prods in cfg.items():
        new_var = rename_map[var]
        new_prods = []
        for prod in prods:
            new_prod = ""
            for symbol in prod:
                if symbol in rename_map:
                    new_prod += rename_map[symbol]
                else:
                    new_prod += symbol
            new_prods.append(new_prod)
        new_cfg[new_var] = new_prods
    
    print("Non-terminals renamed according to the pattern:")
    for old, new in rename_map.items():
        print(f"{old} -> {new}")
    print()
    print_cfg(new_cfg)
    return new_cfg

# Step 4: Alter Rules to Ensure Ascending Order of Non-Terminals
def step4_ensure_ascending_order(cfg):
    print("Step 4: Ensuring non-terminals are in ascending order (Ai -> Aj X, i < j)...")
    
    # Function to get the index of a non-terminal (e.g., A1 -> 1)
    def get_index(non_terminal):
        if non_terminal.startswith('A'):
            try:
                return int(non_terminal[1:])
            except ValueError:
                return float('inf')
        return float('inf')  # For non-A variables
    
    # Check for violations
    violations = []
    for var in cfg:
        var_idx = get_index(var)
        for prod in cfg[var]:
            if prod and prod[0] in cfg:
                first_nt = prod[0]
                first_idx = get_index(first_nt)
                if var_idx >= first_idx:
                    violations.append(f"Violation: {var} -> {prod} (index {var_idx} >= {first_idx})")
    
    if not violations:
        print("All productions satisfy ascending order.\n")
        return cfg
    
    print("Found productions violating ascending order:")
    for violation in violations:
        print(violation)
    print("Resolving...")
    
    # Create a new CFG to store the result
    result_cfg = {var: list(prods) for var, prods in cfg.items()}
    
    # Fix violations by substituting productions
    changed = True
    iteration = 0
    max_iterations = 10  # Prevent infinite loops
    
    while changed and iteration < max_iterations:
        iteration += 1
        changed = False
        
        for var in list(result_cfg.keys()):
            var_idx = get_index(var)
            new_prods = []
            
            for prod in result_cfg[var]:
                if not prod or prod[0] not in result_cfg:
                    new_prods.append(prod)
                    continue
                
                first_nt = prod[0]
                first_idx = get_index(first_nt)
                
                if var_idx >= first_idx:
                    # This is a violation - substitute
                    rest = prod[1:]
                    for sub_prod in result_cfg[first_nt]:
                        new_prod = sub_prod + rest
                        if new_prod not in new_prods:
                            new_prods.append(new_prod)
                            changed = True
                else:
                    new_prods.append(prod)
            
            result_cfg[var] = new_prods
    
    print("Ascending order enforced.")
    print_cfg(result_cfg)
    return result_cfg

# Step 5: Remove Left Recursion
def step5_remove_left_recursion(cfg):
    print("Step 5: Checking for left recursion and removing if present...")
    
    # Check for left recursion
    left_recursive_vars = []
    for var, prods in cfg.items():
        for prod in prods:
            if prod and prod[0] == var:
                if var not in left_recursive_vars:
                    left_recursive_vars.append(var)
                    print(f"Found left recursion: {var} -> {prod}")
    
    if not left_recursive_vars:
        print("No left recursion found.\n")
        return cfg
    
    print("Left recursion found. Removing...")
    
    # Create a new CFG
    result_cfg = {}
    
    # Process each variable
    for var, prods in cfg.items():
        if var not in left_recursive_vars:
            result_cfg[var] = prods
            continue
        
        # Separate recursive and non-recursive productions
        alpha_rules = []  # A -> Aα
        beta_rules = []   # A -> β
        
        for prod in prods:
            if prod and prod[0] == var:
                alpha_rules.append(prod[1:])  # Remove the leading A
            else:
                beta_rules.append(prod)
        
        # Create new variable Z for the recursive part
        new_var = "Z"
        
        # A -> βZ
        new_a_rules = []
        for beta in beta_rules:
            new_a_rules.append(beta + new_var)
        result_cfg[var] = new_a_rules
        
        # Z -> αZ | α
        new_z_rules = []
        for alpha in alpha_rules:
            new_z_rules.append(alpha + new_var)
            new_z_rules.append(alpha)  # Also add α without Z
        result_cfg[new_var] = new_z_rules
    
    print("Left recursion removed.")
    print_cfg(result_cfg)
    return result_cfg

# Initial CFG
cfg = {
    "S": ["CA", "BB"],
    "B": ["b", "SB"],
    "C": ["b"],
    "A": ["a"]
}

# Main execution
print("\n=== Processing CFG ===\n")
print("Starting CFG:")
print_cfg(cfg)

# Apply each step in sequence
cfg = step1_check_remove_unit_null(cfg)
cfg = step2_check_convert_to_cnf(cfg)
cfg = step3_rename_non_terminals(cfg)
cfg = step4_ensure_ascending_order(cfg)
cfg = step5_remove_left_recursion(cfg)

print("Final CFG in GNF:")
print_cfg(cfg)
print("=" * 50)