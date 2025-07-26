import uuid
import bcrypt
from .connection import conn

class UserDB:
    def __init__(self):
        pass

    def createRootUser(self):
        password = "xxxxxxxxxxx"
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        password = hashed_password.decode('utf-8')

        user_data = (uuid.uuid4().hex, 'Sokhavuth', 'sokhavuth@khmerweb.app', password, 'Admin', '', '', '')

        conn.execute("INSERT INTO User VALUES (?,?,?,?,?,?,?,?);", user_data)
        conn.commit()

        conn.sync()
        

    def checkUser(self, email):
        sql = f"SELECT * FROM User WHERE email='{email}'"
        result = conn.execute(sql)
        rows = result.fetchall()
        return rows
                
userDB = UserDB()