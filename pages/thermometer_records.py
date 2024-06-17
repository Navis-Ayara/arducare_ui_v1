import flet as ft


class ThermometerView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/thermometer-records"
        self.padding = 0
        self.scroll = ft.ScrollMode.AUTO

    def build(self):
        self.appbar = ft.AppBar(
            toolbar_height=100,
            elevation=0,
            elevation_on_scroll=0,
            center_title=True,
            title=ft.Text(
                "Thermometer data"
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
            ft.Stack([
                ft.Container(
                    bgcolor=ft.colors.GREEN_ACCENT,
                    expand=True
                ),
                ft.Column([
                    ft.Container(
                        height=self.page.window_height,
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            value="37°C",
                            size=48,
                            weight=ft.FontWeight.BOLD
                        )
                    ),
                    ft.ListView([
                        ft.ListTile(
                            height=140,
                            on_click=lambda _: print("Loading Record..."),
                            title=ft.Text(
                                value="Locked"
                            )
                        )
                    for i in range(7)])
                ])
            ])
        ]
