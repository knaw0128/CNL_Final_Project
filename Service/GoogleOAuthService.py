from Service.BaseOAuthService import BaseOAuthService

class GoogleOAuthService(BaseOAuthService):
    def __init__(self):
        pass

    def InsertStudentInfo(self, token, coursekey):
        return super().InsertStudentInfo(token, coursekey)