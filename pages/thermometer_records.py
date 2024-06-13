import flet as ft


class ThermometerView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/thermometer-records"

    def build(self):
        self.appbar = ft.AppBar(
            elevation=0,
            elevation_on_scroll=0,
            center_title=True,
            title=ft.Text(
                "Thermometer data"
            ),
        )
