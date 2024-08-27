from graphics import Line, Point


class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._win = win

        self.visited = False

    def draw(self):
        if self._win is None:
            return

        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_right = Point(self._x2, self._y2)
        bottom_left = Point(self._x1, self._y2)

        wall_color = "black"
        background_color = "white"

        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall, wall_color)
        else:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall, background_color)

        if self.has_right_wall:
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall, wall_color)
        else:
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall, background_color)

        if self.has_bottom_wall:
            bottom_wall = Line(bottom_right, bottom_left)
            self._win.draw_line(bottom_wall, wall_color)
        else:
            bottom_wall = Line(bottom_right, bottom_left)
            self._win.draw_line(bottom_wall, background_color)

        if self.has_left_wall:
            left_wall = Line(bottom_left, top_left)
            self._win.draw_line(left_wall, wall_color)
        else:
            left_wall = Line(bottom_left, top_left)
            self._win.draw_line(left_wall, background_color)

    def draw_move(self, to_cell, undo=False):
        center_self = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        center_to_cell = Point(
            (to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2
        )

        if undo:
            color = "gray"
        else:
            color = "red"

        move_line = Line(center_self, center_to_cell)
        self._win.draw_line(move_line, color)
