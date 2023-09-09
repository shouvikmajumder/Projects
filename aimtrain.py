import math
import random 
import time
import pygame 
pygame.init()

WIDTH = 800
HEIGHT = 400
BORDERHEIGHT = 50
LIVES = 100
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) # this is the window screen

FONT = pygame.font.SysFont("comicsans",24)

BACKGROUDC = (0,25,40)

pygame.display.set_caption("Aimtrainer via Shouvik Majumder")
TARGETINCREMENT = 400 #speed in ms 
TARGETEVENT = pygame.USEREVENT 
TARGETPADDING = 30#px

class Target:
    MAXSIZE = 35
    GROWTHRATE= 0.2 
    PRIMARYCOLOR = "red"
    SECONDARYCOLOR = "white"
    def __init__(self,target,position) -> None:
        self.target = target
        self.position = position
        self.size = 0
        self.grow = True
    
    def sizeupdate(self):
        if self.size + self.GROWTHRATE >= self.MAXSIZE:
            self.grow = False
        
        if self.grow == True:
            self.size+= self.GROWTHRATE 
        else: 
            self.size -= self.GROWTHRATE

    
    def drawtarget(self, windowobj):
        pygame.draw.circle(windowobj,self.PRIMARYCOLOR,(self.target,self.position),self.size * 1)
        pygame.draw.circle(windowobj,self.SECONDARYCOLOR,(self.target,self.position),self.size * 0.8)
        pygame.draw.circle(windowobj,self.PRIMARYCOLOR,(self.target,self.position),self.size * 0.6)
        pygame.draw.circle(windowobj,self.SECONDARYCOLOR,(self.target,self.position),self.size * 0.4)
    
    def collide(self,x,y):
        dist = math.sqrt((self.target - x)**2 + (self.position- y) **2)
        if dist<= self.size:
            return True


def drawnobj(windowobj, targets):
    windowobj.fill(BACKGROUDC)
    
    for tar in targets:
        tar.drawtarget(windowobj)

    
def draw_top_bar(win, elapsedtime, clicksmade, clicksmissed):
    pygame.draw.rect(WIN, "red", (0, 0, WIDTH, BORDERHEIGHT))
    if elapsedtime == 0:  # Handle zero division
        speed = 0
    else:
        speed = round((clicksmade / elapsedtime), 1)

    timelabel = FONT.render(f"Time: {timeformat(elapsedtime)} ", 1, "black")
    speedlabel = FONT.render(f"speed: {speed} t/s", 1, "black")
    targetlabel = FONT.render(f"Hits: {clicksmade}", 1, "black")
    liveslabel = FONT.render(f"Lives: {LIVES - clicksmissed}", 1, "black")

    win.blit(timelabel, (5, 5))
    win.blit(speedlabel, (200, 5))
    win.blit(targetlabel, (450, 5))
    win.blit(liveslabel, (650, 5))

def timeformat(secs):
    milli = math.floor(int((secs*1000%1000)/100))
    sec = int(round(secs%60,1))
    min  = int(secs//60)

    return f"{min:02d}:{sec:02d}:{milli}"

def main():
    targets = []
     # Triggering targetevent(x) every targetincrement(y)
    clock = pygame.time.Clock()
    clicksmade = 0
    clicksmissed = 0
    starttime = time.time()
    pygame.time.set_timer(TARGETEVENT,TARGETINCREMENT)

    while True: 
        timeelapsed = time.time() - starttime
        mousepos = pygame.mouse.get_pos()
        clock.tick(60) #fps 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == TARGETEVENT:
                x = random.randint(TARGETPADDING,WIDTH-TARGETPADDING)
                y = random.randint(TARGETPADDING,HEIGHT-TARGETPADDING)
                TAR = Target(x,y)
                targets.append(TAR)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicksmade += 1

            for tar in targets:
                tar.sizeupdate()
                if tar.size <= 0:
                    targets.remove(tar)
                    clicksmissed += 1

                if click and tar.collide(*mousepos):
                    targets.remove(tar)
                    clicksmade+=1
            
            if clicksmissed>LIVES:
                break #endgame


        drawnobj(WIN,targets)
        draw_top_bar(WIN, timeelapsed, clicksmade, clicksmissed)
        pygame.display.update()

    pygame.quit()
    




if __name__ == "__main__":
    main()
