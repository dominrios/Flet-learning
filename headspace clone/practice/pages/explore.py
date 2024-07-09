import flet as ft
from flet import *


def build_explore():
    return Container(
        
        Column(
            controls=[
                Container(
                    Text("explorethe orld", color="blue", size=30),
                    height= 200,
                    bgcolor="orange"
                )
            ],
            alignment=MainAxisAlignment.START,
            expand=True  # Ensure Column takes full height available
        ),

    )