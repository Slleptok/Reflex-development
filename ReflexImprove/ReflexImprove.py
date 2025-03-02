"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from . import pages,navigation

from .ui.base_page import base_of_page


class State(rx.State):
    """The app state."""

    label = 'Welcome to Reflex! '

    def handle_input_change(self, val):
        self.label = val

    num = 0
    def count_clicks(self):
        self.num +=1
    def remove_clicks(self):
        self.num -= 1



def index() -> rx.Component:
    # Welcome Page (Index)

        my_child = rx.vstack(
            rx.heading(State.label,State.num, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.input(on_change=State.handle_input_change()),
            rx.hstack(
                rx.button('Plus', on_click=State.count_clicks()), rx.button('Minuse', on_click=State.remove_clicks()),
            ),

            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            align_center="center",
        ),
        return base_of_page(my_child)



app = rx.App()
app.add_page(index)
app.add_page(pages.about_page(),route=navigation.route.ABOUT_ROUTE)
