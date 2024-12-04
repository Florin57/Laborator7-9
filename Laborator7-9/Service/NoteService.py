from Repository.MateriiRepository import MaterieRepository
from Repository.NoteRepository import NoteRepository
from Repository.StudentRepository import StudentRepository
from domain.Validators.notevalidator import NoteValidator
from domain.note import Note


class NoteService:
    def __init__(self,repo_studenti:StudentRepository,validator_note:NoteValidator,repo_materie:MaterieRepository,repo_note:NoteRepository):
        self.__repo_studenti = repo_studenti
        self.__repo_materie = repo_materie
        self.__repo_note = repo_note
        self.__validator_note = validator_note

    def adauga_nota(self, id_nota, id_student, id_materie, valoare):
        student=self.__repo_studenti.cautareStudent(id_student)
        materie=self.__repo_materie.cautareMaterie(id_materie)
        nota=Note(id_nota, student, materie, valoare)
        #validator
        self.__repo_note.addNote(nota)