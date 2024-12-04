class Note:
    def __init__(self,id_nota,st, mat,note):
        self.__st = st
        self.__id = id_nota
        self.__mat = mat
        self.__note = note
    def getid(self):
        return self.__id
    def getStudent(self):
        return self.__st
    def getMat(self):
        return self.__mat
    def getNote(self):
        return self.__note
    def setid(self,id_nota):
        self.__id = id_nota
    def setStudent(self, st):
        self.__st = st
    def setMat(self, mat):
        self.__mat = mat
    def setNote(self, note):
        self.__note = note