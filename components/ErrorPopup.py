# ErrorPopup.py file
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class ErrorPopup(FloatLayout):
    ok = ObjectProperty(None)
    information = ObjectProperty(None)
    popup = ObjectProperty(None)

def open_error_popup(self, information):
    content = ErrorPopup(ok=self.close_popup, information=information)
    content.popup = Popup(title="ERROR", content=content, size_hint=(0.6, 0.2), separator_color=(1,.24,0,1), title_size='18sp')
    content.popup.open()
