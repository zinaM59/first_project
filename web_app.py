from flask import Flask, request
from db_connector import DataBase

app = Flask(__name__)

db = DataBase()

# supported methods
@app.route("/users/get_user_name/<user_id>")
def get_user_name(user_id):
    user_name = db.get_user_name(user_id)
    if user_name == None:
        return "<H1 id='error'>no such user:" + user_id + "</H1>"
    else:
        return "<H1 id='user'>" + user_name + "</H1>"


app.run(host='127.0.0.1', debug=True, port=5001)
