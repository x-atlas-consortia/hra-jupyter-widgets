import traitlets as tr

from ._base import HraBaseWidget
from ._traits import Attribute, Event
from ._stylesheets import FONTS, MATERIAL


class HraFtuExplorerWidget(HraBaseWidget):
    _tag_name = "hra-ftu-ui"
    _scripts = [
        "https://cdn.humanatlas.io/ui/ftu-ui/polyfills.js",
        "https://cdn.humanatlas.io/ui/ftu-ui/main.js",
    ]
    _styles = [*FONTS, *MATERIAL, "https://cdn.humanatlas.io/ui/ftu-ui/styles.css"]

    _base_href = Attribute(
        tr.Unicode("https://cdn.humanatlas.io/ui/ftu-ui/"), attribute_name="base-href"
    )

    selected_illustration = Attribute(tr.Unicode(), help="")
    illustrations = Attribute(tr.Unicode(None, allow_none=True), help="")
    summaries = Attribute(tr.Unicode("assets/TEMP/ftu-cell-summaries.jsonld"), help="")
    datasets = Attribute(tr.Unicode("assets/TEMP/ftu-datasets.jsonld"), help="")

    on_illustration_selected = Event()
    on_cell_click = Event()
    on_cell_hover = Event()
