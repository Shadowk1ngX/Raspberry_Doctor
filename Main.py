from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.metrics import dp, sp

# Import your berry_count_screen
from berry_count_screen import BerryCountScreen

import numpy as np
print(np.__version__)

# --- MAIN SCREEN ---
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Background
        with layout.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(
                source="Assets/Images/placeholderbackground.jpg",
                pos=layout.pos,
                size=Window.size
            )
        layout.bind(pos=self._update_bg, size=self._update_bg)

        # Title Label
        self.title_label = Label(
            text="Raspberry Doctor",
            color=(0.5, 0, 0, 1),  # #800000
            font_size=sp(28),
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'top': 0.98}
        )
        self.title_label.texture_update()
        self.title_label.size = self.title_label.texture_size
        layout.add_widget(self.title_label)

        # Button: Berry Counting
        self.berry_count_btn = Button(
            text="Berry Counting",
            size_hint=(None, None),
            size=(dp(280), dp(50)),
            font_size=sp(18),
            background_normal='',
            background_color=(0.8, 0.7, 0.1, 1),
            pos_hint={'center_x': 0.5, 'top': 0.58}
        )
        self.berry_count_btn.bind(on_press=self.on_berry_count)
        layout.add_widget(self.berry_count_btn)

        # ... You can add other buttons (Irrigation, etc.) here ...

        self.add_widget(layout)

    def _update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def on_berry_count(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = "berry_count"


# --- THE APP WITH SCREENMANAGER ---
class RaspberryApp(App):
    def build(self):
        sm = ScreenManager()
        # Add the main screen and the berry count screen
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(BerryCountScreen(name="berry_count"))
        sm.current = "main"
        return sm

if __name__ == '__main__':
    RaspberryApp().run()
