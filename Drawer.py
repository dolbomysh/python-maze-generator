from Cell import Cell
from Maze import Maze


def convert_maze(maze: Maze, solution: list[Cell] = []):
    new_size = maze.get_size() * 2 + 1
    char_list = [[" "] * new_size for _ in range(new_size)]
    shaded_cell = chr(9608)
    star = "*"
    for i in range(maze.get_size()):
        for j in range(maze.get_size()):
            current_cell = maze.get_cell(i, j)
            if current_cell.check_wall("top"):
                char_list[2 * i][2 * j + 1] = shaded_cell
                char_list[2 * i][2 * j + 2] = shaded_cell
            if current_cell.check_wall("bottom"):
                char_list[2 * i + 2][2 * j + 1] = shaded_cell
                char_list[2 * i + 2][2 * j] = shaded_cell
            if current_cell.check_wall("right"):
                char_list[2 * i + 1][2 * j + 2] = shaded_cell
                char_list[2 * i + 2][2 * j + 2] = shaded_cell
            if current_cell.check_wall("left"):
                char_list[2 * i + 1][2 * j] = shaded_cell
                char_list[2 * i][2 * j] = shaded_cell

    char_list[0][0] = shaded_cell
    char_list[0][new_size - 1] = shaded_cell
    char_list[new_size - 1][0] = shaded_cell
    char_list[new_size - 1][new_size - 1] = shaded_cell

    char_list[maze.get_start().get_x() * 2][0] = shaded_cell
    char_list[maze.get_start().get_x() * 2 + 1][0] = star
    char_list[maze.get_end().get_x() * 2 + 1][new_size - 1] = star
    char_list[maze.get_end().get_x() * 2 + 2][new_size - 1] = shaded_cell

    for i in range(len(solution)):
        char_list[2 * solution[i].get_x() + 1][2 * solution[i].get_y() + 1] = star
        if i < len(solution) - 1:
            dx = solution[i + 1].get_x() - solution[i].get_x()
            dy = solution[i + 1].get_y() - solution[i].get_y()
            char_list[2 * (solution[i].get_x()) + dx + 1][2 * solution[i].get_y() + dy + 1] = star

    result_string = ''
    for i in range(new_size):
        for j in range(new_size):
            result_string += char_list[i][j]
        result_string += "\n"

    return result_string
