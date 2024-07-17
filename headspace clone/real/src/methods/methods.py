from flet import *

def capitalize_first_string(string):
    if len(string) == 0:
        print("hey theres an error somewhere")
        return string
    return string[0].upper() + string[1:]


def get_route(string):
    lowered = string.casefold()
    if lowered.find(" ") == -1:
        return lowered
    else:
        route = lowered.replace(" ", "_")
        return route