import serial
import time

# Function to send data
def send_data(data):
    time.sleep(0.1)
    ser.write(data.encode())  # Convert string to bytes and send
    mes = ser.readline(64)
    if mes != b'':
        print(mes.decode())

# Function to receive data
def receive_data():
    data = ser.readline(64)  # Read a line of data
    return data.decode()   # Convert bytes to string and return




# Set up the serial connection
ser = serial.Serial(
    port='/dev/ttyUSB1',  # Device name
    baudrate=9600,        # Baud rate (this depends on your device)
    timeout=1             # Timeout for read
)

ser.dsrdtr = True
time.sleep(1.0)
print(ser)

# Check if the serial port is open
# if ser.is_open:
#     print("Connection established!")
#     print(ser)
# else:
#     print("Failed to open the serial port.")

# Example code

# send_data(chr(0x14))
send_data('\x14')
send_data('\x11')
# remember to add \r\n in sandwich form of the commend
send_data('\r\nCLEA\r\n')
send_data('\r\nEVTS\r\n')
send_data('\r\n*IDN?\r\n')
# It seems that the commend would first be stored in  buffer
# and then be pushed to machine when the other commend comes in
events = 0
pre_events = 0
while(1):
    #commend = input('Please enter commend: ')
    #commend = '\r\n' + commend + '\r\n'
    #send_data(commend)
    #if commend == '\r\nSTOP\r\n':
    #    break
    send_data('\r\nSTAR\r\n')
    # COUNTER
    time.sleep(0.1)
    ser.write('\r\nEVTS?\r\n'.encode())
    events = int(ser.readline(64).decode())
    if events != pre_events:
        #time.sleep(0.1)
        #ser.write('\r\nSTOP\r\n'.encode())
        send_data('\r\nCOUN?\r\n')
        pre_events = events
        send_data('\r\nCLEA\r\n')
send_data(chr(0x12))
print(ser)
ser.close()
