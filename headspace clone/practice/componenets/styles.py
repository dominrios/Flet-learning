#styles for the themes and such


def get_color_styles(theme):
    """
    Return color styles based on the theme.
    """
    return {
        "border": "#e8e8e8" if theme == "light" else "#32344B",
        "icon_color": "#c0c0c0" if theme == "light" else "#e5e7eb",
        "bgcolor": "#f8f9ff" if theme == "light" else "#050624",
        "active": "black" if theme == "light" else "#f7d046",
        "gradient": ["#ffffff","#f8f9ff"] if theme == "light" else ["black","#050624"],
        "component" : "#797877" if theme =="light" else "#10103d"
    }