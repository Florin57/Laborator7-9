from Repository.StudentRepository import StudentRepositoryException
from Service import StudentService
from Service.MaterieService import MaterieService
from domain.Validators.studentvalidator import StudentValidatorException



class ConsoleUI:
    def __init__(self, Studentservice:StudentService, Materieservice:MaterieService):
        self.__Studentservice = Studentservice
        self.__Materieservice = Materieservice

    def showMenu(self):
        """
        Displays the menu options to the user.
        """
        print("Menu:")
        print("1. Add Student (type 'addstudent')")
        print("2. Edit Student (type 'editstudent')")
        print("3. Delete Student (type 'deletestudent')")
        print("4. Add Materie (type 'addmaterie')")
        print("5. Edit Materie (type 'editmaterie')")
        print("6. Delete Materie (type 'deletematerie')")
        print("7. Exit (type 'quit')")

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
        print("Edit student functionality is not implemented yet.")

    def delete_Student(self):
        """
        Placeholder for deleting a student.
        """
        print("Delete student functionality is not implemented yet.")

    def add_Materie(self):
        """
        Placeholder for adding a materie.
        """
        print("Add materie functionality is not implemented yet.")

    def edit_Materie(self):
        """
        Placeholder for editing a materie.
        """
        print("Edit materie functionality is not implemented yet.")

    def delete_Materie(self):
        """
        Placeholder for deleting a materie.
        """
        print("Delete materie functionality is not implemented yet.")

    def run(self):
        """
        Runs the application, displaying the menu and handling user input.
        """
        dic={
            "addstudent": self.add_Student,
            "editstudent": self.edit_Student,
            "deletestudent": self.delete_Student,
            "addmaterie": self.add_Materie,
            "editmaterie": self.edit_Materie,
            "deletematerie": self.delete_Materie,
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
