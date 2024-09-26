from traitlets import Bool, Dict, Enum, List, Unicode

from ..trait_types import Attribute, Event
from ._stylesheets import Font, Material
from .hra_app import HraAppIframeWidget

_DEFAULT_BASE_HREF = "https://cdn.humanatlas.io/ui/ccf-rui/"
_DEFAULT_THEME = "hubmap"


class Rui(HraAppIframeWidget):
    _tag_name = "ccf-rui"
    _scripts = ["https://cdn.humanatlas.io/ui/ccf-rui/wc.js"]
    _styles = [
        Font.Inter,
        Material.Icons,
        "https://cdn.humanatlas.io/ui/ccf-rui/styles.css",
    ]

    _base_href = Attribute(Unicode(_DEFAULT_BASE_HREF, read_only=True))
    _skip_unsaved_changes_confirmation = Attribute(Bool(True, read_only=True))
    # TODO: _logo_tooltip - Maybe set to empty string

    use_download = Attribute(Bool(False))
    reference_data = Attribute(Unicode(None, allow_none=True))
    user = Attribute(Dict(default_value=None, allow_none=True))  # TODO improve type
    organ = Attribute(Dict(default_value=None, allow_none=True))  # TODO improve type
    edit_registration = Attribute(
        Dict(default_value=None, allow_none=True)
    )  # TODO improve type
    theme = Attribute(Unicode(_DEFAULT_THEME))
    header = Attribute(Bool(False))
    home_url = Attribute(Unicode(None, allow_none=True))  # TODO maybe empty string?
    organ_options = Attribute(List(Unicode(), default_value=None, allow_none=True))
    collisions_endpoint = Attribute(Unicode(None, allow_none=True))
    view = Attribute(Enum(["register", "3d"], default_value=None, allow_none=True))
    view_side = Attribute(
        Enum(
            ["left", "right", "anterior", "posterior"],
            default_value=None,
            allow_none=True,
        )
    )

    # TODO: register - Turn into an output in ccf-rui
    on_registration = Event(event_name="register")
    # TODO: cancelRegistration - Turn into an output in ccf-rui
    on_cancel_registration = Event(event_name="cancelRegistration")
