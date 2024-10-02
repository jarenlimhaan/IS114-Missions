# Set the radio group for communication
radio.set_group(1)
radio.set_transmit_power(1)

# Initialize datalogger
datalogger.set_column_titles("Time")  # Set datalogger headers

class DataLogger:
    def __init__(self):
        self.running = False
        self.seconds = 0
        self.set_handlers()

    def set_handlers(self):

        # Radio receive handler
        def on_received_string(receivedString):
            if receivedString == "reqData":
                self.running = True
                self.log_time()
            if receivedString == "reqDataGameFinish":
                self.running = False
                basic.show_number(self.seconds)  # Show final time
        
        # Button A starts the timer
        def on_button_pressed_a():
            self.running = True
        
        # Button B stops the timer and shows the elapsed time
        def on_button_pressed_b():
            self.running = False
            basic.show_number(self.seconds)
        
        input.on_button_pressed(Button.A, on_button_pressed_a)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        radio.on_received_string(on_received_string)

    def log_time(self):
        while True:
            if self.running:
                # Increment time every second
                basic.pause(1000)
                self.seconds += 1
                
                datalogger.log(datalogger.create_cv("Time", self.seconds))

init_DataLogger = DataLogger()