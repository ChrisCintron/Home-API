import sqlite3
import json


conn = sqlite3.connect('../../main_db.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()


#Make test for this
def get_userinfo(*username):
    if not username:
        query = "SELECT * FROM userinfo"
    else:
        print("PASSED")
        query = "SELECT * FROM userinfo WHERE user_name= '{}'".format(*username)
    #print(query)
    c.execute(query)
    mydata = c.fetchall()
    #figure out how this works
    myobj = json.dumps([dict(ix) for ix in mydata])
    return myobj
