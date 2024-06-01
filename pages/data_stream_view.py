import flet as ft

class DataStreamView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.route = "/data_stream_view"

    def build(self):
        self.appbar = ft.AppBar(
            title=ft.Text(
                "Session #23"
            ),
            center_title=True
        )
