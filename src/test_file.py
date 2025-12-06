import random
import pygame
class bunnies():
    def __init__(self):

        self.surface = self.update_surface()


    def bunny_print_no_hide(screen, bunny):
        background = pygame.image.load('Bunny_no_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))
    def bunny_print_small_hide(screen, bunny):
        background = pygame.image.load('Bunny_small_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))
    
    def level3_bunny_print_no_hide(screen, bunny):
        background = pygame.image.load('level3_Bunny_no_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))
    def level3_bunny_print_small_hide(screen, bunny):
        background = pygame.image.load('level3_Bunny_small_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))



    def level3_bunny_print_big_hide(screen, bunny):
        background = pygame.image.load('level3_Bunny_big_hide.png').convert_alpha()

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
        elif level==3:
            bunny_1a=((0),(160))
            bunny_1b=((133),(160))
            bunny_1c=((266),(160))
            bunny_1d=((399),(160))
            bunny_1e=((534),(160))
            bunny_1f=((667),(160))

            bunny_2a=((0),(270))
            bunny_2b=((133),(270))
            bunny_2c=((266),(270))
            bunny_2d=((399),(270))
            bunny_2e=((534),(270))
            bunny_2f=((667),(270))
            
            bunny_3a=((0),(380))
            bunny_3b=((133),(380))
            bunny_3c=((266),(380))
            bunny_3d=((399),(380))
            bunny_3e=((534),(380))
            bunny_3f=((667),(380))

            bunny_no_hide=[bunny_1a,bunny_1f,bunny_2f,bunny_3c]
            for bunny in bunny_no_hide:
                bunnies.level3_bunny_print_no_hide(screen,bunny)
            bunny_small_hide=(bunny_1b),(bunny_1c),(bunny_1e),(bunny_2b),(bunny_2d),(bunny_3a),(bunny_3e)
            for bunny in bunny_small_hide:
                bunnies.level3_bunny_print_small_hide(screen,bunny)
            bunny_big_hide=[bunny_1d,bunny_2a,bunny_2c,bunny_2e,bunny_3b,bunny_3d,bunny_3f]
            for bunny in bunny_big_hide:
                bunnies.level3_bunny_print_big_hide(screen,bunny)
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
        

def map(screen, level):
    if level==1:
        background = pygame.image.load('supper puppy_level1_plans.png').convert_alpha()
        screen.blit(background, ((0), (0)))
    elif level==2:
        background = pygame.image.load('supper puppy_level2_plans.png').convert_alpha()
        screen.blit(background, ((0), (0)))
    elif level==3:
        background = pygame.image.load('supper puppy_level3_plan.png').convert_alpha()
        screen.blit(background, ((0), (0)))

#key = pygame.key.get_pressed()
       # if key[pygame.K_UP]: # up key
        #    self.dead= Bunny.scare(dog_pos)
class bunny_cordinates():

    def __init__(self, pos, size, life):
        self.pos= pos
        self.size = size
        self.life = life
        self.particles = []
    
    def bunny_tracker(self, level):
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
                particle = Bunny(bunny, size=self.size, life=self.life)
                self.particles.insert(0, particle)
                
    def update(self, dt):
        self._update_particles(dt)
        self._update_pos(dt)

    def _update_particles(self, dt):
        for idx, particle in enumerate(self.particles):
            particle.update(dt)
            if particle.dead:
                del self.particles[idx]

    def _update_particles(self, dt):
        for particle in self.particles:
            particle.update(dt)

    def _update_pos(self, dt):
        x, y = self.pos
        
        self.pos = (x, y)
    
    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)



class Bunny():

    def __init__(self, pos=(0, 0), size=1, life=360):
        self.pos = pos
        self.size = size

        self.age = 0 # in milliseconds
        self.life = life # in milliseconds
        self.dead = False
        self.alpha = 255
        self.surface = self.update_surface()
  
    def scare(self,dog_pos):
        x_cordinate,y_cordinate=dog_pos
        my_x_cordinate,my_y_cordinate=self.pos
        if my_x_cordinate==x_cordinate:
            self.dead=True
        else:
            self.dead=False


    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
    #    self.alpha = 255 * (1 - (self.age / self.life))

    def update_surface(self):
        surf = pygame.Surface((self.size*268, self.size*110))
        background = pygame.image.load('Bunny_no_hide.png').convert_alpha()

        surf.blit(background, (0,0))
        
        
        return surf
    
    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)

    

def bunny_test(screen):
    background = pygame.image.load('test_bunny_square.png').convert_alpha()

    NameTag=screen.blit(background, ((534), (380)))
def move_right(cordinates,level):
    x_cordinate, y_cordinate=cordinates
    if level==1:
        if x_cordinate>=532:
            new_cordinates=cordinates
        else:
            new_cordinates=((x_cordinate +266), (y_cordinate))
    if level==2:
        if x_cordinate>=532:
            new_cordinates=cordinates
        else:
            new_cordinates=((x_cordinate +266), (y_cordinate))
    if level==3:
        if x_cordinate>=665:
            new_cordinates=cordinates
        else:
            new_cordinates=((x_cordinate +133), (y_cordinate))
    result=new_cordinates
    print (result)
    return result

def move_left(cordinates,level):
    x_cordinate, y_cordinate=cordinates
    if level==1:
        if x_cordinate<=0:
            new_cordinates=cordinates
        else:
            new_cordinates=(x_cordinate -266), (y_cordinate)
    if level==2:
        if x_cordinate<=0:
            new_cordinates=cordinates
        else:
            new_cordinates=(x_cordinate -266), (y_cordinate)
    if level==3:
        if x_cordinate<=0:
            new_cordinates=cordinates
        else:
            new_cordinates=(x_cordinate -133), (y_cordinate)
    result=new_cordinates
    print (result)
    return result

#def bunnies():
   # x=5
class supper_puppy():

    def __init__(self, position=(266, 490), size=30, life=1000):
        self.size = size
        self.location=position
        self.age = 0 # in milliseconds
        self.life = life # in milliseconds
        self.dead = False
        self.alpha = 255
        self.surface = self.update_surface()

    def move_dog(self):
        position=self.location
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]: # up key
            position= move_left(self.location)
            print ("moved left")
        elif key[pygame.K_RIGHT]: # up key
            position=move_right(self.location)
            print("moved right")
        else:
            position=position
        self.location=position



    def image(self,screen):
        background = pygame.image.load('Supper_puppy_01.png').convert_alpha()
        position=self.location
        screen.blit(background, ((position)))
      
    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))

    def update_surface(self):
        dog = pygame.image.load('Supper_puppy.png').convert_alpha()
        return dog
    
    def draw(self, surface):
        surface.blit(self.surface, self.location)


class Level3_supper_puppy():

    def __init__(self, position=(266, 490), size=30, life=1000):
        self.size = size
        self.location=position
        self.age = 0 # in milliseconds
        self.life = life # in milliseconds
        self.dead = False
        self.alpha = 255
        self.surface = self.update_surface()

 



    def image(self,screen):
        background = pygame.image.load('Supper_puppy_01.png').convert_alpha()
        position=self.location
        screen.blit(background, ((position)))
      
    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))

    def update_surface(self):
        dog = pygame.image.load('Supper_puppy_level3.png').convert_alpha()
        return dog
    
    def draw(self, surface):
        surface.blit(self.surface, self.location)

  
  
       
        




def main():
    pygame.init()
    pygame.display.set_caption("Supper Puppy")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    #Bunnies = bunnies(resolution)
    fix_dog = (266, 490)
   # Supper_Pupppy=supper_puppy(fix_dog)
    running = True
    fullscreen=False
    Level=1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                  dog_left=move_left(fix_dog,Level)
                  fix_dog=dog_left
                if event.key == pygame.K_RIGHT:
                  dog_right=move_right(fix_dog,Level)
                  fix_dog=dog_right
                if event.key == pygame.K_UP:
                    bunny=Bunny(fix_dog)
                    bunny.scare(fix_dog)
            #elif event.type == pygame.
        if Level==1:   
            Supper_Pupppy=supper_puppy(fix_dog)
        elif Level==2:
            Supper_Pupppy=supper_puppy(fix_dog)
        elif Level==3:
            Supper_Pupppy=Level3_supper_puppy(fix_dog)
        Supper_Pupppy.update(dt)

        black = pygame.Color(255, 255, 255)
        screen.fill(black)
        #bunnies.draw(screen)
        
        map(screen,Level)
        Supper_Pupppy.image(screen)
        bunnies.level_system(Level,screen)
        Supper_Pupppy.draw(screen)
        mouse_resaponse(screen)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
    main()