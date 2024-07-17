import serial
import time

# Function to send data
def send_data(data):
    time.sleep(0.1)
    ser.write(data.encode())  # Convert string to bytes and send
    # mes = ser.readline(64)
    # if mes != b'':
    #     print(mes.decode())

# Function to receive data
def receive_data():
    data = ser.readline(64)  # Read a line of data
    return data.decode()   # Convert bytes to string and return

# Set up writing file
file = open("data.txt", "w")

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
try: 
    while(True):
        send_data('\r\nSTAR\r\n')
        # COUNTER
        time.sleep(0.1)
        ser.write('\r\nEVTS?\r\n'.encode())
        events = int(ser.readline(64).decode())
        if events != pre_events:
            print('Event: ', events)
            send_data('\r\nCOUN?\r\n')
            mes = receive_data()
            if mes != '':
                print(mes)
                data = mes.split(";")
                ch1 = data[0].split(",")
                ch2 = data[1].split(",")
                print(ch1[1], file= file, end = ' ')
                print(ch2[1], file= file, end = '')
            pre_events = events
            send_data('\r\nCLEA\r\n')
            print('start counting!')
except KeyboardInterrupt:
        print('\nKeyboard interrupt!')
finally:
    send_data('\r\nSTOP\r\n')
    send_data(chr(0x13))
    send_data(chr(0x12))
    print(ser)
    ser.close()
