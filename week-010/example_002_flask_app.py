from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Not a real way to store data for an actual project.
# Using a global dicitonary just for an example.
users = {
    "Nick": {"name": "Nick", "age": 42, "job": "programmer"},
    "Elvin": {"name": "Elvin", "age": 30, "job": "doctor"},
    "Jim": {"name": "Jim", "age": 22, "job": "salesperson"}
}

class User(Resource):
    def get(self, name):
        if name in users:
            return users[name], 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("job")
        args = parser.parse_args()

        if name in users:
            return f"User with name {name} already exists", 400

        user = {"name": name, "age": args["age"], "job": args["job"]}
        users[name] = user
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("job")
        args = parser.parse_args()

        if name in users:
            users[name]["age"] = args["age"]
            users[name]["job"] = args["job"]
            return users[name], 200

        user = {"name": name, "age": args["age"], "job": args["job"]}
        users[name] =user
        return user, 201

    def delete(self, name):
        global users
        if name in users:
            del users[name]
        return f"{name} is deleted.", 200

class Display(Resource):
    def get(self):
        return users, 200

api.add_resource(Display, "/display/")
api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
