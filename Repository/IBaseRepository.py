class IBaseRepository:
    def __init__(self, repoType) -> None:
        self.RepoType = repoType

    def Create(self, newData):
        raise NotImplementedError

    def Read(self, primarykey):
        raise NotImplementedError

    def Update(self, newData, primarykey):
        raise NotImplementedError

    def Delete(self, primarykey):
        raise NotImplementedError