import traitlets as tr

from hra_jupyter_widgets.widgets._stylesheets import (
    InterFontStylesheet,
    MaterialIconsStylesheet,
    MaterialSymbolsStylesheet,
)

from ..traits import Input, Output, Script, Style, TagName
from ._base import HraWidgetBase


class HraFtuExplorerWidget(
    HraWidgetBase,
    InterFontStylesheet,
    MaterialIconsStylesheet,
    MaterialSymbolsStylesheet,
):
    """_summary_

    Inputs:
        selected_illustration (_type_): _description_
        illustrations (_type_): _description_

    Outputs:
        on_cell_click (_type_): _description_
        on_cell_hover (_type_): _description_
    """

    _tag_name = TagName("hra-ftu-ui")
    _wc_polyfills_script = Script("https://cdn.humanatlas.io/ui/ftu-ui/polyfills.js")
    _wc_script = Script("https://cdn.humanatlas.io/ui/ftu-ui/main.js")
    _wc_stylesheet = Style("https://cdn.humanatlas.io/ui/ftu-ui/styles.css")

    selected_illustration = Input(tr.Unicode(), required=True)
    illustrations = Input(tr.Unicode())
    summaries = Input("assets/TEMP/ftu-cell-summaries.jsonld", tr.Unicode())
    datasets = Input("assets/TEMP/ftu-datasets.jsonld", tr.Unicode())
    base_href = Input("https://cdn.humanatlas.io/ui/ftu-ui/", tr.Unicode())

    on_illustration_selected = Output(
        help="Triggered when the user selects a different illustration"
    )
    on_cell_click = Output(help="Triggered when the user clicks on a cell")
    on_cell_hover = Output(
        help="Triggered when the user starts or stops hovering on a cell"
    )
