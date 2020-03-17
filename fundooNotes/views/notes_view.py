import cgi
from ..services.note_service import NoteServices
import cgitb

cgitb.enable()

note = NoteServices()


class NoteDetails:
    def __init__(self):
        pass

    def create_note(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        data = {'title': form['title'].value, 'description': form['description'].value,'color': form['color'].value,
                'is_archived': form['is_archived'].value, 'is_deleted': form['is_deleted'].value,
                'is_trashed': form['is_trashed'].value, 'is_restored': form['is_restored'].value, 'is_pinned':
                    form['is_pinned'].value, 'user_id': form['user_id'].value}
        print(data)
        response_data = note.create_notes(data)
        return response_data

    def read_note(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        data = {'note_id': form['note_id'].value}
        response_data = note.read_note(data)
        return response_data

    def update_note(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        condition = {'note_id': 1}
        data = {'title': form['title'].value, 'description': form['description'].value,
                'is_archived': form['is_archived'].value, 'is_deleted': form['is_deleted'].value,
                'is_trashed': form['is_trashed'].value, 'is_restored': form['is_restored'].value, 'is_pinned':
                    form['is_pinned'].value, 'user_id': form['user_id'].value}
        response_data = note.update_note(data, condition)
        return response_data

    def get_notes(self):
        response_data = note.get_notes()
        return response_data

    def delete_note(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        data = {'note_id': form['note_id'].value}
        response_data = note.delete_note(data)
        return response_data

    def collaborator_note(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        data = {'note_id': form['note_id'].value, 'user_id': form['user_id'].value}
        response_data = note.collaborator_notes(data)
        return response_data

    def read_note_by_user(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        data = {'user_id': form['user_id'].value}
        response_data = note.read_note_by_user(data)
        return response_data

    def archive_note(self):
        response_data = note.archive_note()
        return response_data

    def restore_note(self):
        response_data = note.restore_note()
        return response_data

    def pin_notes(self):
        response_data = note.pin_notes()
        return response_data
