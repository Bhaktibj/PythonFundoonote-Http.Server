from easy_profile import SessionProfiler
from sqlalchemy import Column, Integer, String, ForeignKey, SMALLINT
from sqlalchemy.orm import validates

# from fundooNotes.config.database_connection import Base, session
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import LONGBLOB
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
from sqlalchemy.orm import sessionmaker
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
profiler = SessionProfiler()
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    password = Column(String(90), nullable=False)
    email = Column(String(90), nullable=False)
    image = Column(LONGBLOB)
    notes = relationship('Notes', secondary='association_table')

    @validates('email')
    def validates_email(self, key, address):
        assert '@gmail' in address
        return address


class Notes(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    color = Column(String(20), nullable=False)
    is_archived = Column(SMALLINT)
    is_deleted = Column(SMALLINT)
    is_trashed = Column(SMALLINT)
    is_restored = Column(SMALLINT)
    is_pinned = Column(SMALLINT)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users, secondary='association_table')


class AssociationTable(Base):
    __tablename__ = 'association_table'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    note_id = Column(Integer, ForeignKey('notes.id'), primary_key=True)


