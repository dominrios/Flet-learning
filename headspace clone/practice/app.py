import flet as ft
from flet import *

def __view__():
    return View(
        '/index',
            controls=[
                Container(
                    width=120,
                    height=120,
                    bgcolor='blue800',
                    alignment=alignment.center,
                    content=Text("INDEX PAGE")
                ),
                FilledButton(
                    width=120,
                    height=40, 
                    on_click=lambda e: e.page.go("/about")
                )
            ]
    )





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

    def nav_routes(input):
        route_dict = {
            0 : "/",
            1 : "/explore",
            2 : "/saved"
        }
        print(route_dict[input])

    def explore_page(e):
        page.route = "/explore"
        print(page.route)

    
    page.title = "Explore!"
    sheisty = ft.CupertinoNavigationBar(
        inactive_color=colors.GREY,
        active_color=colors.BLACK,
        on_change=lambda e: nav_routes(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
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
    page.add(sheisty)



ft.app(target=main, view=WEB_BROWSER)