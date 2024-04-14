class Cell:
    def __init__(self, x: int, y: int, walls: bool):
        self.__x = x
        self.__y = y
        self.__walls = {"bottom": walls, "top": walls, "left": walls, "right": walls}

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def check_wall(self, direction: str):
        return self.__walls[direction]

    def destroy_wall(self, direction: str):
        self.__walls[direction] = False

    def create_wall(self, direction: str):
        self.__walls[direction] = True
