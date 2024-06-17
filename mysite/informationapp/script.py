import serial 


serial_port = 'COM4'
serial_baud  =  9600
files = "output.txt"

ser = serial.Serial(serial_port,serial_baud)
while True:
    line = ser.readline()
    line = line.decode('utf-8')
    print(line)