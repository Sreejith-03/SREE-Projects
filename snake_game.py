"""
Snake Game with Hand Gesture Control
Control the snake's direction using hand gestures
"""

import pygame
import random
from enum import Enum
from typing import List, Tuple, Optional


class Direction(Enum):
    """Snake movement directions"""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Snake:
    """Snake class to handle snake logic"""
    
    def __init__(self, start_pos: Tuple[int, int], block_size: int):
        self.body = [start_pos]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.block_size = block_size
        self.grow = False
    
    def move(self):
        """Move the snake"""
        self.direction = self.next_direction
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx * self.block_size, head_y + dy * self.block_size)
        
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, new_direction: Direction):
        """Change snake direction (prevent reversing into itself)"""
        # Prevent reversing
        opposite = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        
        if new_direction != opposite.get(self.direction):
            self.next_direction = new_direction
    
    def check_collision(self, width: int, height: int) -> bool:
        """Check if snake collides with walls or itself"""
        head_x, head_y = self.body[0]
        
        # Wall collision
        if (head_x < 0 or head_x >= width or 
            head_y < 0 or head_y >= height):
            return True
        
        # Self collision
        if self.body[0] in self.body[1:]:
            return True
        
        return False
    
    def eat_food(self, food_pos: Tuple[int, int]) -> bool:
        """Check if snake ate food"""
        if self.body[0] == food_pos:
            self.grow = True
            return True
        return False


class Food:
    """Food class"""
    
    def __init__(self, block_size: int, width: int, height: int):
        self.block_size = block_size
        self.width = width
        self.height = height
        self.position = self.generate_position()
    
    def generate_position(self) -> Tuple[int, int]:
        """Generate random food position"""
        x = random.randrange(0, self.width, self.block_size)
        y = random.randrange(0, self.height, self.block_size)
        return (x, y)
    
    def respawn(self, snake_body: List[Tuple[int, int]]):
        """Respawn food at new location (not on snake)"""
        while True:
            self.position = self.generate_position()
            if self.position not in snake_body:
                break


class SnakeGame:
    """Main Snake Game class"""
    
    def __init__(self, width: int = 800, height: int = 600, block_size: int = 20):
        pygame.init()
        
        self.width = width
        self.height = height
        self.block_size = block_size
        
        # Calculate grid dimensions
        self.grid_width = (width // block_size) * block_size
        self.grid_height = (height // block_size) * block_size
        
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game - Hand Gesture Control")
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.DARK_GREEN = (0, 200, 0)
        self.BLUE = (0, 0, 255)
        
        self.reset_game()
    
    def reset_game(self):
        """Reset game to initial state"""
        start_pos = (self.grid_width // 2, self.grid_height // 2)
        self.snake = Snake(start_pos, self.block_size)
        self.food = Food(self.block_size, self.grid_width, self.grid_height)
        self.food.respawn(self.snake.body)
        self.score = 0
        self.game_over = False
        self.paused = False
    
    def handle_gesture(self, gesture: Optional[str]):
        """Handle gesture input to change direction"""
        if self.game_over or self.paused:
            return
        
        gesture_to_direction = {
            # Swipe gestures (primary)
            "swipe_up": Direction.UP,
            "swipe_down": Direction.DOWN,
            "swipe_left": Direction.LEFT,
            "swipe_right": Direction.RIGHT,
            # Pointing gestures (fallback)
            "point_up": Direction.UP,
            "point_down": Direction.DOWN,
            "point_left": Direction.LEFT,
            "point_right": Direction.RIGHT,
            # Alternative gestures
            "thumbs_up": Direction.UP,
            "thumbs_down": Direction.DOWN,
            "peace": Direction.UP,  # Peace sign = up
            "fist": Direction.DOWN,  # Fist = down
        }
        
        if gesture and gesture in gesture_to_direction:
            self.snake.change_direction(gesture_to_direction[gesture])
    
    def handle_keyboard(self, key):
        """Handle keyboard input (for testing/backup)"""
        if self.game_over:
            if key == pygame.K_r:
                self.reset_game()
            return
        
        if key == pygame.K_p:
            self.paused = not self.paused
            return
        
        if self.paused:
            return
        
        key_to_direction = {
            pygame.K_UP: Direction.UP,
            pygame.K_DOWN: Direction.DOWN,
            pygame.K_LEFT: Direction.LEFT,
            pygame.K_RIGHT: Direction.RIGHT,
            pygame.K_w: Direction.UP,
            pygame.K_s: Direction.DOWN,
            pygame.K_a: Direction.LEFT,
            pygame.K_d: Direction.RIGHT,
        }
        
        if key in key_to_direction:
            self.snake.change_direction(key_to_direction[key])
    
    def update(self):
        """Update game state"""
        if self.game_over or self.paused:
            return
        
        self.snake.move()
        
        # Check food collision
        if self.snake.eat_food(self.food.position):
            self.score += 10
            self.food.respawn(self.snake.body)
        
        # Check game over
        if self.snake.check_collision(self.grid_width, self.grid_height):
            self.game_over = True
    
    def draw(self, current_gesture: Optional[str] = None):
        """Draw game elements"""
        self.screen.fill(self.BLACK)
        
        if not self.game_over and not self.paused:
            # Draw food
            pygame.draw.rect(self.screen, self.RED, 
                           (*self.food.position, self.block_size, self.block_size))
            
            # Draw snake
            for i, segment in enumerate(self.snake.body):
                color = self.GREEN if i == 0 else self.DARK_GREEN
                pygame.draw.rect(self.screen, color,
                               (*segment, self.block_size, self.block_size))
                pygame.draw.rect(self.screen, self.BLACK,
                               (*segment, self.block_size, self.block_size), 1)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw gesture info
        if current_gesture:
            gesture_text = self.small_font.render(
                f"Gesture: {current_gesture}", True, self.BLUE)
            self.screen.blit(gesture_text, (10, 50))
        
        # Draw game over screen
        if self.game_over:
            game_over_text = self.font.render("GAME OVER", True, self.RED)
            restart_text = self.small_font.render(
                "Press R to restart or show 'thumbs_up' gesture", True, self.WHITE)
            
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 30))
            restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 10))
            
            self.screen.blit(game_over_text, text_rect)
            self.screen.blit(restart_text, restart_rect)
        
        # Draw pause screen
        if self.paused:
            pause_text = self.font.render("PAUSED", True, self.WHITE)
            text_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(pause_text, text_rect)
        
        # Draw instructions
        if not self.game_over:
            instructions = [
                "Controls:",
                "Point Up = Move Up",
                "Point Down = Move Down",
                "Point Left = Move Left",
                "Point Right = Move Right",
                "P = Pause"
            ]
            y_offset = self.height - 120
            for i, instruction in enumerate(instructions):
                text = self.small_font.render(instruction, True, self.WHITE)
                self.screen.blit(text, (self.width - 200, y_offset + i * 20))
        
        pygame.display.flip()
    
    def run_frame(self, gesture: Optional[str] = None):
        """Run one frame of the game"""
        # Handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                self.handle_keyboard(event.key)
        
        # Handle gesture input
        self.handle_gesture(gesture)
        
        # Update game
        self.update()
        
        # Draw game
        self.draw(gesture)
        
        return True
    
    def quit(self):
        """Clean up pygame"""
        pygame.quit()

