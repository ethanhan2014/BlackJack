from random import*
""" h for heart, c for club, d for diamond , s for spade. This initializes card"""
class Card:
  def __init__(self):
    self.point = [["0","0"],["0","0"],["0","0"],["0","0"]]
    self.index = ["h", "c", "d", "s"]
    self.index2 = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    
    
  def showcard(self,i):
      return self.point[i-1][0] + self.point[i-1][1] # show NO.i card
    

  def start(self):
  # Get random cards
      self.point[0][1] = choice(self.index2)
      self.point[0][0] = choice(self.index)
      self.point[1][1] = choice(self.index2)
      self.point[1][0] = choice(self.index)

  def get1Card(self):
      self.point[2][0]= choice(self.index)
      self.point[2][1]= choice(self.index2)
       

  def get2Card(self):
      self.point[3][0]= choice(self.index)
      self.point[3][1]= choice(self.index2)
 

  def score(self):
    # calculate the total point of cards
    score = 0
    for i in range(4):
        if self.point[i][1] == "A":
          score += 1
        elif self.point[i][1] in ["J","Q","K"]:
          score += 10
        else:
          score += eval(self.point[i][1])
    return score

  def cardclear(self):
    #refresh your cards
    self.point = [["0","0"],["0","0"],["0","0"],["0","0"]]
