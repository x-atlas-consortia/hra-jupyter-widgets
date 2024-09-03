import pathlib
import typing as t

import anywidget
from traitlets import Bytes, Unicode

STATIC_DIR = pathlib.Path(__file__).resolve().parent.parent / "static"


class ModelViewer(anywidget.AnyWidget):
    _esm = STATIC_DIR / "model_viewer.js"
    _css = STATIC_DIR / "model_viewer.css"

    height = Unicode(None, allow_none=True).tag(sync=True)
    width = Unicode(None, allow_none=True).tag(sync=True)

    src = Unicode(None, allow_none=True).tag(sync=True)
    data = Bytes(None, allow_none=True).tag(sync=True)

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        if "src" not in kwargs and "data" not in kwargs:
            raise AttributeError("Must provide either 'src' or 'data'")
        super().__init__(*args, **kwargs)
