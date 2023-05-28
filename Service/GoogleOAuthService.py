from Service.BaseOAuthService import BaseOAuthService

class GoogleOAuthService(BaseOAuthService):
    def __init__(self):
        pass

    def InsertStudentInfo(self, token, coursekey):
        # I should extract student id from the token
        return super().InsertStudentInfo(token, coursekey)