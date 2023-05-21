from BaseOAuth import BaseOAuth

class GoogleOAuth(BaseOAuth):
    def __init__(self):
        pass

    def InsertStudentInfo(self, token, coursekey):
        return super().InsertStudentInfo(token, coursekey)