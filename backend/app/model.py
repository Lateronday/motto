from app.extension import db
from datetime import datetime
import uuid


class BasicModel(db.Model):

    __abstract__ = True

    id = db.Column(db.String(64), primary_key=True, unique=True, nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    def init_id(self):
        self.id = str(uuid.uuid4().hex)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Motto(BasicModel):

    __tablename__ = 'motto'

    content = db.Column(db.Text, unique=True, nullable=False)
    tag = db.Column(db.String(64), unique=True, nullable=False, default='all')
    source = db.Column(db.String(64), nullable=True, index=True)

    def __repr__(self):
        return '<Motto %r>' % self.id
