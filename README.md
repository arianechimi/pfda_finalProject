# Project title: Get Out

# Demo
Demo video: https://youtu.be/wg7f20eHLDQ 

## GitHub Repository
GitHub Repo: https://github.com/arianechimi/pfda_finalProject

## Description

This is a platformer game built using python where a player is stuck in somewhere and has to get out. The player walk and jump across platforms, avoid enemies and lava while collecting coins on their way to the top where the exit is located.

The games has many features like a player that moves around and jumps, platforms that move up and down but also left to right, enemy obstacles, lava, and coin collection with a score counter. There is a start menu. "Start" will start the game and "Exit" will close the game. The game also has music and sounds effects to add to the overall experience.

## Files

GetOut.py which contain my main game file with my game logic, classes, and game loop.

The images folder has all my image assets like my player, tiles, enemies, lava, coin, and UI buttons.

The sounds folder has all my audio asssets like background music, coin, jump, and game over sound effects.

## Design

For the design, I went for a dark forest where no one would like to be stuck in. I choose the tiles to work with that mood also.

The game uses a tile-based map where each number in the world_data list represents a different tile type (this is my grid). This makes it straightforward to design and modify the level and add new tile.

## Future Improvements

I am proud of the game but if I could impove and add anything, I will:
 - Add a timer to stress the player to get out as fast as possible
 - Make a more complicated level and add more enemies
 - Add a feature where if the player falls from the very top then they die
 - The background music and sound effects volume set well to create a better experience 
 - Instead of game over, make the player lose a life every time they die (max 5 lives)