from marshmallow import Schema, fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Note(db.Model):
    __tablename__ = 'note'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title: Mapped[str] = mapped_column(db.String(50), nullable=False)
    content: Mapped[str] = mapped_column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f'Note(id={self.id}, name={self.title}, content={self.content})'

class NoteSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    content = fields.String()
    # user_id = fields.Integer()

class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.Text, nullable=False)
    email: Mapped[str] = mapped_column(db.Text, nullable=True)

    def __repr__(self) -> str:
        return f'User(id={self.id}, username={self.username}, pasword={self.password})'

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String()
    password = fields.String()
    email = fields.String()
    # user_id = fields.Integer()
note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)

user_schema = UserSchema()
