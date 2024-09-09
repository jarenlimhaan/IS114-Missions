# Set the radio group for communication
radio.set_group(1)
radio.set_transmit_power(1)

# Set Touch config?
pins.touch_set_mode(TouchTarget.LOGO, TouchTargetMode.RESISTIVE)

# Constants
MILLISECONDS = 1000

class Alarm:

    def __init__(self):
        self.hours = 0
        self.game_mode = 1
        self.set_handlers()

    # Send request to start the maze game on another micro:bit
    def send_radio_request_for_game(self):
        radio.send_string("reqGame")

    # Send request to start the flappybird game on another micro:bit
    def send_radio_request_for_game2(self):
        radio.send_string("reqGame2")

    # Send request to start logging time 
    def send_radio_request_for_datalogger(self):
        radio.send_string("reqData")

    # Send request to make user put the other micro:bit straight
    def send_radio_request_for_orientation(self):
        radio.send_string("req")

    # Send request to stop logging time data
    def stop_data_logging(self):
        radio.send_string("reqDataGameFinish")

    # Set Event Handlers
    def set_handlers(self):

        ## Set Touch Utils 
        def on_logo_pressed():
            self.game_mode = 2 if self.game_mode == 1 else 1

        ## Set Radio Utils
        def set_radio_receive(receivedString):
            if receivedString == "resGame" or receivedString == "resGame2":
                '''
                Send request to check orientation 
                to make sure user put it straight
                '''
                self.send_radio_request_for_orientation()
            if receivedString == "res":
                '''
                Stop the logging of time data 
                and off the alarm 
                '''
                self.stop_data_logging()
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

        # Set radio event handler, button event handlers 
        # and touch event handler
        input.on_button_pressed(Button.A, on_button_pressed_a)
        input.on_button_pressed(Button.B, on_button_pressed_b)
        radio.on_received_string(set_radio_receive)
        input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

    # Stop the alarm sound
    def off_alarm(self):
        music.stop_melody(MelodyStopOptions.ALL)

    # Play alarm sound
    def play_alarm(self):
        # After alarm, request the game to start
        if self.game_mode == 1:
            self.send_radio_request_for_game()
        else:
            self.send_radio_request_for_game2()
        self.send_radio_request_for_datalogger()

        # Start Melody
        music.set_volume(255)
        music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.FOREVER_IN_BACKGROUND)
        basic.show_icon(IconNames.SAD)
        self.hours = 0
    

# Initialize the alarm class
init_alarm = Alarm()
