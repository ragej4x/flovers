import pygame as pg
import bulk
pg.init()


#ID0
width, height = 1024, 620
window = pg.display.set_mode((width, height))
display = pg.Surface((width/3 , height/3))
pg.display.set_caption("Flovers")

ico = pg.image.load("data/ico.png")
pg.display.set_icon(ico)

clock = pg.time.Clock()
loop = True
bg = pg.image.load("data/bg.jpg")

#ID1
def frameRate():
    font = pg.font.Font("data/bin/font", 18)
    getFps = str(int(clock.get_fps()))
    fpsText = font.render(getFps, True, (255,255,255))
    window.blit(fpsText, (2,2))
#ID2
#EVENT HANDLER
def eventHandler():
    global loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
            break
    
    dynamicResolution = pg.transform.scale(display, (width, height))
    window.blit(dynamicResolution, (0,0))

    frameRate()
    pg.display.flip()
    clock.tick(61)


#MAP
map = bulk.mapClass(pg)

#ID3
while loop == True:
    keyinput = pg.key.get_pressed()
    window.fill(0)
    display.fill((30,30,30))


    #display.blit(bg, (0 - bulk.camera.cameraX ,0 - bulk.camera.cameraY))
    bulk.player.hitbox(pg, display)
    map.updateMap(pg, display)

    bulk.player.mvControls(pg, display, keyinput)
    bulk.player.updatePlayerAnimation(pg, display, keyinput)
    bulk.camera.update(pg, display, keyinput)


    eventHandler()