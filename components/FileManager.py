# FileManager.py file
import os

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.utils import platform

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    popup = ObjectProperty(None)

def show_load(self):
    self.loadDialog = LoadDialog(load=self.export, cancel=self.close_popup)
    PATH = "."
    if platform == "android":
      from android.permissions import request_permissions, Permission
      request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
      app_folder = os.path.dirname(os.path.abspath(__file__))
      PATH = "/storage/emulated/0" #app_folder
    self.loadDialog.ids.filechooser.path = PATH

    self.loadDialog.popup = Popup(title="Load file", content=self.loadDialog,
                        size_hint=(0.9, 0.9))
    self.loadDialog.popup.open()
