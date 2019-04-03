import jwt
from passlib.hash import pbkdf2_sha256

def new_token(name,password):
    #password_hash = hashlib.md5(password.encode()).hexdigest()
    token = pbkdf2_sha256.using(salt_size=6).hash("test")
    encoded = jwt.encode({"password":password},token,algorithm="HS256")
    return{"hash":encoded,"token":token}
