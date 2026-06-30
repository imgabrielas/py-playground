# Street Crossing Game

A Frogger-inspired game built with Python's `turtle` module. Guide a turtle across a busy street filled with oncoming cars — each successful crossing increases the difficulty.

## How to Play

- Run `main.py` to start the game.
- Press the **Up arrow** key to move the turtle forward.
- Reach the top of the screen to complete a crossing and advance to the next level.
- Avoid the cars — any collision ends the game.

## Gameplay

- Cars spawn randomly on the right side of the screen and move left.
- Each time you successfully cross, car speed increases by 2.
- The current level is displayed in the top-left corner.
- A "GAME OVER" message appears on collision.

## Project Structure

| File | Description |
|---|---|
| `main.py` | Game loop, screen setup, collision and finish-line detection |
| `player.py` | Player (turtle) movement and position logic |
| `car_manager.py` | Car spawning, movement, and speed scaling per level |
| `scoreboard.py` | Level display and game-over message |

## Requirements

- Python 3.x
- No external dependencies — uses the built-in `turtle` module

## Running

```bash
python main.py
```
