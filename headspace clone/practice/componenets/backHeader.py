import flet as ft 
from flet import * 
from componenets.styles import get_color_styles

class BackHeader:
    def __init__(self, theme, title):
        self.title = title
        self.color = get_color_styles(theme)
        

    def build_header(self):
        return Container(
            height= 30,
            bgcolor= "blue",
            alignment= Alignment(0.0, -1.0),
            padding=0,
            margin=0,
        )