import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, SMALLINT, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Base(object):
    """Created Base class model """
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )


DeclarativeBase = declarative_base(cls=Base)


class Users(DeclarativeBase):
    """ This class is used to create the user information table in database """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=True)
    last_name = Column(String(80), nullable=True)
    password = Column(String(90), nullable=False)
    email = Column(String(90), nullable=False)
    notes = relationship('Notes', secondary='association_table')


class Notes(DeclarativeBase):
    """ Notes class is used to create note information table in database"""
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(50), nullable=True)
    color = Column(String(20), nullable=False)
    is_archived = Column(SMALLINT, nullable=False)
    is_deleted = Column(SMALLINT, nullable=False)
    is_trashed = Column(SMALLINT, nullable=False)
    is_restored = Column(SMALLINT, nullable=False)
    is_pinned = Column(SMALLINT, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users, secondary='association_table', )


class AssociationTable(DeclarativeBase):
    """ this tabel is used to store the both key in table"""
    __tablename__ = 'association_table'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    note_id = Column(Integer, ForeignKey('notes.id'), primary_key=True)
