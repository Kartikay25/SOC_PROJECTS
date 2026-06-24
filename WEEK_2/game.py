import numpy as np
from constants import ROWS, COLS
 
 
class Game:
    def __init__(self, rows, cols):
        self.rows    = rows
        self.cols    = cols
        self.players = []
 
      
        self.grid = np.zeros((rows, cols), dtype=int)
 
    def add_player(self, player):
        self.players.append(player)
 
    def reset(self):
       
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        for player in self.players:
            player.reset()
 
    def update(self):
        
        next_positions = {}   
        for player in self.players:
            if not player.alive:
                continue
 
            dr, dc   = player.direction
            next_row = player.row + dr
            next_col = player.col + dc
 
            next_positions[player.player_id] = (next_row, next_col)
 
        for player in self.players:
            if not player.alive:
                continue
 
            pid      = player.player_id
            nr, nc   = next_positions[pid]
 
            if nr < 0 or nr >= self.rows or nc < 0 or nc >= self.cols:
                player.alive = False
                continue
 
          
            if self.grid[nr, nc] != 0:
                player.alive = False
                continue
 
        positions_list = list(next_positions.items())  
        for i in range(len(positions_list)):
            for j in range(i + 1, len(positions_list)):
                id_a, pos_a = positions_list[i]
                id_b, pos_b = positions_list[j]
 
              
                player_a = None
                player_b = None
                for p in self.players:
                    if p.player_id == id_a:
                        player_a = p
                    if p.player_id == id_b:
                        player_b = p
 
                if player_a and player_b and player_a.alive and player_b.alive:
                    if pos_a == pos_b:
                        player_a.alive = False
                        player_b.alive = False
 
       
        for player in self.players:
            if not player.alive:
                continue
 
            pid    = player.player_id
            nr, nc = next_positions[pid]
 
            
            self.grid[player.row, player.col] = pid
            player.trail.append((player.row, player.col))
 
            player.row = nr
            player.col = nc
