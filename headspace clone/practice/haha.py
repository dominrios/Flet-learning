import flet as ft
from flet import *
from pages.home import build_home
from pages.explore import build_explore
from pages.saved import build_saved
from pages.profile import build_profile
from componenets.modularFooter import Footer

def wrap_page(content, page, theme, focus):
    footer = Footer(page, theme, focus).build_footer()

    return Stack(
        controls=[
            Column(
                controls=[
                    content,
                    Container(expand=True),
                ],
                expand=True,  
            ),

            Container(
                alignment=Alignment(0.0, 1.0),  
                content=footer,
                margin=0,
                padding=0
            )
        ],
        expand=True,
        fit= StackFit.PASS_THROUGH,
    )


def main(page: Page):
    page.theme_mode = "dark"

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                View(
                    "/",
                    [
                        wrap_page(build_home(), page, page.theme_mode, "Home") 
                    ],
                    padding=0
                )
            )
        elif page.route == "/explore":
            page.views.append(
                View(
                    "/explore",
                    [
                        wrap_page(build_explore(), page, page.theme_mode, "Explore")  # 
                    ],
                    padding=0
                )
            )
        elif page.route == "/saved":
            page.views.append(
                View(
                    "/saved",
                    [
                        wrap_page(build_saved(), page, page.theme_mode, "Saved")  
                    ],
                    padding=0
                )
            )
        elif page.route == "/profile":
            page.views.append(
                View(
                    "/profile",
                    [
                        wrap_page(build_profile(), page, page.theme_mode, "Profile")  
                    ],
                    padding=0
                )
            )
        page.padding  =0 
        page.update()

    page.on_route_change = route_change
    page.go(page.route)
    page.padding = 0  
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
