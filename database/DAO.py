import mysql

from database.DB_connect import get_connection
from model.Analogie import Analogie
from model.corso import Corso
from model.studente import Studente


class DAO:
    @staticmethod
    def getAllCorsi():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * FROM corso"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(**row))
        # processa res

        cursor.close()
        cnx.close()
        return res
    @staticmethod
    def getAllStudenti():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * FROM studente"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Studente(**row))
        # processa res

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllAnalogie():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * FROM iscrizione"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Analogie(**row))
        # processa res

        cursor.close()
        cnx.close()
        return res