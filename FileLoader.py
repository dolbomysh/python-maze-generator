import Drawer
from Maze import Maze


def save(maze: Maze, path: str, path_in_maze=[]):
    file = open(path, "a+")
    file.write(Drawer.convert_maze(maze, path_in_maze))
    file.close()


def load(path: str):
    with open(path) as file:
        maze_as_string_list = []
        for line in file:
            maze_as_string_list.append(line)
        maze = Maze(True, len(maze_as_string_list) // 2)

    shaded_cell = chr(9608)
    for i in range(maze.get_size()):
        if maze_as_string_list[i][0] != shaded_cell:
            maze.set_start(maze.get_cell(i // 2, 0))
        if maze_as_string_list[i][2 * maze.get_size()] != shaded_cell:
            maze.set_end(maze.get_cell(i // 2, maze.get_size() - 1))

    for i in range(maze.get_size()):
        for j in range(maze.get_size()):
            if maze_as_string_list[2 * i][2 * j + 1] != shaded_cell:
                maze.get_cell(i, j).destroy_wall("top")
            if maze_as_string_list[2 * i + 2][2 * j + 1] != shaded_cell:
                maze.get_cell(i, j).destroy_wall("bottom")
            if maze_as_string_list[2 * i + 1][2 * j] != shaded_cell:
                maze.get_cell(i, j).destroy_wall("left")
            if maze_as_string_list[2 * i + 1][2 * j + 2] != shaded_cell:
                maze.get_cell(i, j).destroy_wall("right")

    return maze
