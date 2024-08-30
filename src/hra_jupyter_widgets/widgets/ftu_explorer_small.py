from traitlets import Unicode

from ._base import HraBaseWidget
from ._stylesheets import Font, Material
from ._traits import Attribute, Event

_DEFAULT_BASE_HREF = "https://cdn.humanatlas.io/ui/ftu-ui-small-wc/"
_DEFAULT_SUMMARIES = "assets/TEMP/ftu-cell-summaries.jsonld"
_DEFAULT_DATASETS = "assets/TEMP/ftu-datasets.jsonld"


class FtuExplorerSmall(HraBaseWidget):
    _tag_name = "hra-ftu-ui-small"
    _scripts = ["https://cdn.humanatlas.io/ui/ftu-ui-small-wc/wc.js"]
    _styles = [
        Font.Inter,
        *Material,
        "https://cdn.humanatlas.io/ui/ftu-ui-small-wc/styles.css",
    ]

    _base_href = Attribute(Unicode(_DEFAULT_BASE_HREF, read_only=True))

    selected_illustration = Attribute(Unicode(None, allow_none=True), help="")
    illustrations = Attribute(Unicode(None, allow_none=True), help="")
    summaries = Attribute(Unicode(_DEFAULT_SUMMARIES), help="")
    datasets = Attribute(Unicode(_DEFAULT_DATASETS), help="")

    on_illustration_selected = Event()
    on_cell_click = Event()
    on_cell_hover = Event()
