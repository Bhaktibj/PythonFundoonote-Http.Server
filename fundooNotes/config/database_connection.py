import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
pymysql.install_as_MySQLdb()




from setting import ConfigService

obj = ConfigService()

Base = declarative_base()


class DatabaseService:

    def __init__(self):
        self.session = self.connect()

    def connect(self):
        try:
            engine = create_engine(
                obj.DATABASE['database']
            )
            Base = declarative_base()
            Base.metadata.create_all(engine)
            DBSession = sessionmaker(bind=engine)
            session = DBSession()
            obj.logger.info("==========> database is connected: {}".format(engine))
            return session
        except:
            return "database connection failed"

    def save_into_db(self, obj):
        try:
            if obj is not None:
                self.session.add(obj)
                self.session.commit()
                self.session.close()
        except:
            return False
        return True

    def filter_by(self, tabel, email):
        var = self.session.query(tabel).filter_by(email=email).first()
        return var

    def filter_by_id(self, model, id):
        id = self.session.query(model).filter_by(id=id).first()
        return id

    def filter_by_all(self, model, id):
        id = self.session.query(model).filter_by(id=id).all()
        return id

    def update_query(self, tabel, email, password):
        reset_password = self.session.query(tabel).filter_by(email=email).update({tabel.password: password},
                                                                                 synchronize_session=False)
        self.session.commit()
        self.session.close()
        return reset_password

    def fetch_all(self, model):
        data = self.session.query(model).all()
        return data

    def delete_data_from_db(self, model, id):
        obj = self.session.query(model).filter_by(id=id).first()
        if obj is not None:
            self.session.delete(obj)
            self.session.commit()
            self.session.close()
            return True
        else:
            return False
