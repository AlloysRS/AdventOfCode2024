def part1():
    # Initialise empty lists for rules, updates and invalid_updates, initialise middle_sum as 0
    rules = []
    updates = []
    invalid_updates = []  # Store invalid updates (for Part 2)
    middle_sum = 0

    # Read input from file and split into rules and updates based on separator
    with open('day5input.txt', 'r') as file:
        for line in file:
            if '|' in line:
                parts = line.split('|')
                x = int(parts[0])
                y = int(parts[1])
                rules.append((x, y))
            elif ',' in line:
                parts = line.split(',')
                updates.append([int(num) for num in parts])

    for update in updates:
        # Initialise list of filtered rules and check for presence of X, Y numbers to filter the list of rules to check
        valid = True
        filtered_rules = []
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                filtered_rules.append(rule)

        # For each filtered rule, get the index position of rule(x,y) from the update, and check if x_position > y_position as invalidation criteria
        for rule in filtered_rules:
            x, y = rule
            x_position = update.index(x)
            y_position = update.index(y)
            if x_position > y_position:
                valid = False
                break

        # If update is valid, get middle_number and add to middle_sum, else add to list of invalid_updates
        if valid:
            middle_index = len(update) // 2
            middle_number = update[middle_index]
            middle_sum += middle_number
        else:
            invalid_updates.append(update)

    # Return the sum of middle numbers for part1 answer, and list of invalid_updates and rules for part2
    return middle_sum, invalid_updates, rules


def part2(invalid_updates, rules):
    # Initialise empty list corrected updates, initialise corrected middle sum as 0
    corrected_middle_sum = 0

    # Helper function to sort update based on the rules
    def sort_with_rules(update, rules):
        # Initialise sorted_update as an empty list
        sorted_update = []

        # Sort until all numbers from the update are processed and removed
        while update:
            for num in update:
                can_add = True
                # Check all rules to see if the current number must wait
                for rule in rules:
                    # If num is Y and X is still in the update, num can't be added as X must come before Y, set flag to false and check next number
                    if rule[1] == num and rule[0] in update:
                        can_add = False
                        break
                # If can_add remains True, append num to sorted update list and remove from update list being iterated
                if can_add:
                    sorted_update.append(num)
                    update.remove(num)
                    break

        # Return the sorted update from the helper function
        return sorted_update

    # Iterate over all invalid updates, correct them with sort_with_rules helper function, and sum middle numbers
    for update in invalid_updates:
        corrected_update = sort_with_rules(update, rules)

        middle_index = len(corrected_update) // 2
        middle_number = corrected_update[middle_index]
        corrected_middle_sum += middle_number

    # Return the corrected middle sum for part2 answer
    return corrected_middle_sum

# Get part1 and part2 answers
part1_sum, invalid_updates, rules = part1()
part2_sum = part2(invalid_updates, rules)

# Output the results
print("Part 1 answer:", part1_sum)
print("Part 2 answer:", part2_sum)
