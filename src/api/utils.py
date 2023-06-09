import bcrypt
import bcrypt
import jwt




def get_hashed_password(plain_text_password):

    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):

    return bcrypt.checkpw(plain_text_password, hashed_password)


def get_token(hashed_password):
    encoded_jwt = jwt.encode({'some': hashed_password}, 'secret', algorithm='HS256')

    return encoded_jwt


