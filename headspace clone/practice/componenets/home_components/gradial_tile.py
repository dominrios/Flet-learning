from flet import *
from componenets.styles import get_color_styles
from componenets.methods import get_route, capitalize_first_string

class Tile:
    def __init__(self, theme, input_icon, title) -> None:
        self.color_styles = get_color_styles(theme)
        self.input_icon = input_icon
        self.title = capitalize_first_string(title)
        self.route = get_route(title)

    def gen_tile(self):
        return Container(
            width= 100,
            height= 75,
            border_radius=15,
            content=Column(
                controls=[
                    Row(
                        controls=[
                            Icon(name=self.input_icon, color=self.color_styles['icon_color'], size =30),
                            IconButton(name=icons.POWER_SETTINGS_NEW_ROUNDED, color=self.color_styles['icon_color'], size=30)
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                    ),
                #Location Container(),
                #Device   Container(),
                #Status   Container(),
                ]
            )
        )
    
    #string methods of title of new device, create a new device with route and that route will be automatically
    #generated with a default device template, subpage(defaultTemplate(self.input_icon, self.title, self.route))