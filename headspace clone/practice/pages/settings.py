import flet as ft
from flet import *
from componenets.styles import get_color_styles

class Tabs:
    def __init__(self, theme, title, icon, page):
        self.title = title
        self.color_styles = get_color_styles(theme)
        self.icon = icon
        self.route = f"/profile/settings/{get_route(title)}"
        self.page = page
        

    def init_tab(self):
        return Container(
            content=Row(
                controls=[
                    Container(
                        content=Row(
                            controls=[
                                Icon(name=self.icon, color=self.color_styles['icon_color']),
                                Text(value=self.title, size=20)
                            ],
                            alignment=MainAxisAlignment.START
                        )
                    ),
                    Container(
                        Icon(name=icons.ARROW_FORWARD_IOS_ROUNDED, color=self.color_styles['icon_color'], size=20)
                    )
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=0,
            margin=margin.only(bottom=-10),
            height=50,
            bgcolor=self.color_styles['component'],
            on_click= lambda e: self.page.go(self.route)
        )

def get_route(string):
    lowered = string.casefold()
    if lowered.find(" ") == -1:
        return lowered
    else:
        route = lowered.replace(" ", "_")
        return route

def build_settings_page(theme, page):
    # ADJUST AS NEEDED FOR AS MANY TABS AS NECESSARY
    sections = [
        {
            "header": "Display",
            "tabs": [
                {"title": "Display", "icon": icons.DARK_MODE_ROUNDED},
                {"title" : "Notifications", "icon" : icons.NOTIFICATIONS_ROUNDED}
            ]
        },
        {
            "header": "Sound",
            "tabs": [
                {"title": "Volume Control", "icon": icons.VOLUME_UP_ROUNDED},
                {"title": "Mute", "icon": icons.VOLUME_OFF_ROUNDED}
            ]
        }
    ]

    controls = []

    for section in sections:
        #header
        controls.append(
            Container(
                margin=margin.only(bottom=-7, left=5, top=7),
                content=Text(section["header"], size=14, weight="bold"),
                )
            )

        for tab_info in section["tabs"]:
            tab = Tabs(theme, tab_info["title"], tab_info["icon"], page).init_tab()
            controls.append(tab)

    color_styles = get_color_styles(theme)
    return Container(
        expand=True,
        bgcolor=color_styles['bgcolor'],
        content=Container(
            content=Column(
                controls=controls,
                alignment=MainAxisAlignment.START
            ),
            border_radius=5,
        ),
        padding=padding.symmetric(horizontal=10),
        #margin=margin.symmetric(horizontal=10),
    )