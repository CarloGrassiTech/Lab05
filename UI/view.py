import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name


        # button for the "hello" reply
        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_btn_cerca_iscritti)
        self.corso_dropdown = ft.Dropdown(options=self._controller.get_corsi(), on_change="", width=700)
        row1 = ft.Row([self.corso_dropdown, self.btn_cerca_iscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.txt_matricola = ft.TextField(label = "matricola", width=150, hint_text="insert your number")
        self.txt_nome = ft.TextField(
            label="nome",
            width=300,
            read_only=True
        )
        self.txt_cognome = ft.TextField(label = "cognome", width=300,  read_only=True)
        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca Studente", color="blue", on_click=self._controller.cercaStudente())
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca Corsi", color="blue", on_click=self._controller.cercaCorsi())
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", color="blue", on_click=self._controller.iscriviStudente())
        row3 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
