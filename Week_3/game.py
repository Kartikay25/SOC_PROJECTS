import numpy as np
from constants import ROWS, COLS
from capture   import flood_fill_capture
 
 
class Game:
    def __init__(self):
        self.rows    = ROWS
        self.cols    = COLS
        self.players = []
      
        self.grid = np.zeros((ROWS, COLS), dtype=int)
 
    def add_player(self, player):
        self.players.append(player)
        self._stamp_home_base(player)
 
    def _stamp_home_base(self, player):
       
        r, c = player.row, player.col
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    self.grid[nr][nc] = player.player_id
 
    def reset(self):
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        for player in self.players:
            player.reset()
            self._stamp_home_base(player)
 
    def update(self):
 
        next_pos = {}  
 
        for player in self.players:
            if not player.alive:
                continue
 
            r, c   = player.row, player.col
            dr, dc = player.direction
            nr, nc = r + dr, c + dc
 
            if nr < 0 or nr >= self.rows or nc < 0 or nc >= self.cols:
                next_pos[player.player_id] = (r, c)
                continue
              
            cell = self.grid[nr, nc]
            if cell > 0 and cell != player.player_id:
                next_pos[player.player_id] = (r, c)
                continue
 
            next_pos[player.player_id] = (nr, nc)
        for player in self.players:
            if not player.alive:
                continue
 
            pid       = player.player_id
            nr, nc    = next_pos[pid]
            if nr == player.row and nc == player.col:
                continue
 
            target = self.grid[nr, nc]
 
           
            if target == -pid:
                player.alive = False
                self._erase_player(player)
 
            elif target < 0:
                enemy_id = abs(int(target))
                for enemy in self.players:
                    if enemy.player_id == enemy_id and enemy.alive:
                        enemy.alive = False
                        self._erase_player(enemy)
 
        for player in self.players:
            if not player.alive:
                continue
 
            pid    = player.player_id
            nr, nc = next_pos[pid]
 
            if nr == player.row and nc == player.col:
                continue
 
            old_r, old_c = player.row, player.col
 
            if self.grid[old_r, old_c] != pid:
                self.grid[old_r, old_c] = -pid
                player.off_territory = True
 
      
            player.row = nr
            player.col = nc
          
            if self.grid[nr, nc] == pid and player.off_territory:
                flood_fill_capture(self.grid, pid, self.rows, self.cols)
                player.off_territory = False
 
    def _erase_player(self, player):
        pid = player.player_id
        self.grid[self.grid == pid]  = 0
        self.grid[self.grid == -pid] = 0
