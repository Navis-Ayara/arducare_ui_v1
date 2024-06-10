import flet as ft
import threading

class DataStreamView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.route = "/data_stream_view"

        self.page = page
        
        self.scroll = ft.ScrollMode.ALWAYS
        self.padding = ft.padding.only(left=10, right=10)

        self.multiscope_status = ft.Text(
            color=ft.colors.ERROR,
            value="offline"
        )
        self.status_indicator = ft.Icon(
            name=ft.icons.CIRCLE,
            color=ft.colors.ERROR,
            size=14
        )
        self.not_measuring_indicator = ft.Text(
            value="not measuring... place finger on sensor",
            color=ft.colors.ERROR,
        )

    def build(self):
        self.appbar = ft.AppBar(
            title=ft.Text(
                f"Session"
            ),
            center_title=True
        )

        self.controls = [
            
        ]
