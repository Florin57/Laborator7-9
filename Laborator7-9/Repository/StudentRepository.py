from domain import student
from domain.student import *

class StudentRepositoryException(Exception):
    pass

class StudentRepository:

    def __init__(self):

        self.__students=[]

    def addStudent(self, student):

        for student in self.__students:
            if(student.GetIDStudent()==student.GetIdStudent()):
                raise StudentRepositoryException()

        self.__students.append(student)

    def modifyStudent(self, idstudent,nume):

        ok=False
        for student in self.__students:
            if(int(student.GetIDStudent())== idstudent):
                if(nume!=""):
                    student.setNumeStudent(nume)
                if(len(str(idstudent))>0):
                    student.setIDStudent(str(idstudent))
                ok=True
        if(ok==False):
            raise StudentRepositoryException()

    def deleteStudent(self, idstudent):

        ok=False
        for student in self.__students:
            if(student.getIDStudent() == idstudent):
                self.__students.remove(student)
                ok=True
        if(ok==False):
            raise StudentRepositoryException()
    def cautareStudent(self,idstudent):

        ok=False
        for student in self.__students:
            if(student.GetIDStudent() == idstudent):
                return student
        raise StudentRepositoryException()
    def getAllStudents(self):
        return self.__students