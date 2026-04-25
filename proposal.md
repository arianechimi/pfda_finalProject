Platformer Game
Repository
https://github.com/arianechimi/angm2305-26s-final-project-proposal

Description
I want to create a platformer game where you have to escape a room you are stuck in. The player will have to avoid enemy along the way and collect coins. They will jump all the way to the top where the exit door is located.

Features
Feature 1: Player Movement
The player will jump using a specific key and falls after jumping. The player will also move left and right using another specific keys.
Feature 2: Platformer
Platforms will be placed at different heights to create a vertical path.
Feature 3: Enemy Obstacles
Enemies will move left and right on platforms. If player touch an enemy, a message "Game Over" will appear on the screen and player will die.
Feature 4: Coin collection
Coins will be placed across platforms. When player touches a coin, it disappears and increases the score.
Feature 5: Exit Door
The exit door will be at top of the platformer. You have to reach it to win.
Feature 6: UI
Display player's coin count and message like "Game Over" and "You win!".
Feature 7: Collision
Detect collisions between player, platforms, enemies, and coins.
Feature 8: Restart Mechanic
Press a key to restart the game
Feature 9: Level Design
Game will take place in a room and player can progress to a more challenging level (2 levels minimum)
Challenges
How to implement collision detection between the player, enemies, and coins.
Apply gravity and jumping mechanics for player movement.
Game states (start, playing, game over, win) and restarting the game properly.
Outcomes
Ideal Outcome: At the end, There will be a fully playable platformer where the player can move, jump between platforms, avoid enemies, collect coins, and successfully reach the exit at the top to complete at least 1 level.

Minimal Viable Outcome: A playable platformer where the player can move and jump, land on platforms. The player will avoid at least 1 enemy by jumping then reach thewe exit and win or fall and lose.

Milestones
Week 1

Set up the project in Python with pygame and create main function with basic game loop.
Set up player movement.
Week 2

Add platforms and collision detection so the player can land and move between them.
Implement coins and basic scoring system.
Week 3

Add enemies with simple movement and player collision.
Create the exit door and win condition.
Week 4

Add UI elements liked score, win/lose text, restart.
Polish the game: fix bugs, test full gameplay.
