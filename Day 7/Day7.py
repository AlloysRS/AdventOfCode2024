import itertools

# Helper function to evaluate expressions left-to-right
def evaluate_expression(nums, operators):
    # Initialise result as first number from input numbers, and initialise index as 0 to track the operator
    result = nums[0]
    index = 0 
    # Store the expression as a string for debugging
    expression = str(nums[0])

    # Loop through operators and apply each operator to the current result and the next number
    while index < len(operators):
        if operators[index] == '+':
            result += nums[index + 1]
        elif operators[index] == '*':
            result *= nums[index + 1]
        elif operators[index] == '||':
            # Concatenate digits of two numbers as strings then convert back into int
            result = int(str(result) + str(nums[index + 1]))
        # Add the current operation and next number to the expression string
        expression += f" {operators[index]} {nums[index + 1]}"
        index += 1

    return result, expression

# Helper function to calculate the total calibration result
def calculate_calibration(equations, operators_allowed):
    # Initialise total calibration result as 0
    total_calibration_result = 0

    # Loop through each equation in the list of equations
    for equation in equations:
        # Split the target value (left of ': ') and numbers (right of ': '), example 190: 10 19 becomes target = 190, and nums = (10, 19)
        parts = equation.split(': ')
        target = int(parts[0])
        nums = list(map(int, parts[1].split()))

        # Initialise number of operators to 1 less than the count of numbers in nums
        num_operators = len(nums) - 1

        # Generate all possible combinations of operators using the operators allowed, repeated for the number of operators
        operator_combinations = itertools.product(operators_allowed, repeat=num_operators)

        # Check if any combination of operators can satisfy the equation
        for operators in operator_combinations:
            # Evaluate the expression with the current combination of operators
            result, expression = evaluate_expression(nums, operators)
            if result == target:
                total_calibration_result += target
                # Debug: Print the valid equation and how it matches the target
                #print(f"Match: {expression} = {result} (Target: {target})")
                break  # Stop checking further for this equation
            else:
                # Debug: Print the failed equation and how it compares to the target
                #print(f"No Match: {expression} = {result} (Target: {target})")
                pass

    return total_calibration_result

def part1():
    # Read the  input from file and append each row to equations
    with open("day7input.txt", "r") as file:
        equations = file.read().splitlines()

    # Calculate the total calibration result using + and *
    return calculate_calibration(equations, operators_allowed=['+', '*'])

def part2():
    # Read the  input from file and append each row to equations
    with open("day7input.txt", "r") as file:
        equations = file.read().splitlines()

    # Calculate the total calibration result using +, *, and ||
    return calculate_calibration(equations, operators_allowed=['+', '*', '||'])

# Run the functions and print the results
print("Part 1 answer:", part1())
print("Part 2 answer:", part2())