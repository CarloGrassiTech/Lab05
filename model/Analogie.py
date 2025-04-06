from dataclasses import dataclass
@dataclass
class Analogie:
    matricola: int
    codins: str

    def __eq__(self, other):
        return self.matricola == other[0].matricola and self.codins == other[1]

    def __lt__(self, other):
        return self.matricola < other[0].matricola and self.codins < other[1]

    def __str__(self):
        return self.codins - self.matricola