import heapq
import random

from Cell import Cell
from Graph import Graph
from Maze import Maze


def generate_maze(algorithm: str, size: int):
    if algorithm == "DFS":
        return dsf_generation(size)
    elif algorithm == "MST":
        return mst_generation(size)


def get_unused_neighbour(maze: Maze, cell: Cell, is_used: list[list[bool]]):
    neighbours = []
    for dx in [-1, 1]:
        if 0 <= cell.get_x() + dx < maze.get_size() and not (is_used[cell.get_x() + dx][cell.get_y()]):
            neighbours.append(maze.get_cell(cell.get_x() + dx, cell.get_y()))
    for dy in [-1, 1]:
        if 0 <= cell.get_y() + dy < maze.get_size() and not (is_used[cell.get_x()][cell.get_y() + dy]):
            neighbours.append(maze.get_cell(cell.get_x(), cell.get_y() + dy))
    if len(neighbours) == 0:
        return None
    else:
        return random.choice(neighbours)


def dsf_generation(size: int):
    maze = Maze(True, size)
    is_used = [[False for _ in range(size)] for _ in range(size)]
    stack = []
    current = maze.get_start()
    is_used[current.get_x()][current.get_y()] = True
    stack.append(current)

    while stack:
        neighbour = get_unused_neighbour(maze, current, is_used)
        if neighbour:
            maze.destroy_wall(current, neighbour)
            is_used[neighbour.get_x()][neighbour.get_y()] = True
            stack.append(neighbour)
            current = neighbour
        else:
            stack.pop()
            if stack:
                current = stack[len(stack) - 1]
    generate_exits(maze)
    return maze


def mst_generation(size: int):
    maze = Maze(False, size)
    grind_size = size + 1
    grid_node_graph = Graph((grind_size * grind_size))
    max_edge_weight = 100
    for i in range(grind_size - 1):
        for j in range(grind_size - 1):
            grid_node_graph.add_edge(i + j * grind_size, i + 1 + j * grind_size, random.randint(1, max_edge_weight))
            grid_node_graph.add_edge(i + j * grind_size, i + (j + 1) * grind_size, random.randint(1, max_edge_weight))

    used_vertices = set()
    considered_edges = []
    for i in range(grind_size):
        used_vertices.add(i)
        for edge in grid_node_graph.get_neighbours(i):
            heapq.heappush(considered_edges, edge)

        used_vertices.add(grind_size * grind_size - i - 1)
        for edge in grid_node_graph.get_neighbours(grind_size * grind_size - i - 1):
            heapq.heappush(considered_edges, edge)

        used_vertices.add(grind_size * (i + 1) - 1)
        for edge in grid_node_graph.get_neighbours(grind_size * (i + 1) - 1):
            heapq.heappush(considered_edges, edge)

        used_vertices.add(grind_size * i)
        for edge in grid_node_graph.get_neighbours(grind_size * i):
            heapq.heappush(considered_edges, edge)

        if i < grind_size - 1:
            maze.get_cell(0, i).create_wall("top")
            maze.get_cell(size - 1, i).create_wall("bottom")
            maze.get_cell(i, 0).create_wall("left")
            maze.get_cell(i, size - 1).create_wall("right")

    while considered_edges:
        min_edge = heapq.heappop(considered_edges)
        if not (min_edge.vertex_to in used_vertices):
            used_vertices.add(min_edge.vertex_to)
            for edge in grid_node_graph.get_neighbours(min_edge.vertex_to):
                heapq.heappush(considered_edges, edge)
            if (min_edge.vertex_to - min_edge.vertex_from) % grind_size == 0:
                cell_x = min(min_edge.vertex_to // grind_size, min_edge.vertex_from // grind_size)
                cell_y = min(min_edge.vertex_to, min_edge.vertex_from) % grind_size
                maze.create_wall(maze.get_cell(cell_x, cell_y), maze.get_cell(cell_x, cell_y - 1))
            else:
                cell_x = min(min_edge.vertex_to, min_edge.vertex_from) // grind_size
                cell_y = min(min_edge.vertex_to, min_edge.vertex_from) % grind_size
                maze.create_wall(maze.get_cell(cell_x, cell_y), maze.get_cell(cell_x - 1, cell_y))
    generate_exits(maze)
    return maze


def generate_exits(maze: Maze):
    maze.set_start(maze.get_cell(random.randint(0, maze.get_size() - 1), 0))
    maze.get_start().destroy_wall("left")
    maze.set_end(maze.get_cell(random.randint(0, maze.get_size() - 1), maze.get_size() - 1))
    maze.get_end().destroy_wall("right")
