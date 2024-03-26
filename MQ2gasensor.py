# Raspberry Pi Python Script

import serial

# Configure serial port
ser = serial.Serial('/dev/ttyACM0', 9600) # Use appropriate port name (e.g., '/dev/ttyACM0', '/dev/ttyUSB0') and baud rate

while True:
    try:
        # Read data from serial port
        sensor_data = ser.readline().decode().strip()
        
        # Print received sensor data
        print("Received Sensor Data:", sensor_data)
        
        # Here you can add code to process the sensor data as needed
        # For example, you can store it in a database, display it, or send alerts
        
    except KeyboardInterrupt:
        print("\nExiting program...")
        break

# Close serial port
ser.close()
