import cgi
import cgitb
cgitb.enable()
from ..services.note_service import NoteServices
from ..common.utils import json_response

note_service = NoteServices()  # create object of service class

class NoteDetails:
    """ This class is used to create the note api : create, delete, update note etc.."""

    def __init__(self):
        pass

    def create_note(self):
        """ the method is used create the note """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'title': form['title'].value, 'description': form['description'].value,
                    'color': form['color'].value,
                    'is_archived': form['is_archived'].value, 'is_deleted': form['is_deleted'].value,
                    'is_trashed': form['is_trashed'].value, 'is_restored': form['is_restored'].value, 'is_pinned':
                        form['is_pinned'].value}
            response_data = note_service.create_notes(data)  # pass data to service method and validate data. if valid
            # it store in Db and return data
            return response_data
        except KeyError:
            return json_response("missing values or invalid data")

    def read_note(self):
        """ this method is used to read note by id"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'note_id': form['note_id'].value}  # get note id from user
            response_data = note_service.read_note(data)  # pass to service  method for validation. if it is valid
            return response_data  # return response
        except KeyError:
            return json_response("missing values or invalid data")

    def update_note(self):
        """ this method is used to update the note"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            condition = {'note_id': form['note_id'].value}  # take from user input from update
            data = {'title': form['title'].value, 'description': form['description'].value,
                    'is_archived': form['is_archived'].value, 'is_deleted': form['is_deleted'].value,
                    'is_trashed': form['is_trashed'].value, 'is_restored': form['is_restored'].value, 'is_pinned':
                        form['is_pinned'].value, 'user_id': form['user_id'].value}  # update the data
            response_data = note_service.update_note(data, condition)  # pass the condition and data to service method
            return response_data  # if data is valid it return response
        except KeyError:
            return json_response("missing values or invalid data")

    def list_notes(self):
        """ this method is used to list the all notes"""
        try:
            response_data = note_service.list_notes()  # send request to service method if it valid .
            return response_data  # return response
        except Exception as e:
            return e

    def delete_note(self):
        """ this method is used to delete th note"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'note_id': form['note_id'].value}  # get input from user
            response_data = note_service.delete_note(data)  # send request for validation to service f it is valid
            return response_data  # return response
        except KeyError:
            return json_response("missing values or invalid data")

    def pin_note(self):
        """ this method is used to set pin note"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'note_id': form['note_id'].value}  # get input from user
            response_data = note_service.pin_note(data)  # send request for validation to service f it is valid
            return response_data  # return response
        except KeyError:
            return json_response("missing values or invalid data")

    def archive_note(self):
        """ this method is used to archived the note"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'note_id': form['note_id'].value}  # get input from user
            response_data = note_service.archive_note(data)  # send request for validation to service f it is valid
            return response_data  # return response
        except KeyError:
            return json_response("missing values or invalid data")

    def restore_note(self):
        """ this method is used to restored th note"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'note_id': form['note_id'].value}  # get input from user
            response_data = note_service.restore_note(data)  # send request for validation to service f it is valid
            return response_data  # return response
        except KeyError:
            return json_response("missing values or invalid data")

    def trash_note(self):
        """ this method is used to trash the note"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'note_id': form['note_id'].value}  # get input from user
            response_data = note_service.trash_note(data)  # send request for validation to service f it is valid
            return response_data  # return response
        except KeyError:
            return json_response("missing values or invalid data")

    def list_for_user_notes(self):
        """ read note by user id"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'user_id': form['user_id'].value}  # take user_id input from user
            response_data = note_service.list_user_notes(data)
            return response_data
        except KeyError:
            return json_response("missing values or invalid data")

    def list_for_archive_notes(self):
        try:
            response_data = note_service.list_archive_notes()
            return response_data
        except:
            return json_response("missing values or invalid data")

    def list_for_restore_notes(self):
        try:
            response_data = note_service.list_restore_notes()
            return response_data
        except:
            return json_response("missing values or invalid data")

    def list_for_pin_notes(self):
        try:
            response_data = note_service.list_pin_notes()
            return response_data
        except:
            return json_response("missing values or invalid data")

    def collaborator_note(self):
        """ this method is used to collaborator the notes"""
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': self.headers['Content-Type'], }
        )
        try:
            data = {'note_id': form['note_id'].value, 'user_id': form['user_id'].value}  # get note_id and user_id
            # to collaborate note with user
            response_data = note_service.collaborator_notes(data)  # send request to the service.
            # if it is valid it returns response
            return response_data
        except KeyError:
            return json_response("missing values or invalid data")

    def read_collaborated_notes_list(self):
        """ this method is used to list the collaborated notes"""
        try:
            response_data = note_service.get_collaborator_notes_list()
            return response_data
        except:
            return json_response("missing values or invalid data")


