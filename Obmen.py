import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb


def exchange():
    code = entry.get().upper()


window = Tk()
window.title("Курсы обмена валют")
window.geometry("350x160")

Label(text="Введите код валюты:").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)
window.mainloop()
