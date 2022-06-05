# camera.py file
from kivy.uix.screenmanager import ScreenManager, Screen
import time

class ScreenCamera(Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        
    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'screen_sudoku'

