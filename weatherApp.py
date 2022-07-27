#!/usr/bin/python
import os
import adafruit_dht
import board 
import tkinter as tk
from tkinter import Frame, Label, StringVar, ttk
from datetime import datetime
from dotenv import load_dotenv
import requests

def get_wheather():
    load_dotenv()
    token=os.getenv('APIKEY')
    apiKey = token
    city = 'Varallo'
    state = 'it'
    lang = 'it'
    apiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={apiKey}&lang={lang}&units=metric"
    results = requests.get(apiUrl)
    return results.json()

def set_weather_labels_data(data):

    city_var.set(data['name'])
    weather_var.set(str(data['weather'][0]['description']).capitalize())
    temperature_var.set("{0:0.1f}°C".format(data['main']['temp']))
    feelsLike_var.set("Percepita: {0:0.1f}°C".format(data['main']['feels_like']))
    humidity_var.set(f"{data['main']['humidity']}%")
    weatherFrame = tk.Frame(window)
    
    weatherFrame.columnconfigure(0, weight=1)
    weatherFrame.columnconfigure(1, weight=1)
    weatherFrame.columnconfigure(2, weight=1)
    weatherFrame.columnconfigure(3, weight=1)

    city = tk.Label(
        weatherFrame, 
        textvariable=city_var, 
        font=('Arial', 50)
        ).grid(row=0, column=0, columnspan=4, ipady=22) 
    
    weather = tk.Label(
        weatherFrame, 
        textvariable=weather_var, 
        font=('Arial', 35)
        ).grid(row=2, column=0)
        
    tk.Label(
        weatherFrame, 
        text='Meteo', 
        font=('Arial', 35)
        ).grid(row=1, column=0, padx=5)

    temperature = tk.Label(
        weatherFrame, 
        text='Temperatura', 
        font=('Arial', 35)
        ).grid(row=1, column=1, padx=5)

    tk.Label(
        weatherFrame, 
        textvariable=temperature_var, 
        font=('Arial', 35)
        ).grid(row=2, column=1)

    tk.Label(
        weatherFrame, 
        textvariable=feelsLike_var, 
        font=('Arial', 20)
        ).grid(row=3, column=1)

    humidity = tk.Label(
        weatherFrame, 
        text='Umidià', 
        font=('Arial', 35)
        ).grid(row=1, column=2, padx=5)

    tk.Label(
        weatherFrame, 
        textvariable=humidity_var, 
        font=('Arial', 35)
        ).grid(row=2, column=2)
    
    weatherFrame.grid(row=3, column=0, columnspan=4)
    weatherFrame.after(120000, set_weather_labels_data, get_wheather())

def temp_reader():
    sensor = adafruit_dht.DHT11(board.D27)      
    h = sensor.humidity
    t = sensor.temperature
    
    new_h = 0
    new_t = 0
    if h is not None and h != new_h:
        new_h = h
        humidity_text.set("{0:0.1f}%".format(new_h))
    if t is not None and t != new_t:
        new_t = t
        temperature_text.set('{0:0.1f}°C'.format(new_t))
    date_text.set(datetime.now().strftime('%Y-%m-%d'))
    time_text.set(datetime.now().strftime('%H:%M'))
    
    window.after(60000, temp_reader)

# initialize window
window = tk.Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
window.geometry(f'{screenWidth}x{screenHeight}') 
# window.attributes('-fullscreen', True)

# set grid columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

# set grid rows
# window.rowconfigure(0, weight=0)

#set window title
window.title("Temperature Monior")

date_text = StringVar()
time_text = StringVar()
humidity_text = StringVar()
temperature_text = StringVar()

city_var = StringVar()
weather_var = StringVar()
temperature_var = StringVar()
feelsLike_var = StringVar()
humidity_var = StringVar()
# initialize and place labels

#time frame section
time_frame = tk.Frame(window)

time_frame.columnconfigure(0, weight=4)

label_date = tk.Label(
    time_frame, 
    textvariable=date_text, 
    width=200, 
    font=('Arial', 35)
    ).grid(
        row=1, 
        column=0, 
        columnspan=4, 
        )
lbel_time = tk.Label(
    time_frame,
    textvariable=time_text,
    font=('Arial', 50)
    ).grid(row=0, column=0, columnspan=4)

time_frame.grid(row=0, column=0, columnspan=4, ipady=20, pady=5)




label = tk.Label(
    window, 
    text="Temperatura interna",
    width=200, 
    font=('Arial', 35)
    ).grid(
        row=1,
        column=0,
        columnspan=2
        )

label1 = tk.Label(
    window, 
    text="Umidità",
    width=200, 
    font=('Arial', 35)
    ).grid(
        row=1,
         column=3,
         columnspan=2
         )


label_temperature = tk.Label(
    window, 
    textvariable=temperature_text, 
    width=200, 
    font=('Arial', 50)
    ).grid(
        row=2, 
        column=1
        )

label_humidity = tk.Label(
    window, 
    textvariable=humidity_text, 
    width=200, 
    font=('Arial', 50)
    ).grid(
        row=2, 
        column=3
        )

set_weather_labels_data(get_wheather())
temp_reader(gpio)
window.mainloop()