# main.py file
import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from components import SudokuWidget as SW
from camera import camera as cam
from components import SudokuGrid
from components import SudokuSquare

Window.size = (414, 700)

class SudokuApp(App):
    """Application"""
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SW.SudokuScreen(name='main'))
        sm.add_widget(cam.ScreenCamera(name='camera'))
        return sm


if __name__ == '__main__':
    app = SudokuApp()
    app.run()
