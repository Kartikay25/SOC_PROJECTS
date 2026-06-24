class Player:
    def __init__(self, start_row, start_col, start_dir, player_id):
       
        self.start_row = start_row
        self.start_col = start_col
        self.start_dir = start_dir
        self.player_id = player_id  
        self.row = start_row
        self.col = start_col
      
        self.direction = start_dir
        self.alive = True
        self.off_territory = False
 
    def reset(self):
      
        self.row          = self.start_row
        self.col          = self.start_col
        self.direction    = self.start_dir
        self.alive        = True
        self.off_territory = False
