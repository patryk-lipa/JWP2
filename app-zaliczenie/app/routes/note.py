from flask import Blueprint, request
from marshmallow import ValidationError
from app.repository import NoteRepository
from app.model import db, notes_schema, note_schema
from app.middlewares import auth_required

note_bp = Blueprint('note', __name__, url_prefix='/api/note')
note_repo = NoteRepository(db)


@note_bp.route('/', methods=['GET'])
@auth_required
def all_notes():
    note  = notes_schema.dump(note_repo.find_all())
    return note

@note_bp.route('/<int:id>', methods=['GET'])
@auth_required
def get_note(id):
    note  = note_schema.dump(note_repo.find(id))
    return note

@note_bp.route('/', methods=['POST'])
@auth_required
def create_note():
    json_data = request.get_json()
    if not json_data:
        return {'message': 'No input data provided'}, 400

    title, content = process_upsert(json_data)

    new_note = note_repo.create(title, content)
    message = "Note created successfully"
    new_note_json = note_schema.dump(new_note)

    return {"message": message, "note": new_note_json}, 201

@note_bp.route('/<int:id>', methods=['PUT'])
@auth_required
def update_note(id):
    json_data = request.get_json()
    if not json_data:
        return {'message': 'No input data provided'}, 400

    title, content = process_upsert(json_data)

    new_note = note_schema.dump(note_repo.update(id, title, content))
    message = "Note updated successfully"
    new_note_json = note_schema.dump(new_note)

    return {"message": message, "note": new_note_json}, 200

@note_bp.route('/<int:id>', methods=['DELETE'])
@auth_required
def delete_note(id):
    note_repo.delete(id)
    return {"message": "Note deleted successfully"}, 200

def process_upsert(data):
    try:
        note = note_schema.load(data)
    except ValidationError as err:
        return err.messages, 422
    
    title, content = note['title'], note['content']
    return title, content
