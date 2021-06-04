
from kivy.app import App
from random import sample
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button




class MyApp(App):

    def build(self):
        
        self.box_principal = BoxLayout()
        
        self.box1 = BoxLayout (orientation = 'vertical')
        

        self.box_principal.add_widget (self.box1)

        self.label1 = Label (text = '')
        
        self.botao1 = Button (text = 'GERAR NUMEROS', font_size = '30', on_release = self.incrementar)


        self.box1.add_widget (self.label1)
        self.box1.add_widget (self.botao1)
        
        return self.box_principal

    def incrementar (self, botao1):

        sorteados = sample(range(1, 60), 6)
        self.label1.text = str(sorteados)




MyApp().run()
