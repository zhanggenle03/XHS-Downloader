from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Label, LoadingIndicator

from ..translation import _

__all__ = ["Loading"]


class Loading(ModalScreen):
    BINDINGS = [
        Binding("escape", "cancel_task", _("取消")),
    ]

    def compose(self) -> ComposeResult:
        yield Grid(
            Label(_("程序处理中...")),
            LoadingIndicator(),
            classes="loading",
        )

    def action_cancel_task(self):
        self.app.APP.cancel_task()
