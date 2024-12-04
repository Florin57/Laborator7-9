from domain.materie import Materie

class MaterieValidatorException(Exception):
    def __init__(self, errors):
        self.errors = errors
    def getErrors(self):
        return self.errors

class MaterieValidator:

    def ValidateMaterie(self, m:Materie):
        """

        :param m: Materie(id_materie,Nume,Profesor)
        :return:
        """
        errors = ""
        id_materie = 0
        try:
            if(int(m.GetIDMaterie())<0):
                errors += "IDMaterie must be positive\n"
        except:
            errors += "IDMaterie must be an integer\n"
        if(m.GetNumeMaterie()==""):
            errors += "Nume de materie invalid\n"
        if(m.GetProfesorMaterie()==""):
            errors += "Nume de profesor invalid\n"
        if(len(errors)>0):
            raise MaterieValidatorException(errors)
    @staticmethod
    def TestMaterieValidator():
        materie= Materie(1,"Mate","Ionut")
        validator = MaterieValidator()
        try:
            validator.ValidateMaterie(materie)
            assert False
        except:
            assert True
        materie= Materie(1,"Mate","Ionut")
        validator = MaterieValidator()
        materie= Materie(1,"Mate","")
        try:
            validator.ValidateMaterie(materie)
            assert False
        except:
            assert True
MaterieValidator.TestMaterieValidator()


