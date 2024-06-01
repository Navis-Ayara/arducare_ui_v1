import flet as ft

class DataStreamView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.route = "/data_stream_view"

        self.scroll = ft.ScrollMode.ALWAYS
        self.padding = ft.padding.only(left=10, right=10)

    def build(self):
        self.appbar = ft.AppBar(
            title=ft.Text(
                "Session #23"
            ),
            center_title=True
        )

        self.controls = [
            ft.Row([
                ft.Text(
                    value="Multiscope status: "
                ),
                ft.Row([
                    ft.Text(
                        color=ft.colors.ERROR,
                        value="offline"
                    ),
                    ft.Icon(
                        name=ft.icons.CIRCLE,
                        color=ft.colors.ERROR,
                        size=14
                    )
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
                ft.Text(
                    value="not measuring... place finger on sensor",
                    color=ft.colors.ERROR
                )
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
                ft.Text(
                    value="not measuring... place finger on sensor",
                    color=ft.colors.ERROR
                )
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
                ft.Text(
                    value="not measuring... point device on left temple",
                    color=ft.colors.ERROR
                )
            ], spacing=0),
            ft.Container(
                height=250,
                border=ft.border.all(width=1.6, color=ft.colors.OUTLINE),
                border_radius=14,
            )
        ]
