# Приложение УЧЕБНЫЙ ПЛАН для автоматизированного контроля учебной
# нагрузки по кафедре. Таблица Дисциплины должна иметь следующую структуру записи:
# Код дисциплины, Наименование дисциплины, Специальность, Лекции (колич.часов),
# Практические (колич.часов), Лабораторные (колич.часов), Форма отчетности.
# БД должна обеспечивать получение информации о дисциплинах кафедры по
# наименованию.
import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#AB8BB9', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="img/plus.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить дисциплину', command=self.open_dialog, bg='#C6A5D4',
                                         bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT, padx=10)

        self.update_img = tk.PhotoImage(file="img/redak.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#C6A5D4',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT, padx=10)

        self.delete_img = tk.PhotoImage(file="img/del.png")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#C6A5D4',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT, padx=10)

        self.search_img = tk.PhotoImage(file="img/poisk.png")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#C6A5D4',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT, padx=10)

        self.refresh_img = tk.PhotoImage(file="img/obn.png")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#C6A5D4',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT, padx=10)

        self.tree = ttk.Treeview(self, columns=('code', 'name', 'speciality', 'lectures', 'practical', 'labs', 'form'),
                                 height=15, show='headings')

        self.tree.column('code', width=30, anchor=tk.CENTER)
        self.tree.column('name', width=110, anchor=tk.CENTER)
        self.tree.column('speciality', width=110, anchor=tk.CENTER)
        self.tree.column('lectures', width=70, anchor=tk.CENTER)
        self.tree.column('practical', width=110, anchor=tk.CENTER)
        self.tree.column('labs', width=110, anchor=tk.CENTER)
        self.tree.column('form', width=110, anchor=tk.CENTER)

        self.tree.heading('code', text='Код')
        self.tree.heading('name', text='Наименование')
        self.tree.heading('speciality', text='Специальность')
        self.tree.heading('lectures', text='Лекции')
        self.tree.heading('practical', text='Практические')
        self.tree.heading('labs', text='Лабораторные')
        self.tree.heading('form', text='Форма отчётности')

        self.tree.pack()

    def records(self, code, name, speciality, lectures, practical, labs, form):
        self.db.insert_data(code, name, speciality, lectures, practical, labs, form)
        self.view_records()

    def update_record(self, code, name, speciality, lectures, practical, labs, form):
        self.db.cur.execute(
            "UPDATE plan SET code=?, name=?, speciality=?, lectures=?, practical=?,labs=?, form=?  WHERE code=?",
            (code, name, speciality, lectures, practical, labs, form, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("SELECT * FROM plan")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("DELETE FROM plan WHERE code=?", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, speciality):
        speciality = ("%" + speciality + "%",)
        self.db.cur.execute("SELECT * FROM plan WHERE speciality LIKE ?", speciality)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить дисциплину')
        self.geometry('400x270+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Код')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=170, y=25)

        label_name = tk.Label(self, text='Наименование')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=170, y=50)

        label_speciality = tk.Label(self, text='Специальность')
        label_speciality.place(x=50, y=75)
        self.combobox = ttk.Combobox(self, values=[u'ПОКС', u'МТ', u'СК', u'ИБТ', u'ИБА', u'ИС', u'ИКС', u'СА'],
                                     width=17)
        self.combobox.current(0)
        self.combobox.place(x=170, y=75)

        label_lectures = tk.Label(self, text='Лекции')
        label_lectures.place(x=50, y=100)
        self.entry_lectures = ttk.Entry(self)
        self.entry_lectures.place(x=170, y=100)

        label_practical = tk.Label(self, text='Практические')
        label_practical.place(x=50, y=125)
        self.entry_practical = ttk.Entry(self)
        self.entry_practical.place(x=170, y=125)

        label_labs = tk.Label(self, text='Лабораторные')
        label_labs.place(x=50, y=150)
        self.entry_labs = ttk.Entry(self)
        self.entry_labs.place(x=170, y=150)

        label_form = tk.Label(self, text='Форма отчётности')
        label_form.place(x=50, y=175)
        self.combobox2 = ttk.Combobox(self, values=[u'Зачёт', u'Экзамен'], width=17)
        self.combobox2.current(0)
        self.combobox2.place(x=170, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=200)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=200)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_lectures.get(),
                                                                       self.entry_practical.get(),
                                                                       self.entry_labs.get(),
                                                                       self.combobox2.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=200)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_lectures.get(),
                                                                          self.entry_practical.get(),
                                                                          self.entry_labs.get(),
                                                                          self.combobox2.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.spec_search = ttk.Combobox(self, values=[u'ПОКС', u'МТ', u'СК', u'ИБТ', u'ИБА', u'ИС', u'ИКС', u'СА'])
        self.spec_search.place(x=105, y=20)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.spec_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('plan.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS plan (
                code INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                speciality INTEGER NOT NULL DEFAULT 1,
                lectures INTEGER,
                practical INTEGER,
                labs INTEGER,
                form INTEGER
                )""")

    def insert_data(self, code, name, speciality, lectures, practical, labs, form):
        self.cur.execute(
            "INSERT INTO plan(code, name, speciality, lectures, practical, labs, form) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (code, name, speciality, lectures, practical, labs, form))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Учебный план")
    root.geometry("650x450+300+200")
    root.iconphoto(True, tk.PhotoImage(file='img/book.png'))
    root.resizable(False, False)
    root.mainloop()
