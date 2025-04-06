import flet as ft

import database.DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_btn_cerca_iscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        self._view.txt_result.clean()
        name = self._view.corso_dropdown.value
        if name is None or name == "":
            self._view.create_alert("nessun corso selezionato")
            return
        result = []
        for stud in self._model.studenti:
            if (stud,name) in self._model.analogie:
                result.append(str(stud))
        self._view.txt_result.controls.append(ft.Text(f"ci sono {len(result)} iscritti al corso:"))
        for stud in result:
            self._view.txt_result.controls.append(ft.Text(str(stud)))
        self._view.update_page()

    def get_corsi(self):
        """Popola la tendina del dropdown con i corsi dal DB"""
        options = []
        for c in database.DAO.DAO.getAllCorsi():
        #Supponendo che c abbia un __str__() o un attributo descrittivo (es. c.nome)
            options.append(ft.dropdown.Option(key=c.codins, text=str(c)))
        return options

    def iscriviStudente(self):
        pass

    def cercaCorsi(self):
        if(self._view.txt_result !=None):
            self._view.txt_result.clean()
        name = self._view.txt_matricola.value
        if self.cercaStudente() == False:
            self._view.create_alert("nessun matricola presente uguale a quella selezionata")
            return
        if name is None or name == "":
            self._view.create_alert("nessuna matricola selezionata")
            return
        result = []
        for c in self._model.analogie:
            if c[0] == name:
                result.append(str(c[1]))
        self._view.txt_result.controls.append(ft.Text(f"{name} frequenta {len(result)} corsi: "))
        for stud in result:
            self._view.txt_result.controls.append(ft.Text(str(stud)))
        self._view.update_page()


    def cercaStudente(self):
        other = self._view.txt_matricola.value
        print(other)
        if(other==None):
            self._view.create_alert("nessun studente selezionato")
            return
        flag = self._model.cerca_studente(other)
        if flag != False:
            self._view.txt_matricola.value = other
            self._view.txt_nome.value = flag.nome
            self._view.txt_cognome.value = flag.cognome
            self._view.update_page()
        pass