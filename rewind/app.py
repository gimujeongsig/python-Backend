from flask import Flask, jsonify, request
app = Flask(__name__)
app.users = {}
app.posts = []
app.idCnt = 1

@app.route('/sign-up', methods=['POST'])
def signUp():
    newUser = request.json
    newUser['id'] = app.idCnt
    app.users[app.idCnt] = newUser
    app.idCnt += 1
    return jsonify(newUser)

@app.route('/post', methods=['POST'])
def post():
    payload = request.json
    userID = int(payload['id'])
    msg = payload['msg']

    if userID not in app.users:
        return 'user not found', 400
    if len(msg) > 300:
        return '300 over',400

    app.posts.append({
        'user_id' : userID,
        'post' : msg
    })
    return 'complete', 200
    

if __name__ == '__main__':
    app.run()