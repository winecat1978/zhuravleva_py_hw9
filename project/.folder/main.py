# py C:\Users\mob19\py_hw9\project\.folder\main.py - запуск проги

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config
# импортировали все необходимые элементы

Config.set("graphics","resizable","0")
Config.set("graphics","width","300")
Config.set("graphics","height","300")
# настроили экран 300 на 300 без воз-ти растягиваться

# класс мэйн с функциями
class MainApp(App):
    def __init__(self):
        super().__init__() #Ключевыми понятиями наследования являются подкласс и суперкласс. 
        #Подкласс наследует от суперкласса все публичные атрибуты и методы. 
        #Суперкласс еще называется базовым (base class) или родительским (parent class), 
        #а подкласс - производным (derived class) или дочерним (child class).
        self.switch = True
 
    def tic_tac_toe(self, arg): #исполнение логики приложения
        arg.disabled = True
        arg.text = 'X' if self.switch else 'O'
        self.switch = not self.switch
 
        coordinate = (
            (0,1,2), (3,4,5), (6,7,8), # X
            (0,3,6), (1,4,7), (2,5,8), # Y
            (0,4,8), (2,4,6),          # D
        )
 
        vector = lambda item: [self.buttons[x].text for x in item]
 
        color = [0,1,0,1] #зеленый цвет при выигрыше
 
        for item in coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                win = True
                for i in item:
                    self.buttons[i].color = color
                for button in self.buttons:
                    button.disabled = True
                break
 
    def restart(self, arg):
        self.switch = True
 
        for button in self.buttons:
            button.color = [0,0,0,1]
            button.text = ""
            button.disabled = False
 
    def build(self):
        self.title = "Крестики-нолики"
 
        root = BoxLayout(orientation="vertical", padding=5) #контейнер для кнопок
 
        grid = GridLayout(cols=3)
        self.buttons = []
        for _ in range(9): # настроили цвет, размер кнопок
            button = Button(
                color = [0,0,0,1],
                font_size = 30,
                disabled = False,
                on_press = self.tic_tac_toe
            )
            self.buttons.append(button) #добавили кнопки в список
            grid.add_widget(button)
 
        root.add_widget(grid)
 
        root.add_widget(
            Button(
               text = "Restart",
               size_hint = [1,.1],
               on_press = self.restart
            )
        )
        return root

if __name__ == "__main__":
    MainApp().run()