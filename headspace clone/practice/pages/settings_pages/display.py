import flet as ft 
from flet import * 
from componenets.styles import get_color_styles
from componenets.backHeader import capitalize_first_string


class DisplayPage:
    def __init__(self, switch, theme):
        self.title = capitalize_first_string(switch)
        self.switch = switch
        self.comparason_colors = get_color_styles(switch)
        self.get_colors = get_color_styles(theme)
    
    def build_comparasons(self):
        return Column(
            controls=[
                Container(
                    bgcolor="blue",
                    width=200,
                    margin=margin.symmetric(vertical=10),
                    expand=True,
                    content=Column(
                        controls=[
                            Container(
                                border_radius=15,
                                bgcolor=self.comparason_colors['bgcolor'],
                                height=350,
                                content=Column(
                                    controls=[
                                        Container(
                                            height=30
                                        ),

                                        #should be a card object
                                        Container(
                                            border_radius=5,
                                            bgcolor=self.comparason_colors['component'],
                                            height=30,
                                            margin=margin.only(left=10, right=30),
                                            alignment=alignment.center,
                                            content=Row(
                                                controls=[
                                                    Container(
                                                        width=18,
                                                        height=18,
                                                        bgcolor=self.comparason_colors['icon_color'],
                                                        border_radius=15,
                                                    ),
                                                    Container(
                                                        width=70,
                                                        height=20,
                                                        border_radius = 25,
                                                        bgcolor=self.comparason_colors['icon_color'],
                                                    )
                                                ]
                                            )
                                        ),

                                        #should be a card object
                                        Container(
                                            border_radius=5,
                                            bgcolor=self.comparason_colors['component'],
                                            height=30,
                                            margin=margin.only(left=10, right=30),
                                            alignment=alignment.center,
                                            content=Row(
                                                controls=[
                                                    Container(
                                                        width=18,
                                                        height=18,
                                                        bgcolor=self.comparason_colors['icon_color'],
                                                        border_radius=15,
                                                    ),
                                                    Container(
                                                        width=70,
                                                        height=20,
                                                        border_radius = 25,
                                                        bgcolor=self.comparason_colors['icon_color'],
                                                    )
                                                ]
                                            )
                                        ),

                                        #should be a card object
                                        Container(
                                            border_radius=5,
                                            bgcolor=self.comparason_colors['component'],
                                            height=30,
                                            margin=margin.only(left=10, right=30),
                                            alignment=alignment.center,
                                            content=Row(
                                                controls=[
                                                    Container(
                                                        width=18,
                                                        height=18,
                                                        bgcolor=self.comparason_colors['icon_color'],
                                                        border_radius=15,
                                                    ),
                                                    Container(
                                                        width=70,
                                                        height=20,
                                                        border_radius = 25,
                                                        bgcolor=self.comparason_colors['icon_color'],
                                                    )
                                                ]
                                            )
                                        ),
                                        Container(
                                            margin=0,
                                            padding=0,
                                            height=40,
                                            alignment=alignment.bottom_center,
                                            border=border.only(top=BorderSide(4, self.comparason_colors['border'])),
                                            bgcolor="red",
                                            content=Row(
                                                [   
                                                    #should be a mini icon object
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius= 25,
                                                        bgcolor=self.comparason_colors['active'],
                                                        margin=margin.only(bottom=7)
                                                    ),
                                                    #should be a mini icon object
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius= 25,
                                                        bgcolor=self.comparason_colors['icon_color'],
                                                        margin=margin.only(bottom=7)
                                                    ),
                                                    #should be a mini icon object
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius= 25,
                                                        bgcolor=self.comparason_colors['icon_color'],
                                                        margin=margin.only(bottom=7)
                                                    ),
                                                    #should be a mini icon object
                                                    Container(
                                                        height=20,
                                                        width=20,
                                                        border_radius= 25,
                                                        bgcolor=self.comparason_colors['icon_color'],
                                                        margin=margin.only(bottom=7)
                                                    ),
                                                ],
                                                alignment=MainAxisAlignment.SPACE_AROUND,
                                            )
                                       ),
                                    ],
                                    expand=True,
                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                )
                            )
                        ]
                    )
                ),
            ]
        ) 

def build_display_page(theme, page):
    color_styles = get_color_styles(theme)
    light_view = DisplayPage("light", theme).build_comparasons()
    dark_view = DisplayPage("dark", theme).build_comparasons()
    flip_to = {"dark": "light", "light": "dark"}
    views = [light_view, dark_view]

    return Container(
        expand=True,
        bgcolor="orange",
        padding=padding.symmetric(horizontal=10),
        content=Column(
            controls=[
                Container(
                    bgcolor=color_styles['component'],
                    height=100,
                    expand=True,
                    content=Row(
                        controls=views,
                        alignment=MainAxisAlignment.CENTER,
                        spacing=20,
                    )
                ),
                Container(
                    bgcolor="green",
                    height=200,
                    expand=True
                ),
            ]
        )
    )