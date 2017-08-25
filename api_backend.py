import sqlite3
from flask_restful import Resource


#Make test for these
class DB(object):
    def __init__(self):
        local_db_path = '../Project_files/main_db.db'
        self.connection = sqlite3.connect(local_db_path)
        self.connection.row_factory = sqlite3.Row
        self.c = self.connection.cursor() #Used for interacting with DB

    def disconnect(self):
        self.connection.close()


class DB_Gateway:
    def request(query): #Opens, Queries, then closes the database
        database = DB()
        database.c.execute(query)
        results = database.c.fetchall()
        database.disconnect()
        return results

class AllUsersInfo(Resource):
    def get(self):
        query = """SELECT * FROM userinfo"""
        mydata = DB_Gateway.request(query)
        results = [dict(ix) for ix in mydata]
        return results

class UserInfo(Resource):
    def get(self,username):
        query = "SELECT * FROM userinfo WHERE user_name= '{}'".format(username)
        mydata = DB_Gateway.request(query)
        results = [dict(ix) for ix in mydata]
        return results
