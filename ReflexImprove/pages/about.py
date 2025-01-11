import reflex as rx
from ..ui.base_page import base_of_page



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

def about_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading('About', size="9"),
        rx.heading(State.label, State.num, size="9"),
        rx.text(
            "Information About team",
            size="5",
        ),
        rx.input(on_change=State.handle_input_change()),
        rx.hstack(
            rx.button('Plus', on_click=State.count_clicks()), rx.button('Minuse', on_click=State.remove_clicks()),
        ),

        spacing="5",
        justify="center",
        min_height="85vh",
        align="center",
        align_center="center",
    ),
    return base_of_page(my_child)