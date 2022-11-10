import os
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivymd.uix.behaviors import HoverBehavior
from kivy.properties import ListProperty
import magiceden


Builder.load_string('''
<Screen>:
    cols:1
    size_hint: 1, 1
    pos_hint: {'center_x':0.5,'center_y':0.5}
    canvas.before:
        Color:
            rgb: 26/255, 27/255, 38/255
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size
    Image:
        source: 'logo.png'
        size_hint: 0.5, 0.5
        pos_hint: {"x":0.25 , "top":0.99}

    Label:
        text: 'Mint URL'
        size_hint: 0.2, 0.2
        pos_hint: {"x":0.038, "top":0.6}


    TextInput:
        id: mint_url
        size_hint_x: 0.68
        pos_hint: {"x":0.1, "top":0.48}
        size_hint_y: 0.05
        background_color: 62/ 255, 69 / 255, 98/ 255
        cursor_color: 1, 1, 1
        hint_text_color: 1, 1, 1
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
    Label:
        text: 'Amount'
        size_hint: 0.2, 0.2
        pos_hint: {"x":0.724, "top":0.6}
    TextInput:
        id: mint_url
        size_hint_x: 0.11
        pos_hint: {"x":0.79, "top":0.48}
        size_hint_y: 0.05
        background_color: 62/ 255, 69 / 255, 98/ 255
        cursor_color: 1, 1, 1
        hint_text_color: 1, 1, 1
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1

    Label:
        text: 'Seed Phrase'
        size_hint: 0.2, 0.2
        pos_hint: {"x":0.046, "top":0.48}
    
    TextInput:
        id: seed_phrase
        size_hint_x: 0.8
        pos_hint: {"x":0.1, "top":0.36}
        size_hint_y: 0.05
        background_color: 62/ 255, 69 / 255, 98 / 255
        cursor_color: 1, 1, 1
        hint_text_color: 1, 1, 1
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1

    HoverButton:
        text: "START MINT"
        size_hint: (0.2,0.1)
        bold: True
        pos_hint: {"x":0.4, "top":0.26}
        background_color: 62/ 255, 69 / 255, 98 / 255
        on_press: root.callback()
        canvas.before:
            Color:
                rgb: self.background
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [8]
''')


class HoverButton(Button , HoverBehavior):
    background = ListProperty((62/ 255, 69 / 255, 98 / 255))
    def on_enter(self):
        self.background = 37/255, 42/255, 62 /255
    def on_leave(self):
        self.background = 26/ 255, 27/ 255, 38 / 255


class Screen(FloatLayout):
    def callback(self):
        mint = self.ids.mint_url.text
        phrase = self.ids.seed_phrase.text
        print(mint)
        print(phrase)
        print('oi')
        configFile = open("config.json", 'r')
        config = list(json.load(configFile).values())
        # isWindows = True if os.name == 'nt' else False
        magiceden.mint(config, False)

class MainApp(App):
    def build(self):
        self.icon = 'icon.png'
        self.title = 'DeBots DAO'
        return Screen()

MainApp().run()    

