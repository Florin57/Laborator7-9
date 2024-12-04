import random

from Repository.MateriiRepository import MaterieRepositoryException
from Repository.NoteRepository import NoteRepositoryException
from Repository.StudentRepository import StudentRepositoryException
from Service import StudentService
from Service.MaterieService import MaterieService
from Service.NoteService import NoteService
from domain.Validators.materievalidator import MaterieValidatorException
from domain.Validators.notevalidator import NoteValidatorException
from domain.Validators.studentvalidator import StudentValidatorException



class ConsoleUI:
    def __init__(self, Studentservice:StudentService, Materieservice:MaterieService, Noteservice:NoteService):
        self.__Studentservice = Studentservice
        self.__Materieservice = Materieservice
        self.__Noteservice = Noteservice


    def showMenu(self):
        """
        Displays the menu options to the user.
        """
        print("Menu:")
        print("1. Add Student (type 'addstudent')")
        print("2. Edit Student (type 'editstudent')")
        print("3. Delete Student (type 'deletestudent')")
        print("4. View Student (type 'viewstudent')")
        print("5. Search Student (type 'searchstudent')")
        print("6. Random Student (type 'randomstudent')")
        print("7. Add Materie (type 'addmaterie')")
        print("8. Edit Materie (type 'editmaterie')")
        print("9. Delete Materie (type 'deletematerie')")
        print("10. View Materie (type 'viewmaterie')")
        print("11. Search Materie (type 'searchmaterie')")
        print("12. Add Nota(type 'addnota')")
        print("13. Exit (type 'quit')")

    def add_Student(self):
        """
        Adds a student by taking input from the user.
        """
        id = input("Enter Student ID: ")
        nume = input("Enter Student Name: ")
        try:
            self.__Studentservice.addStudent(id, nume)
            print("Student Added Successfully")
        except StudentRepositoryException:
            print(f"Student ID: {id} Name: {nume} already exists.")
        except StudentValidatorException as e:
            print(f"Validation error: {e}")

    def edit_Student(self):
        """
        Placeholder for editing a student.
        """
        id = input("Enter Student ID: ")
        nume = input("Enter Student Name: ")
        try:
            self.__Studentservice.modifyStudent(id, nume)
            print("Student Edited Successfully")
        except StudentRepositoryException:
            print(f"Student ID: {id} doesn't exist.")

    def delete_Student(self):
        """
        Placeholder for deleting a student.
        """
        id=input("Enter Student ID: ")
        try:
            self.__Studentservice.deleteStudent(id)
        except StudentRepositoryException:
            print(f"Student ID: {id} doesn't exist.")
        print("Student Deleted Successfully")
    def search_Student(self):
        """
        Placeholder for searching a student.
        :return:
        """
        id=input("Enter Student ID: ")
        try:
            print(f"Nume Student:{self.__Studentservice.cautareStudent(id).getNumeStudent()}")
        except StudentRepositoryException:
            print(f"Student ID: {id} doesn't exist.")

    def show_All_Students(self):
        """
        Shows all students.
        :return:
        """
        if(len(self.__Studentservice.getAllStudenti()) == 0):
            print("No students found.")
        for student in self.__Studentservice.getAllStudenti():
            print(f"Student ID: {student.getIDStudent()} Name: {student.getNumeStudent()}")

    def random_Students(self):
        """
        Random Students.
        :return:
        """
        numberOfStudents = int(input("How many students?: "))
        for _ in range(numberOfStudents):
            student = self.__Studentservice.getRandomStudent()
            student_id = random.randint(1, 1000)
            print(f"Student ID: {student_id} Name: {student}")

    def add_Materie(self):
        """
        Placeholder for adding a materie.
        """
        id = input("Enter Materie ID: ")
        nume = input("Enter Materie Name: ")
        profesor= input("Enter Profesor Name: ")
        try:
            self.__Materieservice.addMaterie(id, nume, profesor)
            print("Materie Added Successfully")
        except MaterieRepositoryException:
            print(f"Materie ID: {id} with name: {nume} already exists.")
        except MaterieValidatorException as e:
            print(f"Validation error: {e}")

    def edit_Materie(self):
        """
        Placeholder for editing a materie.
        """
        id = int(input("Enter Materie ID: "))
        nume = input("Enter Materie Name: ")
        profesor= input("Enter Profesor Name: ")
        try:
            self.__Materieservice.modifyMaterie(id, nume, profesor)
            print("Materie Edited Successfully")
        except MaterieRepositoryException:
            print(f"Materie ID: {id} doesn't exist.")


    def delete_Materie(self):
        """
        Placeholder for deleting a materie.
        """
        ok=True
        id = input("Enter Materie ID: ")
        try:
            self.__Materieservice.deleteMaterie(id)
        except MaterieRepositoryException:
            ok=False
            print(f"Materie ID: {id} doesn't exist.")
        if ok:
            print("Materie Deleted Successfully")

    def search_Materie(self):
        """
        Show Materie by taking id from the user.
        :return:
        """
        ok=True
        id = input("Enter Materie ID: ")
        try:
            print(f"Nume materie:{self.__Materieservice.cautareMaterie(id).GetNumeMaterie()}")
            print(f"Profesorul materiei:{self.__Materieservice.cautareMaterie(id).GetProfesorMaterie()}")
        except MaterieRepositoryException:
            ok=False
            print(f"Materie ID: {id} doesn't exist.")
        if ok:
            print("Materie Search Successfully")

    def view_Materie(self):
        """
        Afiseaza toate materiile
        :return:
        """
        if(len(self.__Materieservice.getAllMaterii())==0):
            print("No classes found.")
        for materie in self.__Materieservice.getAllMaterii():
            print(f"Materie ID: {materie.GetIDMaterie()}, Numele Materiei: {materie.GetNumeMaterie()}, Profesorul materiei: {materie.GetProfesorMaterie()}")
    def adauga_nota(self):
        """
        Adauga o nota in lista
        :return:
        """
        id=input("Enter Nota ID: ")
        student=input("Enter student id")
        materie=input("Enter Materie ID: ")
        nota=input("Enter Nota: ")
        try:
            self.__Noteservice.adauga_nota(id, student, materie, nota)
            print("Nota Add Successfully")
        except NoteRepositoryException:
            print(f"Nota ID: {id} already exists.")
        except NoteValidatorException as e:
            print(f"Validation error: {e} " )

    def run(self):
        """
        Runs the application, displaying the menu and handling user input.
        """
        dic={
            "addstudent": self.add_Student,
            "editstudent": self.edit_Student,
            "deletestudent": self.delete_Student,
            "viewstudent": self.show_All_Students,
            "addmaterie": self.add_Materie,
            "editmaterie": self.edit_Materie,
            "deletematerie": self.delete_Materie,
            "randomstudent": self.random_Students,
            "viewmaterie": self.view_Materie,
            "searchmaterie": self.search_Materie,
            "searchstudent": self.search_Student,
            "addnota":self.adauga_nota,
        }
        oprire = False
        while not (oprire):
            self.showMenu()
            command = input("Command: ")
            command=command.lower()
            if command == "quit":
                oprire = True
            elif command == "":
                continue
            elif command in dic:
                dic[command]()
            else:
                print("Invalid command!")
        print("Thank you!")
