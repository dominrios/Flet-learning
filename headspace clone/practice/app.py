import flet as ft
from flet import *
import importlib
from routes import route_config


def main(page: Page):
    page.theme_mode = "dark"

    def route_change(event):
        # Ensure we get the correct route string from the event
        

        page.padding = 0
        page.update()

    page.on_route_change = route_change
    # This ensures the function is called with the correct initial route
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)


#       route = event.route  
#       page.views.clear()
#        
#        module_name, func_name = route_config.get(route, (None, None))
#        if module_name and func_name:
#            module = importlib.import_module(module_name)
#            build_func = getattr(module, func_name)
#            
#            if func_name == "build_profile" or '/settings' in route :
 #               content = build_func(page.theme_mode, page)
 #           else:
 #               content = build_func()
#            wrapped_content = wrap_page(content, page, page.theme_mode, route.split('/')[-1])
#            
#            page.views.append(View(route, [wrapped_content], padding=0))