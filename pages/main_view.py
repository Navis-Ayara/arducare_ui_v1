import flet as ft
from utils.controls import SessionCard


class MainView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/"

        self.scroll = ft.ScrollMode.ALWAYS
        self.padding = ft.padding.only(left=10, right=10)


    def open_new_session_dialog(self, e):
        self.page.overlay.append(self.dlg)
        self.dlg.open = True

        self.page.update()

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
                        icon=ft.icons.ADD_ROUNDED,
                        text="New Session",
                        height=47,
                        on_click=self.open_new_session_dialog
                    )
                )
            ]
        )

        self.dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(
                value="Start a new session"
            ),
            content=ft.Container(
                height=150,
                content=ft.RadioGroup(
                    value="Personal session",
                    content=ft.Column([
                            ft.Radio(
                                label="Personal session",
                                value="Personal session",
                            ),
                            ft.Radio(
                                label="Remote session",
                                value="Remote session"
                            )
                        ], expand_loose=True)
                    )
            ),
            actions=[
                ft.OutlinedButton(
                    text="Cancel",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=7)
                    ),
                    on_click=self.close_drawer
                ),
                ft.FilledButton(
                    text="OK",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=7)
                    ),
                    on_click=self.open_new_session
                )
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
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
                        ft.ListTile(
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
                            on_click=lambda _: print("Works"),
                            height=120
                        ),
                        ft.ListTile(
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
                            on_click=lambda _: print("Works"),
                            height=120
                        ),
                        ft.ListTile(
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
                            on_click=lambda _: print("Works"),
                            height=120
                        ),
                        ft.ListTile(
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
                            on_click=lambda _: print("Works"),
                            height=120
                        )
                    ])
                ]),
            )
        ]


    def open_new_session(self, e):
        if self.dlg.content.content.value.upper() == "PERSONAL SESSION":
            self.page.go("/data_stream_view")
        else:
            self.page.go("/join_remote_session")
            

    def open_record(self, e: ft.ContainerTapEvent):
        match e.control.content.controls[1].controls[0].value:
            case "Blood Oxygen":
                self.page.go("/session_view")
            case "Heart Rate":
                self.page.go("/session_view")
            case "Temperature":
                self.page.go("/session_view")
            case "Blood Pressure":
                self.page.go("/session_view")

    
    
