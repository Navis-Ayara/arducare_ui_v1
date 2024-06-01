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
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.icons.AUTO_GRAPH,
                    label="Monthly Summary"
                )
            ]
        )

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

        self.appbar = ft.AppBar(
            leading=ft.Container(
                margin=ft.margin.only(left=10),
                content=ft.CircleAvatar(),
                on_click=self.open_drawer
            ),
            title=ft.Text(
                value="Hello, Navis",
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

    def open_drawer(self, e):
        self.drawer.open = True

        self.page.update()

    def close_drawer(self, e):
        self.dlg.open = False
        
        self.page.update()

    def open_new_session(self, e):
        self.page.go("/data_stream_view")

    def build(self):
        self.controls = [
            SessionCard(self.page)
        for i in range(12)]
