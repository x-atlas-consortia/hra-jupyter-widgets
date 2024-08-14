from __future__ import annotations

import typing as t

import traitlets


class Script(traitlets.Unicode):
    info_text = "a script url"
    metadata = {"type": "script"}

    def __init__(
        self: Script,
        url: str | bytes,
        config: t.Any = None,
        **kwargs: t.Any,
    ) -> None:
        super().__init__(
            url,
            **kwargs,
            allow_none=False,
            read_only=True,
            help="A javascript url used by the application",
            config=config,
        )
