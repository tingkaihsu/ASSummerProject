import serial
import time

# Function to send data
def send_data(data):
    time.sleep(0.1)
    ser.write(data.encode())  # Convert string to bytes and send
    mes = ser.readline(64)
    if mes != b'':
        print(mes.decode())
    return mes.decode()

# Function to receive data
def receive_data():
    data = ser.readline(64)  # Read a line of data
    return data.decode()   # Convert bytes to string and return

# Set up writing file
file = open("data1.txt", "w")

# Set up the serial connection
ser = serial.Serial(
    port='/dev/ttyUSB0',  # Device name
    baudrate=9600,        # Baud rate (this depends on your device)
    timeout=1             # Timeout for read
)

# Open the flow control
ser.dsrdtr = True
time.sleep(1.0)
print(ser)

# Example code

send_data('\x14')
send_data('\x11')

# remember to add \r\n in sandwich form of the commend
send_data('\r\nCLEA\r\n')
send_data('\r\nEVTS\r\n')
send_data('\r\n*IDN?\r\n')
print('current mode: ', end = '')
send_data('\r\nMODE?\r\n')
events = 0
pre_events = 0
print('start counting!')
print('ch1 ch2', file = file)
try: 
    while(True):
        send_data('\r\nSTAR\r\n')
        # COUNTER/TIME mode
        # time.sleep(0.1)
        # ser.write('\r\nEVTS?\r\n'.encode())
        # events = int(ser.readline(64).decode())
        # if events != pre_events:
        #     print('Event: ', events)
        #     mes = send_data('\r\nCOUN?\r\n')
        #     if mes != '' and mes.startswith('1'):
        #         data = mes.split(";")
        #         ch1 = data[0].split(",")
        #         ch2 = data[1].split(",")
        #         print(ch1[1], file= file, end = ' ')
        #         print(ch2[1], file= file, end = '')
        #     pre_events = events
        #     send_data('\r\nCLEA\r\n')
        #     print('start counting!')
<<<<<<< HEAD
        time.sleep(300.0)
=======
        time.sleep(600.0)
>>>>>>> 1d4a6603a02200f54668af908dcd98f43a676cd9
        mes = send_data('\r\nCOUN?\r\n')
        if mes != '' and mes.startswith('1'):
            data = mes.split(";")
            ch1 = data[0].split(",")
            ch2 = data[1].split(",")
            print("current time: ", time.time(), file=file)
            print(ch1[1], file= file, end = ' ')
            print(ch2[1], file= file, end = '')
except KeyboardInterrupt:
    print('\nKeyboard interrupt!')
    mes = send_data('\r\nCOUN?\r\n')
    if mes != '' and mes.startswith('1'):
        data = mes.split(";")
        ch1 = data[0].split(",")
        ch2 = data[1].split(",")
        print(ch1[1], file= file, end = ' ')
        print(ch2[1], file= file, end = '')
    send_data('\r\nSTOP\r\n')
    print("current time: ", time.time(), file=file)
finally:
    send_data(chr(0x13))
    send_data(chr(0x12))
    print(ser)
    ser.close()
