import Repository.BaseRepository as repo

class AccountService:
    def __init__(self) -> None:
        self.repo = repo.BaseRepository(UserAccount)

    def register(self, username, password):
        # input: username, password
        # output: baserepo create

        pass

    def login(self, username, password):
        # input: username, password
        # send username to baserepo read
        # it returns the correct password
        # this function checks it's correct or not
        pass

    def logout(self, username):
        # input: username
        # clean the cookie
        pass

    