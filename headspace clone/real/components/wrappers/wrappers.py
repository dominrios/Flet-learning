from flet import Column, MainAxisAlignment, Container
from components.modular_components.modularFooter import Footer
from components.modular_components.backHeader import BackHeader

#                                     title
def encase_page(content, page, theme, focus, title="Title", parent="Parent"):
    footer = Footer(page, theme, focus).build_footer()
    header = BackHeader(theme, title, parent, page)

    return Column(
        controls=[
            Container(
                height=90,
                content=header,
                expand=False,
            ),
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

#                                        title
def wrap_main_page(content, page, theme, focus):
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