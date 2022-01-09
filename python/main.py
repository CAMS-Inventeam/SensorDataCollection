import serial
import time

arduino = serial.Serial(port='COM5', baudrate=115200) # this port can be changed
data = {}
while True:
    line = arduino.readline().decode('utf8').strip('\r\n')
    if line == 'DATA_BEGIN':
        data = {}
    elif line == 'DATA_END':
        print(data)
    else:
        try:
            name = line.split(':')[0]
            value = line.split(':')[1]
            data[name] = value
        except:
            print(line)
    time.sleep(.1)
