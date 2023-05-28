import jwt



class JWTService:

    @staticmethod
    def encode(username):
        # TODO: secret 
        encoded_jwt = jwt.encode({"username": username}, "secret", algorithm="HS256")
        return encoded_jwt

    @staticmethod
    def decode(token):
        return jwt.decode(token, "secret", algorithms=["HS256"])