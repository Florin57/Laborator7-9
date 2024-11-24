from Controller.ConsoleUI import ConsoleUI
from Repository.MateriiRepository import MaterieRepository
from Repository.StudentRepository import StudentRepository
from Service.StudentService import StudentService
from Service.MaterieService import MaterieService
from domain.Validators.materievalidator import MaterieValidator
from domain.Validators.studentvalidator import StudentValidator


def main():
    repo_studenti=StudentRepository
    Validator_studenti=StudentValidator
    service_studenti= StudentService(repo_studenti,Validator_studenti)
    repo_materii=MaterieRepository
    Validator_materii=MaterieValidator
    service_materie=MaterieService(repo_materii,Validator_materii)
    ui=ConsoleUI(service_studenti, service_materie)
    ui.run()
if __name__ == '__main__':
    main()