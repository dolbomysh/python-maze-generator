from Cell import Cell
from Maze import Maze


class Drawer:
    @staticmethod
    def convert_maze(maze: Maze, solution: list[Cell] = []):
        new_size = maze.get_size() * 2 + 1
        char_list = [[" "] * new_size for _ in range(new_size)]
        for i in range(maze.get_size()):
            for j in range(maze.get_size()):
                current_cell = maze.get_cell(i, j)
                if current_cell.check_wall("top"):
                    char_list[2 * i][2 * j + 1] = chr(9608)
                    char_list[2 * i][2 * j + 2] = chr(9608)
                if current_cell.check_wall("bottom"):
                    char_list[2 * i + 2][2 * j + 1] = chr(9608)
                    char_list[2 * i + 2][2 * j] = chr(9608)
                if current_cell.check_wall("right"):
                    char_list[2 * i + 1][2 * j + 2] = chr(9608)
                    char_list[2 * i + 2][2 * j + 2] = chr(9608)
                if current_cell.check_wall("left"):
                    char_list[2 * i + 1][2 * j] = chr(9608)
                    char_list[2 * i][2 * j] = chr(9608)

        char_list[0][0] = chr(9608)
        char_list[0][new_size - 1] = chr(9608)
        char_list[new_size - 1][0] = chr(9608)
        char_list[new_size - 1][new_size - 1] = chr(9608)

        char_list[maze.get_start().get_x() * 2][0] = chr(9608)
        char_list[maze.get_start().get_x() * 2 + 1][0] = chr(9673)
        char_list[maze.get_end().get_x() * 2 + 1][new_size - 1] = chr(9673)
        char_list[maze.get_end().get_x() * 2 + 2][new_size - 1] = chr(9608)

        for i in range(len(solution)):
            char_list[2 * solution[i].get_x() + 1][2 * solution[i].get_y() + 1] = chr(9673)
            if (i < len(solution) - 1):
                dx = solution[i + 1].get_x() - solution[i].get_x()
                dy = solution[i + 1].get_y() - solution[i].get_y()
                char_list[2 * (solution[i].get_x()) + dx + 1][2 * solution[i].get_y() + dy + 1] = chr(9673)

        result_string = ''
        for i in range(new_size):
            for j in range(new_size):
                result_string += char_list[i][j]
            result_string += "\n"

        return result_string