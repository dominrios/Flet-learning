from math import e
from multiprocessing import Value
import flet as ft 
from flet import * 
from componenets.styles import get_color_styles
from componenets.backHeader import capitalize_first_string

grp_val = "grp_val"

class DisplayPage:
    def __init__(self, switch, theme, page):
        self.title = capitalize_first_string(switch)
        self.switch = switch
        self.comparason_colors = get_color_styles(switch)
        self.get_colors = get_color_styles(theme)
        self.page = page
        self.theme = theme
    
    def build_comparasons(self):
        return Column(
            controls=[
                Container(
                    #bgcolor="blue",
                    width=200,
                    margin=margin.symmetric(vertical=10),
                    expand=True,
                    content=Column(
                        controls=[
                            Container(
                                border_radius=15,
                                bgcolor=self.comparason_colors['bgcolor'],
                                shadow= BoxShadow(
                                    spread_radius=1,
                                    blur_radius=15,
                                    color=ft.colors.BLUE_GREY_300,
                                    offset=ft.Offset(0, 0),
                                    blur_style=ft.ShadowBlurStyle.OUTER,    
                                ),
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
                                            border_radius= 5,
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
                                            bgcolor=self.comparason_colors['bgcolor'],
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
                            ),
                            Container(
                                margin=margin.only(top=-5),
                                width=200,
                                #bgcolor="#f54cd166",
                                content=Column(
                                    controls=[
                                        Radio(value=self.switch),
                                        Container(
                                            margin=margin.only(top=-15),
                                            content=Text(value=f"{self.title}", size=22)
                                        )
                                    ],
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                )
                            )
                        ]
                    )
                ),
            ]
        ) 
    
def radiomode_change(e, page):
    value = f"You have selected {e.control.value} mode"
    print(value)
    page.theme_mode = e.control.value
    page.update()
    page.update()



def build_display_page(theme, page):
    color_styles = get_color_styles(theme)
    light_view = DisplayPage("light", theme, page).build_comparasons()
    dark_view = DisplayPage("dark", theme, page).build_comparasons()
    #flip_to = {"dark": "light", "light": "dark"}
    views = [light_view, dark_view]

    return Container(
        expand=True,
        #bgcolor="orange",
        padding=padding.symmetric(horizontal=10),
        content=Column(
            controls=[
                Container(
                    bgcolor=color_styles['component'],
                    height=450,
                    #expand=True,
                    content=RadioGroup(
                        value = theme,
                        on_change = lambda e: radiomode_change(e, page),
                        content=Row(
                            controls=views,
                            alignment=MainAxisAlignment.CENTER,
                            spacing=20,
                        ),
                    )
                ),
            ]
        )
    )