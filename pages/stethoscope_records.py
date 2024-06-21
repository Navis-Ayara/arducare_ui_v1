import flet as ft
import json
import os

with open("data/measurement_data.json", "r") as data_file:
    stethoscope_data = json.loads("".join(data_file.readlines()))["stethoscope"]
    data_file.close()

class StethoscopeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.sounds = []

        for s in os.listdir("data/sounds"):
            if s.endswith(".mp3"):
                self.sounds.append(s)

        self.audio_players = [
            ft.Audio(
                src = f"data/sounds/{sound}"
            )
        for sound in self.sounds]

        self.route = "/stethoscope-records"
        self.scroll = ft.ScrollMode.AUTO


    def build(self):
        for audio_player in self.audio_players:
            self.page.overlay.append(
                audio_player
            )

        self.indices = [
            i for i in range(len(self.sounds))
        ]

        self.appbar = ft.AppBar(
            toolbar_height=100,
            elevation=0,
            elevation_on_scroll=0,
            center_title=True,
            title=ft.Text(
                value="Stethoscope Data"
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
            ft.Text(
                value=f"{len(self.sounds)} Sounds",
                size=24,
                weight=ft.FontWeight.W_700
            ),
            ft.ListView(
                controls=[
                    ft.ListTile(
                        title=ft.Text(
                            value=f"{self.sounds[i].removesuffix(".mp3")}"
                        ),
                        on_click=self.play_sound
                    )
                for i in range(len(self.sounds))]
            )
        ]

    def play_sound(self, e):
        for index in self.audio_players:
            index.pause()
        for i in self.indices:
            if self.audio_players[i].src == f"data/sounds/{e.control.title.value}.mp3":

                self.audio_players[i].play()
        self.page.update()
