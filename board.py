import serial

MAX_BUFF_LEN =255

port = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)

# read one char
def read_ser(num_char = 1):
    string = port.read(num_char)
    return string.decode() 

def write_ser(cmd):
    cmd = cmd+'\n'
    port.write(cmd)

while(1):
    string = read_ser(MAX_BUFF_LEN)
    print(string)

    cmd = input()
    write_ser(cmd)