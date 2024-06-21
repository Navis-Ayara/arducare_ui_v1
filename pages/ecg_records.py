import flet as ft

class ECGView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/ecg-records"
        

    def build(self):
        self.appbar = ft.AppBar(
            toolbar_height=100,
            elevation=0,
            elevation_on_scroll=0,
            center_title=True,
            title=ft.Text(
                value="ECG Data"
            ),
            actions=[
                ft.Container(
                    margin=ft.margin.only(right=10),
                    content=ft.FloatingActionButton(
                        icon=ft.icons.ADD_ROUNDED,
                        text="New measurement",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        # height=45,
                        elevation=0
                    )
                )
            ]
        )

        self.controls = [
            ft.Row(
                spacing=25,
                controls=[
                    ft.Column([
                        ft.Text(
                            value="Current",
                            weight=ft.FontWeight.W_500
                        ),
                        ft.Row([
                            ft.Text(
                                value="65",
                                weight=ft.FontWeight.BOLD,
                                size=24
                            ),
                            ft.Text(
                                value="bpm"
                            )
                        ])
                    ]),
                    ft.Column([
                        ft.Text(
                            value="Resting",
                            weight=ft.FontWeight.W_500
                        ),
                        ft.Row([
                            ft.Text(
                                value="67",
                                weight=ft.FontWeight.BOLD,
                                size=24
                            ),
                            ft.Text(
                                value="bpm"
                            )
                        ])
                    ]),
                    ft.Column([
                        ft.Text(
                            value="High",
                            weight=ft.FontWeight.W_500
                        ),
                        ft.Row([
                            ft.Text(
                                value="180",
                                weight=ft.FontWeight.BOLD,
                                size=24
                            ),
                            ft.Text(
                                value="bpm"
                            )
                        ])
                    ])
                ]
            ),
            ft.Container(
                height=320,
                bgcolor=ft.colors.SECONDARY_CONTAINER,
                border_radius=24,
                padding=15,
            ),
            ft.ListView([
                ft.ListTile(
                    height=140,
                    on_click=lambda _: print("Loading Record..."),
                    title=ft.Text(
                        value="Locked"
                    )
                )
            for i in range(30)], expand=True)
        ]
