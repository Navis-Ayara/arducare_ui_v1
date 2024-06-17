import flet as ft


class OximeterView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/bo-records"

    def build(self):
        self.appbar = ft.AppBar(
            toolbar_height=100,
            elevation=0,
            elevation_on_scroll=0,
            center_title=True,
            title=ft.Text(
                value="Oximeter Data"
            ),
            actions=[
                ft.Container(
                    margin=ft.margin.only(right=10),
                    content=ft.FloatingActionButton(
                        icon=ft.icons.ADD_ROUNDED,
                        text="New measurement",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        elevation=0
                    )
                )
            ]
        )
