# Snake Game with Hand Gesture Control 🐍🎮

A classic Snake game controlled entirely by hand gestures! Point in different directions to control where the snake moves.

## Features

- 🐍 Classic Snake gameplay
- 👋 Hand gesture control using MediaPipe
- ⌨️ Keyboard controls as backup
- 🎯 Smooth gesture detection
- 📊 Score tracking
- 🎨 Clean, modern interface

## Requirements

- **Python 3.8 - 3.11** (MediaPipe compatibility)
- Webcam
- Windows/macOS/Linux

## Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Or if using Python 3.11 specifically:
```bash
python3.11 -m pip install -r requirements.txt
```

2. **Run the game:**
```bash
python3.11 main.py
```

## How to Play

### Hand Gesture Controls

**Swipe Controls (Primary):**
| Gesture | Action |
|---------|--------|
| **Swipe Up** 👆 | Move Snake Up ⬆️ |
| **Swipe Down** 👇 | Move Snake Down ⬇️ |
| **Swipe Left** 👈 | Move Snake Left ⬅️ |
| **Swipe Right** 👉 | Move Snake Right ➡️ |

**Pointing Controls (Fallback):**
| Gesture | Action |
|---------|--------|
| **Point Up** | Move Snake Up ⬆️ |
| **Point Down** | Move Snake Down ⬇️ |
| **Point Left** | Move Snake Left ⬅️ |
| **Point Right** | Move Snake Right ➡️ |
| **Thumbs Up** | Move Snake Up (alternative) |
| **Thumbs Down** | Move Snake Down (alternative) |

### Keyboard Controls (Backup)

| Key | Action |
|-----|--------|
| Arrow Keys or WASD | Move Snake |
| P | Pause/Unpause |
| R | Restart (when game over) |

## Game Rules

1. **Control the snake** using hand gestures or keyboard
2. **Eat the red food** to grow and increase your score
3. **Avoid hitting walls** or your own body
4. **Score 10 points** for each food eaten
5. **Game over** when you collide with walls or yourself

## Gesture Tips

### Swipe Controls (Recommended):
- **Swipe upward** - Move your hand upward quickly to move snake up
- **Swipe downward** - Move your hand downward quickly to move snake down
- **Swipe left/right** - Move your hand horizontally to change direction
- **Quick movement** - Make a quick, clear swipe motion
- **Natural motion** - Swipe in the direction you want the snake to go

### Pointing Controls (Fallback):
- **Point clearly** - Extend only your index finger for direction control
- **Hold steady** - Keep your hand visible and stable
- **Good lighting** - Ensure your hand is well-lit for better detection
- **One finger** - For direction control, use only your index finger
- **Alternative gestures** - Thumbs up/down work as up/down controls

## Troubleshooting

### Camera not working
- Make sure no other application is using the camera
- Check camera permissions in system settings
- Try changing `camera_index` in `gesture_controller.py` (try 1, 2, etc.)

### Gestures not detected
- Ensure good lighting
- Keep hand clearly visible in camera frame
- Try different hand positions
- Use keyboard controls as backup

### Game runs too fast/slow
- Adjust FPS in `main.py`: `game.clock.tick(10)` (change 10 to desired FPS)
- Lower number = slower, higher number = faster

### Python version issues
- MediaPipe requires Python 3.8-3.11
- If using Python 3.12+, install Python 3.11:
  ```bash
  brew install python@3.11  # macOS
  python3.11 -m pip install -r requirements.txt
  ```

## Customization

### Change Game Speed
Edit `main.py`:
```python
game.clock.tick(10)  # Change 10 to desired FPS (5-20 recommended)
```

### Change Game Size
Edit `main.py`:
```python
game = SnakeGame(width=800, height=600, block_size=20)
```

### Change Gesture Sensitivity
Edit `gesture_controller.py`:
```python
self.hands = self.mp_hands.Hands(
    min_detection_confidence=0.7,  # Increase for stricter detection
    min_tracking_confidence=0.5     # Increase for better tracking
)
```

### Add New Gestures
Edit `gesture_controller.py` in the `_classify_gesture` method, then update `snake_game.py` in the `handle_gesture` method.

## Project Structure

```
chatbot/
├── main.py                 # Main application entry point
├── snake_game.py           # Snake game logic
├── gesture_controller.py   # Hand gesture detection
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## How It Works

1. **Camera captures** your hand in real-time
2. **MediaPipe detects** hand landmarks (21 points)
3. **Gesture classifier** identifies the gesture (point up/down/left/right)
4. **Game receives** direction command
5. **Snake moves** in that direction
6. **Game updates** and renders continuously

## Future Enhancements

- Multiple difficulty levels
- Power-ups and special foods
- Multiplayer mode
- Custom gesture training
- Score leaderboard
- Different snake skins

## License

This project is provided as-is for educational and personal use.

## Credits

- Built with Pygame for game rendering
- MediaPipe for hand gesture recognition
- OpenCV for camera handling

Enjoy playing! 🎮🐍

