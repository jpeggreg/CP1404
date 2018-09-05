from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicNameAgeApp(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nameslist = []
        with open("names.csv", "r+") as name_file:
            for name in name_file:
                self.nameslist.append(name.strip().split(","))
        print(self.nameslist)

    def build(self):
        self.title = "Dynamic Names and Ages from file"
        self.root = Builder.load_file('dynamic_names_ages.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.nameslist:
            temp_button = Button(text=name[0], id=name[1])
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.name_button.add_widget(temp_button)

    def press_entry(self, instance):
        age = instance.id
        self.status_text = "{}".format(age)


DynamicNameAgeApp().run()