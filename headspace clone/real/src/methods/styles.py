#styles for the themes and such


def get_color_styles(theme):
    """
    Return color styles based on the theme.
    """
    return {
        "border": "#cdcdcd" if theme == "light" else "#32344B",
        "icon_color": "black" if theme == "light" else "white",
        "bgcolor": "#e8e8e8" if theme == "light" else "#050624",
        "active": "black" if theme == "light" else "#f7d046",
        "gradient": ["#fff6e4","#e8e8e8"] if theme == "light" else ["#6000a3","#050624"],
        "component" : "#e7e3d8" if theme =="light" else "#10103d",
        "text" : "black" if theme =="light" else "white",
        "footer_icon_color": "#c0c0c0" if theme == "light" else "#e5e7eb",
    }