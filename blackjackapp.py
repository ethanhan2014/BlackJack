from Card import*
import random
import winsound
class App:
    def __init__(self, interface):
        self.player = Card()
        self.computer = Card()
        self.pscore = 0    #player's score
        self.cscore = 0    #computer's score
        self.interface = interface
        self.hit = 0      # times of player's hitme

    def run(self):
        #start game
        if self.interface.wantToPlay():
            self.player.start()
            self.computer.start()
            self.interface.setPlayerScore(self.pscore)
            self.interface.setComputerScore(self.cscore)
            self.interface.computergetCards()
            self.interface.playergetCards("%s.gif"%(self.player.showcard(1)),"%s.gif"%(self.player.showcard(2)))
            winsound.PlaySound("deal.wav",winsound.SND_FILENAME)
            self.interface.setMessage("Do you want more card?")

        else:
            self.interface.close()

    def Hit1(self):
        # Offer first hitme
        if self.interface.wantToHit():
            self.hit += 1
            self.player.get1Card()
            self.interface.Pget1MoreCard("%s.gif"%(self.player.showcard(3)))
            winsound.PlaySound("deal.wav",winsound.SND_FILENAME) 

        else:
            self.ComputerHit()
            
            
            
    def Hit2(self):
        
        if self.interface.wantToHit() and self.hit == 1:
            self.hit += 1
            self.player.get2Card()
            self.interface.Pget2MoreCard("%s.gif"%(self.player.showcard(4)))
            winsound.PlaySound("deal.wav",winsound.SND_FILENAME)
            self.ComputerHit()

        else:
            self.ComputerHit()
        

        
    def result(self):
        #show the winner and loser
        winsound.PlaySound("untap.wav",winsound.SND_FILENAME)
        if self.player.score() <= 21 and self.computer.score()<=21:
            if self.player.score() - self.computer.score() == 0:
               self.interface.setMessage("Well, it's a Tie")
               self.interface.ShowResult("%s.gif"%(self.computer.showcard(1)),"%s.gif"%(self.computer.showcard(2)),"%s.gif"%(self.computer.showcard(3)),"%s.gif"%(self.computer.showcard(4)))         
               winsound.PlaySound("laugh.wav",winsound.SND_FILENAME)
               self.pscore += 1
               self.cscore += 1
            elif self.player.score() - self.computer.score() > 0:
                self.interface.setMessage("Yeah, You win")
                self.interface.ShowResult("%s.gif"%(self.computer.showcard(1)),"%s.gif"%(self.computer.showcard(2)),"%s.gif"%(self.computer.showcard(3)),"%s.gif"%(self.computer.showcard(4)))         
                winsound.PlaySound("applause.wav",winsound.SND_FILENAME)
                self.pscore += 3
                self.cscore += 0
            else:
                self.interface.setMessage("Oops, You lose")
                self.interface.ShowResult("%s.gif"%(self.computer.showcard(1)),"%s.gif"%(self.computer.showcard(2)),"%s.gif"%(self.computer.showcard(3)),"%s.gif"%(self.computer.showcard(4)))         
                winsound.PlaySound("cryout.wav",winsound.SND_FILENAME)
                self.pscore += 0
                self.cscore += 3
        elif self.player.score() > 21:
            self.interface.setMessage("Oops, You lose")
            self.interface.ShowResult("%s.gif"%(self.computer.showcard(1)),"%s.gif"%(self.computer.showcard(2)),"%s.gif"%(self.computer.showcard(3)),"%s.gif"%(self.computer.showcard(4)))         
            winsound.PlaySound("cryout.wav",winsound.SND_FILENAME)
            self.pscore += 0
            self.cscore += 3
        elif self.computer.score() >21:
            self.interface.setMessage("Yeah, You win")
            self.interface.ShowResult("%s.gif"%(self.computer.showcard(1)),"%s.gif"%(self.computer.showcard(2)),"%s.gif"%(self.computer.showcard(3)),"%s.gif"%(self.computer.showcard(4)))         
            winsound.PlaySound("applause.wav",winsound.SND_FILENAME)
            self.pscore += 3
            self.cscore += 0
        elif self.player.score() > 21 and self.computer.score() >21:
            self.interface.setMessage("Well, it's a Tie")
            self.interface.ShowResult("%s.gif"%(self.computer.showcard(1)),"%s.gif"%(self.computer.showcard(2)),"%s.gif"%(self.computer.showcard(3)),"%s.gif"%(self.computer.showcard(4)))         
            winsound.PlaySound("laugh.wav",winsound.SND_FILENAME)
            self.pscore += 1
            self.cscore += 1
        self.interface.setPlayerScore(self.pscore)
        self.interface.setComputerScore(self.cscore)
        #self.interface.ShowResult("%s.gif"%(self.computer.showcard(1)),"%s.gif"%(self.computer.showcard(2)),"%s.gif"%(self.computer.showcard(3)),"%s.gif"%(self.computer.showcard(4)))         

    def ComputerHit(self):
        # #This is the step that simulate the computer thinking # #
        if 1000*random.random() < 1000*self.computer.score()/21.00:
            self.computer.get1Card()
            self.interface.Cget1MoreCard()
            winsound.PlaySound("deal.wav",winsound.SND_FILENAME)

    def allclear(self):
        #clear the table
        self.player.cardclear()
        self.computer.cardclear()
        self.hit = 0
        self.interface.ClearField()
        self.interface.setMessage("Click Deal to Restart or Click Quit to exit...")

    def quit(self):
        if self.interface.wantToQuit():
            return True
        else:
            return False

            
            
