import Repository.BaseRepository as repo
from Model.UserAccount import UserAccount

class AccountService:
    def __init__(self) -> None:
        self.repo = repo.BaseRepository(UserAccount)

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
        instance = self.repo.Read(UserInfo)
        if instance.password == userAccount.password:
            return True
        else:
            return False 

    def Logout(self, username):
        # input: username
        # clean the cookie
        pass
    def Login(account:str,password:str):
        pass
    def Register(account:str,password:str):
        pass
    def Logout(account:str):
        pass

    