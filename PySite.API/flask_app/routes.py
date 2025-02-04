from flask_app import app
from flask import jsonify, request

# Add initial User
current_id = 0
users = {str(current_id): {"name": "Tommy"}}


@app.route("/api/users", methods=["GET", "POST"])
def handle_users():
    global current_id
    if request.method == "GET":
        return jsonify({"users": users})

    elif request.method == "POST":
        # Recieved new request to add a user
        try:
            data = request.get_json()
            print("printing the data recieved from frontend", data)
            current_id += 1
            users[str(current_id)] = data

            return jsonify({"message": "Users updated successfully"})
        except Exception as e:
            print("Error occured: ", e)
            return jsonify({"message": "could not update users"}), 500


@app.route("/api/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def handle_user(user_id):
    """
    This function takes an ID as dynamic URL parameter, for example 0
    Note:
    - GET method is only available for debugging purposes, to test for a specific user
    open the browser with for example http://localhost:5000/api/users/0 to see the data

    - The assignment is to implement the PUT and DELETE methods for the specific ID, see assignment for specific instructions
    """
    if user_id in users:
        if request.method == "GET":
            return jsonify(users[user_id])
        elif request.method == "PUT":
            try:
                data = request.get_json()
                users[user_id] = data
                return jsonify({"message": "username updated"}) 
            except Exception as e:
                print("Update error: ", e)
                return jsonify({"message": "Failed to update user"})
        elif request.method == "DELETE":
            try: 
                del users[user_id]
                return jsonify({"message: User Deleted"})
            except Exception as e:
                print("Delete error:", e)
                return jsonify({"message": "Failed to delete user"})
    else:
        return jsonify({"message": "User not found"}), 404
