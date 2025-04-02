import database.DAO as d

class Model:
    def __init__(self):
        self.studenti = d.DAO.get_studenti()
        self.corsi = d.DAO.get_corsi()
        self.analogie = d.DAO.get_analogie()
