import Repository.BaseRepository as repo
from Model.UserAccount import UserAccount
from Service.JWTService import JWTService

class AccountService:
    def __init__(self) -> None:
        self.repo = repo.BaseRepository(UserAccount)
        self.jwtService = JWTService()

    def Register(self, userAccount):
        # input: username, password
        # output: baserepo create
        d = {'ID': userAccount.ID, 'password': userAccount.password}
        instance = UserAccount(**d)
        self.repo.Create(instance)

    def Login(self, userAccount):
        # input: username, password
        # send username to baserepo read
        # it returns the correct password
        # this function checks it's correct or not
        d = {'ID':userAccount.ID,'password':None}
        UserInfo = UserAccount(**d)
        all_instance = self.repo.Read(UserInfo)
        same = False
        print(userAccount.password)
        for instance in all_instance:
            print(instance.password)
            if userAccount.password == instance.password:
                same = True
        return same

    def Logout(self, username):
        # input: username
        # clean the cookie
        pass
    
    