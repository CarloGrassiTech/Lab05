# Add whatever it is needed to interface with the DB Table studente
import dataclasses

from database.DB_connect import get_connection
#rappresenta le instanze della tabella studenti
class Studente():
    def __init__(self, matricola, cognome, nome, CDS):
        self.matricola= matricola
        self.cognome = cognome
        self.nome = nome
        self.CDS = CDS
    @classmethod
    def get_studenti(self):
        cnx = get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM studente")
        for row in cursor:
            result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cursor.close()
        cnx.close()
        return result
    def __eq__(self, other):
        return self.matricola==other.matricola
    def __hash__(self):
        return self.matricola
    def __str__(self):
        return f"{str(self.nome).upper}, {str(self.cognome).upper} ({self.matricola})"