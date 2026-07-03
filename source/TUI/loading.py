from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Label, LoadingIndicator

from ..translation import _

__all__ = ["Loading"]


class Loading(ModalScreen):
    BINDINGS = [
        Binding("escape", "cancel_task", _("取消")),
    ]

    def compose(self) -> ComposeResult:
        with Vertical(classes="loading"):
            yield Label(_("程序处理中..."))
            yield LoadingIndicator()
            yield Button(_("取消"), id="cancel", variant="error")

    async def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "cancel":
            self.action_cancel_task()

    def action_cancel_task(self):
        # ponytail: 仅设置取消标志，不 pop_screen。
        #          deal() 的 extract() 循环检测到标志后会自然结束，
        #          然后 deal() 调用 action_back() 正常关闭 loading 屏。
        self.app.APP.cancel_task()
