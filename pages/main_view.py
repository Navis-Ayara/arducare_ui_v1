import flet as ft
import json
import os
        

sounds = os.listdir("data/sounds")

def print_sounds():
    return len(sounds)


class MainView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/"
        self.padding = ft.padding.only(left=10, right=10)

        with open("data/measurement_data.json", "r") as data_file:
            try:
                self.last_thermo_reading = [i for i in json.loads("".join(data_file.readlines()))["thermometer"].values()][0]
            except json.JSONDecodeError:
                self.last_thermo_reading = None
            except IndexError:
                self.last_thermo_reading = None
            try:
                self.last_oximeter_reading = [i for i in json.loads("".join(data_file.readlines()))["oximeter"].values()][0]
            except json.JSONDecodeError:
                self.last_oximeter_reading = None
            except IndexError:
                self.last_thermo_reading = None
            try:
                self.last_electrocardiogram_reading = [i for i in json.loads("".join(data_file.readlines()))["electrocardiogram"].values()][0]
            except json.JSONDecodeError:
                self.last_electrocardiogram_reading = None
            except IndexError:
                self.last_electrocardiogram_reading = None


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
                        icon=ft.icons.SHARE_ROUNDED,
                        text="Share Data",
                        height=47,
                        # on_click=self.open_new_session_dialog
                    )
                )
            ]
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
                        ft.Card(
                            content=ft.ListTile(
                                trailing=ft.Text(
                                    value="Yesterday"
                                ),
                                leading=ft.Image(
                                    src="icons/heart-rate.svg",
                                    width=40,
                                    height=40,
                                    color=ft.colors.ON_BACKGROUND,
                                    fit=ft.ImageFit.COVER
                                ),
                                title=ft.Text(
                                    value="Heart Rate (ECG)"
                                ),
                                subtitle=ft.Text(
                                    value="No data" if self.last_electrocardiogram_reading == None else str(self.last_electrocardiogram_reading)
                                ),
                                on_click=lambda _: self.page.go("/ecg-records"),
                                height=120
                            )
                        ),
                        ft.Card(
                            content=ft.ListTile(
                                trailing=ft.Text(
                                    value="Yesterday"
                                ),
                                leading=ft.Image(
                                    src="icons/stethoscope.svg",
                                    width=40,
                                    height=40,
                                    color=ft.colors.ON_BACKGROUND,
                                    fit=ft.ImageFit.COVER
                                ),
                                title=ft.Text(
                                    value="Stethoscope Sounds"
                                ),
                                subtitle=ft.Text(
                                    value=f"{str(print_sounds())} Sounds"
                                ),
                                on_click=lambda _: self.page.go("/stethoscope-records"),
                                height=120
                            )
                        ),
                        ft.Card(
                            content=ft.ListTile(
                                trailing=ft.Text(
                                    value="Yesterday"
                                ),
                                leading=ft.Image(
                                    src="icons/thermometer.svg",
                                    width=40,
                                    height=40,
                                    color=ft.colors.ON_BACKGROUND,
                                    fit=ft.ImageFit.COVER
                                ),
                                title=ft.Text(
                                    value="Temperature"
                                ),
                                subtitle=ft.Text(
                                    value="No data" if self.last_thermo_reading == None else f"{str(self.last_thermo_reading)}°C"
                                ),
                                on_click=lambda _: self.page.go("/thermometer-records"),
                                height=120
                            )
                        ),
                        ft.Card(
                            content=ft.ListTile(
                                trailing=ft.Text(
                                    value="Yesterday"
                                ),
                                leading=ft.Image(
                                    src="icons/blood.svg",
                                    width=40,
                                    height=40,
                                    color=ft.colors.ON_BACKGROUND,
                                    fit=ft.ImageFit.COVER
                                ),
                                title=ft.Text(
                                    value="Blood Oxygen"
                                ),
                                subtitle=ft.Text(
                                    value="No data" if self.last_oximeter_reading == None else self.last_oximeter_reading
                                ),
                                on_click=lambda _: self.page.go("/bo-records"),
                                height=120
                            )
                        )
                    ])
                ]),
            )
        ]
    
