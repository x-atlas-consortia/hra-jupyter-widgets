from __future__ import annotations

import typing as t

import traitlets


class TagName(traitlets.Unicode):
    info_text = "a html tag name"
    metadata = {"type": "tag_name"}

    def __init__(
        self: TagName,
        tag_name: str | bytes,
        config: t.Any = None,
        **kwargs: t.Any,
    ) -> None:
        super().__init__(
            tag_name,
            **kwargs,
            allow_none=False,
            read_only=True,
            help="The application's html tag name",
            config=config,
        )
