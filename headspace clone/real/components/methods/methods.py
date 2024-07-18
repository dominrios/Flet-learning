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
    
def get_title(string):
    if string =="/":
        return "Home"
    else:
        last_slash = string.rfind("/")
        title = string[last_slash + 1:]
        return capitalize_first_string(title)
        
def get_parent(string):
    if string.count("/") == 1:
        return False
    else:
        last_slash = string.rfind("/")
        parent = string[:last_slash]
        return parent
