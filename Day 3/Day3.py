import re

def part1():
    # Read input from file
    with open('day3input.txt', 'r') as file:
        input_string = file.read()

    # Regex to find multiply pattern
    pattern = r"mul\((\d+),(\d+)\)"

    # Find all matches within input
    matches = re.findall(pattern, input_string)

    # Multiply and sum the numbers for each int a, b in matches
    total_sum = sum(int(a) * int(b) for a, b in matches)

    return total_sum

def part2():
    # Read input from file
    with open('day3input.txt', 'r') as file:
        input_string = file.read()

    # Regex to find multiply pattern or control pattern
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"(do\(\)|don't\(\))"

    # Find all matches for multiply and control instructions
    mul_matches = re.finditer(mul_pattern, input_string)
    control_matches = re.finditer(control_pattern, input_string)

    # Parse control instructions to determine multiply enable/disable states
    controls = []
    for match in control_matches:
        controls.append((match.start(), match.group()))

    # Process multiply instructions with the current state of enable/disable
    enabled = True  # Initial state
    control_index = 0
    total_sum = 0

    for mul_match in mul_matches:
        start_pos = mul_match.start()
        while control_index < len(controls) and controls[control_index][0] < start_pos:
            # Update the state based on the most recent control instruction
            if controls[control_index][1] == "do()":
                enabled = True
            elif controls[control_index][1] == "don't()":
                enabled = False
            control_index += 1

        if enabled:
            # Multiply and sum the numbers for each int a, b in matches
            a, b = map(int, mul_match.groups())
            total_sum += a * b

    return total_sum

# Print the result
print("Part 1 answer:", part1())
print("Part 2 answer:", part2())