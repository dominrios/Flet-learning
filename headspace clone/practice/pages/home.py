from flet import *
from componenets.gradial_background import Background


def build_home(theme):
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