'''
How to install kivy on Windows

https://github.com/flatplanet/kivy-youtube-playlist
https://github.com/flatplanet/kivy-youtube-playlist/blob/main/hello.py

https://www.youtube.com/watch?v=dLgquj0c5_U&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg
https://www.youtube.com/watch?v=E6AmVyYb3QM


'''

import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text="Hello World", font_size=72)


if __name__ == '__main__':
    MyApp().run()