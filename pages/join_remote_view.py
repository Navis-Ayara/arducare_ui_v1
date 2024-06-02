import flet as ft

class RemoteSessionView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.route = "/join_remote_session"

        self.page = page

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.appbar = ft.AppBar(
            
        )

    def build(self):
        self.controls = [
            ft.Column([
                ft.TextField(
                    border_radius=14,
                    label="Enter session link",
                    border_color=ft.colors.SECONDARY_CONTAINER,
                    max_length=8
                )
            ])
        ]
