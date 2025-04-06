import database.DAO


class Model:
    def __init__(self):
        self.studenti = database.DAO.DAO.getAllStudenti()
        self.corsi = database.DAO.DAO.getAllCorsi()
        self.analogie = database.DAO.DAO.getAllAnalogie()

    def cerca_studente(self, other):
        for s in self.studenti:
            if s.matricola == other:
                return s
        return False