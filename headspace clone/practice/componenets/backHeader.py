import flet as ft 
from flet import * 
from componenets.styles import get_color_styles

def capitalize_first_string(string):
    if len(string) == 0:
        print("hey theres an error somewhere")
        return string
    return (f"{string[0].upper() + string[1:]}")

class BackHeader:
    def __init__(self, theme, title, parent):
        self.title = title
        self.color_styles = get_color_styles(theme)
        self.route = f"/{parent}/{capitalize_first_string(title)}"
        self.back = f"/{parent}"

    def build_header(self):
        return Container(
            height= 30,
            bgcolor= "blue",
            alignment= Alignment(0.0, -1.0),
            padding=0,
            margin=0,
            content=Row(
                controls=[
                    IconButton(
                        icon= icons.ARROW_BACK_IOS_NEW_ROUNDED,
                        icon_color= self.color_styles['icon_color']
                    ),
                    Container(
                        bgcolor="green",
                    ),
                    Container()
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                expand=True
            )
        )