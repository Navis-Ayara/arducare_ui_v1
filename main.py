import flet as ft
import json

import pages.main_view
import pages.thermometer_records
import pages.settings
import pages.bo_records
import pages.stethoscope_records
import pages.ecg_records


def main(page: ft.Page):
    page.title = "Arducare UI"

    page.window_full_screen = False

    with open("utils/settings.json", "r") as settings_file:
        settings = json.loads("".join(settings_file.readlines()))
        page.theme_mode = settings["theme"].upper()
        settings_file.close()

    page.fonts = {
        "Onest": "./fonts/Onest.ttf"
    }   

    page.theme = ft.Theme(
        color_scheme_seed="#255CFF",
        color_scheme=ft.ColorScheme(
            primary="#255CFF",
        ),
        page_transitions=ft.PageTransitionsTheme(
            windows=ft.PageTransitionTheme.CUPERTINO
        ),
        font_family="Onest",
        appbar_theme=ft.AppBarTheme(
            elevation=0,
            scroll_elevation=0,
            title_text_style=ft.TextStyle(
                size=18,
                weight=ft.FontWeight.W_700,
                color=ft.colors.ON_BACKGROUND 
            ),
        ),
        dialog_theme=ft.DialogTheme(
            shape=ft.RoundedRectangleBorder(radius=7),
            title_text_style=ft.TextStyle(
                size=18,
                weight=ft.FontWeight.W_700,
                color=ft.colors.ON_BACKGROUND
            )
        ),
        list_tile_theme=ft.ListTileTheme(
            shape=ft.RoundedRectangleBorder(radius=12),
            min_leading_width=64,
            leading_and_trailing_text_style=ft.TextStyle(
                size=16,
                weight=ft.FontWeight.W_700,
                color=ft.colors.ON_BACKGROUND
            )
        ),
        card_theme=ft.CardTheme(
            shape=ft.RoundedRectangleBorder(radius=12),
            surface_tint_color=ft.colors.BACKGROUND,
            elevation=5
        ),
        scrollbar_theme=ft.ScrollbarTheme(
            thickness=10,
            radius=2.5,
            interactive=True
        )
    )


    def on_route_change(route):
        page.views.clear()
        page.views.append(
            pages.main_view.MainView(page)
        )

        if page.route == "/thermometer-records":
            page.views.append(
                pages.thermometer_records.ThermometerView(page)
            )
        elif page.route == "/bo-records":
            page.views.append(
                pages.bo_records.OximeterView(page)
            )
        elif page.route == "/stethoscope-records":
            page.views.append(
                pages.stethoscope_records.StethoscopeView(page)
            )
        elif page.route == "/ecg-records":
            page.views.append(
                pages.ecg_records.ECGView(page)
            )
        elif page.route == "/settings":
            page.views.append(
                pages.settings.Settings(page)
            )

        page.update()

    
    def on_keyboard(e: ft.KeyboardEvent):
        match e.key:
            case "F11":
                page.window_full_screen = True if page.window_full_screen == False else False

        page.update()


    def on_view_pop(e):
        page.views.pop()
        top_view = page.views[-1]

        page.go(top_view.route)


    page.on_route_change = on_route_change
    page.on_view_pop = on_view_pop
    page.on_keyboard_event = on_keyboard

    page.go("/")


ft.app(main)
