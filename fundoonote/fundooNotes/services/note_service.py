from ..common.send_email import SendMail
from ..models.model import Notes, Users, AssociationTable
from ..common.db_operation import *
from ..common.utils import json_response, serialize_data, profiler, cache


class NoteServices:
    """ This class is used to create the note api"""

    def __init__(self):
        pass

    def create_notes(self, data):
        """ this method is used to create the note"""
        try:
            with profiler:  # return the all update from database
                login_user = cache.get_value("login_id")  # take login user_id save with note login user
                if login_user is not None:  # check user is none or not
                    note = Notes(title=data['title'],
                                 description=data['description'],
                                 color=data['color'],
                                 is_archived=data['is_archived'],
                                 is_deleted=data['is_deleted'], is_trashed=data['is_trashed'],
                                 is_restored=data['is_restored'],
                                 is_pinned=data['is_pinned'], user_id=login_user)  # validate all data
                    save(note)  # save note
                else:
                    return json_response("login user id is none")  # if false invalid data
        except:
            return json_response("missing values or invalid data")
        return json_response(success=True, message='Successfully created note', data=data)  # save note

    def read_note(self, data):
        """ This method is used to read the note"""
        try:
            note = filter_by_id(table=Notes, id=data['note_id'])  # filter the note
            print(note)
            if note is not None:  # check note is none or not
                json_data = serialize_data(note)  # serialize the data
                print(json_data)
                return json_response(success=True, message='get note is: ', data=json_data)  # return response
            else:
                return json_response(success=False, message='Not is not found', data=[])
        except:
            return json_response("missing values or invalid data")

    def update_note(self, data, condition):
        """ this method is used to update the note"""
        try:
            note = filter_by_id(table=Notes, id=condition['note_id'])  # pass the update note id
            if note is not None:
                note.update({Notes.title: data['title'], Notes.description: data['description'],
                             Notes.is_archived: data['is_archived'], Notes.is_deleted: data['is_deleted'],
                             Notes.is_trashed: data['is_trashed'], Notes.is_pinned: data['is_pinned'],
                             Notes.is_restored: data['is_restored'], Notes.user_id: data['user_id']},
                            synchronize_session=False)  # update note
                session.commit()
                session.close()
                return json_response(success=True, message="Successfully updated note", data=data)  # return response
            else:
                return json_response(success=False, message="Note does not exist")  # if note is not found
        except:
            return json_response("missing values or invalid data")

    def delete_note(self, data):
        """ this method is used to delete the note"""
        try:
            note = delete_query(id=data['note_id'])  # take note id which you want to delete
            if note is True:
                return json_response(success=True,
                                     message="successfully note is deleted")  # if note deleted return response
            else:
                return json_response(success=False, message="Note does not exist")  # if note is  not found
        except Exception as e:  # exception if invalid note
            return e

    def archive_note(self, data):
        """ This method is used to archive the note"""
        try:
            note = filter_by_id(table=Notes, id=data['note_id'])  # take note_id from user
            if note is not None:  # if note is is not None
                if note.is_archived != 1:  # check note already archive note
                    note.update({Notes.is_archived: 1}, synchronize_session=False)  # update teh note
                    return json_response(success=True, message="successfully archived note")  # return response
            else:
                return json_response(success=False, message="Note does not exist")  # if note is not found
        except Exception as e:  # return exception
            return e

    def pin_note(self, data):
        """ this note is used for pin note"""
        try:  # enter the try block
            note = filter_by_id(table=Notes, id=data['note_id'])  # take note_id from user
            if note is not None:  # if note is not None
                if note.is_pinned != 1:
                    note.update({Notes.is_pinned: 1}, synchronize_session=False)
                    return json_response(success=True, message="Note successfully pinned")
            else:
                return json_response(success=False, message="Note does not exist")
        except Exception as e:
            return e

    def trash_note(self, data):
        """ this method is used to trash the note"""
        try:
            note = filter_by_id(table=Notes, id=data['note_id'])  # take the note for trash note
            if note is not None:  # if note is not None
                if note.is_trashed != 1 and note.is_deleted == 1:  # check note is already trash or not
                    note.update({Notes.is_trashed: 1}, synchronize_session=False)
                    return json_response(success=True, message="successfully trashed note")
            else:
                return json_response(success=False, message="Note does not exist")
        except Exception as e:
            return e

    def restore_note(self, data):
        """ this method is used to restore the note"""
        try:
            note = filter_by_id(table=Notes, id=data['note_id'])
            if note is not None:
                if note.trashed == 1 and note.is_restore != 1:
                    note.update({Notes.is_archived: 1}, synchronize_session=False)
                    return json_response(success=True, message="successfully restore note")
            else:
                return json_response(success=False, message="Note does not exist")
        except Exception as e:
            return e

    def list_notes(self):
        """ This method is used to list the notes"""
        notes = fetch_all(table=Notes)  # fetch all notes
        if notes:
            json_data = serialize_data(notes)  # serialize the notes
            return json_response(success=True, message='List of note : ', data=json_data)
        else:
            return json_response(success=False, message='unsuccessfully', data=[])

    def list_user_notes(self, data):
        """ this method is used for list user notes"""
        note = session.query(Notes).filter_by(user_id=data['user_id']).all()
        if note:
            json_data = serialize_data(note)
            return json_response(success=True, message='list of notes by user', data=json_data)
        else:
            return json_response(success=False, message='Does not exist note or user', data=[])

    def list_archive_notes(self):
        """ this method is used for list archived  note"""
        notes = fetch_all(table=Notes)
        if notes.is_archived == 1:
            json_data = serialize_data(notes)
            return json_response(success=True, message="Successfully note is archived", data=json_data)
        else:
            return json_response(success=False, message="no archived note or empty")

    def list_restore_notes(self):
        """ This method is used for list restored note"""
        notes = fetch_all(table=Notes)
        if notes:
            for note in notes:
                if note.is_restored == 1:
                    json_data = serialize_data(note)
                    return json_response(success=True, message="Successfully restored notes", data=json_data)
                else:
                    return json_response(success=False, message="does not exist restored  note")
        else:
            return json_response(success=False, message="no restored note or empty")

    def list_pin_notes(self):
        """this method is used for list the pinned notes"""
        notes = fetch_all(table=Notes)
        if notes:
            for note in notes:
                if note.is_pinned == 1:
                    json_data = serialize_data(note)
                    return json_response(success=True, message="Successfully list all pinned notes", data=json_data)
        else:
            return json_response(success=False, message="no pinned note or empty")

    def list_trash_notes(self):
        """ This method is used for list the trash notes"""
        notes = fetch_all(table=Notes)
        if notes.is_trashed == 1:
            for note in notes:
                json_data = serialize_data(note)  # serialize the note
                return json_response(success=True, message="Successfully list all trashed notes", data=json_data)
        else:
            return json_response(success=False, message="no trashed note or empty")

    def collaborator_notes(self, data):
        """ This method is used to collaborate the notes"""
        try:
            note = filter_by_id(id=data['note_id'], table=Notes) # get note_id from user
            user = filter_by_id(id=data['user_id'], table=Users) # get user_id from user
            user.notes.append(note) # append the note in user.notes
            session.add(user) # add user
            session.commit() # commit data
            json_data = serialize_data(note) # serialize the object
            # send_mail_service = SendMail()  # create send_mail object
            # send_mail_service.send_mail(email=user.email, data=str(json_data))  # send the email for colloborate user
            return json_response(success=True, message='collaborate note with: ' + str(user.id), data=json_data)
        except:
            return json_response("missing values or invalid data") # missing values or invalid data

    def get_collaborator_notes_list(self):
        try:
            data = []
            for note in session.query(Users, Notes).filter(AssociationTable.user_id == Users.id,
                                                           AssociationTable.note_id == Notes.id).order_by \
                        (AssociationTable.user_id).all():
                json_data = serialize_data(note)
                data.append(json_data)
            return json_response(message="collaborator notes list", data=data)
        except:
            return json_response("invalid response")




