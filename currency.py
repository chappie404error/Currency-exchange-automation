import requests
from twilio.rest import Client
from datetime import datetime

VIRTUAL_TWILIO_NUMBER = "+1334500###6"
VERIFIED_NUMBER = "+91734934####"
TWILIO_SID = "AC965863fd2db06a1351512#####c8db4"
TWILIO_AUTH_TOKEN = "c33439d0b22ec4dd0######d7fd37b88e"
# VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
# VERIFIED_NUMBER = "your own phone number verified with Twilio"
# TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
# TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
# CURRENCY API
API_KEY = 'fca_live_QiRD4yaE7K1aJQIAfVLojfu8J2KPxSXPYkDxxTzc'
url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

resp = requests.get(url)
data = resp.json()
currency_info = data['data']
print(f"STATUS CODE = {resp.status_code}")

CURRENCY_list = ["AUD", "INR", "NZD", "EUR", "CAD", "RUB", "CNY"]
message_text = ""


def final_():
    global message_text
    for i in CURRENCY_list:
        rounded_number = round(currency_info[str(i)],2)
        message_text += f" \n {i} = {rounded_number}$ "

    final_text = f"\n ||||| VALUE OF  ONE DOLLAR =  {message_text} \n +response status code {resp.status_code}"
    return final_text


text = final_()

time_now = datetime.now()


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    body=text,
    from_=+1334500#####,
    to=+9173493#####
    # from_ = VIRTUAL_TWILIO_NUMBER,
    # to = VERIFIED_NUMBER
)

# EUR	Euro
# USD	US Dollar
# JPY	Japanese Yen
# BGN	Bulgarian Lev
# CZK	Czech Republic Koruna
# DKK	Danish Krone
# GBP	British Pound Sterling
# HUF	Hungarian Forint
# PLN	Polish Zloty
# RON	Romanian Leu
# SEK	Swedish Krona
# CHF	Swiss Franc
# ISK	Icelandic Króna
# NOK	Norwegian Krone
# HRK	Croatian Kuna
# RUB	Russian Ruble
# TRY	Turkish Lira
# AUD	Australian Dollar
# BRL	Brazilian Real
# CAD	Canadian Dollar
# CNY	Chinese Yuan
# HKD	Hong Kong Dollar
# IDR	Indonesian Rupiah
# ILS	Israeli New Sheqel
# INR	Indian Rupee
# KRW	South Korean Won
# MXN	Mexican Peso
# MYR	Malaysian Ringgit
# NZD	New Zealand Dollar
# PHP	Philippine Peso
# SGD	Singapore Dollar
# THB	Thai Baht
# ZAR	South African Rand
