# Snake Game

This is a simple Snake Game implemented in Python using the Turtle graphics library. The objective of the game is to control a snake on the screen, guiding it to eat food while avoiding collisions with the walls and itself.

## Getting Started

### Clone the Repository

Clone this repository to your local machine using the following command:

```shell
git clone https://github.com/scienmanas/Nokia-Snake-Game
```
## Navigate to Directory
Change your working directory to the cloned repository:
```bash
cd snake-game
```
## Run the Game
Execute the Python script to start the game:
```bash
python main.py
```
## How to Play

1. **Controls:** Use the arrow keys on your keyboard to control the snake's direction:
   - **Up Arrow:** Move the snake upwards
   - **Down Arrow:** Move the snake downwards
   - **Left Arrow:** Move the snake to the left
   - **Right Arrow:** Move the snake to the right

2. **Objective:** Guide the snake to eat the food items that appear on the screen. Each time the snake consumes a piece of food, its length will increase, and you'll earn points.

3. **Avoid Collisions:** Be careful not to collide with the walls or the snake's own body. If the snake crashes into a wall or itself, the game will end.

## How to Restart

If you'd like to restart the game after a game over or whenever you want to start fresh, follow these steps:

1. Close the game window if it's still open.

2. Open your terminal or command prompt.

3. Run the main.py file again

## Game Features
1. The snake's movement speed can be adjusted by modifying the time.sleep() duration in the code.
2. The game keeps track of your score, displaying it on the screen.
3. If you collide with the walls or the snake's own body, the game will end, and you can restart by pressing the arrow keys.
## ScreenShots
<img width="449" alt="image" src="https://github.com/scienmanas/Nokia-Snake-Game/assets/99756067/33cbd332-6b81-4d5c-99ea-3d0f3b0c8a09">
   
## Dependencies
This Snake Game requires the following Python packages:

1. Turtle: The graphics library used for creating the game's visuals.
## Code Structure
The code is organized into several files to improve readability and maintainability:

1. main.py: The main script that sets up the game environment, listens for user input, and controls the game loop.
2. snake.py: Contains the Snake class, responsible for managing the snake's behavior and movement.
3. food.py: Contains the Food class, responsible for generating and refreshing food items on the screen.
4. scoreboard.py: Contains the ScoreBoard class, responsible for displaying the player's score and game over messages.
## Contributions
Contributions to this Snake Game project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This Snake Game project is licensed under the MIT License.
