# this dictionary is used for declare the all urls
urls = {
    'register': '/register',
    'login': '/login',
    'forgot': '/forgot',
    'change_password': '/change_password',
    'logout': '/logout',
    'upload_image_s3': '/upload/image/s3',
    'get_image_s3': 'get/image/s3/',
    'create_note': '/create/note',
    'read_note': '/read/note',
    'list_note': '/list/note',
    'delete_note': '/delete/note',
    'update_note': '/update/note',
    'pin_note': '/pin/note',
    'trash_note': '/trash/note',
    'archive_note': '/archive/note',
    'restore_note': '/restore/note',
    'collaborate_note': '/coll/note',
    'list_trash_note': '/list/trash/note',
    'list_pin_note': '/list/pin/note',
    'list_archive_note': '/list/archive/note',
    'list_user_note': '/list/user/note',
    'list_coll_note': '/list/coll/note',
    'list_restore_note':'/list/restore/note'
}
# user_urls = ['/register', '/login', '/forgot', '/change_password', '/logout']
# note_urls = ['/create/note', '/read/note', '/list/note', '/delete/note', '/update/note', '/pin/note', '/trash/note',
#              '/archive/note', '/coll/note', '/restore/note']
# urls = []
# for url in note_urls:
#     urls.append(url)
# urls.append(user_urls[2])
# urls.append(user_urls[3])
# urls.append(user_urls[4])
#



# from fundooNotes.views.users_view import UserDetails
# views = UserDetails


# class Userurls:
#     def __init__(self):
#         self.url = self.url_fun()
#
#     def url_fun(self):
#         user_url = {
#             '/register': views.for_registration(self),
#             '/login': views.for_login(self)
#         }
#         return user_url
