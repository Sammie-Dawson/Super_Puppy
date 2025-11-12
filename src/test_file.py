import random
import pygame

def Resize():
    pygame.display.toggle_fullscreen()
    pygame.display.set_mode(pygame.RESIZABLE)
    sizes=pygame.display.get_desktop_sizes()
    
def screenSize_Format_Width(sizes):
    pulled_item = sizes[0]
    Width_screen, Height=pulled_item
    result=Width_screen
    return result

def screenSize_Format_Height(sizes):
    pulled_item = sizes[0]
    Width_screen, Height=pulled_item
    result=Height
    return result

def mouse_resaponse(screen):
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]: # down key
        radius = 50
        ball = pygame.Surface((radius*2-1, radius*2-1))
        x_b, y_b = pygame.mouse.get_pos()
        YELLOW=pygame.Color(186, 155, 89)
        circle=pygame.draw.circle(ball, (YELLOW), (50,50), (radius))
        screen.blit(ball, (x_b, y_b))
        


def move_left(cordinates):
    x_cordinate, y_cordinate=cordinates
    new_cordinates=(x_cordinate +1), (y_cordinate)
    result=new_cordinates
    return result

def move_right(cordinates):
    x_cordinate, y_cordinate=cordinates
    new_cordinates=(x_cordinate -1), (y_cordinate)
    result=new_cordinates
    return result

def bunnies():
    x=5
class supper_puppy():

    def __init__(self, pos=(1, 0), size=30, life=1000):
        self.size = size
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: # up key
            position= move_left(pos)
        elif key[pygame.K_RIGHT]: # up key
            position=move_right(pos)
        else:
            position=pos
        self.pos = position
        self.age = 0 # in milliseconds
        self.life = life # in milliseconds
        self.dead = False
        self.alpha = 255
        self.surface = self.update_surface()
 
      
    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))
    
    def image_run(self, screen, fullscreen):
        self.screen=screen
        self.fullscreen=fullscreen
        background = pygame.image.load('Supper_puppy.png').convert_alpha()

        if fullscreen==True:
            sizes=pygame.display.get_desktop_sizes()
        else:
            sizes=[(800,600)]
        Width=screenSize_Format_Width(sizes)
        height=screenSize_Format_Height(sizes)
        NameTag=screen.blit(background, ((Width//3), (height-200)))

    def update_surface(self):
        dog = image_run(self.screen,self.fullscreen)
        return dog
    
    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)


def main():
    pygame.init()
    pygame.display.set_caption("Supper Puppy")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    #Bunnies = bunnies(resolution)
    Supper_Pupppy=supper_puppy(resolution)
    running = True
    fullscreen=False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                sizes=pygame.display.get_desktop_sizes()
                Width_screen=screenSize_Format_Width(sizes)
                fullscreen=True
        
        if fullscreen==True:
            Supper_Pupppy.update(dt,Width_screen,fullscreen)
            #bunnies.update(dt,Width_screen,fullscreen)
        else:  
            width_normal=800
            supper_puppy.update(dt, width_normal, False)
            #bunnies.update(dt,width_normal,fullscreen)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        #bunnies.draw(screen)
        Supper_Pupppy.draw(screen)
        mouse_resaponse(screen)
        pygame.display.flip()
        dt = clock.tick(6)
    pygame.quit()

if __name__ == "__main__":
    main()