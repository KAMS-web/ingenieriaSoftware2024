from flask import Flask, jsonify, request 

app= Flask(__name__)

#endpoint raiz
@app.route("/")
def root():
    return "hola mundo"


@app.route("/users/<user_id>")
def get_user(user_id):
    user = {
        "id": user_id,
        "name": "kevin",
        "telefono": "75492901"
    }

    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    data["status"] = "user created"
    return jsonify(data), 201

def update_user(users_id):
    data = request.get_json()
    update_user = {
        "id": users_id,
        "name": data.get("name", "kevin"),
        "telefono": data.get("telefono", "75492901"),
        "status": "user updated"
    }
    return jsonify(update_user)

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    reponse = {
        "id": user_id,
        "status": "user deleted"
    }
    return jsonify(reponse), 200

if __name__=='__main__':
    app.run(debug=True) 
