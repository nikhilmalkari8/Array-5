def isRobotBounded(instructions: str) -> bool:
    # Directions: 0 -> North, 1 -> East, 2 -> South, 3 -> West
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y, dir_idx = 0, 0, 0  # Starting position and facing North

    for instruction in instructions:
        if instruction == 'G':
            x += directions[dir_idx][0]
            y += directions[dir_idx][1]
        elif instruction == 'L':
            dir_idx = (dir_idx - 1) % 4  # Turn left (counter-clockwise)
        elif instruction == 'R':
            dir_idx = (dir_idx + 1) % 4  # Turn right (clockwise)

    # If the robot is back at origin or not facing North, it's bounded
    return (x == 0 and y == 0) or dir_idx != 0

# Example usage:
instructions = "GGLLGG"
print(isRobotBounded(instructions))  # Output: True
