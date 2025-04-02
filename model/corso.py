class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self.codins = codins
        self.crediti = crediti
        self.nome = nome
        self.pd = pd
        self.studentiList = []
        self.tupla = []

    def __str__(self):
        return f"{self.nome} ({self.codins}) - {self.crediti} CFU"

    def __hash__(self):
        return hash(self.codins)

    def __eq__(self, other):
        return self.codins == other