from Cell import Cell


class Maze:
    def __init__(self, walls: bool, size: int = 10):
        self.__size = size
        self.__maze = [[Cell(x, y, walls) for y in range(self.__size)] for x in range(self.__size)]
        self.__start = self.__maze[0][0]
        self.__end = self.__maze[size - 1][0]

    def get_size(self):
        return self.__size

    def get_cell(self, x: int, y: int):
        return self.__maze[x][y]

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def set_start(self, cell: Cell):
        self.__start = cell

    def set_end(self, cell: Cell):
        self.__end = cell

    @staticmethod
    def check_wall(first: Cell, second: Cell):
        dx = first.get_x() - second.get_x()
        dy = first.get_y() - second.get_y()
        if dy == 1:
            return first.check_wall("left")
        if dy == -1:
            return first.check_wall("right")
        if dx == 1:
            return first.check_wall("top")
        if dx == -1:
            return first.check_wall("bottom")

    @staticmethod
    def destroy_wall(first: Cell, second: Cell):
        dx = first.get_x() - second.get_x()
        dy = first.get_y() - second.get_y()
        if dy == 1:
            first.destroy_wall("left")
            second.destroy_wall("right")
        if dy == -1:
            first.destroy_wall("right")
            second.destroy_wall("left")
        if dx == 1:
            first.destroy_wall("top")
            second.destroy_wall("bottom")
        if dx == -1:
            first.destroy_wall("bottom")
            second.destroy_wall("top")

    @staticmethod
    def create_wall(first: Cell, second: Cell):
        dx = first.get_x() - second.get_x()
        dy = first.get_y() - second.get_y()
        if dy == 1:
            first.create_wall("left")
            second.create_wall("right")
        if dy == -1:
            first.create_wall("right")
            second.create_wall("left")
        if dx == 1:
            first.create_wall("top")
            second.create_wall("bottom")
        if dx == -1:
            first.create_wall("bottom")
            second.create_wall("top")

    def get_neighbours(self, cell: Cell):
        neighbours = []
        for dx in [-1, 1]:
            if 0 <= cell.get_x() + dx < self.get_size() and not (self.check_wall(cell, self.get_cell(cell.get_x() + dx,
                                                                                                     cell.get_y()))):
                neighbours.append(self.get_cell(cell.get_x() + dx, cell.get_y()))
        for dy in [-1, 1]:
            if 0 <= cell.get_y() + dy < self.get_size() and not (self.check_wall(cell,
                                                                 self.get_cell(cell.get_x(), cell.get_y() + dy))):
                neighbours.append(self.get_cell(cell.get_x(), cell.get_y() + dy))
        else:
            return neighbours
