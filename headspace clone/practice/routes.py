# routes.py
route_config = {
    "/": ("pages.home", "build_home"),
    "/explore": ("pages.explore", "build_explore"),
    "/saved": ("pages.saved", "build_saved"),
    "/profile": ("pages.profile", "build_profile"),
    "/profile/settings": ("pages.settings", "build_settings_page"),
    "/profile/settings/display": ("pages.settings_pages.display", "build_display_page"),
    # Add more routes as needed
}
