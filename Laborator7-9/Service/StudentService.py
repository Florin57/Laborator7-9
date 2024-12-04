from Repository.StudentRepository import StudentRepository
from domain.Validators.studentvalidator import StudentValidator
from domain.student import Student


class StudentService:

    def __init__(self, repository: StudentRepository, validator: StudentValidator):
        self.repository = repository
        self.validator = validator

    def addStudent(self,id,nume):

        student=Student(id,nume)
        self.validator.ValidateStudent(student)
        self.repository.addStudent(student)

    def modifyStudent(self,id,nume):
        self.repository.modifyStudent(id,nume)

    def deleteStudent(self,id):

        self.repository.deleteStudent(id)

    def getAllStudenti(self):

        return self.repository.getAllStudents()

    def cautareStudent(self,id_student):

        return self.repository.cautareStudent(id_student)

    def getRandomStudent(self):
        return self.repository.getRandomStudent()

