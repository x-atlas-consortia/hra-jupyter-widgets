import traitlets as tr

from ._base import HraBaseWidget
from ._traits import Attribute, Event


class HraMedicalIllustrationWidget(HraBaseWidget):
    _tag_name = "hra-medical-illustration"
    _scripts = ["https://cdn.humanatlas.io/ui/medical-illustration/wc.js"]
    _styles = ["https://cdn.humanatlas.io/ui/medical-illustration/styles.css"]

    selected_illustration = Attribute(tr.Unicode(), help="")
    illustrations = Attribute(tr.Unicode(), help="")
    highlight = Attribute(tr.Unicode(allow_none=True), help="")

    on_cell_click = Event()
    on_cell_hover = Event()
