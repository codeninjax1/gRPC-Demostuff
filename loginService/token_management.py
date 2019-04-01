import jwt
import hashlib

def new_token(name,password):
    password_hash = hashlib.md5(password.encode()).hexdigest()
    token = jwt.encode({"password":password},password_hash,algorithm="HS256")
    return{"hash":password_hash,"token":token}
