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

    def on_submit(self, e):
        self.page.go("/data_stream_view")

    def build(self):
        self.page.pubsub.subscribe_topic(
            topic="/data_stream_view",
            handler=self.on_submit
        )

        self.controls = [
            ft.Column([
                ft.TextField(
                    border_radius=14,
                    label="Enter session link",
                    border_color=ft.colors.SECONDARY_CONTAINER,
                    max_length=16,
                    capitalization=ft.TextCapitalization.CHARACTERS,
                    on_submit=self.on_submit
                )
            ])
        ]
