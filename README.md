## Генератор лабиринтов

#### Описание проекта
Реализация базовых алгоритмов для генерации и решения лабиринтов.

#### Функционал
* Генерация с помощью DFS или минимального остовного дерева (поддержка обоих вариантов)<br>
* Вариант генерации выбирается с помощью аргумента командной строки<br>
* Отображение лабиринтов в консоли с помощью специальных символов<br>
* Сохранение/загрузка лабиринтов в/из файлов<br>
* Решение лабиринтов и отображение пути. 

#### Архитектура
Описание основных классов, их атрибутов и методов.
| Название      	|            Описание           	|                                                                                                    Атрибуты                                                                                                    	|                                                                                                                                                      Методы                                                                                                                                                     	|
|:---------------:|:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| *Maze*         	| Непосредственно лабиринт      	| *__size* - размер стороны лабиринта<br><br> __adjacency_list - списки смежности клеток<br><br> *__horizontal_walls, __vertical_walls* - списки стен, каждая задается парой клеток<br><br> *__end, __begin* - клетки начала и конца лабиринта 	| *def wall_destroy(self, Сell, Cell) -> None* - удаление стены<br><br> функции получения "приватных" полей                                                                                                                                                                                                                	|
| *Cell*          	| Клетка, внутренний класс *Maze* 	| *__x, __y* - координаты в лабиринте                                                                                                                                                                              	| функции получения "приватных" полей                                                                                                                                                                                                                                                                             	|
| *MazeGenerator* 	| Генератор лабиринтов          	|                                                                                                                                                                                                                	| *def generate_maze(self, str, size) -> Maze* - общая функция генерации, вызывающая конкретный алгоритм.<br><br> *def dfs_generation(self, str, size) -> Maze<br><br> def mst_generation(self, str, size) -> Maze* - алгоритмы генерации. <br><br> *def generate_exits(self, Maze) -> None* - генерация входа и выхода  в уже готовом лабиринте 	|
| *Solver*        	| Поиск пути                    	|                                                                                                                                                                                                                	| *def path_in_maze(self, Maze) -> list[Cell]* - путь в данном лабиринте                                                                                                                                                                                                                                            	|
| *Drawer*        	| Вывод в консоль лабиринта     	|                                                                                                                                                                                                                	| *def convert_maze(self, Maze, list[Cell] = []) -> str* - преобразование лабиринта  (возможно, с решением) в строку для дальнейшего вывода в консоль или файл<br><br> *def draw_maze(self, Maze, list[Cell] = []) -> None* - вывод лабиринта в консоль  с помощью специальных символов                                       	|
| *FileLoader*    	| Загрузка лабиринтов из/в файл 	|                                                                                                                                                                                                                	| *def load_maze(self, str) -> Maze* - загрузка лабиринта из файла<br><br> *def save(self, Maze, str, list[Cell] = []) -> None* - сохранение лабиринта в файл                                                                                                                                                                 	|
