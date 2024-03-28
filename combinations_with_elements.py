def generate_combinations_string(elements):
    combinations = []
    for i in range(len(elements)):
        for j in range(i, len(elements)):
            for k in range(j, len(elements)):
                for l in range(k, len(elements)):
                    combination = str(elements[i]) + str(elements[j]) + str(elements[k]) + str(elements[l])
                    combinations.append(combination)
                    if elements[i] != elements[j]:
                        combinations.append(str(elements[j]) + str(elements[i]) + str(elements[k]) + str(elements[l]))
                    if elements[j] != elements[k] and elements[i] != elements[k]:
                        combinations.append(str(elements[k]) + str(elements[j]) + str(elements[i]) + str(elements[l]))
                    if elements[k] != elements[l] and elements[j] != elements[l] and elements[i] != elements[l]:
                        combinations.append(str(elements[l]) + str(elements[k]) + str(elements[j]) + str(elements[i]))
    return "\n".join(combinations)

# Example usage:
elements = ['1', '2', '3', '4']
result_string = generate_combinations_string(elements)
print("All possible combinations as a string without spaces:")
print(result_string)