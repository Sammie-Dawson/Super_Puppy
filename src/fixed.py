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
        elif level==4:
            print("level 4 map!")
        else:
            print("something wrong with map")



class bunnies():
    def __init__(self):

        #self.surface = self.update_surface()
        self.level1_bunny_no_hide=[]

        self.level2_bunny_no_hide=[]
        self.level2_bunny_small_hide=[]

        self.level3_bunny_no_hide=[]
        self.level3_bunny_small_hide=[]
        self.level3_bunny_big_hide=[]
        self.L1gA_scare=False
        self.L1gA_scare=False
        self.L1gA_scare=False

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

    def scare(self, cordinates_dog, level):
        x_cordinate,y_cordinate=cordinates_dog
       # if cordinates of dog  x=0 remove group a from 
        if level==1:
            if x_cordinate==0:
                self.L1gA_scare=True
            elif x_cordinate==266:
                self.L1gB_scare=True
            elif x_cordinate==534:
                self.L1gC_scare=True
            else:
                print("level 1 group not detected")
    
    def level_system(self,level,screen):
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

            self.level1_bunny_no_hide_gA=[(bunny_2a),(bunny_3a)]
            self.level1_bunny_no_hide_gB=[(bunny_1b),(bunny_3b)]
            self.level1_bunny_no_hide_gC=[(bunny_1c),(bunny_2c),(bunny_3c)]
            #while self.L1gA_scare==False:
            for bunny in self.level1_bunny_no_hide_gA:
                bunnies.bunny_print_no_hide(screen,bunny)
                print(bunny)
            #while self.L1gB_scare==False:
            for bunny in self.level1_bunny_no_hide_gB:
                bunnies.bunny_print_no_hide(screen,bunny)
                print(bunny)
            #while self.L1gC_scare==False:
            for bunny in self.level1_bunny_no_hide_gC:
                bunnies.bunny_print_no_hide(screen,bunny)
                print(bunny)
            #self.level1_bunny_no_hide=[(bunny_1b),(bunny_1c),(bunny_2a),(bunny_2c),(bunny_3a),(bunny_3b),(bunny_3c)]
            #for bunny in self.level1_bunny_no_hide:
                #bunnies.bunny_print_no_hide(screen,bunny)
                #print(bunny)
        if level==3:
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

            self.level3_bunny_no_hide=[bunny_1a,bunny_1f,bunny_2f,bunny_3c]
            for bunny in self.level3_bunny_no_hide:
                bunnies.level3_bunny_print_no_hide(screen,bunny)
            self.level3_bunny_small_hide=(bunny_1b),(bunny_1c),(bunny_1e),(bunny_2b),(bunny_2d),(bunny_3a),(bunny_3e)
            for bunny in self.level3_bunny_small_hide:
                bunnies.level3_bunny_print_small_hide(screen,bunny)
            self.level3_bunny_big_hide=[bunny_1d,bunny_2a,bunny_2c,bunny_2e,bunny_3b,bunny_3d,bunny_3f]
            for bunny in self.level3_bunny_big_hide:
                bunnies.level3_bunny_print_big_hide(screen,bunny)
        if level==2:
            bunny_1a=((0),(160))
            bunny_1b=((266),(160))
            bunny_1c=((534),(160))

            bunny_2a=((0),(270))
            bunny_2b=((266),(270))
            bunny_2c=((534),(270))
            
            bunny_3a=((0),(380))
            bunny_3b=((266),(380))
            bunny_3c=((534),(380))
            self.level2_bunny_no_hide=[bunny_1a,bunny_2c,bunny_3b]
            for bunny in self.level2_bunny_no_hide:
                bunnies.bunny_print_no_hide(screen,bunny)
            self.level2_bunny_small_hide=(bunny_1b),(bunny_1c),(bunny_2a),(bunny_2b),(bunny_3a),(bunny_3c)
            for bunny in self.level2_bunny_small_hide:
                bunnies.bunny_print_small_hide(screen,bunny)

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
    if level==4:
        new_cordinates=(0),(0)

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
    if level==4:
        new_cordinates=(0),(0)
    result=new_cordinates
    print (result)
    return result

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
        background = pygame.image.load('Supper_puppy_level3.png').convert_alpha()
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

def level_determine(dt):
    if dt<=2000:
        level=1
        print ("level 1")
    elif (dt>=2001 and dt<=4000):
        level=2
        print ("level 2")
    elif dt>=4001 and dt<=6000:
        level=3
        print ("level 3")
    else:
        level=4
        print ("game over")
    print (dt)
    return level

def main():
    pygame.init()
    pygame.display.set_caption("Supper Puppy")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    #Bunnies = bunnies(resolution)
    fix_dog = (266, 490)
    fix_bunny=(0, 380)
    Supper_Bunny=bunnies()
   # Supper_Pupppy=supper_puppy(fix_dog)
    running = True
    fullscreen=False
    Level=level_determine(dt)
    #Level=1
    while running:
        Time=pygame.time.get_ticks()
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
                    Supper_Bunny.scare(fix_dog, Level)
            #elif event.type == pygame.
        Level=level_determine(Time)
        if Level==1:   
            Supper_Pupppy=supper_puppy(fix_dog)

        elif Level==2:
            Supper_Pupppy=supper_puppy(fix_dog)
            Supper_Bunny=bunnies()
        elif Level==3:
            Supper_Pupppy=Level3_supper_puppy(fix_dog)
            Supper_Bunny=bunnies()

        Supper_Pupppy.update(dt)

        BLACK = pygame.Color(0, 0, 0)
        screen.fill(BLACK)
       # bunnies.draw(screen)
        
        map(screen,Level)
        Supper_Pupppy.image(screen)
        Supper_Bunny.level_system(Level,screen)
      
        Supper_Pupppy.draw(screen)
        #Supper_Bunny.draw(screen)
        mouse_resaponse(screen)
        pygame.display.flip()
        
        dt = clock.tick(12)
        
    pygame.quit()

if __name__ == "__main__":
    main()