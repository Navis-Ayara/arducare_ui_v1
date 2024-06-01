import flet as ft
class SessionCard(ft.Card):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.shape = ft.RoundedRectangleBorder(radius=12)

    def open_session(self, e):
        self.page.go("/session_view")

    def build(self):
        self.content = ft.Container(
            height=120,
            content=ft.ListTile(
                shape=ft.RoundedRectangleBorder(radius=12),
                on_click=self.open_session
            )
        )
