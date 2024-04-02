from collections import deque

def bfs_2d_array(matrix, start, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    visited = set()
    queue = deque([(start, [])])  # Store both current position and moves made to reach it

    while queue:
        current_pos, moves_made = queue.popleft()
        x, y = current_pos

        if current_pos == target:
            print("Target position found:", current_pos)
            print("Moves made to reach the target:", moves_made)
            return True

        visited.add(current_pos)

        # Define possible directions: up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            new_pos = (new_x, new_y)

            if 0 <= new_x < rows and 0 <= new_y < cols and matrix[new_x][new_y] == 1 and new_pos not in visited:
                new_moves = moves_made + [new_pos]  # Append the move to the list of moves made
                queue.append((new_pos, new_moves))

    print("Target position not found!")
    return False

# Example usage:

# Define the 2D array
matrix = [
		[1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
		[0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
		[1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
		[1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
		[1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
		[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
		[1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
	]

# Define the starting position
start_position = (8, 0)

# Define the target value to search for
target_value = (0, 0)

# Run BFS algorithm
found = bfs_2d_array(matrix, start_position, target_value)

# Print the result
if found:
    print(f"Target value {target_value} found!")
else:
    print(f"Target value {target_value} not found!")
