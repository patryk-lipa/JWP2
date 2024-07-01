from flask import Blueprint, current_app, redirect, render_template, session, url_for, request
import jwt
from app.repository import UserRepository
from app.model import db, user_schema
from sqlalchemy.exc import SQLAlchemyError

login_bp = Blueprint('login', __name__, template_folder='templates')
user_repo = UserRepository(db)

@login_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html', logged_in=session.get('logged_in'), register=False)

@login_bp.route('/register', methods=['GET'])
def register():
    return render_template('index.html', logged_in=session.get('logged_in'), register=True)

@login_bp.route('/login', methods=['GET'])
def login():
    return redirect(url_for('login.index'))

@login_bp.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login.index'))

@login_bp.route('/user', methods=['POST'])
def create_user():
    name = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    user = user_repo.create(name, password, email)
    message = "Note created successfully"
    new_user_json = user_schema.dump(user)

    return {"message": message, "note": new_user_json}, 201

@login_bp.route('/auth', methods=['POST'])
def auth():
    name = request.form.get('username')
    password = request.form.get('password')
    print(name, password)
    try:
        user = user_repo.find_by_username(name)
        if not user or not user.password == password:
            raise SQLAlchemyError('not found')
        print(user)
    except SQLAlchemyError as err:
        return {'error': 'account does not exist'}, 401
    token = jwt.encode({'user': user.username}, current_app.config['SECRET_KEY'], algorithm='HS256')
    session['logged_in'] = True
    return {'access_token': token}

