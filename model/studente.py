class Studente:
    def __init__(self,matricola,nome,cognome,cds):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.cds =cds
        self.corsiList = []

    def __str__(self):
        return f"({self.matricola}) nome: {self.nome}, cognome: {self.cognome}"
    def __hash__(self):
       return self.matricola
    def __eq__(self, other):
        return self.matricola==other