def perform_operation(value):
    # Define the upper and lower bounds
    lower_bound = 0
    upper_bound = 100
    
    # Perform bounds checking
    if value < lower_bound:
        value = lower_bound
    elif value > upper_bound:
        value = upper_bound

    # Perform the operation with the validated value
    result = value * 2
    return result

# Example usage
input_value = 150
output = perform_operation(input_value)
print(output)  # Output: 200 (as the input value is outside the bounds, it is set to the upper bound)
