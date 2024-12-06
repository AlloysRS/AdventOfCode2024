def get_grid_info():
    # Initialise empty list for grid, and blank variables for start position and start direction
    grid = []
    start_position = None
    start_direction = None

    # Read grid input from file and append each row to grid
    with open('day6input.txt', 'r') as file:
        for line in file:
            grid.append(line)

    # Get number of rows and columns in grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Dictionary of directions as direction: (rows, cols) to adjust
    directions = {
        "^": (-1, 0),   # Up
        "v": (1, 0),    # Down
        "<": (0, -1),   # Left
        ">": (0, 1)}    # Right

    # Find the starting position (index) and direction (symbol)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] in directions:
                start_position = (row, col)
                start_direction = grid[row][col]
                break
        # Once found, break out of loop
        if start_position:
            break
    # Return the grid, starting position, starting direction, directions, number of rows and cols
    return grid, start_position, start_direction, directions, rows, cols

# Helper function to simulate given route
def simulate_route(grid, current_pos, direction, directions, rows, cols):
    # Initialise a empty set for visited positions and empty list for the route
    visited = set()
    route = []

    # Loop while the current position and direction has not been visited before
    while (current_pos, direction) not in visited:
        # Add current position and direction to visited set, and current position to route
        visited.add((current_pos, direction))
        route.append(current_pos)

        # Determine the next position
        d_row, d_col = directions[direction]
        next_pos = (current_pos[0] + d_row, current_pos[1] + d_col)

        # Check if the guard exits the map as termination criteria
        if next_pos[0] < 0 or next_pos[0] == rows or next_pos[1] < 0 or next_pos[1] == cols:
            break

        # If obstruction found, turn right based on current direction
        if grid[next_pos[0]][next_pos[1]] == "#":
            if direction == "^":
                direction = ">"
            elif direction == ">":
                direction = "v"
            elif direction == "v":
                direction = "<"
            elif direction == "<":
                direction = "^"
        # If no obstruction, continue in current direction
        else:
            current_pos = next_pos

    # Return the route and the number of distinct positions visited
    return route, len({pos for pos, _ in visited})

# Helper function to test if adding an obstruction causes a loop
def causes_loop_with_obstruction(obstruction_pos, grid, current_pos, direction, directions, rows, cols):
    visited = set()

    # Loop while the current position and direction has not been visited before
    while True:
        # Check if we've been in this position with the same direction before
        state = (current_pos, direction)
        # If state already visited, then we are in a loop
        if state in visited:
            return True  # Loop detected
        visited.add(state)

        # Determine the next position
        d_row, d_col = directions[direction]
        next_pos = (current_pos[0] + d_row, current_pos[1] + d_col)

        # Check if the guard exits the map as termination criteria
        if next_pos[0] < 0 or next_pos[0] == rows or next_pos[1] < 0 or next_pos[1] == cols:
            return False # No loop detected

        # If obstruction is found at the next position, turn right
        if next_pos == obstruction_pos or grid[next_pos[0]][next_pos[1]] == "#":
            if direction == "^":
                direction = ">"
            elif direction == ">":
                direction = "v"
            elif direction == "v":
                direction = "<"
            elif direction == "<":
                direction = "^"
        # If no obstruction, move to the next position
        else:
            current_pos = next_pos

def part1(grid, start_position, start_direction, directions, rows, cols):
    _, steps_taken = simulate_route(grid, start_position, start_direction, directions, rows, cols)
    return steps_taken

def part2(grid, start_position, start_direction, directions, rows, cols):
    starting_route, _ = simulate_route(grid, start_position, start_direction, directions, rows, cols)

    # Initialise empty list for loop positions
    loop_positions = []

    # Loop iteration over positions on the starting patrol route
    for position in starting_route:
        # Loop check in each direction
        for direction in directions:
            d_row, d_col = directions[direction]
            # Get neighbouring cell given current direction
            neighbor = (position[0] + d_row, position[1] + d_col)
            # Check if is valid to move to
            if (
                0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols # Check within grid boundaries
                and neighbor != start_position # Check is not starting position
                and grid[neighbor[0]][neighbor[1]] == "." # Check is empty space for movement
            ):
                # Check if not already in loop positions and if causes_loop_with_obstruction returns True (results in a loop)
                if neighbor not in loop_positions and causes_loop_with_obstruction(
                    neighbor, grid, start_position, start_direction, directions, rows, cols
                ):
                    # Append neighbour to loop positions
                    loop_positions.append(neighbor)
    # Return number of loop positions (can also print these for debugging)
    return len(loop_positions)

grid, start_position, start_direction, directions, rows, cols = get_grid_info()
print("Part 1 answer:", part1(grid, start_position, start_direction, directions, rows, cols))
print("Part 2 answer:", part2(grid, start_position, start_direction, directions, rows, cols))