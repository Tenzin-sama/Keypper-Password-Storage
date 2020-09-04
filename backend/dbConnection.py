import mysql.connector

# there are two tables in the database:
# +users (userid and password for login/signup)
# +data (<userid> <account> <email> <username> <password>)

class dbK:
    def __init__(self):
        self.my_connection = mysql.connector.connect(
            host='localhost',
            user="root",
            passwd="temppass",
            database="keypper"
        )
        self.my_cursor = self.my_connection.cursor()

    def add_users(self, qry, values):
        """ execute sql code for adding new userid or deleting old data to users/data table"""
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()

    def check_user(self, qry, userid):
        """ execute sql codes to check if given userid exists"""
        val = userid
        self.my_cursor.execute(qry)
        myresult = self.my_cursor.fetchall()
        for x in myresult:
            if val in x:
                return True
        return False

    def check_pass(self, qry, userid, password):
        """ execute sql codes to check password"""
        val = password
        self.my_cursor.execute(qry, userid)
        myresult = self.my_cursor.fetchone()
        for x in myresult:
            if val in x:
                return True
        return False

    def add_data(self,qry, values):
        """ execute sql code to add new data to data table"""
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()

    def show_data(self, qry, val):
        """ execute sql code to show data"""
        self.my_cursor.execute(qry, val)
        data = self.my_cursor.fetchall()
        return data

    def show_id(self, qry, val):
        self.my_cursor.execute(qry, val)
        myresult = self.my_cursor.fetchone()

