from database.DB_connect import get_connection
@dataclasses
class Analogie:
    matricola : str
    codins : int
    @classmethod
    def get_analogie(self):
        cnx = get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM iscrizione")
        for row in cursor:
            result.append(Corso(row["matricola"], row["codins"]))
        cursor.close()
        cnx.close()
        return result