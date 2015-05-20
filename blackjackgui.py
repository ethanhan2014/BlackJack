from graphics import *
from button import Button
class GraphicsInterface:
    def __init__(self):
        # initilising the starting windows
        self.win = GraphWin("21 Black Jack", 900, 600)
        self.win.setBackground("green3")

        # create a  greeting banner
        banner = Text(Point(450,50), "Welcome to Python  Poker  BlackJack")
        banner.setSize(36)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        
        #create a explantory message
        self.message = Text(Point(450,550),"3 for a Win,1 for a Tie, 0 for a lose")
        self.message.draw(self.win)
        self.message.setSize(30)
        self.message.setStyle("bold")

        # create a round counter
        self.roundmess = Text(Point(420,150),"Round")
        self.roundmess.setSize(27)
        self.roundmess.setStyle("bold")
        self.roundmess.draw(self.win)

        #create a score board 
        side1 = Text(Point(200,150),"Player")
        self.mpscore = Text(Point(200,200),"Score:")
        side1.setSize(24)
        side1.setStyle("italic")
        side1.draw(self.win)
        self.mpscore.draw(self.win)
        
        side2 = Text(Point(700,150),"Computer")
        self.mcscore  = Text(Point(700,200),"Score:")
        side2.setSize(24)
        side2.setStyle("italic")
        side2.draw(self.win)
        self.mcscore.draw(self.win)
        
        self.dealbutton = Button(self.win,Point(450,300),90,40,"Deal")
        self.hitmebutton = Button(self.win,Point(450,350),90,40,"Hit Me")
        self.untapbutton = Button(self.win,Point(450,400),90,40,"Untap")
        self.quitbutton = Button(self.win,Point(450,450),90,40,"Quit")
        self.dealbutton.activate()
        self.quitbutton.activate()

        
        self.slot1 = Point(100,300)
        self.slot2 = Point(200,300)
        self.slot3 = Point(300,300)
        self.slot4 = Point(100,400)
        self.slot5 = Point(600,300)
        self.slot6 = Point(700,300)
        self.slot7 = Point(800,300)
        self.slot8 = Point(800,400)

        self.PMC = 0   # the more cards that player get
        self.CMC = 0   # the more cards that computer get
        self.round = 0

        
    def setPlayerScore(self, score):
        self.mpscore.setText("Score: %d" % (score))
        
    def setComputerScore(self, score):
        self.mcscore.setText("Score: %d" % (score))

    def wantToPlay(self):
        p = self.win.getMouse()
        if self.dealbutton.clicked(p):
            self.round += 1
            self.dealbutton.deactivate()
            self.quitbutton.deactivate()
            self.hitmebutton.activate()
            self.untapbutton.activate()
            self.roundmess.setText("Round%d"%(self.round))
            return True
        
        else:
            return False

    def close(self):
        self.win.close()

    def setMessage(self, text):
        self.message.setText("%s"%(text))

    def playergetCards(self,filename1,filename2):
        self.card1=Image(self.slot1,filename1)
        self.card1.draw(self.win)
        self.card2=Image(self.slot2,filename2)
        self.card2.draw(self.win)

    def computergetCards(self):
        self.card5 = Image(self.slot5, "bg.gif")
        self.card6 = Image(self.slot6, "bg.gif")
        self.card5.draw(self.win)
        self.card6.draw(self.win)

    def Pget1MoreCard(self,filename):
        self.PMC += 1
        self.card3=Image(self.slot3,filename)
        self.card3.draw(self.win)

    def Pget2MoreCard(self,filename):
        self.PMC += 1
        self.card4=Image(self.slot4,filename)
        self.card4.draw(self.win)

    def Cget1MoreCard(self):
        self.CMC += 1
        self.card7=Image(self.slot7,"bg.gif")
        self.card7.draw(self.win)

    def Cget2MoreCard(self):
        self.CMC += 1
        self.card8=Image(self.slot8,"bg.gif")
        self.card8.draw(self.win)

    def ClearField(self):
        #clear all card objects
#        if self.round > 1:
        self.card1.undraw()
        self.card2.undraw()
        self.card5.undraw()
        self.card6.undraw()
            
        if self.PMC == 1:
            self.card3.undraw()
        elif self.PMC == 2:
            self.card3.undraw()
            self.card4.undraw()
            
        if self.CMC== 1:
            self.card7.undraw()
        elif self.CMC== 2:
            self.card7.undraw()
            self.card8.undraw()
        self.PMC = 0
        self.CMC = 0

    def wantToHit(self):
        p1 = self.win.getMouse()
        if self.hitmebutton.clicked(p1):
            return True
        else:
            return False
    
    def ShowResult(self,f1,f2,f3,f4):
        #load the card picture
        self.card5.undraw()
        self.card6.undraw()
        self.card5 = Image(self.slot5,f1)
        self.card6 = Image(self.slot6,f2)
        self.card5.draw(self.win)
        self.card6.draw(self.win)
        
        if self.CMC== 1:
            self.card7.undraw()
            self.card7 = Image(self.slot7,f3)
            self.card7.draw(self.win)
        elif self.CMC== 2:
            self.card7.undraw()
            self.card7 = Image(self.slot7,f3)
            self.card7.draw(self.win)
            
            self.card8.undraw()
            self.card8 = Image(self.slot8,f4)
            self.card8.draw(self.win)

        self.dealbutton.activate()
        self.quitbutton.activate()
        self.hitmebutton.deactivate()
        self.untapbutton.deactivate()

    def wantToQuit(self):
        p1 = self.win.getMouse()
        if self.quitbutton.clicked(p1):
            return True
        else:
            return False
        

     

#a = GraphicsInterface()
#a.playergetCards("hJ.gif", "d2.gif")

