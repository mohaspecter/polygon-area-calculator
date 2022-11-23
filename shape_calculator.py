#set_width
#set_height
#get_area: Returns area (width * height)
#get_perimeter: Returns perimeter (2 * width + 2 * height)
#get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
#get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
#get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
    self.area = self.width * self.height
    self.perimeter = self.width * 2 +  self.height * 2
    self.diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
  def __repr__(self):
    return str("Rectangle(width=%s, height=%s)" % (self.width,self.height))
    

  def set_width(self,width):
    self.width = width
    return self.width
  def set_height(self,height):
    self.height = height
    return self.height
  def get_area(self):
    self.area = self.width * self.height
    return self.area   
  def get_perimeter(self):  
    return self.perimeter
  def get_diagonal(self):
    return self.diagonal
  def get_picture(self):
    if self.width>50 or self.height>50:
      return "Too big for picture."
    else:
      line = ""
      total = ""
      for i in range(0,self.width):
        line = line + "*"
      for i in range(0,self.height):
        total = total + line + "\n"
      return total
  def get_amount_inside(self,another):
    if self.height>=another.height and self.width>=another.width:
      return self.get_area()//another.get_area()
    else:
      return 0

class Square(Rectangle):
  def __init__(self,widthheight):
    self.width = widthheight
    self.height = widthheight
    self.area = self.width * self.height
    self.perimeter = self.width * 4
    self.diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
  def __repr__(self):
      return str("Square(side=%s)" % self.width)

  def set_width(self,widthheight):
    self.width = widthheight
    self.height = widthheight

  def set_height(self,widthheight):
    self.height = widthheight
    self.width = widthheight

  def set_side(self,widthheight):
    self.height = widthheight
    self.width = widthheight
