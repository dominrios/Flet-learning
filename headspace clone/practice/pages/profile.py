import flet as ft
from flet import *
from componenets.styles import get_color_styles

def build_profile(theme):
    color_styles = get_color_styles(theme)
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
                alignment=alignment.Alignment(0.0, -0.7),  # Align the parent container at -0.7 vertically
                content=Container(
                    width=300,
                    height=300,
                    border_radius=35,
                    bgcolor="purple",
                    alignment=alignment.center,  # Center aligns the child within this container
                    content=
                    
                    Container(
                        bgcolor="yellow",
                        width=50,
                        height=50,
                        border_radius=250,
                        alignment=alignment.center,  # Center aligns content inside this child container
                    )
                
                
                ),
                expand=False  # Allow the parent container to size itself without expanding
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
                    on_click=lambda e: print("hello world"),
                    mouse_cursor=MouseCursor.CLICK,
                ),
                expand=False  # The floating button does not require expanding
            ),
        ],
        expand=True  # Ensure the stack itself takes up the full width available
    )
