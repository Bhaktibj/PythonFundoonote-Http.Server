# import lib
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import warnings
pymysql.install_as_MySQLdb()
from setting import DATABASE, MYSQL_DB_CONFIG, logger
from ..models.model import DeclarativeBase

with warnings.catch_warnings():   # with warnings
    warnings.simplefilter('ignore') # if warning just ignore that
    try:
        db_engine = create_engine(
            'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'.format(**MYSQL_DB_CONFIG))
        db_engine.execute("CREATE DATABASE IF NOT EXISTS {} ".format(MYSQL_DB_CONFIG.get("db_name"))) # create the engin
        logger.info("mysql database connected: {}".format(db_engine))
        DeclarativeBase.metadata.create_all(db_engine)  # create all engine
    except:
        raise Exception("Connection error") # if database not created or connection failed


def db_session():
    """ this method is used to create the session"""
    try:
        if db_engine:   # if db_engine
            Session = sessionmaker()  # create session using sessionmaker() lib
            Session.configure(bind=db_engine)  # configure engine
            session = Session()
            return session  # return session object
    except:
        raise Exception("connection error") # if database is not created

