import traitlets as tr

from ..traits import Input, Output, Script, Style, TagName
from ._base import HraWidgetBase


class HraMedicalIllustrationWidget(HraWidgetBase):
    """_summary_

    Inputs:
        selected_illustration (_type_): _description_
        illustrations (_type_): _description_
        highlight (_type_): _description_

    Outputs:
        on_cell_click (_type_): _description_
        on_cell_hover (_type_): _description_
    """

    _tag_name = TagName("hra-medical-illustration")
    _wc_script = Script("https://cdn.humanatlas.io/ui/medical-illustration/wc.js")
    _wc_stylesheet = Style("https://cdn.humanatlas.io/ui/medical-illustration/styles.css")

    selected_illustration = Input(tr.Unicode(), required=True)
    illustrations = Input(tr.Unicode(), required=True)
    highlight = Input(tr.Unicode())

    on_cell_click = Output(help="Triggered when the user clicks on a cell")
    on_cell_hover = Output(
        help="Triggered when the user starts or stops hovering on a cell"
    )
