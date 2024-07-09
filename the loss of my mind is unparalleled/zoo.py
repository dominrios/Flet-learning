import flet as ft
from flet import (
    Page, Column, Container, Row, MainAxisAlignment, CrossAxisAlignment, LinearGradient, alignment, transform, animation, IconButton, icons
)
import time

class MainPage:
    def __init__(self):
        self._main_row = None
        self._icon_list = [
            icons.EXPLORE_SHARP,
            icons.HOME_ROUNDED,
            icons.SEARCH_ROUNDED,
            icons.FAVORITE_ROUNDED,
            icons.NOTIFICATION_ADD_ROUNDED,
            icons.BOOKMARK_OUTLINE_ROUNDED
        ]

    def _animate_icon(self, e):
        e.control.scale = transform.Scale(0.65)
        e.control.update()
        time.sleep(0.15)
        e.control.scale = transform.Scale(1)
        e.control.update()

        for control in self._main_row.content.controls[:]:
            control.content.selected = False
            control.content.icon_color = "white54"
            control.content.update()

            if e.control.content.selected != True:
                e.control.content.selected = True
                e.control.content.icon_color = "white"
                e.control.content.update()

    def build_page(self, page: Page):
        # title
        page.title = "Flet Animated Icons"

        # alignment
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"

        # main row
        self._main_row = Container(
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[],
            ),
        )

        for icon in self._icon_list:
            __ = Container(
                on_click=lambda e: self._animate_icon(e),
                animate_scale=animation.Animation(duration=500, curve="bounceOut"),
                scale=transform.Scale(1),
                content=IconButton(
                    icon=icon,
                    icon_size=32,
                    icon_color="white54",
                    selected=False,
                ),
            )
            self._main_row.content.controls.append(__)

            if icon == icons.DISCORD_ROUNDED:
                __.content.icon_color, __.content.selected = "white", True

        # main container
        _main_container = Container(
            width=580,
            height=260,
            rotate=transform.Rotate(0, alignment=alignment.center),
            animate_rotation=animation.Animation(duration=500, curve="decelerate"),
            border_radius=35,
            bgcolor="black",
            alignment=alignment.bottom_center,
            padding=20,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self._main_row,
                ],
            ),
        )

        page.add(
            Container(
                width=1400,
                height=800,
                gradient=LinearGradient(
                    begin=alignment.bottom_left,
                    end=alignment.top_right,
                    colors=["black", "blue100"],
                ),
                padding=50,
                content=Column(
                    alignment="end",
                    horizontal_alignment="center",
                    controls=[_main_container],
                ),
            )
        )
        page.update()

def main(page: Page):
    main_page = MainPage()
    main_page.build_page(page)

if __name__ == "__main__":
    ft.app(target=main)
