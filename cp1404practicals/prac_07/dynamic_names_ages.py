from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicNameAgeApp(App):

    status_text = StringProperty()

    def __init__(self, **names_ages):
        super().__init__(**names_ages)
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
        for i in range(len(self.nameslist)):
            temp_name = Button(text=str([i][0]))
            temp_name.bind(on_release=self.press_entry(self.nameslist[name][0]))
            self.root.ids.name.add_widget(temp_name)

    def press_entry(self, temp_name):
        self.status_text = "{}".format(self.nameslist[temp_name][1])


    '''def new_label(self):
        for name in self.nameslist:
            self.status_text = "{}".format(self.nameslist[name][1])

    def show_age(self, nameslist):
        for name in range(len(nameslist)):
            print(name)'''

DynamicNameAgeApp().run()