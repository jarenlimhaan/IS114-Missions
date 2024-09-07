class DisplayOrientation:

    def __init__(self):
        self.set_handlers()

    def set_handlers(self):
        def set_radio_receive(recieved_string):
            if recieved_string == "reqOri":
                self.check_orientation()

        radio.on_received_string(set_radio_receive)

    def send_radio_request_for_done_checking_orientation(self):
        radio.send_string("resOri")

    def check_orientation(self):
        while True:
            # Read accelerometer values
            x = input.acceleration(Dimension.X)
            y = input.acceleration(Dimension.Y)
            z = input.acceleration(Dimension.Z)
            # Define thresholds for determining orientation
            threshold = 200
            # Once the orientation is determined, send a radio response
            if not (abs(z) > abs(x) + threshold and abs(z) > abs(y) + threshold):
                self.send_radio_request_for_done_checking_orientation()
            # Pause to update every half second
            basic.pause(100)

init_displayOrientation = DisplayOrientation()