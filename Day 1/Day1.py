def part1():
    with open('day1input.txt', 'r') as file:
        # Initialise empty list for both lists
        list1 = []
        list2 = []

        # For each row, split data and append to each list (as ints)
        for row in file:
            lists = row.split()
            list1.append(int(lists[0]))
            list2.append(int(lists[1]))

    # Initialise total distance to 0
    total_distance = 0

    # For each value in both sorted lists, calculate the absolute distance and add this to the total distance  
    for value1, value2 in zip(sorted(list1), sorted(list2)):
        distance = abs(value1 - value2)
        total_distance += distance
 
    # Finally, return the total distance
    return total_distance

def part2():
    with open('day1input.txt', 'r') as file:
        # Initialise empty list for both lists
        list1 = []
        list2 = []

        # For each row, split data and append to each list (as ints)
        for row in file:
            lists = row.split()
            list1.append(int(lists[0]))
            list2.append(int(lists[1]))
    
    # Create a dictionary for counts, for each num in list1, if is in list2, count occurences else 0
    counts = {}
    for num in list1:
        if num in list2:
            counts[num] = list2.count(num)
        else:
            counts[num] = 0

    # Initialise similarity to 0, for each num in list1, add to similarity the product of num and counts of that number
    similarity = 0
    for num in list1:
        similarity += num *counts[num]

    # Finally, return the similarity score
    return similarity

if __name__ == '__main__':
    print("Part 1 answer:", part1())
    print("Part 2 answer:", part2())