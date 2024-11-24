from Repository.MateriiRepository import MaterieRepository
from domain.Validators.materievalidator import MaterieValidator
from domain.materie import Materie


class MaterieService:

    def __init__(self, repository: MaterieRepository, validator: MaterieValidator):
        self.__repository = repository
        self.__validator = validator

    def addMaterie(self, id,nume,profesor):

        materie=Materie(id,nume,profesor)
        self.__validator.ValidateMaterie(materie)
        self.__repository.addMaterie(materie)

    def modifyMaterie(self,id,nume,profesor):

        self.__repository.modifyMaterie(id,nume,profesor)

    def deleteMaterie(self,id):

        self.__repository.deleteMaterie(id)

    def getAllMaterii(self):

        return self.__repository.getAllMaterii()

    def cautareMaterie(self,id_client):

        return self.__repository.cautareMaterie(id_client)