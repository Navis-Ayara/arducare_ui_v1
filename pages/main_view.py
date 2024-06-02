import flet as ft
from utils.controls import SessionCard


class MainView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/"

        self.scroll = ft.ScrollMode.ALWAYS
        self.padding = ft.padding.only(left=10, right=10)

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

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
                value=f"Hello, {self.username}",
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
                content=ft.Text(
                    value="No sessions yet\nClick the '+' to start a new one",
                    text_align=ft.TextAlign.CENTER
                )
            )
        ]

    def open_new_session(self, e):
        if self.dlg.content.value.upper() == "PERSONAL SESSION":
            self.page.go("/data_stream_view")
        else:
            self.page.go("/join_remote_session")
