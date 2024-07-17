import flet as ft 
from flet import * 
from componenets.styles import get_color_styles
from componenets.methods import capitalize_first_string

class BackHeader:
    def __init__(self, theme, title, parent, page):
        self.title = title
        self.page = page
        self.color_styles = get_color_styles(theme)
        self.route = f"/{parent}/{capitalize_first_string(title)}"
        self.back = f"/{parent}"

    def build_header(self):
        return Container(
            height=30,
            bgcolor= self.color_styles['bgcolor'],
            alignment=alignment.top_center,
            padding=0,
            margin=0,
            border=border.only(bottom=BorderSide(4, self.color_styles['border'])),
            content=Row(
                controls=[
                    Container(
                        content=IconButton(
                            icon=icons.ARROW_BACK_IOS_NEW_ROUNDED,
                            icon_size= 30,
                            icon_color=self.color_styles['icon_color'],
                            tooltip="Back",
                            on_click=lambda e: self.page.go(self.back)),
                    ),
                    Container(expand=True),  # This empty container expands to fill available space
                    Container(
                        content=ft.Text(f"{self.title}", color=self.color_styles['text'], size=24),
                        alignment=alignment.center,
                    ),
                    Container(width=200, expand=True)  # This empty container expands to fill available space after the centered content
                ],
                alignment=MainAxisAlignment.START,
                vertical_alignment=MainAxisAlignment.CENTER,
                expand=True  # Ensure the row takes up the full width available
            )
        )