from domain.note import *
from domain.materie import *
from domain.student import *

class NoteValidatorException(Exception):
    def __init__(self, errors):
        self.errors = errors
    def getErrors(self):
        return self.errors

class NoteValidator:

    def ValidateNote(self, n:Note):
        """
        Validates a note object.
        :param n:
        :return:
        """
        errors = ""
        try:
            if(int(n.getNote())<0):
                errors += "Invalid Nota Id\n"
        except:
            print("Nota id invalid. Nota id must be an integer.")
        if(len(errors)>0):
            raise NoteValidatorException(errors)
    @staticmethod
    def TestNoteValidator():
        student= Student(1,"Cornel")
        materie = Materie(2,"Matematica","Alin")
        note= Note( 1, 2, 1)
        validator = NoteValidator()
        try:
            validator.ValidateNote(n)
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

