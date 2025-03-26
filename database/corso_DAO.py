# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
#rappresenta le instanze della tabella Corsi


class Corso():
    def __init__(self,codins, crediti, nome, pd):
        self.codins = codins
        self.crediti = crediti
        self.nome = nome
        self.pd = pd
    @classmethod
    def get_corsi(self):
        cnx = get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM corso")
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result
    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return self.codins

    def __str__(self):
        return f"{self.nome} ({str(self.codins)})"