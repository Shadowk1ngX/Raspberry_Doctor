import sys
import subprocess
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp, sp
from kivy.graphics import Color, Rectangle

class BerryCountScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        # 1) Home button at the very top
        home_btn = Button(
            text="Home",
            size_hint=(None, None),
            size=(dp(120), dp(50)),
            pos_hint={'center_x': 0.5, 'top': 0.95},
            background_normal='',
            background_color=(0.6, 0.4, 0.8, 1)  # a purple-ish color
        )
        home_btn.bind(on_press=self.go_home)
        layout.add_widget(home_btn)

        # 2) A large area for the camera feed (placeholder).
        camera_feed_placeholder = Button(
            text="",
            size_hint=(1, None),
            height=dp(300),
            pos_hint={'x': 0, 'top': 0.75},
            background_normal='',
            background_color=(0.9, 0.9, 0.9, 1)  # light gray
        )
        layout.add_widget(camera_feed_placeholder)

        # 3) Instruction label below the camera feed
        instruction_label = Label(
            text="Take new video/image or pick one from the gallery",
            font_size=sp(20),
            color=(0, 0, 0, 1),
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'top': 0.58}
        )
        layout.add_widget(instruction_label)

        # 4) Results label (white background) for detection results
        results_label = Label(
            text="Detection results will appear here.",
            font_size=sp(18),
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=dp(40),
            pos_hint={'x': 0, 'top': 0.52}
        )
        layout.add_widget(results_label)

        # 5) Camera button (bottom-left)
        camera_btn = Button(
            text="Camera",
            size_hint=(None, None),
            size=(dp(120), dp(50)),
            pos_hint={'center_x': 0.3, 'y': 0.05},
            background_normal='',
            background_color=(0.6, 0.4, 0.8, 1)
        )
        # Optionally, bind camera_btn to a method for handling camera actions:
        # camera_btn.bind(on_press=self.open_camera)
        layout.add_widget(camera_btn)

        # 6) Gallery button (bottom-right)
        gallery_btn = Button(
            text="Gallery",
            size_hint=(None, None),
            size=(dp(120), dp(50)),
            pos_hint={'center_x': 0.7, 'y': 0.05},
            background_normal='',
            background_color=(0.6, 0.4, 0.8, 1)
        )
        gallery_btn.bind(on_press=self.open_gallery)
        layout.add_widget(gallery_btn)

        self.add_widget(layout)

    def go_home(self, instance):
        # Swipe to the right when returning home
        self.manager.transition.direction = 'right'
        self.manager.current = "main"

    def open_gallery(self, instance):
        # This function runs an external script (e.g., gallery_script.py)
        try:
            script = "berrycounter.py"  # Adjust the script name/path if needed
            # Use sys.executable to call the current Python interpreter.
            subprocess.Popen([sys.executable, script])
        except Exception as e:
            print("Error running gallery script:", e)
