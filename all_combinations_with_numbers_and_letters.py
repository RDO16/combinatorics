from itertools import product

def generate_combinations(input_data):
    # Convert the input data to a string
    input_str = str(input_data)
    
    # Generate all possible combinations of the digits and letters
    combinations = set()
    for perm in product(input_str, repeat=len(input_str)):
        combinations.add(''.join(perm))
        combinations.add(''.join(reversed(perm)))  # Add mirror of the combination
    
    return combinations

# Test the function
input_data = input("Enter a number or letters: ")
combinations = generate_combinations(input_data)
print("All possible combinations:")
for combination in sorted(combinations):
    print(combination)