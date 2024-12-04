from random import random
import random

from domain.student import Student
from domain.student import *

class StudentRepositoryException(Exception):
    pass

class StudentRepository:

    def __init__(self):

        self.__students=[]

    def addStudent(self, student):

        for students in self.__students:
            if(students.getIDStudent()==student.getIDStudent()):
                raise StudentRepositoryException()

        self.__students.append(student)

    def modifyStudent(self, idstudent,nume):
        ok=False
        for student in self.__students:
            if(student.getIDStudent()== idstudent):
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
        """
        Search student by id
        :param idstudent:
        :return:
        """

        ok=False
        for student in self.__students:
            if(student.getIDStudent() == idstudent):
                return student
        raise StudentRepositoryException()
    def getAllStudents(self):
        """
        Show all students
        :return:
        """
        return self.__students

    def getRandomStudent(self):
        options=("Andrei","Liviu","Laur","Florin","Cornel","Gigel","Klaus")
        option=random.choice(options)
        return option
