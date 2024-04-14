import argparse

from Drawer import Drawer
from MazeGenerator import MazeGenerator
from Solver import Solver

parser = argparse.ArgumentParser()
parser.add_argument("algorithm", type=str, help="DFS or MST generation algorithm")
parser.add_argument("--size", type=int, default=10, help="Choose maze length")
parser.add_argument("--solution", type=str, default="no", help="Show solution or no")
parser.add_argument("--output", type=str, default="console", help="Enter path to output file or word \"console\"")
args = parser.parse_args()

maze = MazeGenerator.generate_maze(args.algorithm, args.size)

if args.solution == "yes":
    print(Drawer.convert_maze(maze, Solver.path_in_maze(maze)))
else:
    print(Drawer.convert_maze(maze))
