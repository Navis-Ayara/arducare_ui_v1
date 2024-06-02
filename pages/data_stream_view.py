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
        self._not_measuring_indicator = ft.Text(
            value="not measuring... point device on left temple",
            color=ft.colors.ERROR
        )

    def build(self):
        # self.session_number = self.page.client_storage.get("session_number")
        
        self.appbar = ft.AppBar(
            title=ft.Text(
                f"Session #{self.session_number}"
            ),
            center_title=True
        )

        self.controls = [
            ft.Row([
                ft.Text(
                    value="Multiscope status: "
                ),
                ft.Row([
                    self.multiscope_status,
                    self.status_indicator
                ])
            ], spacing=0),
            ft.Column([
                ft.Row([
                    ft.Text(
                        value="Heart rate",
                        size=21,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Icon(
                        name=ft.icons.FAVORITE_ROUNDED
                    )
                ]),
                self.not_measuring_indicator
            ], spacing=0),
            ft.Container(
                height=250,
                border=ft.border.all(width=1.6, color=ft.colors.OUTLINE),
                border_radius=14,
            ),
            ft.Column([
                ft.Row([
                    ft.Text(
                        value="Blood Oxygen",
                        size=21,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Icon(
                        name=ft.icons.BLOODTYPE_ROUNDED
                    )
                ]),
                self.not_measuring_indicator
            ], spacing=0),
            ft.Container(
                height=250,
                border=ft.border.all(width=1.6, color=ft.colors.OUTLINE),
                border_radius=14,
            ),
            ft.Column([
                ft.Row([
                    ft.Text(
                        value="Temperature",
                        size=21,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Icon(
                        name=ft.icons.HEAT_PUMP
                    )
                ]),
                self._not_measuring_indicator
            ], spacing=0),
            ft.Container(
                height=250,
                border=ft.border.all(width=1.6, color=ft.colors.OUTLINE),
                border_radius=14,
            )
        ]
