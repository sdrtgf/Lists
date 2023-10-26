def remove_duplicates(input_list):# Define a function called 'remove_duplicates' that takes an 'input_list' as an argument.
    unique_digits = []# Define a function called 'remove_duplicates' that takes an 'input_list' as an argument.
    for digit in input_list:
        # Check if the 'digit' is not already in the 'unique_digits' list.
    
        if digit not in unique_digits:
            unique_digits.append(digit)
    return unique_digits


input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# Call the 'remove_duplicates' function with the input list and store the result in 'result_list'.

result_list = remove_duplicates(input_list)
print(result_list)


