def part1():
    # Initialse grid as empty list
    grid = []
    # Read input from file
    with open('day4input.txt', 'r') as file:
        for row in file:
            grid.append(list(row.strip()))

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Define all 8 possible directions
    directions = [
        (0, -1),    # Left
        (0, 1),     # Right
        (-1, 0),    # Up
        (1, 0),     # Down
        (-1, -1),   # Diagonal up-left
        (1, -1),    # Diagonal down-left
        (-1, 1),    # Diagonal up-right
        (1, 1)      # Diagonal down-right
    ]

    # Iterate through the grid to find starting 'X'
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'X':
                # Check all 8 directions for 'XMAS'
                for dr, dc in directions:
                    if (
                        0 <= row + 3 * dr < rows and 0 <= col + 3 * dc < cols and  # Ensure within bounds
                        grid[row + 1 * dr][col + 1 * dc] == 'M' and
                        grid[row + 2 * dr][col + 2 * dc] == 'A' and
                        grid[row + 3 * dr][col + 3 * dc] == 'S'
                    ):
                        count += 1

    return count

# Function to count X-MAS patterns
def part2():
    # Initialse grid as empty list
    grid = []
    # Read input from file
    with open('day4input.txt', 'r') as file:
        for row in file:
            grid.append(list(row.strip()))

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Loop through the grid (excluding border rows/columns) and find 'A' (center of 'MAS')
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == 'A':
                # Get the diagonal values
                top_left = grid[row - 1][col - 1]
                bottom_right = grid[row + 1][col + 1]
                top_right = grid[row - 1][col + 1]
                bottom_left = grid[row + 1][col - 1]

                # Check if diagonals form "MAS" or "SAM" in both directions
                if (
                    (top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M")
                ) and (
                    (top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M")
                ):
                    count += 1
    return count

# Print results for both parts
print("Part 1 answer:", part1())
print("Part 2 answer:", part2())