from flask import Flask
import api


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/query/v1.0/")
def api_main_page():
    return "getuserdata: /api/query/v1.0/userinfo"

@app.route("/api/query/v1.0/userinfo", methods=['GET'])
def get_userinfo():
    return api.get_userinfo()

@app.route("/api/query/v1.0/userinfo/<username>", methods=['GET'])
def get_userinfo_by_username(username):
    return api.get_userinfo(username)


if __name__ == '__main__':
    app.run()
