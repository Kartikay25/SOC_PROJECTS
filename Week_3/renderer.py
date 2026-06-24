import numpy as np
import pygame
from constants import (
    ROWS, COLS, CELL_SIZE,
    SCREEN_WIDTH, SCREEN_HEIGHT,
    BLACK, WHITE, GRAY,
    RED, DARK_RED, BLUE, DARK_BLUE,
)
 
 
class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.color_table = np.array([
            DARK_BLUE,  
            DARK_RED,   
            BLACK,      
            RED,         
            BLUE,        
        ], dtype=np.uint8)
 
    def render(self, game):
      
        clipped = np.clip(game.grid, -2, 2) + 2   
        color_grid = self.color_table[clipped]

        scaled = np.repeat(np.repeat(color_grid, CELL_SIZE, axis=0),
                           CELL_SIZE, axis=1)
 
        screen_array = np.transpose(scaled, (1, 0, 2))
 
        pygame.surfarray.blit_array(self.screen, screen_array)

        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (SCREEN_WIDTH, y))
 
        for player in game.players:
            if not player.alive:
                continue
            cx = player.col * CELL_SIZE + CELL_SIZE // 2
            cy = player.row * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(self.screen, WHITE, (cx, cy), CELL_SIZE // 2 - 1)
