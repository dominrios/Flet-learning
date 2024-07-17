from pages.home import build_home
from pages.explore import build_explore
from pages.saved import build_saved
from pages.profile import build_profile
from pages.settings import build_settings_page

ROUTES =  {
    "/": ["main",build_home],
    "/explore": ["main",build_explore],
    "/saved": ["main",build_saved],
    "/profile": ["main",build_profile],
    "/profile/settings": ["sub",build_settings_page]
}