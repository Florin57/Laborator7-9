from domain.materie import *

class MaterieRepositoryException(Exception):
    pass

class MaterieRepository:

    """
    clasa pentru stocarea datelor de tip materoe
    permite folosierea "bazei de date" cu materie la cel mai jos nivel, si implementeaza operatiile de
    tip CRUD (Create, Read Update, Delete):
    """
    def __init__(self):
        """
        Lista in care vom salva clienti nostri
        """
        self.__materii=[]

    def addMaterie(self, materie):
        """
        Functie care adauga clientul in lista de clienti
        :param client: parametru de tip client
        """
        for m in self.__materii:
            if(m.GetIDMaterie()==materie.GetIDMaterie()):
                raise MaterieRepositoryException()

        self.__materii.append(materie)

    def modifyMaterie(self, idMaterie,nume,profesor):
        ok=False
        for materie in self.__materii:
            if (int(materie.GetIDMaterie()) == idMaterie):
                if(nume!=""):
                    materie.SetNumeMaterie(nume)
                if(len(str(idMaterie))>0):
                    materie.SetIDMaterie(str(idMaterie))
                if(profesor!=""):
                    materie.setProfesor(profesor)
                ok=True
        if(ok==False):
            raise MaterieRepositoryException()

    def deleteMaterie(self, idMaterie):
        """
        Functie care scoate un client cu id=client_id din lista de clienti
        :param client_id: id-ul clientului care trebuie scos
        Daca nu exista un astfel de client se ridica o eroare
        """
        ok=False
        for materie in self.__materii:
            if(materie.GetIDMaterie() == idMaterie):
                self.__materii.remove(materie)
                ok=True
        if(ok==False):
            raise MaterieRepositoryException()
    def cautareMaterie(self,idMaterie):
        """
        Functie care cauta o client dupa id-ul dat
        :param client_id: de tip int
        :return: returneaza clientul gaisit
        Daca nu gaseste un client ridica o eroare
        """
        ok=False
        for materie in self.__materii:
            if(materie.GetIDMaterie() == idMaterie):
                return materie
        raise MaterieRepositoryException()
    def getAllMaterii(self):
        """
        Functie care retuneaza lista cu clienti
        """
        return self.__materii