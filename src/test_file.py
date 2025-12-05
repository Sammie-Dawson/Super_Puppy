import random
import pygame
class bunnies():

    def bunny_print_no_hide(screen, bunny):
        background = pygame.image.load('Bunny_no_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))
    def bunny_print_small_hide(screen, bunny):
        background = pygame.image.load('Bunny_small_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))
    def level_system(level,screen):
        if level==1:
            bunny_1a=((0),(160))
            bunny_1b=((266),(160))
            bunny_1c=((534),(160))

            bunny_2a=((0),(270))
            bunny_2b=((266),(270))
            bunny_2c=((534),(270))
            
            bunny_3a=((0),(380))
            bunny_3b=((266),(380))
            bunny_3c=((534),(380))
            bunny_no_hide=[(bunny_1b),(bunny_1c),(bunny_2a),(bunny_2c),(bunny_3a),(bunny_3b),(bunny_3c)]
            for bunny in bunny_no_hide:
                bunnies.bunny_print_no_hide(screen,bunny)
        elif level==2:
            bunny_1a=((0),(160))
            bunny_1b=((266),(160))
            bunny_1c=((534),(160))

            bunny_2a=((0),(270))
            bunny_2b=((266),(270))
            bunny_2c=((534),(270))
            
            bunny_3a=((0),(380))
            bunny_3b=((266),(380))
            bunny_3c=((534),(380))
            bunny_no_hide=[bunny_1a,bunny_2c,bunny_3b]
            for bunny in bunny_no_hide:
                bunnies.bunny_print_no_hide(screen,bunny)
            bunny_small_hide=(bunny_1b),(bunny_1c),(bunny_2a),(bunny_2b),(bunny_3a),(bunny_3c)
            for bunny in bunny_small_hide:
                bunnies.bunny_print_small_hide(screen,bunny)


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
        return  x_b, y_b 
        
def image(screen, fullscreen):
    background = pygame.image.load('Supper_puppy.png').convert_alpha()
    if fullscreen==True:
        sizes=pygame.display.get_desktop_sizes()
    else:
        sizes=[(800,600)]
    Width=screenSize_Format_Width(sizes)
    height=screenSize_Format_Height(sizes)
    NameTag=screen.blit(background, ((Width//3), (height-200)))

def map(screen):
    background = pygame.image.load('supper puppy_level1_plans.png').convert_alpha()

    NameTag=screen.blit(background, ((0), (0)))

def bunny_test(screen):
    background = pygame.image.load('test_bunny_square.png').convert_alpha()

    NameTag=screen.blit(background, ((534), (380)))
def move_left(cordinates):
    x_cordinate, y_cordinate=cordinates
    new_cordinates=((x_cordinate +10), (y_cordinate))
    result=new_cordinates
    print (result)
    return result

def move_right(cordinates):
    x_cordinate, y_cordinate=cordinates
    new_cordinates=(x_cordinate -1), (y_cordinate)
    result=new_cordinates
    return result

#def bunnies():
   # x=5
class supper_puppy():

    def __init__(self, position=(0, 0), size=30, life=1000):
        self.size = size
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: # up key
            position= move_left(position)
        elif key[pygame.K_RIGHT]: # up key
            position=move_right(position)
        else:
            position=position
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
    
    #def image_run():
        
       # background = pygame.image.load('Supper_puppy.png').convert_alpha()

      

    def update_surface(self):
        dog = pygame.image.load('Supper_puppy.png').convert_alpha()
        return dog
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

        x_b, y_b = pygame.mouse.get_pos()
        print(self.pos)
   
        #surface.blit(self.surface, (x_b, y_b))
       # if self.dead:
         #      return
        #self.surface.set_alpha(self.alpha)
       
        



def main():
    pygame.init()
    pygame.display.set_caption("Supper Puppy")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    #Bunnies = bunnies(resolution)
    fix_dog = (400, 400)
    Supper_Pupppy=supper_puppy(fix_dog)
    running = True
    fullscreen=False
    Level=2
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                sizes=pygame.display.get_desktop_sizes()
                Width_screen=screenSize_Format_Width(sizes)
                fullscreen=True
        if fullscreen==True:
            Supper_Pupppy.update(dt)
            #Supper_Pupppy.update(dt,Width_screen,fullscreen)
            #bunnies.update(dt,Width_screen,fullscreen)
        else:  
            width_normal=800
            Supper_Pupppy.update(dt)
            #Supper_Pupppy.update(dt, width_normal, False)
            #bunnies.update(dt,width_normal,fullscreen)
        black = pygame.Color(255, 255, 255)
        screen.fill(black)
        #bunnies.draw(screen)
        image(screen, fullscreen)
        map(screen)
        bunnies.level_system(Level,screen)
        Supper_Pupppy.draw(screen)
        mouse_resaponse(screen)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
    main()