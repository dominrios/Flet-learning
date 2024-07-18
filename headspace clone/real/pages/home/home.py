from flet import *
from components.templates.gradial_background import Background


def build_home(theme, page):
    z = page
    bg = Background(theme).build_background()
    print(f"Background: {bg}")

    col = Column(
        controls=[
            bg
        ],
        expand=True
    )
    print(f"Column: {col}")

    return Stack(
        controls=[
            col,
        ],
        expand=True,
        alignment=alignment.center,
    )