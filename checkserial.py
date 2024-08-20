from pyfirmata import Arduino, util

PORT = 'COM6'  # Change this to match your port

# Establish a connection to the Arduino
board = Arduino(PORT)

# Start an iterator thread so that serial buffer doesn't overflow
it = util.Iterator(board)
it.start()

# Get a reference to the digital pin where you want to read the RFID data
# For example, if you are using pin 2 for receiving RFID data
# Replace it with the appropriate pin number you are using
digital_input_pin = board.get_pin('d:9:i')

try:
    while True:
        # Read RFID data sent by Arduino via Firmata
        incoming_data = board.iterate()
        if incoming_data is not None:
            print(f"Received RFID Tag ID: {incoming_data}")
except KeyboardInterrupt:
    pass
