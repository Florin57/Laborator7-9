from domain.student import Student
class StudentValidatorException(Exception):
    def __init__(self, errors):
        self.__errors = errors

    def getErrors(self):
        """
        Functie care returneaza suma erorilor unui student
        :return:
        """
        return self.__errors

class StudentValidator:

   def ValidateStudent(self, s: Student):
        errors = ""
        id_student=0
        try:
            if (int(s.getIDStudent()) < 0):
                errors += "Invalid Student Id!"
        except:
            errors += "Id Student must be an integer!"
        if(s.getNumeStudent()==""):
            errors+="Invalid Student name!"
        if(len(errors)>0):
            raise StudentValidatorException(errors)

def TestStudentValidator():
    student=Student(1,"Cornel")
    validator=StudentValidator()
    try:
        validator.ValidateStudent(student)
        assert False
    except:
        assert True
    student = Student(1, "Florin")
    validator.ValidateStudent(student)
    student = Student(1, "")
    try:
        validator.ValidateStudent(student)
        assert False
    except:
        assert True
TestStudentValidator()