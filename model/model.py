import database.studente_DAO


class Model:
    def __init__(self):
        self.studenti = database.studente_DAO.Studente.get_studenti()
        self.corsi = database.corso_DAO.Corso.get_corsi()
        self.analogie = database.analogie_DAO.Analogie.get_analogie()
