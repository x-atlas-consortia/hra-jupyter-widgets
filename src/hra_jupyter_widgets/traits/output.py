from __future__ import annotations

import typing as t

import ipywidgets
import traitlets

OutputListener = t.Callable[[t.Any], t.Any]


class OutputListenerHandler:
    def __init__(self, event_name: str, widget: ipywidgets.Widget) -> None:
        self.event_name = event_name
        self.dispatcher = ipywidgets.CallbackDispatcher()
        widget.on_msg(self.__handle_msg)

    def __call__(self, callback: OutputListener, remove=False) -> None:
        self.dispatcher.register_callback(callback, remove)

    def __handle_msg(
        self, _widget: ipywidgets.Widget, content: t.Any, _buffers: t.Any
    ) -> None:
        if self.__should_handle_msg(content):
            self.dispatcher(content["data"])

    def __should_handle_msg(self, content: t.Any) -> bool:
        return (
            isinstance(content, dict)
            and "event" in content
            and "data" in content
            and content["event"] == self.event_name
        )


class Output(
    traitlets.TraitType[OutputListenerHandler, OutputListenerHandler],
):
    info_text = "an output handler"
    metadata = {"type": "output"}

    def __init__(
        self: Output,
        event_name: str | None = None,
        help: str | None = None,
        config: t.Any = None,
        **kwargs: t.Any,
    ) -> None:
        super().__init__(
            **kwargs,
            allow_none=False,
            read_only=True,
            help=help,
            config=config,
        )
        self.event_name = event_name

    def class_init(self, cls: type[traitlets.HasTraits], name: str | None) -> None:
        if self.event_name is None and name is not None:
            self.event_name = name.removeprefix("on_").replace("_", "-")
        super().class_init(cls, name)

    def default(self, widget: ipywidgets.Widget) -> OutputListenerHandler:
        return OutputListenerHandler(self.event_name, widget)
