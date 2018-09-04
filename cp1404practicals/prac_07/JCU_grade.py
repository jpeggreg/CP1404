from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class JCU_grade(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "JCU Grade Giver"
        self.root = Builder.load_file('JCU_grade.kv')
        return self.root

    def handle_score(self):
        value = self.get_validated_score()
        if value >=85 and value <=100:
            self.root.ids.output_label.text = "High Distinction"
        elif value >=76:
            self.root.ids.output_label.text = "Distinction"
        elif value >=65:
            self.root.ids.output_label.text = "Credit"
        elif value >=50:
            self.root.ids.output_label.text = "Pass"
        else:
            self.root.ids.output_label.text = "Fail"

    def get_validated_score(self):
        try:
            value = float(self.root.ids.input_score.text)
            return value
        except ValueError:
            return 0

JCU_grade().run()
