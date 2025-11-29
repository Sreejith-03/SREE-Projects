"""
Main application: Snake Game with Hand Gesture Control
Run this file to start the game
"""

import sys
import time
from snake_game import SnakeGame
from gesture_controller import GestureController


def main():
    """Main game loop"""
    print("=" * 10)
    print("Snake Game - Hand Gesture Control")
    print("=" * 10)
    print()
    print("Controls:")
    print("  Point Up    → Move Up")
    print("  Point Down  → Move Down")
    print("  Point Left  → Move Left")
    print("  Point Right → Move Right")
    print("  Thumbs Up   → Move Up (alternative)")
    print("  Thumbs Down → Move Down (alternative)")
    print()
    print("Keyboard Controls (backup):")
    print("  Arrow Keys or WASD → Move")
    print("  P → Pause")
    print("  R → Restart (when game over)")
    print()
    print("Starting game...")
    print()
    
    # Initialize game
    game = SnakeGame(width=800, height=600, block_size=20)
    
    # Initialize gesture controller
    gesture_controller = None
    use_gestures = True
    
    try:
        gesture_controller = GestureController(camera_index=0)
        gesture_controller.start_camera()
        print("✅ Camera initialized - Gesture control enabled")
    except Exception as e:
        print(f"⚠️  Could not initialize camera: {e}")
        print("   Game will run with keyboard controls only")
        use_gestures = False
    
    # Game loop
    running = True
    last_gesture = None
    gesture_cooldown = 0.1  # Minimum time between gesture changes (seconds)
    last_gesture_time = 0
    
    try:
        while running:
            # Detect gesture
            current_gesture = None
            if use_gestures:
                try:
                    current_gesture = gesture_controller.detect_gesture()
                    
                    # Apply cooldown to prevent rapid direction changes
                    current_time = time.time()
                    if (current_gesture and 
                        current_gesture != last_gesture and 
                        current_time - last_gesture_time > gesture_cooldown):
                        last_gesture = current_gesture
                        last_gesture_time = current_time
                    elif current_gesture == last_gesture:
                        current_gesture = None  # Don't repeat same gesture
                except Exception as e:
                    print(f"Gesture detection error: {e}")
                    current_gesture = None
            
            # Run game frame
            running = game.run_frame(current_gesture)
            
            # Control game speed
            game.clock.tick(10)  # 10 FPS for snake movement
    
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user")
    
    finally:
        # Cleanup
        game.quit()
        if gesture_controller:
            gesture_controller.release()
        print("Game closed. Thanks for playing!")


if __name__ == "__main__":
    main()

