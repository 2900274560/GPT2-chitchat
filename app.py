import json
import logging

from flask import Flask, request

from app_util import chat

"""
curl -# -X POST -H "Content-Type: application/json"  -d '{"token":"2bf8eda6303bc094ad34c935e79da587"}' http://127.0.0.1:5000/XxXxSQL -o face.sql.des3
"""

logger = logging.getLogger(__file__)

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


userinfo_data = {}


def get_userinfo(username):
    userinfo = userinfo_data.get(username)
    if not userinfo:
        userinfo = {'username': username, 'history': []}
        userinfo_data[username] = userinfo
    return userinfo


@app.route('/chat', methods=['POST', "GET"])
def robot_chat():
    if request.get_json():
        msg = request.get_json().get('msg')
        username = request.get_json().get('username')
        if username:
            userinfo = get_userinfo(username)
            try:
                text, userinfo['history'] = chat.chat(userinfo, msg)
                print(f"{username}:{msg}   robot:{text}")
            except Exception as e:
                userinfo['history'] = []
                text = ''
                print(f"error {username}:{msg}   robot:{text} {e}")
            return json.dumps({'username': username, 'replay': text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=23695, debug=False)
