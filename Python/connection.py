import serial
import time
# Set up the serial connection
ser = serial.Serial(
    port='/dev/ttyUSB0',  # Device name
    baudrate=9600,        # Baud rate (this depends on your device)
    timeout=1             # Timeout for read
)

# Check if the serial port is open
if ser.is_open:
    print("Connection established!")
else:
    print("Failed to open the serial port.")

# Function to send data
def send_data(data):
    ser.write(data.encode())  # Convert string to bytes and send
    #time.sleep(0.1)
    data = ser.readline(16)
    print(data.decode().strip())

# Function to receive data
def receive_data():
    data = ser.readline()  # Read a line of data
    return data.decode()   # Convert bytes to string and return

# Example code

#send_data(chr(0x14))
send_data('\x14')
send_data('\x11')
ser.write('*IDN?')
print(receive_data())
print('*IDN?'.encode())
print('type of chr(0x14): ', type(chr(0x14)))
print('type of \'0x14\': ', type('0x14'))
print(chr(0x14).encode())
print('\x14'.encode())
send_data(chr(0x12))
ser.close()
