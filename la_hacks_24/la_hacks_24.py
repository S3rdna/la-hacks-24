"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    def current_url(self) -> str:
        return self.router.page.full_raw_path
    


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Get started by editing ", rx.code(filename)),
            rx.button(
                "Check out our docs!",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            rx.button("Check out Gemini", on_click=lambda: rx.redirect("/gemini")),
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

# def gemini() -> rx.Component:
#     return rx.center(
#         rx.theme_panel(),
#         rx.vstack(
#             rx.heading("Welcome to Gemini!", size="9"),
#             rx.text("Get started by editing ", rx.code(filename)),
#             rx.button(
#                 "Check out our docs!",
#                 on_click=lambda: rx.redirect(docs_url),
#                 size="4",
#             ),
#             rx.logo(),
#             align="center",
#             spacing="7",
#             font_size="2em",
#         ),
#         height="100vh",
#     )


def gemini():
    return rx.text("Gemini AI")

app = rx.App()
app.add_page(index)
app.add_page(gemini)
