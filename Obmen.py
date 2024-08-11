import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb


def exchange():
    code = entry.get().upper()
    if code:
        try:
            resource = requests.get('https://open.er-api.com/v6/latest/USD')
            resource.raise_for_status()
            data = resource.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo('Курс обмена', f"Курс {exchange_rate:.2f} {code} за 1 доллар")
            else:
                mb.showerror("Ошибка", f"Валюта с кодом {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка {e}")
    else:
        mb.showwarning("Внимание", "Введите код валюты")


window = Tk()
window.title("Курсы обмена валют")
window.geometry("350x160")

Label(text="Введите код валюты:").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)
window.mainloop()
