import kivy
import os
kivy.require('1.9.1')

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from sudoku import Sudoku

from components import FileManager as FileManager
from components import ErrorPopup as Error
import analyzer.validator as validator
import analyzer.solver as solver

# class SudokuWidget(Widget):
    # grid_widget = ObjectProperty(None)

    # def solve_button_action(self):
        # self.grid = self.grid_widget.to_array()
        # (solvable, information) = validator.validate_sudoku(self.grid)
        # if solvable:
            # self.solve()
        # else:
            # Error.open_error_popup(self, information)
                    
    # def clean_button_action(self):
        # self.grid_widget.clear()

    # def export_button_action(self):
        # FileManager.show_load(self)

    # def scan_button_action(self):
        # FileManager.show_load(self)
          
    # def close_popup(self, popup):
        # popup.dismiss()
        
    # def solve(self):
        # puzzle = Sudoku(3, 3, board=self.grid.tolist())
        # solution = puzzle.solve(raising=True)
        # self.grid_widget.update_from_array(solution.board)

    # def export(self, path, filename):
        # board = solver.get_board_from_image(os.path.join(path, filename[0]))
        # self.grid_widget.update_from_image_board(board)
        
        # self.close_popup(self.loadDialog.popup)
        
from kivy.uix.screenmanager import ScreenManager, Screen

class SudokuScreen(Screen):
    grid_widget = ObjectProperty(None)

    def solve_button_action(self):
        self.grid = self.grid_widget.to_array()
        (solvable, information) = validator.validate_sudoku(self.grid)
        if solvable:
            self.solve()
        else:
            Error.open_error_popup(self, information)
                    
    def clean_button_action(self):
        self.grid_widget.clear()

    def export_button_action(self):
        FileManager.show_load(self)
          
    def close_popup(self, popup):
        popup.dismiss()
        
    def solve(self):
        puzzle = Sudoku(3, 3, board=self.grid.tolist())
        solution = puzzle.solve(raising=True)
        self.grid_widget.update_from_array(solution.board)

    def export(self, path, filename):
        board = solver.get_board_from_image(os.path.join(path, filename[0]))
        self.grid_widget.update_from_image_board(board)
        
        self.close_popup(self.loadDialog.popup)
        