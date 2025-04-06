from dataclasses import dataclass
@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int

    def __eq__(self, other):
        return self.codins == other.codins

    def __lt__(self, other):
        return self.codins == other.codins

    def __str__(self):
        return f"{self.nome} ({self.codins})"