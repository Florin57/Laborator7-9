
class NoteRepositoryException(Exception):
    pass
class NoteRepository:

    def __init__(self):
        self.__note=[]
    def addNote(self,nota):
        for note in self.__note:
            if(note.getNote() == nota.getNote()):
                raise NoteRepositoryException()
            self.__note.append(nota)

    def get_all(self):
        return [self.__note[x] for x in self.__note]

