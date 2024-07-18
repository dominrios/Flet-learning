import flet as ft
from flet import *


def build_saved(theme, page):
    return Container(
        
        Column(
            controls=[
                Container(
                    Text("what you got saved in here little guy", color="blue", size=30),
                    height= 200,
                    bgcolor="orange"
                )
            ],
            alignment=MainAxisAlignment.START,
            expand=True  # Ensure Column takes full height available
        ),

    )