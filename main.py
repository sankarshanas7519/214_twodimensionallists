parkingLot = [[0,0,0,0,0], [0,2,1,1,2], [0,1,1,2,1], [0,0,0,0,0], [0,1,2,2,1]]
freeSpaces = 0
for row in parkingLot:
  for col in row:
    if col == 2:
      freeSpaces += 1
    print(col, end = " ")
  print()
print()
print()
print("Available Spaces (marked as 2): " + str(freeSpaces))






