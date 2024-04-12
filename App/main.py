from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDRoundFlatIconButton 

KV = '''
MDScreen:
    md_bg_color: "#f7f2fa"

    MDBoxLayout:
        id: box
        spacing: "56dp"
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .5}

        MDRoundFlatIconButton:
            text: "Lesen"
            icon: "read"
            text_color: "black"
            on_press: app.on_press

        MDRoundFlatIconButton:
            text: "Meditation"
            icon: "meditation"
            text_color: "black"
            on_press: app.on_press

        MDRoundFlatIconButton:
            text: "Sport"
            icon: "weight-lifter"
            text_color: "black"
            on_press: app.on_press


'''


class MoMoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)
    
    def on_press(self):
        pass 



MoMoApp().run()