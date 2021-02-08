from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Подбор щеток AEZ. Ver.1.24.10.2020")
root.geometry('350x150')

def printRecords():
    connection = sqlite3.connect('brush2text.db')
    cur = connection.cursor()

    cur.execute("SELECT number, comment FROM brush WHERE width = ? AND height = ?", (wi.get(), he.get()))
    results = cur.fetchall()
    messagebox.showinfo("Номера щеток по вашему запросу:", results)
    print(results)

Label(root, text="Введите ширину:       ").grid(row=1, column=1)
Label(root, text="Введите высоту:       ").grid(row=2, column=1)

wi = Entry()
he = Entry()
wi.grid(row=1, column=2, padx=5, pady=5)
he.grid(row=2, column=2, padx=5, pady=5)
root.update()

SearchButton = Button(root, text="Подобрать", command=printRecords)
SearchButton.grid(row=3, column=2)

root.mainloop()
