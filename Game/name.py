import pygame,time,random
pygame.init()
soundTrack = pygame.mixer.Sound('Sounds/CandyShop.mp3')
gojo = pygame.mixer.Sound('Sounds/Gojo.wav')
bruh = pygame.mixer.Sound('Sounds/Bruh.mp3')
sukuna = pygame.mixer.Sound('Sounds/Money Go.wav')

info = pygame.display.Info()



screenWidth = 1920
screenHeight = 1080
imgWidth = 200
imgHeight = 200
xMid = screenWidth/2.5
yMid = screenHeight/2.5


screen = pygame.display.set_mode((info.current_w,info.current_h))
c1 = random.randrange(0,255)
c2 = random.randrange(0,255)
c3 = random.randrange(0,255)
color = (c1,c2,c3)

tempImg = pygame.image.load('Images/ABJump.gif').convert_alpha()
tempImg2 = pygame.image.load('Images/shid.jpeg')
tempImg3 = pygame.image.load('Images/GojoPic.jpg')
tempImg4 = pygame.image.load('Images/Sukuna.jpg')
imageSize = (imgWidth,imgHeight)
img = pygame.transform.scale(tempImg,imageSize)
img2 = pygame.transform.scale(tempImg2,imageSize)
img3 = pygame.transform.scale(tempImg3,imageSize)
img4 = pygame.transform.scale(tempImg4,imageSize)

imgFlip = pygame.transform.flip(img,True,False)




rect1 = img.get_rect()
rect2 = img2.get_rect()
rect3 = img3.get_rect()
rect4 = img4.get_rect()

rects = [rect1]




running = True
flip = False
right = True

clock =  pygame.time.Clock()
fps = 240
targetFps = 60

oldTime = time.time()
xVelocity = -5
yVelocity = -5


rect1.x = random.randrange(0,screenWidth-imgWidth)
rect1.y = random.randrange(0,screenHeight-imgHeight)
while running:
    if right:
        flip = False
    else:
        flip = True
    mouse = pygame.mouse.get_pos()
    clock.tick(fps)
    now = time.time()
    dt = now - oldTime
    dt *= targetFps
    oldTime = now

    if 0 < c1 < 255:
        c1 += 1
    elif c1 >= 255:
        c1 -= 255
    elif c1 <= 0:
        c1 += 3

    
    
    color = (c1,c2,c3)

    screen.fill(color)

    if flip:
        screen.blit(imgFlip,rect1)
    else:
        screen.blit(img,rect1)
    pygame.display.update()


    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        rect1.x -= 10 *dt 
    if key[pygame.K_d] == True:
        rect1.x += 10 *dt 
    if key[pygame.K_s] == True:
        rect1.y += 10 *dt 
    if key[pygame.K_w] == True:
        rect1.y -= 10 *dt 

    if key[pygame.K_LEFT] == True:
        rect2.x -= 10 *dt
    if key[pygame.K_RIGHT] == True:
        rect2.x += 10 *dt
    if key[pygame.K_DOWN] == True:
        rect2.y += 10 *dt
    if key[pygame.K_UP] == True:
        rect2.y -= 10 *dt
        
    if key[pygame.K_g] == True:
        rect3.x = xMid
        rect3.y = yMid
        for i in range(10):
            pygame.draw.rect(screen, (255,0,50), rect3)
            screen.blit(img3,rect3)
            pygame.display.update()
            gojo.play()
    
    if key[pygame.K_b] == True:
        rect4.x = xMid
        rect4.y = yMid
        for i in range(10):
            pygame.draw.rect(screen, (255,0,50), rect4)
            screen.blit(img4,rect4)
            pygame.display.update()
            sukuna.play()

    
            
    
        
    for rect in rects:
        #rect.x += xVelocity *dt
        #rect.y += yVelocity *dt
        
        if rect.centerx > mouse[0]:
            rect.x += xVelocity *dt
            right = True
        if rect.centerx < mouse[0]:
            rect.x -= xVelocity * dt
            right = False
        if rect.centery > mouse[1]:
            rect.y += yVelocity *dt
        if rect.centery < mouse[1]:
            rect.y -= yVelocity * dt
        
        
        if rect.centerx == mouse[0] and rect.centery == mouse[1]:
            if visible != False:
                bruh.play()
            visible = False
            pygame.mouse.set_visible(False)
        else:
            visible = True
            pygame.mouse.set_visible(True)

        '''
        if rect.centerx <= 0 or rect.right >= screenWidth+90:
            xVelocity = -xVelocity
            if (xVelocity > 0):
                right = True
            else:
                right = False
            
        if rect.top <= -70 or rect.bottom >= screenHeight+60:
            yVelocity = -yVelocity
        '''
    

        

        
        

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit