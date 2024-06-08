import flet as ft
from utils.controls import SessionCard


class MainView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/"

        self.scroll = ft.ScrollMode.ALWAYS
        self.padding = ft.padding.only(left=10, right=10)

        self.drawer = ft.NavigationDrawer(
            on_change=self.navigate,
            tile_padding=10,
            selected_index=[-1],
            indicator_color=ft.colors.TRANSPARENT,
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.icons.AUTO_GRAPH,
                    label="Monthly Summary"
                ),
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

    def open_new_session_dialog(self, e):
        self.page.overlay.append(self.dlg)
        self.dlg.open = True

        self.page.update()

    def navigate(self, e):
        match e.control.selected_index:
            case 0:
                self.page.go("/summary_view")
            case 1:
                self.page.go("/settings")

    def open_drawer(self, e):
        self.drawer.open = True

        self.page.update()

    def close_drawer(self, e):
        self.dlg.open = False
        
        self.page.update()

    def build(self):
        self.dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(
                value="Start a new session"
            ),
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
                        weight=ft.FontWeight.W_600
                    ),
                    ft.Row([
                        ft.Container(
                            expand=True,
                            height=200,
                            bgcolor="#B8C9FF",
                            border_radius=24,
                            padding=20,
                            on_click=self.open_record,
                            content=ft.Column([
                                ft.Icon(
                                    name=ft.icons.FAVORITE,
                                    size=52
                                ),
                                ft.Column([
                                    ft.Text(
                                        value="Heart Rate",
                                        size=21,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    ft.Text(
                                        value="80 bpm"
                                    )
                                ], spacing=0)
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ),
                        ft.Container(
                            expand=True,
                            height=200,
                            bgcolor="#BBEAFE",
                            border_radius=24,
                            on_click=self.open_record,
                            padding=20,
                            content=ft.Column([
                                ft.Icon(
                                    name=ft.icons.BLOODTYPE,
                                    size=52
                                ),
                                ft.Column([
                                    ft.Text(
                                        value="Blood Pressure",
                                        size=21,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    ft.Text(
                                        value="12080 mmHG"
                                    )
                                ], spacing=0)
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ),
                        ft.Container(
                            expand=True,
                            height=200,
                            bgcolor="#F4C6FF",
                            on_click=self.open_record,
                            border_radius=24,
                            padding=20,
                            content=ft.Column([
                                ft.Icon(
                                    name=ft.icons.HEAT_PUMP,
                                    size=52
                                ),
                                ft.Column([
                                    ft.Text(
                                        value="Temperature",
                                        size=21,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    ft.Text(
                                        value="37°"
                                    )
                                ], spacing=0)
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ),
                        ft.Container(
                            expand=True,
                            height=200,
                            bgcolor="#FEB46A",
                            border_radius=24,
                            padding=20,
                            on_click=self.open_record,
                            content=ft.Column([
                                ft.Icon(
                                    name=ft.icons.CO2,
                                    size=52
                                ),
                                ft.Column([
                                    ft.Text(
                                        value="Blood Oxygen",
                                        size=21,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    ft.Text(
                                        value="__"
                                    )
                                ], spacing=0)
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        )
                    ]),
                ]),
            )
        ]

    def open_new_session(self, e):
        if self.dlg.content.value.upper() == "PERSONAL SESSION":
            self.page.go("/data_stream_view")
        else:
            self.page.go("/join_remote_session")

    def open_record(self, e):
        match e.control.content.controls[1].controls[0].value:
            case "Blood Oxygen":
                self.page.go("/session_view")
            case "Heart Rate":
                self.page.go("/session_view")
            case "Temperature":
                self.page.go("/session_view")
            case "Blood Pressure":
                self.page.go("/session_view")
