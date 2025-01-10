import reflex as rx
from .navbar import navbar


def base_page(child: rx.Component ,*args, **kwargs) -> rx.Component:

    return rx.fragment(
        navbar(),
        child,

        rx.color_mode.button(position="bottom-left"),
        rx.logo(),

        align="center",
        align_center="center",

    )
