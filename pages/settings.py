import flet as ft


class Settings(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/settings"

    def build(self):
        self.appbar = ft.AppBar(
            title=ft.Text(
                value="Settings"
            ),
            center_title=True,
            elevation=0,
            elevation_on_scroll=0
        )
