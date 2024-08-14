from __future__ import annotations

import pathlib

import anywidget
import traitlets

_root_path = pathlib.Path(__file__).parent.parent


class HraWidgetBase(anywidget.AnyWidget):
    _esm = _root_path / "static" / "widget.js"
    _css = _root_path / "static" / "widget.css"

    _application = traitlets.Dict().tag(sync=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._application = {
            "tag_name": self.__get_tag_name(),
            "scripts": self.__get_scripts(),
            "styles": self.__get_styles(),
            "inputs": self.__get_inputs(),
            "outputs": self.__get_outputs(),
        }

        missing_inputs = []
        for name in self.traits(type="input", required=True):
            if name not in kwargs:
                missing_inputs.append(name)

        if missing_inputs:
            print("Missing values for required inputs:", missing_inputs)

    def __get_tag_name(self) -> str:
        return list(self.trait_values(type="tag_name").values())[0]

    def __get_scripts(self) -> list[str]:
        return list(self.trait_values(type="script").values())

    def __get_styles(self) -> list[str]:
        return list(self.trait_values(type="style").values())

    def __get_inputs(self) -> dict[str, str]:
        return {
            name: trait.attribute for name, trait in self.traits(type="input").items()
        }

    def __get_outputs(self) -> list[str]:
        return [trait.event_name for trait in self.traits(type="output").values()]
