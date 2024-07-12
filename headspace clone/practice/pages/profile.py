import flet as ft
from flet import *
from componenets.styles import get_color_styles

def build_profile(theme,page):
    color_styles = get_color_styles(theme)
    page=page
    page.title = "Profile"
    return Stack(
        [
            # Background for profile page
            Column(
                controls=[
                    Container(
                        gradient=LinearGradient(
                            begin=alignment.top_center,
                            end=alignment.bottom_center,
                            colors=[f"{color_styles['gradient'][0]}", f"{color_styles['gradient'][1]}"]
                        ),
                        padding=0,
                        height=200,
                        margin=0,
                        expand=True  # Ensure this container takes up the full width
                    ),
                    Container(
                        padding=0,
                        margin=0,
                        bgcolor=color_styles['bgcolor'],
                        expand=True  # This container will also expand to full width
                    )
                ],
                alignment=MainAxisAlignment.START,
                auto_scroll=True,
                spacing=0,
                expand=True  # Make the column take up the full available space in its parent
            ),
            # Centrally positioned content with nested container
            Container(
                alignment=alignment.Alignment(0.0, -0.9),  # Align the parent container at -0.7 vertically
                content=Container(
                    width=300,
                    height=300,
                    border_radius=35,
                    #bgcolor="purple",
                    alignment=alignment.center,  # Center aligns the child within this container
                    content=Column(
                            controls=[
                                Container(
                                    border=border.all(2, color_styles["border"]),
                                    bgcolor="yellow",
                                    width=175,
                                    height=175,
                                    border_radius=250,
                                    alignment=alignment.bottom_center,  # Center aligns content inside this child container
                                ),
                                Container(
                                    margin=margin.only(top=10),
                                    #bgcolor="green",
                                    width=140,
                                    height=30,
                                    content=Text(
                                        "Dominic Rios",
                                        text_align=TextAlign.CENTER,
                                        size=20,
                                        )
                                ),
                                Container(
                                    height=30,
                                    width=140,
                                    #bgcolor="red",
                                    content=Text(
                                        value="Joined in 2024",
                                        text_align=TextAlign.CENTER,
                                        size=12,
                                    )
                                )
                            ],
                            spacing=0,
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment="center",
                        )
                ),
                expand=False
            ),
            Container(
                bgcolor=color_styles['bgcolor'],
                border_radius=35,
                margin=10,
                width=60,
                height=60,
                border=border.all(2, color_styles["border"]),
                content=IconButton(
                    icon=icons.SETTINGS_OUTLINED,
                    icon_size=30,
                    icon_color=color_styles['icon_color'],
                    tooltip="Settings",
                    on_click=lambda e: page.go('/profile/settings'),
                    mouse_cursor=MouseCursor.CLICK,
                ),
                expand=False
            ),
        ],
        expand=True
    )
