from .model import Note, User


class NoteRepository:
    def __init__(self, db):
        self.db = db

    def create(self, title, content):
        note = Note(title=title, content=content)
        self.db.session.add(note)
        self.db.session.commit()
        return note

    def find(self, id):
        return Note.query.get_or_404(id)

    def find_all(self):
        notes = Note.query.all()
        return notes

    def update(self, id, title, content):
        note = Note.query.get_or_404(id)
        note.title = title
        note.content = content
        self.db.session.commit()
        return note

    def delete(self, id):
        note = Note.query.get_or_404(id)
        self.db.session.delete(note)
        self.db.session.commit()



class UserRepository:
    def __init__(self, db):
        self.db = db

    def create(self, username, password, email):
        user = User(username=username, password=password, email=email)
        self.db.session.add(user)
        self.db.session.commit()

    def find(self, id):
        return User.query.get_or_404(id)

    def find_by_username(self, username):
        return User.query.filter_by(username=username).first()

