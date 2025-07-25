import uuid
import bcrypt
from .connection import engine
import sqlalchemy as db

class UserDB:
    def __init__(self):
        pass

    def createRootUser(self):
        password = "xxxxxxxxx"
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        password = hashed_password.decode('utf-8')

        metadata_obj = db.MetaData()
        User = db.Table("User", metadata_obj, autoload_with=engine)

        stmt = db.insert(User).values(
            id = uuid.uuid4().hex,
            name = 'Sokhavuth',
            email = 'xxxxxxxxxxxx',
            password = password,
            role = 'Admin',
            thumb = '',
            content = '',
            date = ''
        )

        with engine.begin() as conn:
            conn.execute(stmt)

    def checkUser(self, email):
        metadata_obj = db.MetaData()
        User = db.Table("User", metadata_obj, autoload_with=engine)

        stmt = db.select(User).where(User.c.email == email)
        with engine.begin() as conn:
            result = conn.execute(stmt)
            return result
                

userDB = UserDB()