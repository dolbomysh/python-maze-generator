from Drawer import Drawer
from Maze import Maze


class FileLoader:
    @staticmethod
    def save(maze: Maze, path: str, path_in_maze = []):
        with open(path) as file:
            file.write(Drawer.convert_maze(maze, path_in_maze))
    @staticmethod
    def load(path: str):
        with open(path) as file:
            maze_as_string = file.read()
