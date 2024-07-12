import flet as ft 
from flet import * 
from componenets.styles import get_color_styles

def build_display_page(theme, page):
    color_styles = get_color_styles(theme)

    return Container(
        expand=True,
        bgcolor="orange"
    )