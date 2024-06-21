import flet as ft
import json

with open("data/measurement_data.json", "r") as data_file:
    thermometer_data = json.loads("".join(data_file.readlines()))["thermometer"]
    data_file.close()


class ThermometerView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        _thermometer_data = [value for value in thermometer_data.values()]
        self.curr_temp = _thermometer_data[0]

        self.route = "/thermometer-records"
        self.padding = ft.padding.only(left=10, right=10)
        self.scroll = ft.ScrollMode.AUTO
        self.bgcolor = ft.colors.GREEN_ACCENT if self.curr_temp < 40 else ft.colors.RED_ACCENT
        

    def build(self):
        self.appbar = ft.AppBar(
            bgcolor = ft.colors.GREEN_ACCENT if self.curr_temp < 40 else ft.colors.RED_ACCENT,
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
                        elevation=0
                    )
                )
            ]
        )

        self.controls = [
            ft.Container(
                height=720,
                alignment=ft.alignment.center,
                content=ft.Text(
                    value=f"{str(self.curr_temp)}°C",
                    size=48,
                    weight=ft.FontWeight.BOLD
                )
            ),
            ft.ListView([
                ft.ListTile(
                    hover_color=ft.colors.with_opacity(0.4, ft.colors.GREY),
                    height=140,
                    on_click=lambda _: print("Loading Record..."),
                    title=ft.Text(
                        value="Locked"
                    )
                )
            for i in range(7)])
        ]
