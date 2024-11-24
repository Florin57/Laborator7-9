class Materie:
    def __init__(self,idMaterie,nume,profesor):
        self.__id_materie = idMaterie
        self.__nume_materie = nume
        self.__profesor_materie = profesor

    def GetIDMaterie(self):
        return self.__id_materie

    def GetNumeMaterie(self):
        return self.__nume_materie

    def GetProfesorMaterie(self):
        return self.__profesor_materie

    def SetIDMaterie(self,id):
        self.__id_materie=id

    def SetNumeMaterie(self,nume):
        self.__nume_materie=nume

    def setProfesor(self,profesor):
        self.__profesor_materie=profesor

    @staticmethod
    def TestMaterie():
        m=Materie(1,"Romana", "Ciprian")
        assert m.GetIDMaterie()==1
        assert m.GetNumeMaterie()=="Romana"
        assert m.GetProfesorMaterie()=="Ciprian"
        m.SetIDMaterie(3)
        assert m.GetIDMaterie()==3
Materie.TestMaterie()

