# The program draws the following shape:
# ------------
# --*****-----
# --*****-----
# --*****-----
# ------------
# ----******--
# ----******--
# ------------

# These are two rectangles defined by the coordinates of their
# top left corner, their height, and length.
# Notice that the top left corner of the main picture has coordinates (1,1),
# that is, the row coordinates starts with 1 and the column coordinates
# starts with 1.

# Data about the First Rectangle
r1 = 2
c1 = 3
width1 = 5
height1 = 3

# Data about the Second Rectangle
r2 = 6
c2 = 5
width2 = 6
height2 = 2

# Data about the whole picture
maxWidth = 12
maxHeight = 8

row = 1
shape = ''
while row <= maxHeight:
  col = 1
  while col <= maxWidth:    
    if (
      col >= c1 and col < c1 + width1 and row >= r1 and row < r1 + height1
    ) or (
      col >= c2 and col < c2 + width2 and row >= r2 and row < r2 + height2
    ):
      shape = shape + '*'
    else:
      shape = shape + '-'
    col += 1
  shape += '\n'
  row += 1
  
print(shape)