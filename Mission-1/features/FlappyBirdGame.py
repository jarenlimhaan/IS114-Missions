# Set the radio group for communication
radio.set_group(1)
radio.set_transmit_power(1)

def move_columns():
    # Move obstacles to the left
    for index in range(4):
        for obstacle in obstacles:
            obstacle.change(LedSpriteProperty.X, -1)
        basic.pause(500)

def create_column():
    # Generate a new column of obstacles
    global empty_column_y
    empty_column_y = randint(0, 4)
    for index in range(5):
        if index != empty_column_y:
            obstacles.append(game.create_sprite(4, index))

def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def remove_offscreen_columns():
    # Remove obstacles that reach the left edge
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()

empty_column_y = 0
bird: game.LedSprite = None
obstacles: List[game.LedSprite] = []
bird = game.create_sprite(0, 2)
bird.set(LedSpriteProperty.BLINK, 300)
n = 5
games_played = 0

def main_game_loop():
    global games_played, n
    while games_played != n:  # Make the player play n number of times
        create_column()  # Create a new set of obstacles
        move_columns()  # Move the obstacles
        remove_offscreen_columns()  # Remove obstacles that go off-screen

        games_played += 1

        # Check for collision
        for obstacle in obstacles:
            if obstacle.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) and obstacle.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y):
                games_played = 0
                control.reset()  # Restart the game upon collision
    
    send_radio_request_for_game_over()
    game.game_over()

# Send game over message back to the alarm micro:bit
def send_radio_request_for_game_over():
    radio.send_string("resGame2")

def set_radio_receive(receivedString):
    if receivedString == "reqGame2":
        '''
        Send request to check orientation
        to make sure user put it straight
        '''
        # Start the game loop
        main_game_loop()

radio.on_received_string(set_radio_receive)