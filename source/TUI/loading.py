from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Label, LoadingIndicator

from ..translation import _

__all__ = ["Loading"]


class Loading(ModalScreen):
    BINDINGS = [
        Binding("escape", "cancel_task", _("取消任务")),
    ]

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label(_("程序处理中...")),
            LoadingIndicator(),
            Button(_("取消"), id="cancel", variant="error"),
            classes="loading",
        )

    async def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "cancel":
            self.action_cancel_task()

    def action_cancel_task(self):
        self.app.APP.cancel_task()
        self.app.pop_screen()
