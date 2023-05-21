from IBaseRepository import IBaseRepository

class BaseRepository(IBaseRepository):
    def __init__(self, repoType) -> None:
        super().__init__(repoType)

    def Create(self, newData):
        return super().Create(newData)
    
    def Read(self, primarykey):
        return super().Read(primarykey)
    
    def Update(self, newData, primarykey):
        return super().Update(newData, primarykey)
    
    def Delete(self, primarykey):
        return super().Delete(primarykey)