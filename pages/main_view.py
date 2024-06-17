import flet as ft


class MainView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/"

        self.scroll = ft.ScrollMode.AUTO
        self.padding = ft.padding.only(left=10, right=10)

    def navigate(self, e):
        match e.control.selected_index:
            case 0:
                self.page.go("/settings")

    def open_drawer(self, e):
        self.drawer.open = True

        self.page.update()

    def close_drawer(self, e):
        self.dlg.open = False
        
        self.page.update()

    def build(self):
        self.drawer = ft.NavigationDrawer(
            on_change=self.navigate,
            tile_padding=10,
            selected_index=[-1],
            indicator_color=ft.colors.TRANSPARENT,
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.icons.SETTINGS_ROUNDED,
                    label="Settings"
                )
            ]
        )

        self.appbar = ft.AppBar(
            leading=ft.Container(
                margin=ft.margin.only(left=10),
                content=ft.CircleAvatar(),
                on_click=self.open_drawer
            ),
            title=ft.Text(
                value="Hello",
            ),
            actions=[
                ft.Container(
                    margin=ft.margin.only(right=10),
                    content=ft.FloatingActionButton(
                        shape=ft.RoundedRectangleBorder(radius=7),
                        icon=ft.icons.SHARE_ROUNDED,
                        text="Share Data",
                        height=47,
                        # on_click=self.open_new_session_dialog
                    )
                )
            ]
        )

        self.controls = [
            ft.Container(
                expand=True,
                content=ft.Column([
                    ft.Text(
                        value="Dashboard",
                        size=28,
                        weight=ft.FontWeight.W_600,
                    ),
                    ft.Column([
                        ft.Card(
                            content=ft.ListTile(
                                trailing=ft.Text(
                                    value="Yesterday"
                                ),
                                leading=ft.Image(
                                    src="icons/heart-rate.svg",
                                    color=ft.colors.ON_BACKGROUND,
                                    fit=ft.ImageFit.COVER
                                ),
                                title=ft.Text(
                                    value="Heart Rate (ECG)"
                                ),
                                subtitle=ft.Text(
                                    value="Some past data here"
                                ),
                                on_click=lambda _: self.page.go("/ecg-records"),
                                height=120
                            )
                        ),
                        ft.Card(
                            content=ft.ListTile(
                                trailing=ft.Text(
                                    value="Yesterday"
                                ),
                                leading=ft.Image(
                                    src="icons/stethoscope.svg",
                                    color=ft.colors.ON_BACKGROUND,
                                    fit=ft.ImageFit.COVER
                                ),
                                title=ft.Text(
                                    value="Stethoscope Sounds"
                                ),
                                subtitle=ft.Text(
                                    value=f"{str(0)} Sounds"
                                ),
                                on_click=lambda _: self.page.go("/stethoscope-records"),
                                height=120
                            )
                        ),
                        ft.Card(
                            content=ft.ListTile(
                                trailing=ft.Text(
                                    value="Yesterday"
                                ),
                                leading=ft.Image(
                                    src="icons/thermometer.svg",
                                    color=ft.colors.ON_BACKGROUND,
                                    fit=ft.ImageFit.COVER
                                ),
                                title=ft.Text(
                                    value="Temperature"
                                ),
                                subtitle=ft.Text(
                                    value="Some past data here"
                                ),
                                on_click=lambda _: self.page.go("/thermometer-records"),
                                height=120
                            )
                        ),
                        ft.Card(
                            content=ft.ListTile(
                                trailing=ft.Text(
                                    value="Yesterday"
                                ),
                                leading=ft.Image(
                                    src="icons/blood.svg",
                                    color=ft.colors.ON_BACKGROUND,
                                    fit=ft.ImageFit.COVER
                                ),
                                title=ft.Text(
                                    value="Blood Oxygen"
                                ),
                                subtitle=ft.Text(
                                    value="Some past data here"
                                ),
                                on_click=lambda _: self.page.go("/bo-records"),
                                height=120
                            )
                        )
                    ])
                ]),
            )
        ]
    
