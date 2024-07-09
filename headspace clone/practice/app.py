import flet as ft
from flet import *

def create_card(title, subtitle, bgcolor):
    return Card(
        content=Container(
            bgcolor=bgcolor,
            content=Column(
                [
                    ListTile(
                        leading=Icon(icons.ALBUM),
                        title=Text(title),
                        subtitle=Text(subtitle),
                    ),
                ]
            ),
            width=400,
            padding=10,
            border_radius=100,
        )
    )


def nav_routes(input, page):
    route_dict = {
        0: "/",
        1: "/explore",
        2: "/saved"
    }
    var = route_dict[input]
    print(var)
    
    if var not in [view.route for view in page.views]:  # Avoid duplicate views in stack
        page.views.clear()
        if var == "/explore":
            page.views.append(explore_page(page))
        elif var == "/saved":
            page.views.append(saved_page(page))
        else:
            page.views.append(home_page(page))
    
    # Update the page route
    page.route = var
    page.update()

def explore_page(page):
    return View(
        "/explore",
        controls=[
            create_navigation_bar(page, 1),
            Text("Explore page"),
        ]
    )

def saved_page(page):
    return View(
        "/saved",
        controls=[
            create_navigation_bar(page, 2),
            Text("Saved page"),
            ElevatedButton(bgcolor="PINK", on_click=(zoo_zree())),
            Text(f"{static}"),
        ],
    )

def zoo_zree():
    global static
    static =+ 1
    print(static)

def home_page(page):
    return View(
        "/",
        horizontal_alignment=CrossAxisAlignment.CENTER,
        controls=[
            create_navigation_bar(page, 0),
            Text("Home page"),
            Column(
                width = 420,
                controls=[create_card("A Great Chaos", "Album by Ken Carson", "BLUE")]
            )
        ]
    )

def create_navigation_bar(page, selected_index):
    return ft.CupertinoNavigationBar(
        inactive_color=colors.GREY,
        active_color=colors.BLACK,
        selected_index=selected_index,
        on_change=lambda e: nav_routes(e.control.selected_index, page),
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

def main(page: ft.Page):
    page.theme_mode = "dark"
    print(page.theme_mode)
    page.title = "Home"
    
    global BLUE
    PINK = '#f160b7'
    BLUE = '#6fdfd8'

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER    
    home_view = home_page(page)
    page.views.append(home_view)
    page.update()


static = 0


ft.app(target=main)
