import  pygame
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, filename, alex_x = 600, alex_y = 650, x_speed = 0, y_speed = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = alex_x
        self.rect.y = alex_y

        self.alex_x = alex_x
        self.alex_y = alex_y
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x = self.rect.x + self.x_speed
        self.rect.y = self.rect.y + self.y_speed

alex = Player("Alex.png")
print(alex.__dict__)

window_w = 1200
window_h = 800
speed = 0
sdvig_fona = 0

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Самостоятельная работа 3.4")
fon = "Fon1.jpg"
img1 = pygame.image.load(fon)
back_fon = pygame.transform.scale(img1, (window_w, window_h))

sound_streli=pygame.mixer.Sound("Vp2.mp3")
sound_streli.play()

a = True
while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #speed = 2
                
                alex.x_speed = 2
            if event.key == pygame.K_LEFT:
                #speed = -2
                
                alex.x_speed = -2
            if event.key == pygame.K_UP:

                alex.y_speed = -2
            if event.key == pygame.K_DOWN:
                alex.y_speed = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                speed = 0
                alex.x_speed = 0
            if event.key == pygame.K_LEFT:
                speed = 0
                alex.x_speed = 0
            if event.key == pygame.K_UP:
                speed = 0
                alex.y_speed = 0
            if event.key == pygame.K_DOWN:
                #speed = 0
                alex.y_speed = 0

                                #для границ верха и низа
    if alex.rect.y<=0 and alex.y_speed<0:
        alex.rect.y=alex.rect.y-alex.y_speed
    if alex.rect.y+200>=900and alex.y_speed>0:
        alex.rect.y=alex.rect.y-alex.y_speed
    #для границ слева и справа
    if alex.rect.x + 100 >= 1250 and alex.x_speed > 0:
        alex.rect.x= alex.rect.x - alex.x_speed
        speed=-2
    if alex.rect.x <0  and alex.x_speed < 0:
        alex.rect.x= alex.rect.x-alex.x_speed
        speed=2

    sdvig_fona = (sdvig_fona + speed) % window_w
    #print(sdvig_fona)

    window.blit(back_fon, (sdvig_fona, 0))
    if sdvig_fona!=0:
        window.blit(back_fon, (sdvig_fona - window_w, 0))

    alex.update()
    window.blit(alex.image, (alex.rect.x, alex.rect.y))

    pygame.display.update()

pygame.quit()

    























                
