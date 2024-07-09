import flet as ft
from flet import *
from modularFooter import Footer


def main(page: Page):
    footer = Footer()

    stack = Stack(
        controls=[
            Column(
                controls=[
                    Text("Hello there", color="blue", size=30),
                    Container(expand=True)  # Expand to push footer down
                ],
                expand=True,  # Ensure Column takes full height available
            ),
            Container(
                alignment=Alignment(0.0, 1.0),  # Align the footer to the bottom center
                content=footer.build_footer(),
                margin=0,  # No margin around the footer
                padding=0  # No padding around the footer
            )
        ],
        expand=True  # Ensure Stack takes full height of the page
    )

    # Add the stack to the page
    page.add(stack)
    page.padding = 0  # Remove any default page padding
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
