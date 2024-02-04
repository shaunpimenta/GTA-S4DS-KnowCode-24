from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/api/v1/user-login', methods=['GET,POST'])
def login():
    print("Logged In")
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/api/v1/', methods=['GET,POST'])
def signup():
    print(request.data)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/api/v1/user-me', methods=['GET'])
def userdata():
    print("Test")
    data = {
        'sId': "1",
        'fullName': "Shaun Pimenta",
        'email': "test@gmail.com",
        'password': "12345",
        'gender': "Male",
        'weight': 50,
        'height': 180,
        'bmi': 100,
        'createdAt': "1:00:00",
    }

    # Sending data with a 200 response
    return json.dumps(data), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
