# Swipe Controls Guide 🎮👋

## How to Control Snake with Swipes

The game now supports **swipe gestures** - move your hand in a direction to control the snake!

---

## Quick Start

1. **Run the game:**
   ```bash
   python3.11 main.py
   ```

2. **Position your hand:**
   - Hold your hand in front of the camera
   - Keep it visible and well-lit

3. **Swipe to control:**
   - **Swipe UP** → Snake moves up ⬆️
   - **Swipe DOWN** → Snake moves down ⬇️
   - **Swipe LEFT** → Snake moves left ⬅️
   - **Swipe RIGHT** → Snake moves right ➡️

---

## Detailed Swipe Instructions

### ⬆️ Swipe Up (Move Snake Up)

**How to do it:**
1. Start with your hand at a lower position
2. Quickly move your hand **upward** (toward the top of the screen)
3. Make a clear, quick upward motion
4. The snake will move up!

**Visual:**
```
Start:  👋 (hand lower)
         ↓ (swipe upward)
End:    👋 (hand higher)
```

**Tips:**
- Make a quick, clear upward motion
- Don't move too slowly
- Keep your hand visible throughout the swipe

---

### ⬇️ Swipe Down (Move Snake Down)

**How to do it:**
1. Start with your hand at a higher position
2. Quickly move your hand **downward** (toward the bottom of the screen)
3. Make a clear, quick downward motion
4. The snake will move down!

**Visual:**
```
Start:  👋 (hand higher)
         ↓ (swipe downward)
End:    👋 (hand lower)
```

---

### ⬅️ Swipe Left (Move Snake Left)

**How to do it:**
1. Start with your hand on the right side
2. Quickly move your hand **to the left** (toward your left)
3. Make a clear, quick leftward motion
4. The snake will move left!

**Visual:**
```
Start:     👋 (hand on right)
            ← (swipe left)
End:   👋 (hand on left)
```

---

### ➡️ Swipe Right (Move Snake Right)

**How to do it:**
1. Start with your hand on the left side
2. Quickly move your hand **to the right** (toward your right)
3. Make a clear, quick rightward motion
4. The snake will move right!

**Visual:**
```
Start:  👋 (hand on left)
          → (swipe right)
End:        👋 (hand on right)
```

---

## Tips for Best Results

### ✅ DO:
- **Make quick swipes** - Fast, clear movements work best
- **Swipe in one direction** - Keep the motion straight (up, down, left, or right)
- **Keep hand visible** - Don't move hand out of camera frame
- **Good lighting** - Ensure your hand is well-lit
- **Natural motion** - Swipe naturally in the direction you want to go
- **Wait between swipes** - Give the system time to detect (about 0.3 seconds)

### ❌ DON'T:
- Don't move too slowly - The system needs to detect movement speed
- Don't make circular motions - Keep swipes straight
- Don't swipe too frequently - There's a cooldown between swipes
- Don't block your hand - Keep it fully visible
- Don't use in dark lighting - Camera needs to see your hand

---

## How Swipe Detection Works

1. **Camera tracks your hand position** over time
2. **System calculates movement** - direction and speed
3. **Detects swipe** - if movement is fast and clear enough
4. **Snake changes direction** - based on swipe direction

### Technical Details:
- **Swipe threshold**: Movement must be at least 5% of screen size
- **Speed threshold**: Movement must be fast enough to be a swipe
- **Cooldown**: 0.3 seconds between swipes (prevents rapid changes)
- **Direction detection**: System determines if swipe is primarily up/down/left/right

---

## Troubleshooting

### Swipe not detected?

1. **Check movement speed:**
   - Make sure you're swiping quickly
   - Slow movements won't be detected as swipes

2. **Check movement distance:**
   - Swipe must be significant (at least 5% of screen)
   - Small movements won't trigger

3. **Check cooldown:**
   - Wait about 0.3 seconds between swipes
   - Too frequent swipes may be ignored

4. **Check hand visibility:**
   - Keep hand in camera frame
   - Ensure good lighting

5. **Try pointing instead:**
   - If swipes don't work, the game falls back to pointing gestures
   - Point your index finger in the direction you want

---

## Comparison: Swipe vs Pointing

| Method | How It Works | Best For |
|--------|-------------|----------|
| **Swipe** | Move hand quickly in direction | Quick direction changes, natural motion |
| **Pointing** | Point index finger in direction | Precise control, holding direction |

**Both methods work!** The game tries swipe first, then falls back to pointing if no swipe is detected.

---

## Example Gameplay with Swipes

```
1. Start game → Snake moving right
2. Swipe UP → Snake changes to up ⬆️
3. Swipe RIGHT → Snake changes to right ➡️
4. Swipe DOWN → Snake changes to down ⬇️
5. Swipe LEFT → Snake changes to left ⬅️
6. Continue swiping to control direction
```

---

## Customization

### Adjust Swipe Sensitivity

Edit `gesture_controller.py`:

```python
self.swipe_threshold = 0.05  # Increase for larger swipes needed
self.swipe_speed_threshold = 0.02  # Increase for faster swipes needed
self.swipe_cooldown = 0.3  # Increase for longer wait between swipes
```

### Disable Swipe (Use Only Pointing)

Edit `main.py`:

```python
gesture_controller = GestureController(camera_index=0, use_swipe=False)
```

---

## Quick Reference

```
⬆️ Swipe Up    → Snake goes UP
⬇️ Swipe Down  → Snake goes DOWN
⬅️ Swipe Left  → Snake goes LEFT
➡️ Swipe Right → Snake goes RIGHT
```

**Remember:** Make quick, clear swipes in the direction you want the snake to move!

Enjoy playing! 🐍🎮




