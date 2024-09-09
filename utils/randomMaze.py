def generateRandomMaze():
    maze = []
    for row in range(5):
        mazeRow = []
        for col in range(5):
            # Ensure start (0,0) and end (4,4) are always paths (0)
            if (row == 0 and col == 0) or (row == 4 and col == 4):
                mazeRow.append(0)
            else:
                # Randomly assign 0 (path) or 1 (wall)
                mazeRow.append(0 if Math.random() < 0.5 else 1)
        maze.append(mazeRow)
    return maze