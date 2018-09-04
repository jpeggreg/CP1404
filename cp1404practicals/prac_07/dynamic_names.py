# dynamically create buttons based on simple list of strings
# by Greg Taylor for CP1404 JCU

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicFruitApp(App):

    def __init__(self, *fruit):
        super().__init__(*fruit)
        self.fruitlist = ['apples', 'bananas', 'oranges', 'grapes', 'pears']

    def build(self):
        self.title = "Dynamic Fruit"
        self.root = Builder.load_file('dynamic_names.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for fruit in self.fruitlist:
            temp_fruit = Label(text=fruit)
            temp_fruit.bind(on_release=self.new_label)
            self.root.ids.fruit.add_widget(temp_fruit)

    def new_label(self):
        for fruit in self.fruitlist:
            self.status_text("{}".format(self.fruitlist[fruit]))

DynamicFruitApp().run()
