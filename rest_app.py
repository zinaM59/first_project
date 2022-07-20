from flask import Flask, request
from db_connector import DataBase

app = Flask(__name__)

db = DataBase()

# supported methods
@app.route('/data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    print(user_id, request.method)

    if request.method == 'GET':
        try:
            user_name = db.get_user_name(user_id)
            return {"status": "ok", "user_name": user_name}, 200
        except:
            return {"status": "error", "reason": "no such id"}, 500

    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # creating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        try:
            db.create_user(user_id, user_name)
            return {'status': 'ok', 'user_name': user_name}, 200
        except:
            return {'status': 'error', 'reason': 'id already exists'}, 500

    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')

        try:
            db.update_user(user_id, user_name)
            return {'status': 'ok', 'user_updated': user_name}, 200
        except:
            return {'status': 'error', 'reason': "no such id"}, 500

    elif request.method == 'DELETE':
        try:
            db.delete_user(user_id)
            return {'success':'ok'}, 200
        except:
            return {'success':'false'}, 500


app.run(host='127.0.0.1', debug=True, port=5000)
