import flet as ft
from flet import *


def build_profile():
    return Container(
        
        Column(
            controls=[
                Container(
                    Text("Hello this is your profile", color="blue", size=30),
                    height= 200,
                    bgcolor="orange",
                    alignment = alignment.center,
                )
            ],
            alignment=MainAxisAlignment.START,
            expand=True  # Ensure Column takes full height available
        ),

    )