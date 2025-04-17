import serial
import time
ser = serial.Serial('COM3', 115200, timeout = 1)

time.sleep(2)
ser.write(b'1')
time.sleep(4)
ser.write(b'0')
