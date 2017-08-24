from flask import Flask
import api_backend
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return "Home-Api Mainpage"

api.add_resource(api_backend.AllUsersInfo, "/api/query/v1.0/userinfo/" )
api.add_resource(api_backend.UserInfo, "/api/query/v1.0/userinfo/<string:username>")


if __name__ == '__main__':
    app.run()
