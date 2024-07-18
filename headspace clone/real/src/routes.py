import components.wrappers.wrappers as wrapper


route_config = {
    "/": ("pages.home", "build_home", "main"),
    "/explore": ("pages.explore", "build_explore", "main"),
    "/saved": ("pages.saved", "build_saved", "main"),
    "/profile": ("pages.profile", "build_profile", "main"),
    "/profile/settings": ("pages.settings", "build_settings_page", "sub"),
    "/profile/settings/display": ("pages.settings_pages.display", "build_display_page", "sub"),
}

def config_page(page_type, content, page, theme, focus, title="Title", parent="Parent"):
    if page_type == "main":
        return wrapper.wrap_main_page(content, page, theme, focus)
    elif page_type == "sub":
        return wrapper.wrap_sub_page(content, page, theme, title, parent)
    elif page_type == "enc":
        return wrapper.encase_page(content, page, theme, title, parent)
