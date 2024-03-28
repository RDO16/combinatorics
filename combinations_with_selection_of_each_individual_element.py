from itertools import product

def generate_combinations():
    uppercase_letter = ['A']
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2']
    
    combinations = product(uppercase_letter, lowercase_letters, lowercase_letters, lowercase_letters, numbers, numbers, numbers)
    
    filtered_combinations = []
    for combination in combinations:
        if combination[0] == 'A' and combination[1] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] and combination[2] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] \
            and combination[3] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] and combination[4] in ['0', '1', '2'] and combination[5] in ['0', '1', '2'] \
            and combination[6] in ['0', '1', '2']:
            filtered_combinations.append(combination)
    
    return filtered_combinations

# Generate and print combinations
combinations = generate_combinations()
for combination in combinations:
    print(''.join(combination))