from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class VentasWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class VentasApp(App):
    def build(self):
        return VentasWindow()
    
if __name__=='__main__':
    VentasApp().run()

    