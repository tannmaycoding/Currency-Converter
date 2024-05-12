import requests
from tkinter import *
from tkinter import ttk

key = "Your-API-Key"
baseURL = "https://api.freecurrencyapi.com/v1/latest?apikey=Your-API-Key"
currencies = ["USD", "INR", "AUD", "CAD", "EUR", "GBP", "JPY", "CHF"]


def convert(base):
    getCurrencies = ",".join(currencies)
    getURL = f"{baseURL}&base_currency={base}&currencies={getCurrencies}"
    try:
        response = requests.get(getURL)
        data = response.json()
        return data["data"]
    except Exception as e:
        print("Invalid Currency")
        return None


while True:
    base = input("Base Currency(code) and q to quit: ").upper()
    if base == "Q":
        break
    amount = input("Amount of base currency: ")
    money: dict = convert(base)
    if not money:
        continue
    del money[base]
    for currency, cash in money.items():
        print(f"{amount}{currency}: {float(amount)*cash}")
