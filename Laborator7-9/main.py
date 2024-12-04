from Application.ConsoleUI import ConsoleUI
from Repository.MateriiRepository import MaterieRepository
from Repository.NoteRepository import NoteRepository
from Repository.StudentRepository import StudentRepository
from Service.NoteService import NoteService
from Service.StudentService import StudentService
from Service.MaterieService import MaterieService
from domain.Validators.materievalidator import MaterieValidator
from domain.Validators.notevalidator import NoteValidator
from domain.Validators.studentvalidator import StudentValidator


def main():

    repo_studenti=StudentRepository()
    Validator_studenti=StudentValidator()
    service_studenti= StudentService(repo_studenti,Validator_studenti)
    repo_materii=MaterieRepository()
    Validator_materii=MaterieValidator()
    service_materie=MaterieService(repo_materii,Validator_materii)
    repo_note=NoteRepository()
    Validator_note=NoteValidator()
    service_note=NoteService(repo_note,repo_materii,repo_studenti,Validator_note)
    ui=ConsoleUI(service_studenti, service_materie, service_note)
    ui.run()
if __name__ == '__main__':
    main()