import flet as ft
from flet import *


def build_home():
    return Container(
        
        Column(
            controls=[
                Container(
                    Text("Hello poop", color="blue", size=30),
                    height= 200, 
                    bgcolor="orange",
                    alignment= alignment.center,
                )
            ],
            alignment=MainAxisAlignment.START,
            expand=True  # Ensure Column takes full height available
        ),

    )