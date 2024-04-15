from Cell import Cell
from Maze import Maze


class Solver:
    @staticmethod
    def path_in_maze(maze: Maze):
        path = []
        parent = [[maze.get_end() for _ in range(maze.get_size())] for _ in range(maze.get_size())]
        is_used = [[False for _ in range(maze.get_size())] for _ in range(maze.get_size())]
        Solver.path_by_dfs(maze, maze.get_start(), parent, is_used)

        path.append(maze.get_end())
        current_parent = parent[maze.get_end().get_x()][maze.get_end().get_y()]
        while current_parent != maze.get_end():
            path.append(current_parent)
            current_parent = parent[current_parent.get_x()][current_parent.get_y()]

        return path

    @staticmethod
    def path_by_dfs(maze: Maze, cell: Cell, parent: list[list[Cell]], is_used: list[list[bool]]):
        is_used[cell.get_x()][cell.get_y()] = True
        neighbours = maze.get_neighbours(cell)
        for neighbour_cell in neighbours:
            if not (is_used[neighbour_cell.get_x()][neighbour_cell.get_y()]):
                parent[neighbour_cell.get_x()][neighbour_cell.get_y()] = cell
                Solver.path_by_dfs(maze, neighbour_cell, parent, is_used)
