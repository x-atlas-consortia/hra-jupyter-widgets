from __future__ import annotations

import typing as t

from traitlets import Integer, List, Unicode

from ._base import HraBaseWidget
from ._traits import Attribute


class NodeDistVis(HraBaseWidget):
    _tag_name = "hra-node-dist-vis"
    _scripts = [
        "https://cdn.jsdelivr.net/gh/cns-iu/hra-node-dist-vis/docs/hra-node-dist-vis.wc.js"
    ]
    _styles = []

    _max_height = "600px"

    nodes = Attribute(Unicode() | List(), required=True)
    node_target_key = Attribute(Unicode(), required=True)
    node_target_value = Attribute(Unicode(), required=True)
    edges = Attribute(Unicode(None, allow_none=True) | List())
    max_edge_distance = Attribute(Integer())
    color_map = Attribute(Unicode(None, allow_none=True) | List())
    color_map_key = Attribute(Unicode(None, allow_none=True))
    color_map_data = Attribute(Unicode(None, allow_none=True))
    selection = Attribute(List(default_value=None, allow_none=True))

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        if "edges" not in kwargs and "max_edge_distance" not in kwargs:
            raise AttributeError(
                "max_edge_distance must be set when not providing edges"
            )

        super().__init__(*args, **kwargs)
