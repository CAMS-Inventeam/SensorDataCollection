import serial
import time
from tkinter import *
import csv

arduino = serial.Serial(port='COM5', baudrate=115200) # this port can be changed

window = Tk()
window.geometry("700x400")

v_bpm = StringVar()
l_bpm = Label(window, textvariable=v_bpm)
l_bpm.place(x=70, y=50)

v_confidence = StringVar()
l_confidence = Label(window, textvariable=v_confidence)
l_confidence.place(x=70, y=100)

v_oxygen = StringVar()
l_oxygen = Label(window, textvariable=v_oxygen)
l_oxygen.place(x=70, y=150)

v_status = StringVar()
l_status = Label(window, textvariable=v_status)
l_status.place(x=70, y=200)

data = {}

def update_data():
    global data
    global arduino
    line = arduino.readline().decode('utf8').strip('\r\n')
    if line == 'DATA_BEGIN':
        data = {}
    elif line == 'DATA_END':
        v_bpm.set('Heartrate: ' + data['Heartrate'])
        v_confidence.set('Confidence: ' + data['Confidence'] + '%')
        v_oxygen.set('Oxygen: ' + data['Oxygen'])
        v_status.set('Status: ' + data['Status'])
    else:
        try:
            name = line.split(':')[0]
            value = line.split(':')[1]
            data[name] = value
        except:
            print(line)
    time.sleep(.1)
    window.after(1, update_data) # call every 250 milliseconds

window.after(0, update_data) # run the update data function
window.mainloop()