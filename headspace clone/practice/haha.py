import flet as ft
from flet import *
from pages.home import build_home
from pages.explore import build_explore
from pages.saved import build_saved
from pages.profile import build_profile
from pages.settings import build_settings_page
from pages.settings_pages.display import build_display_page
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

def wrap_sub_page(content, page, theme, title="Title", parent="Parent"):
    header = BackHeader(theme, title, parent, page).build_header()

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
            page.title = "Home"
            page.views.append(
                View(
                    "/",
                    [
                        wrap_page(build_home(page.theme_mode), page, page.theme_mode, "Home") 
                    ],
                    padding=0
                )
            )
        elif page.route == "/explore":
            page.title = "Explore"
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
            page.title = "Saved"
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
            page.title = "Profile"
            page.views.append(
                View(
                    "/profile",
                    [
                        wrap_page(build_profile(page.theme_mode,page), page, page.theme_mode, "Profile")  
                    ],
                    padding=0
                )
            )
        elif page.route == "/profile/settings":
            page.title= "Settings"
            page.views.append(
                View(
                    "/profile/settings",
                    [
                        wrap_sub_page(build_settings_page(page.theme_mode, page), page, page.theme_mode, "Settings", "profile")
                    ],
                    padding=0,
                )
            )
        elif page.route == "/profile/settings/display":
            page.title= "Display"
            page.views.append(
                View(
                    "/profile/settings/display",
                    [
                        wrap_sub_page(build_display_page(page.theme_mode, page), page, page.theme_mode, "Display", "profile/settings")
                    ],
                    padding=0,
                )
            )
        page.padding = 0
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
