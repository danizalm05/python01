"""
 The Kivy Builder - Python Kivy GUI Tutorial #6
 https://www.youtube.com/watch?v=dVVPOPuPPc0&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=6
 https://github.com/flatplanet/kivy-youtube-playlist/blob/main/builder.py

 """

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('whatever.kv')
class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)


    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        #print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!')
        # Print it to the screen
        #self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!'))
        print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!')
        # Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class AwesomeApp(App):

    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    AwesomeApp().run()