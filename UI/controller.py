import flet as ft

import database.corso_DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_btn_cerca_iscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.corso_dropdown.value
        if name is None or name == "":
            self._view.create_alert("nessun corso selezionato")
            return
        result = []
        for stud in self._model.studenti:
            if (stud,name) in self._model.analogie:
                result.append(str(stud))
        self._view.txt_result.controls.append(ft.Text(f"ci sono {len(result)} iscritti al corso:"))
        self._view.update_page()

    def get_corsi(self):
        """devo qui popolare la tendina di dropwon"""
        options = []
        for corso in self._model.corsi:
            options.append(ft.dropdown.Option(key = corso.codins, text=str(corso)))
        return options

    def iscriviStudente(self):
        pass

    def cercaCorsi(self):
        pass

    def cercaStudente(self):
        pass