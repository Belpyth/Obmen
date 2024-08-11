import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event):
    code = t_combobox.get()
    name = cur[code]
    c_label.config(text=name)

def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    if t_code and b_code:
        try:
            resource = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            resource.raise_for_status()
            data = resource.json()
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo('Курс обмена', f"Курс {exchange_rate:.2f} {t_name} за 1 {b_name}")
            else:
                mb.showerror("Ошибка", f"Валюта с кодом {t_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка {e}")
    else:
        mb.showwarning("Внимание", "Введите код валюты")

cur = {
    "RUB": "Российский рубль",
    "USD": "Доллар",
    "EUR": "Евро",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "GBP": "Британский фунт стерлингов",
    "JPY": "Японская йена",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}


window = Tk()
window.title("Курсы обмена валют")
window.geometry("300x300")

Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(pady=7, padx=10)
#b_combobox.bind("<<ComboboxSelected>>", update_c_label)

Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(pady=7, padx=10)
t_combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(pady=7, padx=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=7)
window.mainloop()
