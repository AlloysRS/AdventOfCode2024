# Helper function to check if a report is safe
def is_safe(report):
    # Initialise is_decreasing and is_increasing to True
    is_increasing = True
    is_decreasing = True

    # Iterate over each number in the report
    for i in range(1, len(report)):
        # If is_increasing is true, check if still True
        if is_increasing:
            if report[i] < report[i - 1]:
                is_increasing = False
        # If is_decreasing is true, check if still True
        if is_decreasing:
            if report[i] > report[i - 1]:
                is_decreasing = False
        # If either are true, check if numbers are equal, or if variation is more than 3
        if is_increasing or is_decreasing:
            if report[i] == report[i - 1]:
                return False
            if abs(report[i] - report[i - 1]) > 3:
                return False
        # If neither is true, break
        else:
            break

    return is_increasing or is_decreasing

# Part 1 function
def part1():
    with open('day2input.txt', 'r') as file:
        # Parse input into reports
        reports = [[int(num) for num in row.split()] for row in file]

    # Count valid reports
    valid_reports = sum(1 for report in reports if is_safe(report))
    return valid_reports

# Part 2 function
def part2():
    with open('day2input.txt', 'r') as file:
        # Parse input into reports
        reports = [[int(num) for num in row.split()] for row in file]

    # Initialise valid_reports as 0
    valid_reports = 0

    # Iterate over each report with checks
    for report in reports:
        # First, check if the report is already safe
        if is_safe(report):
            valid_reports += 1
            continue

        # If not safe, remove one level at a time and recheck
        for i in range(len(report)):
            # Create a new report with one level removed
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                valid_reports += 1
                break

    return valid_reports

# Print results for both parts
print("Part 1 answer:", part1())
print("Part 2 answer:", part2())