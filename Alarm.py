# Set the radio group for communication
radio.set_group(1)
radio.set_transmit_power(1)
MILLISECONDS = 1000

class Alarm:

    def __init__(self):
        self.hours = 0
        self.set_handlers()

    # Send request to start the game on another micro:bit
    def send_radio_request_for_game(self):
        radio.send_string("reqGame")

    # Send request to check light and start logging
    def send_radio_request_for_light_and_datalogger(self):
        radio.send_string("reqLight")

    def send_radio_request_for_orientation(self):
        radio.send_string("reqOri")

    def stop_light_and_data_logging(self):
        radio.send_string("reqLightGameFinish")

    # Set event handlers
    def set_handlers(self):

        ## Set Radio Utils
        def set_radio_receive(receivedString):
            if receivedString == "resGame":
                '''
                Send request to check orientation 
                to make sure user put it straight
                '''
                self.send_radio_request_for_orientation
            if receivedString == "resOri":
                '''
                Stop the logging of light and data 
                and off the alarm 
                '''
                self.stop_light_and_data_logging()
                self.off_alarm()

        ## Set Timer Utils 
        def on_button_pressed_a():
            self.hours += 1
            basic.show_number(self.hours)
            basic.clear_screen()

        def on_button_pressed_b():
            basic.show_number(self.hours)
            basic.clear_screen()
            for index in range(self.hours):
                basic.pause(MILLISECONDS)
                basic.clear_screen()
            self.play_alarm()

        # Set radio and button event handlers
        input.on_button_pressed(Button.A, on_button_pressed_a)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        radio.on_received_string(set_radio_receive)

    # Stop the alarm sound
    def off_alarm(self):
        music.stop_melody(MelodyStopOptions.ALL)

    # Play alarm sound
    def play_alarm(self):
        # After alarm, request the game to start
        self.send_radio_request_for_game()
        self.send_radio_request_for_light_and_datalogger()
        music.set_volume(255)
        music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.FOREVER_IN_BACKGROUND)
        basic.show_icon(IconNames.SAD)
        self.hours = 0
    

# Initialize the alarm class
init_alarm = Alarm()
