from itertools import product

def generate_combinations(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Generate all possible combinations of the digits
    combinations = set()
    for perm in product(num_str, repeat=len(num_str)):
        combinations.add(''.join(perm))
        combinations.add(''.join(reversed(perm)))  # Add mirror of the combination
    
    return combinations

# Test the function
number = int(input("Enter a number: "))
combinations = generate_combinations(number)
print("All possible combinations:")
for combination in sorted(combinations):
    print(combination)