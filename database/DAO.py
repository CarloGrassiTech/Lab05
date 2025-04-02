import database.DB_connect as d
import model.studente as s
import model.corso as c
class DAO():
    @classmethod
    def get_corsi(self):
        cnx = d.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM corso")
        for row in cursor:
            result.append(c.Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result

    @classmethod
    def get_studenti(self):
        cnx = d.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM studente")
        for row in cursor:
            result.append(s.Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cursor.close()
        cnx.close()

    @classmethod
    def get_analogie(self):
        cnx = d.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM iscrizione")
        for row in cursor:
            result.append(c.Corso.tupla.append(row["matricola"], row["codins"]))
        cursor.close()
        cnx.close()
        return result