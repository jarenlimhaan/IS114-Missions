# Set the radio group for communication
radio.set_group(1)
radio.set_transmit_power(1)

class Game:
    def __init__(self):
        # Maze and player variables
        self.maze = [[0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0]]

        self.playerX = 0
        self.playerY = 0
        self.set_handlers()

    # Function to plot maze and player
    def displayMazeAndPlayer(self, x: number, y: number):
        for row in range(5):
            for col in range(5):
                if self.maze[row][col] == 1:
                    led.plot_brightness(col, row, 80)
                else:
                    led.unplot(col, row)
        led.plot_brightness(x, y, 255)

    # Function to handle game
    def run_game(self):
        playerX, playerY, maze   = self.playerX, self.playerY, self.maze
        while True:
            if input.button_is_pressed(Button.A):
                if playerX > 0 and maze[playerY][playerX - 1] == 0:
                    playerX -= 1
                    self.displayMazeAndPlayer(playerX, playerY)
                basic.pause(100)
            if input.button_is_pressed(Button.B):
                if playerX < 4 and maze[playerY][playerX + 1] == 0:
                    playerX += 1
                    self.displayMazeAndPlayer(playerX, playerY)
                basic.pause(100)
            if input.acceleration(Dimension.Y) < -300:
                if playerY > 0 and maze[playerY - 1][playerX] == 0:
                    playerY -= 1
                    self.displayMazeAndPlayer(playerX, playerY)
                basic.pause(100)
            if input.acceleration(Dimension.Y) > 300:
                if playerY < 4 and maze[playerY + 1][playerX] == 0:
                    playerY += 1
                    self.displayMazeAndPlayer(playerX, playerY)
                basic.pause(100)
            if playerX == 4 and playerY == 4:
                basic.show_icon(IconNames.HAPPY)
                basic.pause(1000)
                self.send_radio_request_for_game_over()
                game.game_over()

    # Send game over message back to the alarm micro:bit
    def send_radio_request_for_game_over(self):
        radio.send_string("resGame")

    def set_handlers(self):
        # Receive radio request to start the game
        def set_radio_receive(receivedString):
            if receivedString == "reqGame":
                self.displayMazeAndPlayer(self.playerX, self.playerY)
                self.run_game()

        # Set radio event handler
        radio.on_received_string(set_radio_receive)

init_game = Game()