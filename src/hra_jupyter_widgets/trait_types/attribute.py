from __future__ import annotations

import typing as t

from traitlets import HasTraits, TraitType, Undefined, Union


class Attribute(Union):
    info_text = "an attribute"

    @property
    def attribute_name(self) -> str:
        if self.metadata["attribute_name"]:
            return self.metadata["attribute_name"]
        elif self.name:
            return self.name.replace("_", "-")
        else:
            raise AttributeError("Cannot determine an attribute_name")

    @property
    def required(self) -> bool:
        return self.metadata["required"]

    @property
    def definition(self):
        return {"name": self.attribute_name, "key": self.name}

    def __init__(
        self,
        trait: TraitType,
        default_value: t.Any = Undefined,
        attribute_name: str | None = None,
        required=False,
        allow_none=False,
        read_only: bool | None = None,
        help: str | None = None,
    ) -> None:
        super().__init__(
            [trait],
            default_value=default_value,
            allow_none=allow_none,
            read_only=read_only,
            help=help,
        )
        self.info_text = f"an attribute of {trait.info_text}"
        self.tag(
            type="attribute",
            attribute_name=attribute_name,
            required=required,
            sync=True,
        )
