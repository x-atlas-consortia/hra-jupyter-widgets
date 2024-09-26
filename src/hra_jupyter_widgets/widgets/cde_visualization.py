import json

from traitlets import Dict, Float, Integer, List, Unicode

from ..trait_types import Attribute, Event
from .hra_app import HraAppIframeWidget


def _as_string_or_json(value, _widget) -> str:
    return value if value is None or isinstance(value, str) else json.dumps(value)


class CdeVisualization(HraAppIframeWidget):
    _tag_name = "cde-visualization"
    _scripts = [
        "https://cdn.humanatlas.io/ui/cde-visualization-wc/polyfills.js",
        "https://cdn.humanatlas.io/ui/cde-visualization-wc/main.js",
    ]
    _styles = ["https://cdn.humanatlas.io/ui/cde-visualization-wc/styles.css"]

    nodes = Attribute(Unicode() | List(), required=True).tag(to_json=_as_string_or_json)
    node_target_key = Attribute(Unicode(None, allow_none=True))
    node_target_value = Attribute(Unicode(None, allow_none=True))
    edges = Attribute(Unicode(None, allow_none=True) | List()).tag(
        to_json=_as_string_or_json
    )
    max_edge_distance = Attribute(Integer(None, allow_none=True))
    color_map = Attribute(Unicode(None, allow_none=True) | List())
    color_map_key = Attribute(Unicode(None, allow_none=True))
    color_map_value_key = Attribute(Unicode(None, allow_none=True))
    metadata = Attribute(Unicode(None, allow_none=True) | Dict())
    title = Attribute(Unicode(None, allow_none=True))
    organ = Attribute(Unicode(None, allow_none=True))
    technology = Attribute(Unicode(None, allow_none=True))
    sex = Attribute(Unicode(None, allow_none=True))
    age = Attribute(Integer(None, allow_none=True))
    thickness = Attribute(Float(None, allow_none=True))
    pixel_size = Attribute(Integer(None, allow_none=True))
    creation_timestamp = Attribute(Integer(None, allow_none=True))

    on_node_click = Event(event_name="nodeClick")
    on_node_hover = Event(event_name="nodeHover")
