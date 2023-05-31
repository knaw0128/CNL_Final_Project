from Service.BaseOAuthService import BaseOAuthService

class GoogleOAuthService(BaseOAuthService):
    def __init__(self):
        pass

    def InsertStudentInfo(self, access_token, status):
        # I should extract student id from the token
        return super().InsertStudentInfo(token, coursekey)