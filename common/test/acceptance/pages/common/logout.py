"""
Logout Page.
"""
from bok_choy.page_object import PageObject
from . import BASE_URL


class LogoutPage(PageObject):
    """
    Logout page to logout current logged in user.
    """

    url = BASE_URL + "/logout"

    def is_browser_on_page(self):
        return self.q(css='.cta-login').present
