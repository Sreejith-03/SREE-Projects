"""
Hand Gesture Controller for Snake Game
Detects hand gestures and maps them to directions
"""

import cv2
import mediapipe as mp
import numpy as np
from typing import Optional, List, Tuple
import time
from collections import deque


class GestureController:
    """Hand gesture detection for snake game control with swipe detection"""
    
    def __init__(self, camera_index: int = 0, use_swipe: bool = True):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.6,  # Lowered for better initial detection
            min_tracking_confidence=0.6  # Increased for more stable tracking
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.camera_index = camera_index
        self.cap = None
        
        # Swipe detection parameters
        self.use_swipe = use_swipe
        self.position_history: deque = deque(maxlen=10)  # Store last 10 positions
        self.swipe_threshold = 0.05  # Minimum distance for swipe (5% of frame)
        self.swipe_speed_threshold = 0.02  # Minimum speed for swipe
        self.last_swipe_time = 0
        self.swipe_cooldown = 0.3  # Minimum time between swipes (seconds)
        
        # Temporal smoothing for gesture detection
        self.gesture_history: deque = deque(maxlen=5)  # Store last 5 detected gestures
        self.gesture_confidence_threshold = 3  # Need 3/5 frames to confirm gesture
    
    def start_camera(self):
        """Start camera capture"""
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise Exception(f"Could not open camera {self.camera_index}")
        return True
    
    def detect_gesture(self) -> Optional[str]:
        """
        Detect hand gesture from camera (swipe or static gesture)
        Returns: gesture name or None
        """
        if self.cap is None:
            return None
        
        ret, frame = self.cap.read()
        if not ret:
            return None
        
        # Flip frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Convert to RGB
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_image)
        
        if not results.multi_hand_landmarks:
            self.position_history.clear()  # Clear history if hand not detected
            self.gesture_history.clear()  # Clear gesture history too
            return None
        
        hand_landmarks = results.multi_hand_landmarks[0]
        
        # Get current hand position (using wrist or index finger tip)
        wrist = hand_landmarks.landmark[0]
        current_pos = (wrist.x, wrist.y)
        current_time = time.time()
        
        # Detect swipe first (if enabled)
        # Swipes are quick intentional movements, so they bypass smoothing
        if self.use_swipe:
            swipe_gesture = self._detect_swipe(current_pos, current_time)
            if swipe_gesture:
                # Clear gesture history when swipe detected (swipe takes priority)
                self.gesture_history.clear()
                return swipe_gesture
        
        # Store current position for swipe tracking
        self.position_history.append((current_pos, current_time))
        
        # Extract key points for static gesture detection
        landmarks = []
        for landmark in hand_landmarks.landmark:
            landmarks.append([landmark.x, landmark.y, landmark.z])
        landmarks = np.array(landmarks)
        
        # Detect static gesture (fallback)
        gesture = self._classify_gesture(landmarks)
        
        # Apply temporal smoothing
        if gesture:
            self.gesture_history.append(gesture)
        else:
            self.gesture_history.append(None)
        
        # Return gesture only if it appears consistently
        return self._get_smoothed_gesture()
    
    def _detect_swipe(self, current_pos: Tuple[float, float], current_time: float) -> Optional[str]:
        """
        Detect swipe gesture based on hand movement
        Returns: swipe direction or None
        """
        if len(self.position_history) < 3:
            return None
        
        # Check cooldown
        if current_time - self.last_swipe_time < self.swipe_cooldown:
            return None
        
        # Get positions from history
        old_pos, old_time = self.position_history[0]
        new_pos = current_pos
        
        # Calculate movement
        dx = new_pos[0] - old_pos[0]  # Horizontal movement
        dy = new_pos[1] - old_pos[1]  # Vertical movement (note: y increases downward)
        dt = current_time - old_time
        
        # Calculate distance and speed
        distance = np.sqrt(dx**2 + dy**2)
        speed = distance / dt if dt > 0 else 0
        
        # Check if movement is significant enough to be a swipe
        if distance < self.swipe_threshold or speed < self.swipe_speed_threshold:
            return None
        
        # Determine swipe direction
        # Use absolute values to find dominant direction
        abs_dx = abs(dx)
        abs_dy = abs(dy)
        
        # Check if movement is primarily in one direction
        if abs_dy > abs_dx * 1.5:  # Vertical swipe
            if dy < 0:  # Moving up (y decreases upward)
                self.last_swipe_time = current_time
                return "swipe_up"
            else:  # Moving down (y increases downward)
                self.last_swipe_time = current_time
                return "swipe_down"
        elif abs_dx > abs_dy * 1.5:  # Horizontal swipe
            if dx < 0:  # Moving left (x decreases leftward)
                self.last_swipe_time = current_time
                return "swipe_left"
            else:  # Moving right (x increases rightward)
                self.last_swipe_time = current_time
                return "swipe_right"
        
        return None
    
    def _get_smoothed_gesture(self) -> Optional[str]:
        """
        Apply temporal smoothing to reduce false positives
        Returns gesture only if it appears consistently in recent frames
        """
        if len(self.gesture_history) < self.gesture_confidence_threshold:
            return None
        
        # Count occurrences of each gesture in recent history
        recent_gestures = list(self.gesture_history)
        gesture_counts = {}
        
        for gesture in recent_gestures:
            if gesture:
                gesture_counts[gesture] = gesture_counts.get(gesture, 0) + 1
        
        # Return gesture if it appears enough times
        for gesture, count in gesture_counts.items():
            if count >= self.gesture_confidence_threshold:
                return gesture
        
        return None
    
    def _classify_gesture(self, landmarks: np.ndarray) -> Optional[str]:
        """
        Classify gesture based on hand landmarks
        Returns direction-based gestures for snake control
        """
        # Get finger tip and joint positions
        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]
        thumb_mcp = landmarks[2]
        index_tip = landmarks[8]
        index_pip = landmarks[6]
        index_mcp = landmarks[5]
        middle_tip = landmarks[12]
        middle_pip = landmarks[10]
        ring_tip = landmarks[16]
        ring_pip = landmarks[14]
        pinky_tip = landmarks[20]
        pinky_pip = landmarks[18]
        wrist = landmarks[0]
        
        # Check if fingers are extended with improved thresholds
        # Use a small tolerance to account for slight variations
        tolerance = 0.02
        index_extended = index_tip[1] < index_pip[1] - tolerance
        middle_extended = middle_tip[1] < middle_pip[1] - tolerance
        ring_extended = ring_tip[1] < ring_pip[1] - tolerance
        pinky_extended = pinky_tip[1] < pinky_pip[1] - tolerance
        
        # Improved thumb detection - check if thumb is extended outward
        # For right hand: thumb tip should be to the right of thumb IP
        # For left hand: thumb tip should be to the left of thumb IP
        # Use wrist position to determine hand side
        hand_side = "right" if thumb_mcp[0] < wrist[0] else "left"
        if hand_side == "right":
            thumb_extended = thumb_tip[0] > thumb_ip[0] + tolerance
        else:
            thumb_extended = thumb_tip[0] < thumb_ip[0] - tolerance
        
        # Point gestures: Only index finger extended, others closed
        if (index_extended and 
            not middle_extended and 
            not ring_extended and 
            not pinky_extended):
            
            # Calculate relative position of index tip to wrist
            dx = index_tip[0] - wrist[0]  # Horizontal offset
            dy = index_tip[1] - wrist[1]  # Vertical offset (positive = down)
            
            # Use improved thresholds with angle-based detection
            # Require clear directional bias (at least 0.08 difference)
            threshold = 0.08
            
            # Check if pointing in a clear direction (dominant axis)
            abs_dx = abs(dx)
            abs_dy = abs(dy)
            
            # Point Up: index tip significantly above wrist
            if abs_dy > abs_dx * 1.2 and dy < -threshold:
                return "point_up"
            
            # Point Down: index tip significantly below wrist
            elif abs_dy > abs_dx * 1.2 and dy > threshold:
                return "point_down"
            
            # Point Left: index tip significantly to the left of wrist
            elif abs_dx > abs_dy * 1.2 and dx < -threshold:
                return "point_left"
            
            # Point Right: index tip significantly to the right of wrist
            elif abs_dx > abs_dy * 1.2 and dx > threshold:
                return "point_right"
        
        # Thumbs Up: Thumb extended up, others closed
        # Check vertical position relative to thumb IP joint
        thumb_vertical_diff = thumb_ip[1] - thumb_tip[1]  # Positive if thumb is up
        if (thumb_extended and 
            thumb_vertical_diff > 0.05 and  # Thumb is clearly above IP joint
            not index_extended and
            not middle_extended and
            not ring_extended and
            not pinky_extended):
            return "thumbs_up"
        
        # Thumbs Down: Thumb extended down, others closed
        thumb_vertical_diff_down = thumb_tip[1] - thumb_ip[1]  # Positive if thumb is down
        if (thumb_extended and 
            thumb_vertical_diff_down > 0.05 and  # Thumb is clearly below IP joint
            not index_extended and
            not middle_extended and
            not ring_extended and
            not pinky_extended):
            return "thumbs_down"
        
        # Peace sign (V) - can be used for up
        if (index_extended and
            middle_extended and
            not ring_extended and
            not pinky_extended):
            return "peace"
        
        # Fist - can be used for down
        if (not index_extended and
            not middle_extended and
            not ring_extended and
            not pinky_extended):
            return "fist"
        
        return None
    
    def draw_landmarks(self, image):
        """Draw hand landmarks on image for visualization"""
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_image)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                    self.mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
                )
        return image
    
    def get_camera_frame(self):
        """Get current camera frame for display"""
        if self.cap is None:
            return None
        
        ret, frame = self.cap.read()
        if not ret:
            return None
        
        frame = cv2.flip(frame, 1)
        frame = self.draw_landmarks(frame)
        return frame
    
    def release(self):
        """Release camera and resources"""
        if self.cap is not None:
            self.cap.release()
        self.hands.close()
        cv2.destroyAllWindows()

