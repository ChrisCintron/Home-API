import sqlite3
from flask_restful import Resource


conn = sqlite3.connect('../Project_files/main_db.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

#Make test for these
class AllUsersInfo(Resource):
    def get(self):
        query = "SELECT * FROM userinfo"
        c.execute(query)
        mydata = c.fetchall()
        results = [dict(ix) for ix in mydata]
        return results

class UserInfo(Resource):
    def get(self,username):
        query = "SELECT * FROM userinfo WHERE user_name= '{}'".format(username)
        c.execute(query)
        mydata = c.fetchall()
        results = [dict(ix) for ix in mydata]
        return results
