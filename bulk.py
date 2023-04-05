import math
import random
import csv
import os 

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
import json
class mapClass():
    def __init__(self, pg) -> None:
        self.showGrid = True
        self.texture = pg.image.load("data/bin/texture/street.png")


        """
        

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

        """

        #LENGTH OF A TEXTURE
        self.tileLength = self.texture.get_width()
        
        #SURFACE OF A TILE TO RENDER
        self.tile = pg.Surface((16,16))

        #RENDER IN ONE IMAGE
        self.renderMap = pg.Surface((1024//3,620//3)) #OPTIMIZATION

    def updateMap(self, pg, display):
        self.renderMap.fill(0)
        #self.tile.fill(0)



        with open("data/level0_data.csv") as data:
            
            #self.tile.fill(0)
            csv_reader = csv.reader(data, delimiter=',')
            y = 0
            for row in csv_reader:
                
                x = 0
                for column in range(len(row)):
                    x += 1

                    #SKIP 1 NUM EXAMPLE 17 JUMP TO 19
                    #BECAUSE THE COLUMN STARTS WITH 0
                    


                    #IF THE TILE IS IN THE ROW THEN WE RENDERING IT
                    
                    if row[column] == "1":
                        self.tile.blit(self.texture,(0,0))

                    elif row[column] == "2":
                        self.tile.blit(self.texture,(-16,0))

                    elif row[column] == "3":
                        self.tile.blit(self.texture,(-16 * 2 , 0))

                    elif row[column] == "4":
                        self.tile.blit(self.texture,(-16 * 3 ,0))

                    elif row[column] == "5":
                        self.tile.blit(self.texture,(-16 * 4 ,0))

                    elif row[column] == "6":
                        self.tile.blit(self.texture,(-16 * 5 ,0))

                    elif row[column] == "7":
                        self.tile.blit(self.texture,(-16 * 6 ,0))

                    elif row[column] == "8":
                        self.tile.blit(self.texture,(-16 * 7 ,0))

                    elif row[column] == "9":
                        self.tile.blit(self.texture,(-16 * 8 ,0))

                    elif row[column] == "10":
                        self.tile.blit(self.texture,(-16 * 9 ,0))

                    elif row[column] == "11":
                        self.tile.blit(self.texture,(-16 * 10 ,0))

                    elif row[column] == "12":
                        self.tile.blit(self.texture,(-16 * 11 ,0))

                    elif row[column] == "13":
                        self.tile.blit(self.texture,(-16 * 12 ,0))

                    elif row[column] == "14":
                        self.tile.blit(self.texture,(-16 * 13 ,0))

                    elif row[column] == "15":
                        self.tile.blit(self.texture,(-16 * 14 ,0))



                    elif row[column] == "17":
                        self.tile.blit(self.texture,(0 ,-16))
                    
                    elif row[column] == "18":
                        self.tile.blit(self.texture,(-16 , - 16))

                    elif row[column] == "19":
                        self.tile.blit(self.texture,(-16 * 2 , - 16))
                    
                    elif row[column] == "20":
                        self.tile.blit(self.texture,(-16 * 3 ,-16))
                    
                    elif row[column] == "21":
                        self.tile.blit(self.texture,(-16 * 4 ,-16))

                    elif row[column] == "22":
                        self.tile.blit(self.texture,(-16 * 5 ,- 16))

                    elif row[column] == "23":
                        self.tile.blit(self.texture,(-16 * 6 , - 16))

                    elif row[column] == "24":
                        self.tile.blit(self.texture,(-16 * 7 , - 16))

                    elif row[column] == "25":
                        self.tile.blit(self.texture,(-16 * 8 , - 16))

                    elif row[column] == "26":
                        self.tile.blit(self.texture,(-16 * 9 , - 16))

                    elif row[column] == "27":
                        self.tile.blit(self.texture,(-16 * 10 , - 16))

                    elif row[column] == "28":
                        self.tile.blit(self.texture,(-16 * 11 , - 16))

                    elif row[column] == "29":
                        self.tile.blit(self.texture,(-16 * 12 , - 16))

                    elif row[column] == "30":
                        self.tile.blit(self.texture,(-16 * 13 , - 16))

                    elif row[column] == "31":
                        self.tile.blit(self.texture,(-16 * 14 , - 16))



                    elif row[column] == "33":
                        self.tile.blit(self.texture,(0  , - 16 * 2))

                    elif row[column] == "34":
                        self.tile.blit(self.texture,(-16  , - 16 * 2))

                    elif row[column] == "35":
                        self.tile.blit(self.texture,(-16 * 2 , - 16 * 2))

                    elif row[column] == "36":
                        self.tile.blit(self.texture,(-16 * 3 , - 16 * 2))

                    elif row[column] == "37":
                        self.tile.blit(self.texture,(-16 * 4 , - 16 * 2))

                    elif row[column] == "38":
                        self.tile.blit(self.texture,(-16 * 5 , - 16 * 2))

                    elif row[column] == "39":
                        self.tile.blit(self.texture,(-16 * 6 , - 16 * 2))

                    elif row[column] == "40":
                        self.tile.blit(self.texture,(-16 * 7 , - 16 * 2))

                    elif row[column] == "41":
                        self.tile.blit(self.texture,(-16 * 8 , - 16 * 2))

                    elif row[column] == "42":
                        self.tile.blit(self.texture,(-16 * 9 , - 16 * 2))

                    elif row[column] == "43":
                        self.tile.blit(self.texture,(-16 * 10 , - 16 * 2))

                    elif row[column] == "44":
                        self.tile.blit(self.texture,(-16 * 11 , - 16 * 2))

                    elif row[column] == "45":
                        self.tile.blit(self.texture,(-16 * 12 , - 16 * 2))

                    elif row[column] == "46":
                        self.tile.blit(self.texture,(-16 * 13 , - 16 * 2))

                    elif row[column] == "47":
                        self.tile.blit(self.texture,(-16 * 14 , - 16 * 2))



                    elif row[column] == "49":
                        self.tile.blit(self.texture,(0 , - 16 * 3))

                    elif row[column] == "50":
                        self.tile.blit(self.texture,(-16 , - 16 * 3))

                    elif row[column] == "51":
                        self.tile.blit(self.texture,(-16 * 2 , - 16 * 3))

                    elif row[column] == "52":
                        self.tile.blit(self.texture,(-16 * 3 , - 16 * 3))

                    elif row[column] == "53":
                        self.tile.blit(self.texture,(-16 * 4 , - 16 * 3))

                    elif row[column] == "54":
                        self.tile.blit(self.texture,(-16 * 5 , - 16 * 3))

                    elif row[column] == "55":
                        self.tile.blit(self.texture,(-16 * 6 , - 16 * 3))

                    elif row[column] == "56":
                        self.tile.blit(self.texture,(-16 * 7 , - 16 * 3))

                    elif row[column] == "57":
                        self.tile.blit(self.texture,(-16 * 8 , - 16 * 3))
                    
                    elif row[column] == "58":
                        self.tile.blit(self.texture,(-16 * 9 , - 16 * 3))

                    elif row[column] == "59":
                        self.tile.blit(self.texture,(-16 * 10 , - 16 * 3))

                    elif row[column] == "60":
                        self.tile.blit(self.texture,(-16 * 11 , - 16 * 3))

                    elif row[column] == "61":
                        self.tile.blit(self.texture,(-16 * 12 , - 16 * 3))

                    elif row[column] == "62":
                        self.tile.blit(self.texture,(-16 * 13 , - 16 * 3))
                    
                    elif row[column] == "63":
                        self.tile.blit(self.texture,(-16 * 14 , - 16 * 3))




                    elif row[column] == "65":
                        self.tile.blit(self.texture,(0  , - 16 * 4))

                    elif row[column] == "66":
                        self.tile.blit(self.texture,(-16  , - 16 * 4))

                    elif row[column] == "67":
                        self.tile.blit(self.texture,(-16 * 2 , - 16 * 4))

                    elif row[column] == "68":
                        self.tile.blit(self.texture,(-16 * 3, - 16 * 4))

                    elif row[column] == "69":
                        self.tile.blit(self.texture,(-16 * 4 , - 16 * 4))

                    elif row[column] == "70":
                        self.tile.blit(self.texture,(-16 * 5 , - 16 * 4))

                    elif row[column] == "71":
                        self.tile.blit(self.texture,(-16 * 6 , - 16 * 4))

                    elif row[column] == "72":
                        self.tile.blit(self.texture,(-16 * 7 , - 16 * 4))

                    elif row[column] == "73":
                        self.tile.blit(self.texture,(-16 * 8 , - 16 * 4))

                    elif row[column] == "74":
                        self.tile.blit(self.texture,(-16 * 9 , - 16 * 4))

                    elif row[column] == "75":
                        self.tile.blit(self.texture,(-16 * 10 , - 16 * 4))

                    elif row[column] == "76":
                        self.tile.blit(self.texture,(-16 * 11 , - 16 * 4))

                    elif row[column] == "77":
                        self.tile.blit(self.texture,(-16 * 12 , - 16 * 4))

                    elif row[column] == "78":
                        self.tile.blit(self.texture,(-16 * 13 , - 16 * 4))

                    elif row[column] == "79":
                        self.tile.blit(self.texture,(-16 * 14 , - 16 * 4))



                    elif row[column] == "81":
                        self.tile.blit(self.texture,(0 , -16 * 5))

                    elif row[column] == "82":
                        self.tile.blit(self.texture,(-16 , -16 * 5))

                    elif row[column] == "83":
                        self.tile.blit(self.texture,(-16 * 2 , -16 * 5))

                    elif row[column] == "84":
                        self.tile.blit(self.texture,(-16 * 3 , -16 * 5))

                    elif row[column] == "85":
                        self.tile.blit(self.texture,(-16 * 4 , -16 * 5))

                    elif row[column] == "86":
                        self.tile.blit(self.texture,(-16 * 5 , -16 * 5))

                    elif row[column] == "87":
                        self.tile.blit(self.texture,(-16 * 6 , -16 * 5))

                    elif row[column] == "88":
                        self.tile.blit(self.texture,(-16 * 7 , -16 * 5))

                    elif row[column] == "89":
                        self.tile.blit(self.texture,(-16 * 8 , -16 * 5))

                    elif row[column] == "90":
                        self.tile.blit(self.texture,(-16 * 9 , -16 * 5))

                    elif row[column] == "91":
                        self.tile.blit(self.texture,(-16 * 10 , -16 * 5))

                    elif row[column] == "92":
                        self.tile.blit(self.texture,(-16 * 11 , -16 * 5))

                    elif row[column] == "93":
                        self.tile.blit(self.texture,(-16 * 12 , -16 * 5))

                    elif row[column] == "94":
                        self.tile.blit(self.texture,(-16 * 13 , -16 * 5))

                    elif row[column] == "95":
                        self.tile.blit(self.texture,(-16 * 14 , -16 * 5))


                    #print(-16 * 10)


                    

                    self.renderMap.blit(self.tile,(x * 16 - camera.cameraX, y * 16 - camera.cameraY))

                y += 1
                

            
        player.x += player.dx
        player.y += player.dy

        display.blit(self.renderMap,(0,0))



        


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