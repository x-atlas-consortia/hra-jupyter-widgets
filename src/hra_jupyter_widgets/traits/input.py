from __future__ import annotations

import typing as t

import traitlets as tr

G = t.TypeVar("G")
S = t.TypeVar("S")


class Input(tr.TraitType[G, S]):
    info_text = "an input value"
    metadata = {"type": "input", "sync": True}

    if t.TYPE_CHECKING:

        @t.overload
        def __init__(
            self: Input[G, S],
            default_value: S,
            trait: tr.TraitType[G, S] | None = ...,
            attribute: str | None = ...,
            required: t.Literal[False] = ...,
            help: str | None = ...,
            config: t.Any = ...,
        ) -> None: ...

        @t.overload
        def __init__(
            self: Input[G | None, S],
            trait: tr.TraitType[G, S] | None = ...,
            attribute: str | None = ...,
            required: bool = ...,
            help: str | None = ...,
            config: t.Any = ...,
        ) -> None: ...

    def __init__(
        self: Input[G, S],
        default_value: S | tr.TraitType[G, S] | None = None,
        trait: tr.TraitType[G, S] | None = None,
        attribute: str | None = None,
        required: bool = False,
        help: str | None = None,
        config: t.Any = None,
        **kwargs: t.Any,
    ) -> None:
        if trait is None and isinstance(default_value, tr.TraitType):
            trait = default_value
            default_value = None

        if trait is not None:
            trait.allow_none = True
            trait.read_only = False

        super().__init__(
            default_value,
            **kwargs,
            allow_none=True,
            read_only=False,
            help=help,
            config=config,
        )

        self.trait = trait
        self.attribute = attribute
        self.required = self.metadata["required"] = required

    def validate(self, obj: t.Any, value: t.Any) -> G | None:
        if self.trait is None:
            return t.cast(G, value)
        try:
            return self.trait._validate(obj, value)
        except tr.TraitError as error:
            self.error(obj, value, error)

    def class_init(self, cls: type[tr.HasTraits], name: str | None) -> None:
        if self.attribute is None and name is not None:
            self.attribute = name.replace("_", "-")
        if self.trait is not None:
            self.trait.class_init(cls, None)
        super().class_init(cls, name)

    def subclass_init(self, cls: type[tr.HasTraits]) -> None:
        if self.trait is not None:
            self.trait.subclass_init(cls)

    def from_string(self, s: str) -> G | None:
        return (
            super().from_string(s) if self.trait is None else self.trait.from_string(s)
        )
