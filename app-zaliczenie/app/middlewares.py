from functools import wraps
from flask import current_app, request, g, abort
from jwt import decode, exceptions
import json

def auth_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        authorizaton = request.headers.get('Authorizaton', None)
        if not authorizaton:
            resp =  json.dumps({'error': 'no authorization provided'})
            return resp, 401, {'Content-Type': 'application/json'}
        try:
            token = authorizaton.split(' ')[1]
            resp = decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            g.user = resp['user']
        except exceptions.DecodeError as e:
            resp =  json.dumps({'error': 'invalid authorization token'})
            return resp, 401, {'Content-Type': 'application/json'}
        return f(*args, **kwargs)
    return wrap


