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



class bunnies_level_1():
    def __init__(self):
        self.total_bunnnies_scared=0
        self.total_no_hide_scared=0
        self.total_small_hide_scared=0
        self.total_big_hide_scared=0
        #self.surface = self.update_surface()

        self.level1_bunny_no_hide_gA=[]
        self.level1_bunny_no_hide_gB=[]
        self.level1_bunny_no_hide_gC=[]

        self.L1gA_scare=0
        self.L1gB_scare=0
        self.L1gC_scare=0

    def bunny_print_no_hide(screen, bunny):
        background = pygame.image.load('Bunny_no_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def scare(self, cordinates_dog, level):
        x_cordinate,y_cordinate=cordinates_dog
        if level==1:
            if x_cordinate==0:
                if self.L1gA_scare==0:
                    self.L1gA_scare+=1
                print("L1gA")
            elif x_cordinate==266:
                self.L1gB_scare+=1
                print("L1gB")
            elif x_cordinate==532:
                self.L1gC_scare+=1
                print("L1gC")
            else:
                print("level 1 group not detected")
            print(self.L1gA_scare)
        elif level==2:
            bunny_2=bunnies_level_2()
            bunny_2.scare(cordinates_dog, level)
        elif level==3:
            bunny_3=bunnies_level_3()
            bunny_3.scare(cordinates_dog, level)
        elif level==4:
             print("gameover")

        
    def level_1_2_no_hide_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
        if scare_level_tracker==False:
                for bunny in hide_type_group:
                    bunnies_level_1.bunny_print_no_hide(screen,bunny)


    def Level_1_kill_system(self,screen):
            if self.L1gA_scare==0:
                for bunny in self.level1_bunny_no_hide_gA:
                    bunnies_level_1.bunny_print_no_hide(screen,bunny)
            if self.L1gB_scare==0:
                for bunny in self.level1_bunny_no_hide_gB:
                    bunnies_level_1.bunny_print_no_hide(screen,bunny)
            if self.L1gC_scare==0:
                for bunny in self.level1_bunny_no_hide_gC:
                    bunnies_level_1.bunny_print_no_hide(screen,bunny)
                 
    def level_system(self,level, screen):
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
            bunnies_level_1.Level_1_kill_system(self,screen)
        


class bunnies_level_2():
    def __init__(self):
        self.total_bunnnies_scared=0
        self.total_no_hide_scared=0
        self.total_small_hide_scared=0
        self.total_big_hide_scared=0

        self.level2_bunny_small_hide=[]
        self.level2_bunny_small_hide_gA=[]
        self.level2_bunny_small_hide_gB=[]
        self.level2_bunny_small_hide_gC=[]

        self.L2gA_NH_scare=0
        self.L2gB_NH_scare=0
        self.L2gC_NH_scare=0

        self.L2gA_SH_scare=0
        self.L2gB_SH_scare=0
        self.L2gC_SH_scare=0

    def bunny_print_no_hide(screen, bunny):
        background = pygame.image.load('Bunny_no_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))
    
    def bunny_print_small_hide(screen, bunny,scare):
        background = pygame.image.load('Bunny_small_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def scare(self, cordinates_dog, level):
        x_cordinate,y_cordinate=cordinates_dog
       # if cordinates of dog  x=0 remove group a from 
        if level==2:
            if x_cordinate==0:
                self.L2gA_NH_scare+=1
                self.L2gA_SH_scare+=1
                print("L2gA")
            elif x_cordinate==266:
                self.L2gB_NH_scare+=1
                self.L2gB_SH_scare+=1
                print("L2gB")
            elif x_cordinate==532:
                self.L2gC_NH_scare+=1
                self.L2gC_SH_scare+=1
                print("L2gC")
            else:
                print("level 2 group not detected")
            print(self.L2gC_SH_scare)

    def level_1_2_no_hide_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
        if scare_level_tracker==False:
                for bunny in hide_type_group:
                    bunnies_level_2.bunny_print_no_hide(screen,bunny)

    def level_1_2_small_hide_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
            if scare_level_tracker==0:
                for bunny in hide_type_group:
                    bunnies_level_2.bunny_print_small_hide(screen,bunny,scare_level_tracker)
            elif scare_level_tracker==1:
                for bunny in hide_type_group:
                    bunnies_level_2.bunny_print_small_hide(screen,bunny,scare_level_tracker)

    def Level_2_kill_system(self,screen):
            bunnies_level_2.level_1_2_no_hide_scare_tracker(self,self.L2gA_NH_scare,self.level2_bunny_no_hide_gA, screen)
            bunnies_level_2.level_1_2_no_hide_scare_tracker(self,self.L2gB_NH_scare,self.level2_bunny_no_hide_gB, screen)
            bunnies_level_2.level_1_2_no_hide_scare_tracker(self,self.L2gC_NH_scare,self.level2_bunny_no_hide_gC, screen)

            bunnies_level_2.level_1_2_small_hide_scare_tracker(self,self.L2gA_SH_scare,self.level2_bunny_small_hide_gA, screen)
            bunnies_level_2.level_1_2_small_hide_scare_tracker(self,self.L2gB_SH_scare,self.level2_bunny_small_hide_gB, screen)
            bunnies_level_2.level_1_2_small_hide_scare_tracker(self,self.L2gC_SH_scare,self.level2_bunny_small_hide_gC, screen)

    def level_system(self,level,screen):
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
            self.level2_bunny_no_hide_gA=[bunny_1a]
            self.level2_bunny_no_hide_gB=[bunny_3b]
            self.level2_bunny_no_hide_gC=[bunny_2c]

            self.level2_bunny_small_hide_gA=[bunny_2a,bunny_3a]
            self.level2_bunny_small_hide_gB=[bunny_1b,bunny_2b]
            self.level2_bunny_small_hide_gC=[bunny_1c,bunny_3c]
            bunnies_level_2.Level_2_kill_system(self,screen)

class Bunny_summons():

    def __init__(self):
        self.total_bunnnies_scared=0

        
    def scare(cordinates_dog, level):
            bunny_1=bunnies_level_1()
            bunny_1.scare(cordinates_dog, level)
            bunny_2=bunnies_level_2()
            bunny_2.scare(cordinates_dog, level)
            bunny_3=bunnies_level_3()
            bunny_3.scare(cordinates_dog, level)

    def level_system(level,screen):
            bunny_1=bunnies_level_1()
            bunny_1.level_system(level, screen)
            bunny_2=bunnies_level_2()
            bunny_2.level_system(level, screen)
            bunny_3=bunnies_level_3()
            bunny_3.level_system(level, screen)
        



class bunnies_level_3():
    def __init__(self):
        self.total_bunnnies_scared=0
        self.total_no_hide_scared=0
        self.total_small_hide_scared=0
        self.total_big_hide_scared=0

        self.level3_bunny_no_hide_gA=[]
        self.level3_bunny_no_hide_gB=[]
        self.level3_bunny_no_hide_gC=[]
        self.level3_bunny_no_hide_gD=[]
        self.level3_bunny_no_hide_gE=[]
        self.level3_bunny_no_hide_gF=[]

        self.level3_bunny_small_hide=[]
        self.level3_bunny_small_hide_gA=[]
        self.level3_bunny_small_hide_gB=[]
        self.level3_bunny_small_hide_gC=[]
        self.level3_bunny_small_hide_gD=[]
        self.level3_bunny_small_hide_gE=[]
        self.level3_bunny_small_hide_gF=[]

        self.level3_bunny_big_hide=[]
        self.level3_bunny_big_hide_gA=[]
        self.level3_bunny_big_hide_gB=[]
        self.level3_bunny_big_hide_gC=[]
        self.level3_bunny_big_hide_gD=[]
        self.level3_bunny_big_hide_gE=[]
        self.level3_bunny_big_hide_gF=[]


        self.L3gA_NH_scare=0
        self.L3gB_NH_scare=0
        self.L3gC_NH_scare=0
        self.L3gD_NH_scare=0
        self.L3gE_NH_scare=0
        self.L3gF_NH_scare=0

        self.L3gA_SH_scare=0
        self.L3gB_SH_scare=0
        self.L3gC_SH_scare=0
        self.L3gD_SH_scare=0
        self.L3gE_SH_scare=0
        self.L3gF_SH_scare=0

        self.L3gA_BH_scare=0
        self.L3gB_BH_scare=0
        self.L3gC_BH_scare=0
        self.L3gD_BH_scare=0
        self.L3gE_BH_scare=0
        self.L3gF_BH_scare=0

    def scare_counter_level_3(self, no_hide, small_hide, big_hide):
                if no_hide==0:
                    self.total_bunnnies_scared+=1
                    self.total_no_hide_scared+=1
                if small_hide==1:
                    self.total_bunnnies_scared+=1
                    self.total_small_hide_scared+=1

                if big_hide==2:
                    self.total_bunnnies_scared+=1
                    self.total_big_hide_scared+=1
    
    def level3_bunny_print_no_hide(screen, bunny):
        background = pygame.image.load('level3_Bunny_no_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def level3_bunny_print_small_hide(screen, bunny,scare):
        background = pygame.image.load('level3_Bunny_small_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def level3_bunny_print_big_hide(screen, bunny, scare_level):
        background = pygame.image.load('level3_Bunny_big_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def scare(self, cordinates_dog, level):
        x_cordinate,y_cordinate=cordinates_dog
        if level==3:
            if x_cordinate==0:
                self.L3gA_NH_scare+=1
                self.L3gA_SH_scare+=1
                self.L3gA_BH_scare+=1
                print("L3gA")
            elif x_cordinate==133:
                self.L3gB_NH_scare+=1
                self.L3gB_SH_scare+=1
                self.L3gB_BH_scare+=1
                print("L3gB")

            elif x_cordinate==266:
                self.L3gC_NH_scare+=1
                self.L3gC_SH_scare+=1
                self.L3gC_BH_scare+=1
                print(self.L3gC_NH_scare)
                print("L3gC")

            elif x_cordinate==399:
                self.L3gD_NH_scare+=1
                self.L3gD_SH_scare+=1
                self.L3gD_BH_scare+=1
                print("L3gD")

            elif x_cordinate==532:
                self.L3gE_NH_scare+=1
                self.L3gE_SH_scare+=1
                self.L3gE_BH_scare+=1
                print("L3gE")

            elif x_cordinate==665:
                self.L3gF_NH_scare+=1
                self.L3gF_SH_scare+=1
                self.L3gF_BH_scare+=1
                print("L3gF")

            else:
                print("level 3 group not detected")

    def level_3_small_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
        if scare_level_tracker==0:
                for bunny in hide_type_group:
                    bunnies_level_3.level3_bunny_print_small_hide(screen,bunny,scare_level_tracker)
        elif scare_level_tracker==1:
                for bunny in hide_type_group:
                    bunnies_level_3.level3_bunny_print_small_hide(screen,bunny,scare_level_tracker)
        elif scare_level_tracker==2:
            self.total_bunnnies_scared+=1
            self.total_small_hide_scared+=1
             
    def level_3_big_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
        
            if scare_level_tracker==0:
                for bunny in hide_type_group:
                    bunnies_level_3.level3_bunny_print_big_hide(screen,bunny,scare_level_tracker)
            elif scare_level_tracker==1:
                for bunny in hide_type_group:
                    bunnies_level_3.level3_bunny_print_big_hide(screen,bunny,scare_level_tracker)
            elif scare_level_tracker==2:
                for bunny in hide_type_group:
                    bunnies_level_3.level3_bunny_print_big_hide(screen,bunny,scare_level_tracker)
            elif scare_level_tracker==3:
                self.total_bunnnies_scared+=1
                self.total_big_hide_scared+=1

    def level_3_no_hide_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
            if scare_level_tracker==0:
                for bunny in hide_type_group:
                    bunnies_level_3.level3_bunny_print_no_hide(screen,bunny)
           # elif scare_level_tracker==1 and scared==True:
              #  self.total_bunnnies_scared+=1
                #self.total_small_hide_scared+=1 
                
                #print(self.total_small_hide_scared)  
               # print(self.total_bunnnies_scared)        

    def Level_3_kill_system(self,screen):
            bunnies_level_3.level_3_no_hide_scare_tracker(self,self.L3gA_NH_scare,self.level3_bunny_no_hide_gA, screen)
            #self.L3gA_NH_scare+=1
            bunnies_level_3.level_3_no_hide_scare_tracker(self,self.L3gB_NH_scare,self.level3_bunny_no_hide_gB, screen)
           # self.L3gB_NH_scare+=1
            bunnies_level_3.level_3_no_hide_scare_tracker(self,self.L3gC_NH_scare,self.level3_bunny_no_hide_gC, screen)
            #self.L3gC_NH_scare+=1
            bunnies_level_3.level_3_no_hide_scare_tracker(self,self.L3gD_NH_scare,self.level3_bunny_no_hide_gD, screen)
           # self.L3gD_NH_scare+=1
            bunnies_level_3.level_3_no_hide_scare_tracker(self,self.L3gE_NH_scare,self.level3_bunny_no_hide_gE, screen)
          #  self.L3gE_NH_scare+=1
            bunnies_level_3.level_3_no_hide_scare_tracker(self,self.L3gF_NH_scare,self.level3_bunny_no_hide_gF, screen)
          #  self.L3gF_NH_scare+=1


            bunnies_level_3.level_3_small_scare_tracker(self,self.L3gA_SH_scare,self.level3_bunny_small_hide_gA, screen)
            bunnies_level_3.level_3_small_scare_tracker(self,self.L3gB_SH_scare,self.level3_bunny_small_hide_gB, screen)
            bunnies_level_3.level_3_small_scare_tracker(self,self.L3gC_SH_scare,self.level3_bunny_small_hide_gC, screen)
            bunnies_level_3.level_3_small_scare_tracker(self,self.L3gD_SH_scare,self.level3_bunny_small_hide_gD, screen)
            bunnies_level_3.level_3_small_scare_tracker(self,self.L3gE_SH_scare,self.level3_bunny_small_hide_gE, screen)
            bunnies_level_3.level_3_small_scare_tracker(self,self.L3gF_SH_scare,self.level3_bunny_small_hide_gF, screen)


            bunnies_level_3.level_3_big_scare_tracker(self,self.L3gA_BH_scare,self.level3_bunny_big_hide_gA, screen)
            bunnies_level_3.level_3_big_scare_tracker(self,self.L3gB_BH_scare,self.level3_bunny_big_hide_gB, screen)
            bunnies_level_3.level_3_big_scare_tracker(self,self.L3gC_BH_scare,self.level3_bunny_big_hide_gC, screen)
            bunnies_level_3.level_3_big_scare_tracker(self,self.L3gD_BH_scare,self.level3_bunny_big_hide_gD, screen)
            bunnies_level_3.level_3_big_scare_tracker(self,self.L3gE_BH_scare,self.level3_bunny_big_hide_gE, screen)
            bunnies_level_3.level_3_big_scare_tracker(self,self.L3gF_BH_scare,self.level3_bunny_big_hide_gF, screen)

    def level_system(self,level,screen):
                 
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

            self.level3_bunny_no_hide_gA=[bunny_1a]
            self.level3_bunny_no_hide_gB=[]
            self.level3_bunny_no_hide_gC=[bunny_3c]
            self.level3_bunny_no_hide_gD=[]
            self.level3_bunny_no_hide_gE=[]
            self.level3_bunny_no_hide_gF=[bunny_1f,bunny_2f]
            
            self.level3_bunny_small_hide_gA=[bunny_3a]
            self.level3_bunny_small_hide_gB=[bunny_1b, bunny_2b]
            self.level3_bunny_small_hide_gC=[bunny_1c]
            self.level3_bunny_small_hide_gD=[bunny_2d]
            self.level3_bunny_small_hide_gE=[bunny_1e, bunny_3e]
            self.level3_bunny_small_hide_gF=[]

            self.level3_bunny_big_hide_gA=[bunny_2a]
            self.level3_bunny_big_hide_gB=[bunny_3b]
            self.level3_bunny_big_hide_gC=[bunny_2c]
            self.level3_bunny_big_hide_gD=[bunny_1d,bunny_3d]
            self.level3_bunny_big_hide_gE=[bunny_2e]
            self.level3_bunny_big_hide_gF=[bunny_3f]

            bunnies_level_3.Level_3_kill_system(self,screen)



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
    #print (result)
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
        #print ("level 1")
    elif (dt>=2001 and dt<=4000):
        level=2
       # print ("level 2")
    elif dt>=4001 and dt<=6000:
        level=3
        #print ("level 3")
    else:
        level=4
        #print ("game over")
    #print (dt)
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
    scare=False
   # Supper_Pupppy=supper_puppy(fix_dog)
    running = True
    fullscreen=False
    #bunny=Bunny_summons()
    #Level=level_determine(dt)
    Level=3
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
                    Bunny_summons.scare(fix_dog, Level)
                    scare=True
                    print("SCARE")
        #Level=level_determine(Time)
        if Level==1:   
            Supper_Pupppy=supper_puppy(fix_dog)
            
        elif Level==2:
            Supper_Pupppy=supper_puppy(fix_dog)

        elif Level==3:
            Supper_Pupppy=Level3_supper_puppy(fix_dog)
 
        Supper_Pupppy.update(dt)
        BLACK = pygame.Color(0, 0, 0)
        screen.fill(BLACK)
        map(screen,Level)
        Bunny_summons.level_system(Level, screen)
        scare=False
        Supper_Pupppy.image(screen)
        Supper_Pupppy.draw(screen)
        mouse_resaponse(screen)
        pygame.display.flip()
        
        dt = clock.tick(12)
        
    pygame.quit()

if __name__ == "__main__":
    main()