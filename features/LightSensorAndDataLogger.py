# Set the radio group for communication
radio.set_group(1)
radio.set_transmit_power(1)

# Initialize datalogger
datalogger.set_column_titles("Time", "Light Level")  # Set datalogger headers

class LightSensorAndLogger:
    def __init__(self):
        self.light_threshold = 50
        self.running = False
        self.seconds = 0
        self.set_handlers()

    def set_handlers(self):

        # Radio receive handler
        def on_received_string(receivedString):
            if receivedString == "reqLight":
                self.running = True
                self.log_time_and_light()
            if receivedString == "reqLightGameFinish":
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

    # Continuous logging of time and light level
    def log_time_and_light(self):
        while True:
            if self.running:
                # Increment time every second
                basic.pause(1000)
                self.seconds += 1
                
                # Check the current light level
                light_level = input.light_level()
                
                # Log both time and light level continuously
                datalogger.log(datalogger.create_cv("Time", self.seconds), datalogger.create_cv("Light Level", light_level))

init_lightSensorAndLogger = LightSensorAndLogger()