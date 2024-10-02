# Set the radio group for communication
radio.set_group(1)
radio.set_transmit_power(1)

class DisplayOrientation:

    def __init__(self):
        self.set_handlers()

    def set_handlers(self):
        def set_radio_receive(recieved_string):
            if recieved_string == "req":
                self.check_orientation()

        radio.on_received_string(set_radio_receive)

    def send_radio_request_for_done_checking_orientation(self):
        radio.send_string("res")

    def check_orientation(self):
        while True:
            # Read accelerometer values
            x = input.acceleration(Dimension.X)
            y = input.acceleration(Dimension.Y)
            z = input.acceleration(Dimension.Z)
            # Define thresholds for determining orientation
            threshold = 200
            # Any other orientation
            if not (abs(z) > abs(x) + threshold and abs(z) > abs(y) + threshold):
                basic.show_number(2)
                self.send_radio_request_for_done_checking_orientation()
            # Pause to update every half second
            basic.pause(100)

init_displayOrientation = DisplayOrientation()