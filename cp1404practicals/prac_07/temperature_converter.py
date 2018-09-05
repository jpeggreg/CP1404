
from kivy.app import App
from kivy.lang import Builder

# Simple app to convert celcius to ferenheit from user input
class TempConverterApp(App):
    def build(self):
        self.title = "Convert Celcius to Farenheit"
        self.root = Builder.load_file('temperature_converter.kv')
        return self.root

    def handle_conversion(self):
        #initial converter from celcius input to farenheit
        temp = self.get_validated_temp()
        result = float(temp * 9.0 / 5 + 32)
        self.root.ids.output_temp.text = str(result)

    def handle_increment(self, change):
        # handles the increment pressed by user up or down to change celcius temp
        temp = self.get_validated_temp() + change
        self.root.ids.input_temp.text = str(temp)
        self.handle_conversion()

    def get_validated_temp(self):
        # validate user inout to be int otherwise return zero
        try:
            temp = float(self.root.ids.input_temp.text)
            return temp
        except ValueError:
            return 0

TempConverterApp().run()