import flet as ft

class SummaryView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/summary_view"

        self.appbar = ft.AppBar(

        )
