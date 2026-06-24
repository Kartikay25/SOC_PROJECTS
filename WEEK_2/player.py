class Player:
    def __init__(self, start_row, start_col, start_direction, color, player_id):
      
        self.start_row       = start_row
        self.start_col       = start_col
        self.start_direction = start_direction
 

        
        self.row       = start_row
        self.col       = start_col
        self.direction = start_direction   
        self.color     = color
        self.player_id = player_id
        self.alive     = True
 
        
        self.trail = []
 
    def reset(self):
        self.row       = self.start_row
        self.col       = self.start_col
        self.direction = self.start_direction
        self.alive     = True
        self.trail     = []
