import sqlite3
from flask_restful import Resource, reqparse


#parser = reqparse.RequestParser()
#parser.add_argument('username', type=int, help='The user username')
#parser.add_argument('password', type=str, help="The password")
#args = parser.parse_args()



parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('userid')


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
        database.connection.commit()
        database.disconnect()
        return results

class AllUsersInfo(Resource):
    def get(self):
        query = "SELECT * FROM userinfo"
        mydata = DB_Gateway.request(query)
        results = [dict(ix) for ix in mydata]
        return results

    def put(self):
        args = parser.parse_args() #Args comes in {'username': "jeff", 'password': 'pass12'}
        query = "INSERT INTO userinfo (user_name,user_password) values ('{}','{}');".format(args['username'],args['password'])
        mydata = DB_Gateway.request(query)
        results = "Success: User was PUT!"
        return results

    def delete(self):
        args = parser.parse_args()
        query = "DELETE FROM userinfo where user_id='{}';".format(args['userid'])
        mydata = DB_Gateway.request(query)
        results = "Success: User_id [{}] was DELETED!".format(args['userid'])
        return results



class UserInfo(Resource):
    def get(self,username):
        query = "SELECT * FROM userinfo WHERE user_name= '{}'".format(username)
        mydata = DB_Gateway.request(query)
        results = [dict(ix) for ix in mydata]
        return results
