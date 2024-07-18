import flet as ft
from flet import *
import importlib
from real.src.routes import route_config, config_page
from real.components.methods.methods import get_parent, get_route, get_title

def main(page: Page):
    page.theme_mode = "dark"

    def route_change(route):
        route_list = set(route_config.keys())
        if page.route in route_list:
            page.views.clear()
            page.title = get_title(page.route)
            
            module_path, build_func_name, page_type = route_config[page.route]

            try: 
                module = importlib.import_module(module_path)
                build_func = getattr(module, build_func_name)
                view = build_func(page.theme_mode, page)
            except (ImportError, AttributeError) as e:
                print(f"Error importing module or function: {e}")
                return

            content = config_page(page_type, view, page, page.theme_mode, page.title, get_parent(page.title))

            page.views.append(
                View(
                    f"{get_route(page.title)}",
                    [content]
                )
            )
        
        page.padding = 0
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
