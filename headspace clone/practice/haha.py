import flet as ft
from flet import *
from pages.home import build_home
from pages.explore import build_explore
from pages.saved import build_saved
from pages.profile import build_profile
from componenets.modularFooter import Footer
from componenets.backHeader import BackHeader

def wrap_page(content, page, theme, focus):
    footer = Footer(page, theme, focus).build_footer()

    return Column(
        controls=[
            content,
            Container(
                height=90,
                bgcolor="yellow",
                content=footer,
                expand=False  # Ensure this container does not expand
            )
        ],
        expand=True,
        alignment=MainAxisAlignment.SPACE_BETWEEN,
    )

def wrap_sub_page(content, page, theme):
    header = BackHeader.build_header(theme)

    return Column(
        controls=[
            Container(
                height=90,
                bgcolor="yellow",
                content=header,
                expand=False  # Ensure this container does not expand
            ),
            content,
        ],
        expand=True,
        alignment=MainAxisAlignment.SPACE_BETWEEN,
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
                        wrap_page(build_profile(page.theme_mode), page, page.theme_mode, "Profile")  
                    ],
                    padding=0
                )
            )
        elif page.route == "/profile/settings":
            page.views.append(
                View(
                    "/profile/settings",
                    [
                        wrap_sub_page(build_profile(), page, page.theme_mode)  
                    ],
                    padding=0
                )
            )
        page.padding = 0
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
