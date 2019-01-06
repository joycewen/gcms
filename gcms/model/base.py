# coding: utf-8

from sqlalchemy import create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from gcms.utils.config import get as config_get
from gcms.utils.exception import DatabaseError

BaseModel = declarative_base()

db_host = config_get("gcms_db", "host")
db_port = config_get("gcms_db", "port")
db_user = config_get("gcms_db", "user")
db_pssswd = config_get("gcms_db", "passwd")
db_database = config_get("gcms_db", "database")

engine = create_engine(
    'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % (db_user, db_pssswd, db_host, db_port, db_database), pool_size=100,
    pool_recycle=3600)
db_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(object):
    def __init__(self):
        self.session = db_session()

    def add(self, instance):
        try:
            self.session.add(instance)
            self.session.flush()
            self.session.commit()
        except Exception, e:
            self.session.rollback()
            raise e

    def delete(self, instance):
        try:
            self.session.delete(instance)
            self.session.flush()
            self.session.commit()
        except Exception, e:
            self.session.rollback()
            raise e

    def first(self, model, is_del=False, **kwargs):
        """

        Args:
            model:
            **kwargs:

        Returns:
        """
        kwargs['is_del'] = is_del
        result = self.session.query(model).filter_by(**kwargs).first()
        return result

    def filter_all(self, model, filters, is_del=False, **kwargs):
        """

        Args:
            model:
            **kwargs:

        Returns:
        """
        kwargs['is_del'] = is_del
        result = self.session.query(model).filter(filters).filter_by(**kwargs).all()
        return result

    def all(self, model, filters=None, page=None, order_by=None, filter_by=None, is_del=False, **kwargs):
        query = self.session.query(model)

        if order_by:
            query = query.order_by(desc(order_by))

        if filter_by:
            kwargs.update(filter_by)
        if filters:
            query = query.filter(filters)
        kwargs['is_del'] = is_del
        query = query.filter_by(**kwargs)

        if page:
            query = query.limit(10).offset(10 * int(page) - 10)

        result = query.all()
        return result

    def count(self, model, is_del=False, **kwargs):
        kwargs['is_del'] = is_del
        return self.session.query(model).filter_by(**kwargs).count()

    def tick(self, instance):
        self.reload(instance)
        instance.tick()

    def commit(self):
        try:
            self.session.flush()
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise DatabaseError(DatabaseError.DATABASE_COMMIT_ERROR, args=str(e))

    def expire(self, instance):
        self.session.expire(instance)

    def refresh(self, instance):
        self.session.refresh(instance)

    def reload(self, instance):
        self.expire(instance)
        self.refresh(instance)

    def flush(self):
        self.session.flush()

    def close(self):
        self.session.close()
        self.session.remove()
