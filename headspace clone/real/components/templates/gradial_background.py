from flet import *
from components.methods.styles import get_color_styles

class Background:
    def __init__(self, theme) -> None:
        self.color_styles = get_color_styles(theme)

    def build_background(self):
        return Container(
            expand=True,
            gradient=RadialGradient(
                center=Alignment(0.4, -1.25),
                radius=1.4,
                colors=self.color_styles['gradient']
            )
        )