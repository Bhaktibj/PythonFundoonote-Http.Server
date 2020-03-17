from fundooNotes.views.users_view import UserDetails
views = UserDetails


class Userurls:
    def __init__(self):
        self.url = self.url_fun()

    def url_fun(self):
        user_url = {
            '/register': views.for_registration(self),
            '/login': views.for_login(self)
        }
        return user_url
