import flet as ft
import json


class Settings(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.route = "/settings"

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.END

        self.padding = ft.padding.only(
            left=100,
            right=100,
            top=50
        )

        self.theme_dlg = ft.AlertDialog(
            modal=False,
            content=ft.Container(
                height=135,
                content=ft.RadioGroup(
                    on_change=self.change_theme,
                    value="System",
                    content=ft.Column([
                        ft.Radio(
                            value="Light",
                            label="Light"
                        ),
                        ft.Radio(
                            value="Dark",
                            label="Dark"
                        ),
                        ft.Radio(
                            value="System",
                            label="System"
                        )
                    ])
                )
            )
        )

        self.clear_data_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(
                value="Are you sure?"
            ),
            content=ft.Text(
                value="This will clear all recordings from the database"
            ),
            actions=[
                ft.TextButton(
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=12)
                    ),
                    text="Cancel",
                    on_click=self.close_dlg
                ),
                ft.ElevatedButton(
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=12)
                    ),
                    text="Yes"
                )
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        

    def build(self):
        self.appbar = ft.AppBar(
            title=ft.Text(
                value="Settings"
            ),
            center_title=True,
            elevation=0,
            elevation_on_scroll=0
        )

        self.controls = [
            ft.Container(
                expand=True,
                padding=10,
                border_radius=ft.border_radius.only(
                    top_left=24,
                    top_right=24
                ),
                bgcolor=ft.colors.with_opacity(0.4, ft.colors.SECONDARY_CONTAINER),
                content=ft.Column([
                    ft.ListTile(
                        shape=ft.RoundedRectangleBorder(
                            radius=12
                        ),
                        on_click=self.open_theme_picker,
                        title=ft.Text(
                            value="Theme"
                        )
                    ),
                    ft.Divider(),
                    ft.ListTile(
                        shape=ft.RoundedRectangleBorder(
                            radius=12
                        ),
                        title=ft.Checkbox(
                            value="Auto Sync",
                            label="Auto Sync"
                        ),
                        toggle_inputs=True
                    ),
                    ft.Divider(),
                    ft.ListTile(
                        shape=ft.RoundedRectangleBorder(
                            radius=12
                        ),
                        title=ft.Text(
                            value="Clear Data",
                        ),
                        on_click=self.open_clear_data_dlg
                    ),
                ])
            )
        ]

    def open_theme_picker(self, e):
        self.page.overlay.append(self.theme_dlg)
        self.theme_dlg.open = True
        self.page.update()


    def change_theme(self, e):
        if e.control.value == "Light":
            self.page.theme_mode = ft.ThemeMode.LIGHT
        elif e.control.value == "Dark":
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.SYSTEM

        with open("utils/settings.json", "r") as file:
            settings = json.loads("".join(file.readlines()))

            file.close()

        with open("utils/settings.json", "w") as settings_file:
            settings["theme"] = e.control.value

            settings_file.writelines(
                json.dumps(settings, indent=4)
            )

            settings_file.close()

        self.page.update()

    
    def open_clear_data_dlg(self, e):
        self.page.overlay.append(
            self.clear_data_dlg
        )
        self.clear_data_dlg.open = True

        self.page.update()

    def close_dlg(self, e):
        self.clear_data_dlg.open = False

        self.page.update()


"""
TODO: Implement actual data clearing
"""
