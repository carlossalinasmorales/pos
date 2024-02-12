from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class VentasWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def admin(self):
        print('Admin presionado')

    def signout(self):
        print('Sign Out presionado')

    def pagar(self):
        print('Pagar')
    
    def nueva_compra(self):
        print('Nueva compra')

    def eliminar_producto(self):
        print('eliminar_producto presionado')
        
    def modificar_producto(self):
        print('modificar_producto presionado')

    def agregar_producto_codigo(self, codigo):
        print('Se mando', codigo)
    
    def agregar_producto_nombre(self, nombre):
        print('Se mando', nombre)

class VentasApp(App):
    def build(self):
        return VentasWindow()
    
if __name__=='__main__':
    VentasApp().run()

    