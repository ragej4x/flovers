import math
import random
from data import mapid


#CLASSID20
#PLAYER
class playerClass():
    def __init__(self):
        self.showHitbox = True

        self.x = 100
        self.y = 100

        self.left = False
        self.right = False
        self.up = False 
        self.down = False

        self.playerSpeed = 2
        
        self.dx = 0
        self.dy = 0

    def hitbox(self, pg, display):
        self.fixedHitBox = pg.Rect((self.x - camera.cameraX , self.y - camera.cameraY - 13, 13,10))
        self.hitBox = pg.Rect((self.x - camera.cameraX , self.y - camera.cameraY, 13,10))  


        if self.showHitbox == True:
            pg.draw.rect(display, (100,100,200), (self.fixedHitBox))
            pg.draw.rect(display, (100,100,200), (self.hitBox))

    def mvControls(self, pg, display, keyinput):
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
        self.showGrid = True
    
        #TILES
        self.stoneTile1 = pg.image.load("data/bin/texture/tile1.png")
        self.stoneTile2 = pg.image.load("data/bin/texture/tile2.png")
        self.stoneTile3 = pg.image.load("data/bin/texture/tile3.png")
        self.stoneTile4 = pg.image.load("data/bin/texture/tile4.png")
        self.stoneTile5 = pg.image.load("data/bin/texture/tile5.png")
        self.stoneTile6 = pg.image.load("data/bin/texture/tile6.png")


        self.curvedTopLeft = pg.image.load("data/bin/texture/curvedTileLeft.png")
        self.curvedTopRight = pg.image.load("data/bin/texture/curvedTileRight.png")
        self.curvedDownLeft = pg.image.load("data/bin/texture/curvedTileDownLeft.png")
        self.curvedDownRight = pg.image.load("data/bin/texture/curvedTileDownRight.png")


        self.grassTile1 = pg.image.load("data/bin/texture/grassTile1.png")
        self.grassTile2 = pg.image.load("data/bin/texture/grassTile2.png")
        self.grassTile3 = pg.image.load("data/bin/texture/grassTile3.png")
        self.grassTile4 = pg.image.load("data/bin/texture/grassTile4.png")
        self.grassTile5 = pg.image.load("data/bin/texture/grassTile5.png")
        self.grassTile6 = pg.image.load("data/bin/texture/grassTile6.png")


        self.roadCurvedLeft = pg.image.load("data/bin/texture/roadCurvedLeft.png")
        self.roadCurvedRight = pg.image.load("data/bin/texture/roadCurvedLeft.png")
        self.roadVertical = pg.image.load("data/bin/texture/roadVertical.png")
        self.roadHorizontal = pg.image.load("data/bin/texture/roadHorizontal.png")
        self.roadCurvedBottomLeft = pg.image.load("data/bin/texture/roadCurvedBottomLeft.png")
        self.roadCurvedBottomRight = pg.image.load("data/bin/texture/roadCurvedBottomRight.png")

        #OBJECTS
        self.cone = pg.image.load("data/bin/texture/cone.png")
        self.bin = pg.image.load("data/bin/texture/bin.png")
        self.manHole = pg.image.load("data/bin/texture/manHole.png")


    def updateMap(self, pg, display):
        y = 0
        for i in mapid.mapdata.testMapData:
            x = 0
            for tile in i:
                x += 1

                #STONE TILE
                if tile == 1:
                    display.blit(self.stoneTile1, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 2:
                    display.blit(self.stoneTile2, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 3:
                    display.blit(self.stoneTile3, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 4:
                    display.blit(self.stoneTile4, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 5:
                    display.blit(self.stoneTile5, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 6:
                    display.blit(self.stoneTile6, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))


                #GRASS TILE
                if tile == 7:
                    display.blit(self.grassTile1, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 8:
                    display.blit(self.grassTile2, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 9:
                    display.blit(self.grassTile3, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 10:
                    display.blit(self.grassTile4, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 11:
                    display.blit(self.grassTile5, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 12:
                    display.blit(self.grassTile6, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))


                #ROAD TILE
                if tile == 13:
                    display.blit(self.roadCurvedBottomRight, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 14:
                    display.blit(self.roadCurvedBottomLeft, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 15:
                    display.blit(self.roadCurvedLeft, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 16:
                    display.blit(self.roadCurvedRight, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 17:
                    display.blit(self.roadHorizontal, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 18:
                    display.blit(self.roadVertical, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))


                #OBJECT
                if tile == 19:
                    display.blit(self.cone, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 20:
                    display.blit(self.bin, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                if tile == 21:
                    display.blit(self.manHole, (x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16))

                #COLLIDER

                if tile == -1:
                    block = pg.Rect(x * 16 - camera.cameraX , y * 16 - camera.cameraY , 16,16)
                    if self.showGrid == True:
                        pg.draw.rect(display, (255, 0, 255), (block), 1)
                    
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


        self.idlRightframeCount = 1
        self.idlLeftframeCount = 1
        self.idlUpframeCount = 1
        self.idlDownframeCount = 1

        self.wRightList = []
        self.wLeftList = []
        self.wUpList = []
        self.wDownList = []

        self.wLeftframeCount = 1
        self.wRightframeCount = 1
        self.wUpframeCount = 1
        self.wDownframeCount = 1


        self.idlframeSpeed = 0.05
        self.wframeSpeed = 0.2


    
    #IDLE
    def idleLeftAnimation(self, pg, display):
        image = pg.image.load(f"data/bin/anim/id{int(self.idlRightframeCount)}.anim")
        image = pg.transform.flip(image, True, False)
        image.set_colorkey((255,0,255))
        display.blit(image, (player.x - camera.cameraX , player.y - 22 - camera.cameraY))

        self.idlRightframeCount += self.idlframeSpeed
        if self.idlRightframeCount > 6:
            self.idlRightframeCount  = 1

    def idleRightAnimation(self, pg, display):
        image = pg.image.load(f"data/bin/anim/id{int(self.idlLeftframeCount)}.anim")
        image.set_colorkey((255,0,255))
        display.blit(image, (player.x - camera.cameraX , player.y - 22 - camera.cameraY))

        self.idlLeftframeCount += self.idlframeSpeed
        if self.idlLeftframeCount > 6:
            self.idlLeftframeCount  = 1


    def idleUpAnimation(self, pg, display):
        image = pg.image.load(f"data/bin/anim/idU{int(self.idlDownframeCount)}.anim")
        image.set_colorkey((255,0,255))
        display.blit(image, (player.x - camera.cameraX , player.y - 22 - camera.cameraY))

        self.idlDownframeCount += self.idlframeSpeed
        if self.idlDownframeCount > 6:
            self.idlDownframeCount  = 1

    def idleDownAnimation(self, pg, display):
        image = pg.image.load(f"data/bin/anim/idD{int(self.idlUpframeCount)}.anim")
        image.set_colorkey((255,0,255))
        display.blit(image, (player.x - camera.cameraX , player.y - 22 - camera.cameraY))

        self.idlUpframeCount += self.idlframeSpeed
        if self.idlUpframeCount > 6:
            self.idlUpframeCount  = 1
        

    #WALK
    def walkLeftAnimation(self, pg, display):
        image = pg.image.load(f"data/bin/anim/r{int(self.wLeftframeCount)}.anim")
        image = pg.transform.flip(image, True, False)
        image.set_colorkey((255,0,255))
        display.blit(image, (player.x - camera.cameraX , player.y - 22 - camera.cameraY))

        self.wLeftframeCount += self.wframeSpeed
        if self.wLeftframeCount > 6:
            self.wLeftframeCount = 1


    def walkRightAnimation(self, pg, display):
        image = pg.image.load(f"data/bin/anim/r{int(self.wRightframeCount)}.anim")
        image.set_colorkey((255,0,255))
        display.blit(image, (player.x - camera.cameraX , player.y - 22 - camera.cameraY))

        self.wRightframeCount += self.wframeSpeed
        if self.wRightframeCount > 6:
            self.wRightframeCount = 1


    def walkUpAnimation(self, pg, display):
        image = pg.image.load(f"data/bin/anim/rU{int(self.wUpframeCount)}.anim")
        image.set_colorkey((255,0,255))
        display.blit(image, (player.x - camera.cameraX , player.y - 22 - camera.cameraY))

        self.wUpframeCount += self.wframeSpeed
        if self.wUpframeCount > 6:
            self.wUpframeCount = 1

    def walkDownAnimation(self, pg, display):

        image = pg.image.load(f"data/bin/anim/rD{int(self.wDownframeCount)}.anim")
        image.set_colorkey((255,0,255))
        display.blit(image, (player.x - camera.cameraX , player.y - 22 - camera.cameraY))

        self.wDownframeCount += self.wframeSpeed
        if self.wDownframeCount > 6:
            self.wDownframeCount  = 1
            

animate = animationClass()