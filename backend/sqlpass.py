from backend.dbConnection import dbK

# TABLE users = <id> <userid> <password>
# TABLE data = <id> <userid> <account> <email> <username> <password>
class data:
    def __init__(self):
        self.db = dbK()

    def add_user(self, userid, password):
        """ add new users to users table"""
        qry = "INSERT INTO users (userid, password) VALUES (%s, %s)"
        values = (userid, password)
        self.db.add_users(qry, values)
        return True

    def check_user(self, userid):
        """ check if given userid exists in users table"""
        qry = "SELECT userid FROM users"
        user_exists = self.db.check_user(qry, userid)
        return user_exists

    def check_pass(self, userid, password):
        """ check if the password for given userid matches or not in users table"""
        qry = "SELECT password FROM users WHERE userid = %s"
        userid = (userid,)
        pass_confirm = self.db.check_pass(qry, userid, password)
        return pass_confirm

    def add_data(self,userid, account, email, username, password):
        """ add new users to users table"""
        qry = "INSERT INTO data (userid, account, email, username, password) VALUES (%s, %s, %s, %s, %s)"
        values = (userid, account, email, username, password)
        self.db.add_data(qry, values)
        return True

    def show_data(self, userid):
        """show the data stored in data table"""
        # retieve id from users
        qry = "SELECT account, email, username, password FROM data WHERE userid = %s"
        val = (userid, )
        data = self.db.show_data(qry, val)
        return data

    def show_users(self, userid):
        """show the data stored in data table"""
        # retieve id from users
        qry = "SELECT userid, password FROM users WHERE userid = %s"
        val = (userid,)
        data = self.db.show_data(qry, val)
        return data

    def search_acc(self, userid, account):
        """ when searching for specific accounts"""
        qry = "SELECT account, email, username, password FROM data WHERE userid= %s AND account = %s"
        val = (userid, account)
        data = self.db.show_data(qry, val)
        return data

    def delete_item(self,userid, account, username):
        """ delete data according to their account and username"""
        qry = "DELETE FROM data WHERE userid= %s AND account = %s and username = %s"
        values = (userid, account, username)
        self.db.add_users(qry, values)
        return True

    def sort_dataDesc(self, userid):
        """ to sort data by account in decending form"""
        qry = "SELECT account, email, username, password FROM data WHERE userid = %s ORDER BY account DESC"
        val = (userid,)
        data = self.db.show_data(qry, val)
        return data

    def sort_dataAsc(self, userid):
        """ to sort data by account in ascending form"""
        qry = "SELECT account, email, username, password FROM data WHERE userid = %s ORDER BY account"
        val = (userid,)
        data = self.db.show_data(qry, val)
        return data
#


