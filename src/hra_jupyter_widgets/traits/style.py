from __future__ import annotations

import typing as t

import traitlets


class Style(traitlets.Unicode):
    info_text = "a style url"
    metadata = {"type": "style"}

    def __init__(
        self: Style,
        url: str | bytes,
        config: t.Any = None,
        **kwargs: t.Any,
    ) -> None:
        super().__init__(
            url,
            **kwargs,
            allow_none=False,
            read_only=True,
            help="A style sheet url used by the application",
            config=config,
        )
