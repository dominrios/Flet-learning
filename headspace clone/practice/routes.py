from pages.home import build_home
from pages.explore import build_explore
from pages.saved import build_saved
from pages.profile import build_profile
from pages.settings import build_settings_page

ROUTES =  {
    "/": build_home,
    "/explore": build_explore,
    "/saved": build_saved,
    "/profile": build_profile,
    "/profile/settings": build_settings_page
}