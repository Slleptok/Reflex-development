import reflex as rx

from . import route

class NavState(rx.State):
    def to_home(self):
        return rx.redirect(route.HOME_ROUTE)
    def to_about(self):
        return rx.redirect(route.ABOUT_ROUTE)

