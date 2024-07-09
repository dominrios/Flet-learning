import flet as ft
from flet import *

class Footer:
    def __init__(self, page, theme, focus):
        self.page = page
        self.icon_list = {
            icons.HOME_OUTLINED: ["/", "Home"],
            icons.EXPLORE_OUTLINED: ["/explore", "Explore"],
            icons.BOOKMARK_OUTLINE_ROUNDED: ["/saved", "Saved"],
            icons.PERSON_OUTLINE_ROUNDED: ["/profile", "Profile"]
        }
        self.color_styles = {
            "border" : "#e8e8e8" if theme == "light" else "#32344B",
            "icon_color" : "#e8e8e8" if theme == "light" else "#e5e7eb",
            "bgcolor" : "#ffffff" if theme == "light" else "#050624",
            "active" : "black" if theme == "light" else "#f7d046"
        }
        self.focus = focus

    def build_button(self, input_icon):
        hoverClr = self.color_styles["active"]
        activity = self.color_styles["icon_color"]
        if self.icon_list[input_icon][1] == self.focus:
            activity = self.color_styles["active"]
            hoverClr = self.color_styles["bgcolor"]

        
        return IconButton(
            icon=input_icon,
            icon_color=activity,
            hover_color=hoverClr,
            icon_size=30,
            mouse_cursor=MouseCursor.CLICK,
            tooltip=self.icon_list[input_icon][1],
            on_click=lambda e: self.page.go(self.icon_list[input_icon][0])
        )

    def build_footer(self):
        buttons = []
        for icon in self.icon_list:
            buttons.append(self.build_button(icon))
        return Container(
            bgcolor=self.color_styles["bgcolor"],
            padding=10,
            border= border.only(top=border.BorderSide(4,self.color_styles["border"])),
            content=Row(
                controls=buttons,
                alignment=MainAxisAlignment.SPACE_AROUND,
            ),
            expand=True,
        )
