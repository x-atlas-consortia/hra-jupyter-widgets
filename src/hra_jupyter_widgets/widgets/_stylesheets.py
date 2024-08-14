import traitlets

from ..traits import Style


class InterFontStylesheet(traitlets.HasTraits):
    _inter_font_stylesheet = Style(
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&display=swap"
    )


class MaterialIconsStylesheet(traitlets.HasTraits):
    _material_icons_stylesheet = Style(
        "https://fonts.googleapis.com/icon?family=Material+Icons|Material+Icons+Outlined"
    )


class MaterialSymbolsStylesheet(traitlets.HasTraits):
    _material_symbols_stylesheet = Style(
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    )
