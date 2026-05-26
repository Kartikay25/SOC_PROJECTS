obstacles = [
   (1, 1),
   (0, 5),
   (2, 3),
   (2, 9),
   (1, 8)
]


while True:
   grid = []
   for i in range(rows):
       row = []
       for j in range(cols):
           if i == player_x and j == player_y:
               row.append("P")
           elif (i,j) in obstacles :
               row.append("X")
           else:
               row.append(".")
       grid.append(row)


   for row in grid:


       print(" ".join(row))
   command  = input("What is your command :").lower()


   new_x = player_x
   new_y = player_y


   if command == "w" and player_x > 0:
       new_x -= 1


   elif command == "s" and player_x < rows - 1:
       new_x += 1


   elif command== "a" and player_y > 0:
       new_y -= 1


   elif command == "d" and player_y < cols - 1:
       new_y += 1
   else :
       print ( "Invalid move " )


   if 0 <= new_x < rows and 0 <= new_y < cols:


       if (new_x, new_y) not in obstacles:
           player_x = new_x
           player_y = new_y
       else:
           print("You hit an obstacle!")
