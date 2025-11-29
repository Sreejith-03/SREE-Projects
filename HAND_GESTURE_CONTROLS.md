# Hand Gesture Controls Guide 🎮👋

Complete guide on how to control the Snake game using hand gestures.

## Quick Start

1. **Run the game:**
   ```bash
   python3.11 main.py
   ```

2. **Position yourself:**
   - Sit in front of your webcam
   - Make sure your hand is clearly visible
   - Ensure good lighting

3. **Show gestures:**
   - Point your index finger in the direction you want the snake to move
   - The snake will move in that direction!

---

## Gesture Controls

### ⬆️ Move Up (Point Up)

**How to do it:**
- Extend **only your index finger** (pointing finger)
- Point it **upward** (toward the ceiling)
- Keep other fingers closed (middle, ring, pinky)
- Keep thumb relaxed/closed

**Visual:**
```
    👆 (Index finger pointing up)
    |
    |
```

**Alternative gestures for UP:**
- **Thumbs Up** 👍 - Extend thumb upward, close all other fingers
- **Peace Sign** ✌️ - Extend index and middle fingers (V sign)

---

### ⬇️ Move Down (Point Down)

**How to do it:**
- Extend **only your index finger**
- Point it **downward** (toward the floor)
- Keep other fingers closed

**Visual:**
```
    |
    |
    👇 (Index finger pointing down)
```

**Alternative gestures for DOWN:**
- **Thumbs Down** 👎 - Extend thumb downward, close all other fingers
- **Fist** ✊ - Close all fingers into a fist

---

### ⬅️ Move Left (Point Left)

**How to do it:**
- Extend **only your index finger**
- Point it **to your left** (camera's right)
- Keep other fingers closed
- Make sure your finger is clearly to the left of your wrist

**Visual:**
```
👈 (Index finger pointing left)
```

**Tip:** Rotate your hand so the index finger is clearly to the left side of your wrist.

---

### ➡️ Move Right (Point Right)

**How to do it:**
- Extend **only your index finger**
- Point it **to your right** (camera's left)
- Keep other fingers closed
- Make sure your finger is clearly to the right of your wrist

**Visual:**
```
👉 (Index finger pointing right)
```

**Tip:** Rotate your hand so the index finger is clearly to the right side of your wrist.

---

## Complete Gesture Reference

| Gesture | Action | How to Make It |
|---------|--------|----------------|
| **Point Up** 👆 | Move Up | Index finger only, pointing upward |
| **Point Down** 👇 | Move Down | Index finger only, pointing downward |
| **Point Left** 👈 | Move Left | Index finger only, pointing left |
| **Point Right** 👉 | Move Right | Index finger only, pointing right |
| **Thumbs Up** 👍 | Move Up | Thumb up, other fingers closed |
| **Thumbs Down** 👎 | Move Down | Thumb down, other fingers closed |
| **Peace Sign** ✌️ | Move Up | Index and middle fingers extended (V) |
| **Fist** ✊ | Move Down | All fingers closed |

---

## Step-by-Step Instructions

### For Best Results:

1. **Start the game:**
   ```bash
   python3.11 main.py
   ```

2. **Position your hand:**
   - Hold your hand in front of the camera
   - Keep it at a comfortable distance (about 1-2 feet from camera)
   - Make sure your entire hand is visible in the frame

3. **Make the gesture:**
   - For **UP**: Point index finger upward
   - For **DOWN**: Point index finger downward
   - For **LEFT**: Point index finger to your left
   - For **RIGHT**: Point index finger to your right

4. **Hold the gesture:**
   - Keep the gesture steady for a moment
   - The snake will change direction
   - You don't need to hold it continuously - just show it when you want to change direction

5. **Change direction:**
   - Show a new gesture to change direction
   - The snake will move in the new direction

---

## Tips for Better Detection

### ✅ DO:
- **Use only your index finger** for direction control (most reliable)
- **Point clearly** - make sure the finger is fully extended
- **Keep hand steady** - avoid rapid movements
- **Good lighting** - ensure your hand is well-lit
- **Full hand visible** - keep entire hand in camera frame
- **Point distinctly** - make sure the direction is clear (up/down/left/right)

### ❌ DON'T:
- Don't extend multiple fingers (except for peace sign/thumbs)
- Don't move too fast - give the camera time to detect
- Don't block your hand - keep it fully visible
- Don't use in dark lighting - camera needs to see your hand clearly
- Don't point at an angle - point clearly in one direction

---

## Troubleshooting

### Gesture not detected?

1. **Check lighting:**
   - Move to a brighter area
   - Face a light source
   - Avoid backlighting

2. **Check hand position:**
   - Make sure entire hand is visible
   - Keep hand at comfortable distance (not too close/far)
   - Point clearly in one direction

3. **Check gesture:**
   - Use only index finger for direction control
   - Make sure finger is fully extended
   - Point distinctly (not at an angle)

4. **Use keyboard backup:**
   - Arrow keys or WASD work as backup
   - Press P to pause if needed

### Snake not moving in correct direction?

1. **Check gesture direction:**
   - Point clearly UP for up, DOWN for down, etc.
   - Make sure you're pointing in the intended direction

2. **Check hand orientation:**
   - For left/right, rotate your hand so the direction is clear
   - The index finger should be clearly to the left or right of your wrist

3. **Try alternative gestures:**
   - Use thumbs up/down for up/down
   - Use peace sign for up
   - Use fist for down

---

## Practice Tips

1. **Start simple:**
   - Practice pointing up and down first
   - These are usually the easiest to detect

2. **Get comfortable:**
   - Find a comfortable hand position
   - Practice making each gesture clearly

3. **Watch the game:**
   - The game shows "Gesture: [name]" when detected
   - Use this to see if your gestures are being recognized

4. **Use keyboard as backup:**
   - If gestures aren't working, use arrow keys
   - You can mix gestures and keyboard controls

---

## Example Gameplay

```
1. Start game → Snake appears moving right
2. Point UP → Snake changes direction to up ⬆️
3. Point RIGHT → Snake changes direction to right ➡️
4. Point DOWN → Snake changes direction to down ⬇️
5. Point LEFT → Snake changes direction to left ⬅️
6. Eat food → Snake grows, score increases
7. Continue pointing to control direction
```

---

## Advanced: Customizing Gestures

If you want to change how gestures work, edit `gesture_controller.py`:

- Adjust detection thresholds
- Add new gestures
- Modify gesture recognition logic

See the code comments for details on how gesture detection works.

---

## Quick Reference Card

```
⬆️ UP:    Point index finger UP
⬇️ DOWN:  Point index finger DOWN  
⬅️ LEFT:  Point index finger LEFT
➡️ RIGHT: Point index finger RIGHT

Alternatives:
👍 Thumbs Up = UP
👎 Thumbs Down = DOWN
✌️ Peace Sign = UP
✊ Fist = DOWN
```

**Remember:** The most reliable control is pointing with your index finger in the direction you want to go!

Enjoy playing! 🐍🎮

