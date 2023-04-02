import math
import random
from data import mapid


#CLASSID20
#PLAYER
class playerClass():
    def __init__(self):
        self.x = 100
        self.y = 100

        self.left = False
        self.right = False
        self.up = False 
        self.down = False

        self.playerSpeed = 2


    def mvControls(self, pg, display, keyinput):
        self.fixedHitBox = pg.draw.rect(display, (100,100,200), (self.x - camera.cameraX , self.y - camera.cameraY - 13, 13,10))
        self.hitBox = pg.draw.rect(display, (200,100,100), (self.x - camera.cameraX , self.y - camera.cameraY, 13,10))
        self.dx = 0
        self.dy = 0


        #MOVEMENT
        if keyinput[pg.K_a]:
            self.dx -= self.playerSpeed
            
            self.left = True
            self.right = False
            self.up = False
            self.down = False

        if keyinput[pg.K_d]:
            self.dx += self.playerSpeed

            self.right = True
            self.left = False
            self.up = False 
            self.down = False

        if keyinput[pg.K_w]:
            self.dy -= self.playerSpeed

            self.up = True
            self.left = False
            self.right = False 
            self.down = False


        if keyinput[pg.K_s]:
            self.dy += self.playerSpeed

            self.down = True
            self.left = False
            self.right = False
            self.up = False

        #FIX SPEED

        if keyinput[pg.K_a] and keyinput[pg.K_w]:
            self.playerSpeed = 1

        elif keyinput[pg.K_a] and keyinput[pg.K_s]:
            self.playerSpeed = 1


        elif keyinput[pg.K_w] and keyinput[pg.K_d]:
            self.playerSpeed = 1


        elif keyinput[pg.K_w] and keyinput[pg.K_d]:
            self.playerSpeed = 1


        elif keyinput[pg.K_s] and keyinput[pg.K_d]:
            self.playerSpeed = 1


        elif keyinput[pg.K_s] and keyinput[pg.K_a]:
            self.playerSpeed = 1

        else:
            self.playerSpeed = 2

    #CALLING THE ANIMATION FUNC

    def updatePlayerAnimation(self, pg, display, keyinput):
        if not keyinput[pg.K_a] and self.left == True:
            animate.idleLeftAnimation(pg, display)

        elif not keyinput[pg.K_d] and self.right == True:
            animate.idleRightAnimation(pg, display)


        elif not keyinput[pg.K_w] and self.up == True:
            animate.idleUpAnimation(pg, display)
         

        elif not keyinput[pg.K_s] and self.down == True:
            animate.idleDownAnimation(pg, display)
          


        if keyinput[pg.K_a] and self.left == True:
            animate.walkLeftAnimation(pg, display)
            pass

        elif keyinput[pg.K_d] and self.right == True:
            animate.walkRightAnimation(pg, display)
            pass

        elif keyinput[pg.K_w] and self.up == True:
            animate.walkUpAnimation(pg, display)
            pass

        elif keyinput[pg.K_s] and self.down == True:
            animate.walkDownAnimation(pg, display)
            pass


player = playerClass()

#CAMERA

class cameraClass():
    def __init__(self):
         self.cameraX = player.x - 1024/6.3
         self.cameraY = player.y - 620/5.5
         self.cameraSpeed = 1
         self.cameraFixSpeed = 2

    def update(self, pg, display, keyinput):
        camCenter = pg.draw.rect(display, (255,30,255), (1024/6.3 ,620/5.5 , 2,2))

        angle = math.atan2(player.y - self.cameraY - 620/5.5, player.x - self.cameraX - 1024/6.3)
        cdx = math.cos(angle)
        cdy = math.sin(angle)


        if not camCenter.colliderect(player.hitBox):
            self.cameraX += cdx * self.cameraSpeed
            self.cameraY += cdy * self.cameraSpeed
        
        if self.cameraX > player.x - 90:
            self.cameraSpeed = self.cameraFixSpeed
            
        elif self.cameraX + 220 < player.x:
            self.cameraSpeed = self.cameraFixSpeed
           # print("AAAA")
            
        #elif self.cameraY > player.y - 70:
        elif self.cameraY + 60 >  player.y:
            self.cameraSpeed = self.cameraFixSpeed

        elif self.cameraY + 160 <  player.y:
            self.cameraSpeed = self.cameraFixSpeed

        else:
            self.cameraSpeed = 1

camera = cameraClass()

#MAP

class mapClass():
    def __init__(self, pg) -> None:
        pass

    def testMap(self, pg, display):
        y = 0
        for i in mapid.mapdata.testMapData:
            x = 0
            for tile in i:
                x += 1
                if tile == 1:
                    block = pg.draw.rect(display, (255,255,255), (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))
                    
                    #BLOCK COLLITION FOR X
                    if block.colliderect(player.hitBox.x + player.dx, player.hitBox.y, player.hitBox.width, player.hitBox.height):
                        player.dx = 0

                    #BLOCK COLLITION FOR Y
                    if block.colliderect(player.hitBox.x, player.hitBox.y + player.dy, player.hitBox.width, player.hitBox.height):
                        player.dy = 0
            
                    
                    #FIXED BLOCK COLLITION FOR X
                    if block.colliderect(player.fixedHitBox.x + player.dx, player.fixedHitBox.y, player.fixedHitBox.width, player.fixedHitBox.height):
                        player.dx = 0

                    #FIXED BLOCK COLLITION FOR Y
                    if block.colliderect(player.fixedHitBox.x, player.fixedHitBox.y + player.dy, player.fixedHitBox.width, player.fixedHitBox.height):
                        player.dy = 0      
            
            y += 1
            
        player.x += player.dx
        player.y += player.dy

        #print(camera.cameraY , player.y)

#map = mapClass()



#ANIMATION

class animationClass():
    def __init__(self):

        self.idlLeftList = []
        self.idlRightList = []
        self.idlUpList = []
        self.idlDownList = []


        self.idlRightframeCount = 0
        self.idlLeftframeCount = 0
        self.idlUpframeCount = 0
        self.idlDownframeCount = 0

        self.wRightList = []
        self.wLeftList = []
        self.wUpList = []
        self.wDownList = []

        self.wLeftframeCount = 0
        self.wRightframeCount = 0
        self.wUpframeCount = 0
        self.wDownframeCount = 0


        self.idlframeSpeed = 0.01
        self.wframeSpeed = 0.03

    #IDLE
    def idleLeftAnimation(self, pg, display):
        for frame in range(1, 6 + 1):
            image = pg.image.load(f"data/bin/anim/id{frame}.anim")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.idlLeftList.append(image)
            display.blit(self.idlLeftList[int(self.idlLeftframeCount)], (player.x - camera.cameraX , player.y - 22 - camera.cameraY))
            self.idlLeftframeCount += self.idlframeSpeed


    def idleRightAnimation(self, pg, display):
        for frame in range(1, 6 + 1):
            image = pg.image.load(f"data/bin/anim/id{frame}.anim")
            image.set_colorkey((255,0,255))
            self.idlRightList.append(image)
            display.blit(self.idlRightList[int(self.idlRightframeCount)], (player.x - camera.cameraX , player.y - 22 - camera.cameraY))
            self.idlRightframeCount += self.idlframeSpeed


    def idleUpAnimation(self, pg, display):
        for frame in range(1, 6 + 1):
            image = pg.image.load(f"data/bin/anim/idU{frame}.anim")
            image.set_colorkey((255,0,255))
            self.idlUpList.append(image)
            display.blit(self.idlUpList[int(self.idlUpframeCount)], (player.x - camera.cameraX , player.y - 22 - camera.cameraY))
            self.idlUpframeCount += self.idlframeSpeed


    def idleDownAnimation(self, pg, display):
        for frame in range(1, 6 + 1):
            image = pg.image.load(f"data/bin/anim/idD{frame}.anim")
            image.set_colorkey((255,0,255))
            self.idlDownList.append(image)
            display.blit(self.idlDownList[int(self.idlDownframeCount)], (player.x - camera.cameraX , player.y - 22 - camera.cameraY))
            self.idlDownframeCount += self.idlframeSpeed


    #WALK
    def walkLeftAnimation(self, pg, display):
        for frame in range(1, 6 + 1):
            image = pg.image.load(f"data/bin/anim/r{frame}.anim")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.wLeftList.append(image)
            display.blit(self.wLeftList[int(self.wLeftframeCount)], (player.x - camera.cameraX , player.y - 22 - camera.cameraY))
            self.wLeftframeCount += self.wframeSpeed


    def walkRightAnimation(self, pg, display):
        for frame in range(1, 6 + 1):
            image = pg.image.load(f"data/bin/anim/r{frame}.anim")
            image.set_colorkey((255,0,255))
            self.wRightList.append(image)
            display.blit(self.wRightList[int(self.wRightframeCount)], (player.x - camera.cameraX , player.y - 22 - camera.cameraY))
            self.wRightframeCount += self.wframeSpeed

    def walkUpAnimation(self, pg, display):
        for frame in range(1, 6 + 1):
            image = pg.image.load(f"data/bin/anim/rU{frame}.anim")
            image.set_colorkey((255,0,255))
            self.wUpList.append(image)
            display.blit(self.wUpList[int(self.wUpframeCount)], (player.x - camera.cameraX , player.y - 22 - camera.cameraY))
            self.wUpframeCount += self.wframeSpeed

    def walkDownAnimation(self, pg, display):
        for frame in range(1, 6 + 1):
            image = pg.image.load(f"data/bin/anim/rD{frame}.anim")
            image.set_colorkey((255,0,255))
            self.wDownList.append(image)
            display.blit(self.wDownList[int(self.wDownframeCount)], (player.x - camera.cameraX , player.y - 22 - camera.cameraY))
            self.wDownframeCount += self.wframeSpeed

animate = animationClass()