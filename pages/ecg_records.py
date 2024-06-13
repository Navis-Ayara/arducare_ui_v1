import flet as ft


class ECGView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/ecg-records"

    def build(self):
        self.appbar = ft.AppBar(
            toolbar_height=100,
            elevation=0,
            elevation_on_scroll=0,
            center_title=True,
            title=ft.Text(
                value="ECG Data"
            ),
            actions=[
                ft.Container(
                    margin=ft.margin.only(right=10),
                    content=ft.FloatingActionButton(
                        icon=ft.icons.ADD_ROUNDED,
                        text="New measurement",
                        shape=ft.RoundedRectangleBorder(radius=12),
                        # height=45,
                        elevation=0
                    )
                )
            ]
        )

        data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(0, 3),
                    ft.LineChartDataPoint(2.6, 2),
                    ft.LineChartDataPoint(4.9, 5),
                    ft.LineChartDataPoint(6.8, 3.1),
                    ft.LineChartDataPoint(8, 4),
                    ft.LineChartDataPoint(9.5, 3),
                    ft.LineChartDataPoint(11, 4),
                ],
                stroke_width=5,
                color=ft.colors.CYAN,
                curved=True,
                stroke_cap_round=True,
            )
        ]

        self.controls = [
            ft.Container(
                height=320,
                bgcolor=ft.colors.SECONDARY_CONTAINER,
                border_radius=24,
                padding=15,
                content=ft.LineChart(
                    horizontal_grid_lines=ft.ChartGridLines(
                        interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
                    ),
                    vertical_grid_lines=ft.ChartGridLines(
                        interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
                    ),
                    left_axis=ft.ChartAxis(
                        title=ft.Text("Voltage"),
                        labels=[
                            ft.ChartAxisLabel(
                                label=ft.Text("0"),
                                value=0
                            ),
                            ft.ChartAxisLabel(
                                label=ft.Text("500"),
                                value=500
                            ),
                            ft.ChartAxisLabel(
                                label=ft.Text("1000"),
                                value=1000
                            ),
                            ft.ChartAxisLabel(
                                label=ft.Text("1500"),
                                value=1500
                            ),
                            ft.ChartAxisLabel(
                                label=ft.Text("2000"),
                                value=2000
                            )
                        ]
                    ),
                    bottom_axis=ft.ChartAxis(
                        title=ft.Text("Time")
                    ),
                    data_series=[
                        ft.LineChartData(
                            color=ft.colors.CYAN,
                            data_points=[
                                ft.LineChartDataPoint(0*1000, 3.44*1000),
                                ft.LineChartDataPoint(2.6*1000, 3.44*1000),
                                ft.LineChartDataPoint(4.9*1000, 3.44*1000),
                                ft.LineChartDataPoint(6.8*1000, 3.44*1000),
                                ft.LineChartDataPoint(8*1000, 3.44*1000),
                                ft.LineChartDataPoint(9.5*1000, 3.44*1000),
                                ft.LineChartDataPoint(11*1000, 3.44*1000),ft.LineChartDataPoint(0*1000, 500*1000),
                                ft.LineChartDataPoint(540*1000, 453*1000),
                            ]
                        )
                    ]
                )
            )
        ]
