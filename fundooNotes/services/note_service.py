from ..models.model import Notes, Users
from ..common.response import JsonResponse as obj
from ..common.serializer import serialize_data
from ..config.database_connection import DatabaseService
from easy_profile import SessionProfiler

profiler = SessionProfiler()
db_obj = DatabaseService()


class NoteServices:
    def __init__(self):
        pass

    def create_notes(self, data):
        with profiler:
            if data['is_archived'] and data['is_deleted'] and data['is_trashed'] and data['is_restored'] \
                    and data['is_pinned'] == 0 or 1:
                note = Notes(title=data['title'], description=data['description'], color=data['color'],
                             is_archived=data['is_archived'],
                             is_deleted=data['is_deleted'], is_trashed=data['is_trashed'],
                             is_restored=data['is_restored'],
                             is_pinned=data['is_pinned'], user_id=data['user_id'])
                if note:
                    db_obj.save_into_db(note)
                    return obj.response(success=True, message='Successfully created note', data=profiler.stats)
                else:
                    return obj.response(success=False, message='Please enter proper format', data=[])
            else:
                return {'please enter 0 or 1 which is true or false'}

    def read_note(self, data):
        try:
            note = db_obj.session.query(Notes).filter_by(id=data['note_id']).first()
            print(note)
            if note:
                json_data = serialize_data(note)
                return obj.response(success=True, message='get note is: ', data=json_data)
            else:
                return obj.response(success=False, message='Not is not found', data=[])
        except Exception as e:
            return e

    def update_note(self, data, condition):
        try:
            note = db_obj.filter_by_id(model=Notes, id=condition['note_id'])
            if note:
                note.update({Notes.title: data['title'], Notes.description: data['description'],
                             Notes.is_archived: data['is_archived'], Notes.is_deleted: data['is_deleted'],
                             Notes.is_trashed: data['is_trashed'], Notes.is_pinned: data['is_pinned'],
                             Notes.is_restored: data['is_restored'], Notes.user_id: data['user_id']},
                            synchronize_session=False)
                db_obj.session.commit()
                db_obj.session.close()
                return obj.response(success=True, message="Successfully updated note", data=data)
            else:
                return obj.response(success=False, message="Note does not exist")
        except Exception as e:
            return e

    def delete_note(self, data):
        try:
            note = db_obj.delete_data_from_db(model=Notes, id=data['note_id'])
            if note is True:
                return obj.response(success=True, message="successfully note is deleted")
            else:
                return obj.response(success=False, message="Note does not exist")
        except Exception as e:
            return e

    def get_notes(self):
        notes = db_obj.fetch_all(model=Notes)
        if notes:
            json_data = serialize_data(notes)
            return obj.response(success=True, message='List of note : ', data=json_data)
        else:
            return obj.response(success=False, message='unsuccessfully', data=[])

    def collaborator_notes(self, data):
        note = db_obj.filter_by_id(id=data['note_id'], model=Notes)
        user = db_obj.filter_by_id(id=data['user_id'], model=Users)
        if note and user:
            user.notes.append(note)
            print(user.notes)
            db_obj.save_into_db(user)
            json_data = serialize_data(note)
            return obj.response(success=True, message='collaborate note with: ' + str(user.id), data=json_data)
        else:
            return obj.response(success=False, message='Does not exist note or user', data=[])

    def read_note_by_user(self, data):
        note = db_obj.session.query(Notes).filter_by(user_id=data['user_id']).all()
        if note:
            json_data = serialize_data(note)
            return obj.response(success=True, message='list of notes by user', data=json_data)
        else:
            return obj.response(success=False, message='Does not exist note or user', data=[])

    def archive_note(self):
        notes = db_obj.fetch_all(model=Notes)
        if notes.is_archived == 1:
            json_data = serialize_data(notes)
            return obj.response(success=True, message="Successfully note is archived", data=json_data)
        else:
            return obj.response(success=False, message="does not exist note")

    def restore_note(self):
        notes = db_obj.fetch_all(model=Notes)
        if notes:
            for note in notes:
                if note.is_restored == 1:
                    json_data = serialize_data(note)
                    return obj.response(success=True, message="Successfully restored notes", data=json_data)
                else:
                    return obj.response(success=False, message="does not exist restored  note")
        else:
            return obj.response(success=False, message="not found note")

    def pin_notes(self):
        notes = db_obj.fetch_all(model=Notes)
        if notes.is_pinned == 1:
            return obj.response(success=True, message="Successfully restored notes")
        else:
            return obj.response(success=False, message="does not exist note")
