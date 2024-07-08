import serial

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

# Function to receive data
def receive_data():
    data = ser.readline()  # Read a line of data
    return data.decode()   # Convert bytes to string and return

# Example usage
send_data(chr(0x14))
response = receive_data()
print("Received:", response)

# Close the serial connection
ser.close()
