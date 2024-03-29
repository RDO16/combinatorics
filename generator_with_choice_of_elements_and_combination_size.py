def generate_combinations_string(elements, combo_size):
    def backtrack(start, combo):
        nonlocal count
        if len(combo) == combo_size:
            combinations.append("".join(map(str, combo)))
            count += 1
            
            # Generate mirror combinations
            if combo != combo[::-1]:  # Ensure the mirror combination is not the same as the original
                mirror_combo = combo[::-1]
                combinations.append("".join(map(str, mirror_combo)))
                count += 1
            return
        for i in range(start, len(elements)):
            combo.append(elements[i])
            backtrack(i, combo)  # Allow repetition
            combo.pop()

    combinations = []
    count = 0
    backtrack(0, [])
    result_string = "\n".join(combinations)
    return result_string, count

# Example usage:
elements = ['a', 'b', 'c', 'd']
combo_size = 4
result_string, count = generate_combinations_string(elements, combo_size)
print("All possible combinations of size", combo_size, "as a string without spaces:")
print(result_string)