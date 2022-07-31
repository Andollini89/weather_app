from logging import root
import time
import tkinter as tk
from tkinter import ttk, font
import adafruit_dht
import board

class SensorTemperatureHumidityFrame(tk.Frame):
    
    def __init__(self, root):
        super().__init__()
        
        self.root = root
        self.sensor = adafruit_dht.DHT11(board.D27)
        self.sensor._trig_wait = 25000
        self.temperature_text = tk.StringVar()
        self.humidity_text = tk.StringVar()
        self.label_font = font.Font(self, family='Arial', size= 30)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.master_label = tk.Label(self, text="Sensor Readings", font=self.label_font)
        self.temperature_label = tk.Label(self, text="Temperarure:", font=self.label_font)
        self.humidity_label = tk.Label(self, text="Humidity:", font=self.label_font)

        self.temperature_data_label = tk.Label(self, textvariable=self.temperature_text, font=self.label_font)
        self.humidity_data_label = tk.Label(self, textvariable=self.humidity_text, font=self.label_font)

        self.master_label.grid(row=0, column=0, columnspan=2)
        
        self.temperature_label.grid(row=1, column=0)
        self.temperature_data_label.grid(row=1, column=1)

        self.humidity_label.grid(row=2, column=0)
        self.humidity_data_label.grid(row=2, column=1)

        self.grid(row=1, column=1, columnspan=2)

        self.get_sensor_readings()


    def get_sensor_readings(self):

        try:
            h = self.sensor.humidity
            t = self.sensor.temperature
            if h is not None and t is not None: 
                self.set_readings_to_labels(h, t)

        except RuntimeError as error:
            print(error)
            pass 
        
        time.sleep(2)
        self.after(120000, self.get_sensor_readings)

    def set_readings_to_labels(self, h, t):        
        # data = self.get_sensor_readings()
        # print(data)

        if self.humidity_text.get() != f"{h}%": 
            self.humidity_text.set(f"{h}%")

        if self.temperature_text.get() != f"{t}°C":
            self.temperature_text.set(f"{t}°C")



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    sensor_readings =  SensorTemperatureHumidityFrame(root)
    root.mainloop()
