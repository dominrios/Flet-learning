import flet as ft
from flet import *

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
#def create_navigation_bar(page, selected_index):
#    return ft.CupertinoNavigationBar(
#        inactive_color=colors.GREY,
#        active_color=colors.BLACK,
#        selected_index=selected_index,
#        on_change=lambda e: nav_routes(e.control.selected_index, page),
#        destinations=[
#            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
#            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
#            ft.NavigationBarDestination(
#                icon=ft.icons.BOOKMARK_BORDER,
#                selected_icon=ft.icons.BOOKMARK,
#                label="Saved",
  #          ),
 #       ]
#    )

def main(page:Page):
    

    pass

ft.app(target=main)