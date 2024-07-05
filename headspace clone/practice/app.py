import flet as ft
from flet import *

def __view__():
    pass





def main(page: ft.Page):
    def something():
        one= Card(
            content=Container(
                bgcolor= BLUE,
                border_radius= 100,
                content=Column(
                    [
                        ListTile(
                            leading=Icon(icons.ALBUM),
                            title=Text("A Great Chaos Delux"),
                            subtitle=Text("Music by Kitty Carson"),
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
        page.add(one)
    
    page.title = "Explore!"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Saved",
            ),
        ]
    
    )

    PINK = '#f160b7'
    BLUE = '#6fdfd8'


    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.Text("New music for you~!"))
    something()



ft.app(target=main, view=WEB_BROWSER)