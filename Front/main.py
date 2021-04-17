from kivy.app import App
# from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass
class Menu (Screen):
    pass

from kivy.uix.scrollview import ScrollView

class Tarefas(Screen): #classe vazia que passará pela classe principal que no nosso caso é a Test
    def __init__(self, tarefas=[], **kwargs): #dicionário que é passado para o init
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa)) #associação de label e botão
    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text=''
class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text
class Test(App):
    def build(self):
        return Gerenciador()

    # def build(self):
    #     box = BoxLayout(orientation = 'vertical')    #faz os botoes ficarem um cima do outro
    #     button = Button(text='Botao 1', font_size = 30, on_release=self.incrementar)
    #     self.label = Label(text='Texto 1', font_size=30)
    #     box.add_widget(button)
    #     box.add_widget(self.label)
    #     return box
    # def incrementar(self, button):
    #     self.label.text = str(int(self.label.text)+1)





Test().run()