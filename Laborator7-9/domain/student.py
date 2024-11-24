class Student():
    def __init__(self,idstudent,nume):
        self.__nume_student = nume
        self.__id_student = idstudent

    def getIDStudent(self):
        return self.__id_student

    def getNumeStudent(self):
        return self.__nume_student

    def setNumeStudent(self,name):
        self.__nume_student = name

    def setIDStudent(self,id):
        self.__id_student = id

    @staticmethod
    def TestStudent():
        s=Student(1,"Andrei")
        assert s.getNumeStudent()=="Andrei"
        assert s.getIDStudent()==1
        s.setIDStudent(2)
        assert s.getIDStudent()==2
Student.TestStudent()

