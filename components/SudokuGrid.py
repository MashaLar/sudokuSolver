# SudokuGrid.py file
import numpy as np
import kivy
kivy.require('1.9.1')

from kivy.uix.gridlayout import GridLayout
from components import SudokuSquare as SS

class SudokuGrid(GridLayout):
    """9*9 input Grid."""

    def __init__(self, **kwargs):
        super(SudokuGrid, self).__init__(cols=3, spacing=[2, 2], **kwargs)
        self.squares = []
        for i in range(9):
            subgrid = GridLayout(cols=3)
            for j in range(9):
                square = SS.SudokuSquare()
                subgrid.add_widget(square)
                self.squares.append(square)
            self.add_widget(subgrid) 

    def to_array(self):
        user_input = [0 if square.text == '' else int(square.text)
                      for square in self.squares]
        subgrids = np.vsplit(np.array(user_input).reshape(27, 3), 9)
        grid = np.vstack((np.hstack(subgrids[0:3]),
                          np.hstack(subgrids[3:6]),
                          np.hstack(subgrids[6:9])))
        return grid

    def update_from_array(self, grid):
        subgrids = [np.hsplit(num, 3) for num in np.vsplit(np.array(grid), 3)]
        output_values = np.vstack(subgrids).reshape(1, 81)[0]
        for square, value in zip(self.squares, output_values):
            square.text = str(value)

    def update_from_image_board(self, grid):
        subgrids = [np.hsplit(num, 3) for num in np.vsplit(np.array(grid), 3)]
        output_values = np.vstack(subgrids).reshape(1, 81)[0]
        for square, value in zip(self.squares, output_values):
            square.text = '' if value == 0 else str(value)

    def clear(self):
        for square in self.squares:
            square.text = ""