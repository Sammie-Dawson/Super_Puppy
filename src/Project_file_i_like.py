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

 
        

def map(screen, level):
    
        if level==0:
            background = pygame.image.load('introduction_to_supper_puppy.png').convert_alpha()
            screen.blit(background, ((0), (0)))
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
       
        self.level1_bunny_no_hide_gA=[]
        self.level1_bunny_no_hide_gB=[]
        self.level1_bunny_no_hide_gC=[]

        self.level2_bunny_no_hide=[]
        self.level2_bunny_no_hide_gA=[]
        self.level2_bunny_no_hide_gB=[]
        self.level2_bunny_no_hide_gC=[]

        self.level2_bunny_small_hide=[]
        self.level2_bunny_small_hide_gA=[]
        self.level2_bunny_small_hide_gB=[]
        self.level2_bunny_small_hide_gC=[]


        #self.level3_bunny_no_hide=[]
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




        self.L1gA_scare=False
        self.L1gB_scare=False
        self.L1gC_scare=False

        self.L2gA_NH_scare=0
        self.L2gB_NH_scare=0
        self.L2gC_NH_scare=0

        self.L2gA_SH_scare=0
        self.L2gB_SH_scare=0
        self.L2gC_SH_scare=0


        self.L3gA_NH_scare=0  #1
        self.L3gB_NH_scare=0#0
        self.L3gC_NH_scare=0  #1
        self.L3gD_NH_scare=0#0
        self.L3gE_NH_scare=0#0
        self.L3gF_NH_scare=0      #2


        self.L3gA_SH_scare=0  #1
        self.L3gB_SH_scare=0      #2
        self.L3gC_SH_scare=0  #1
        self.L3gD_SH_scare=0  #1
        self.L3gE_SH_scare=0      #2
        self.L3gF_SH_scare=0#0


        self.L3gA_BH_scare=0  #1
        self.L3gB_BH_scare=0  #1
        self.L3gC_BH_scare=0  #1
        self.L3gD_BH_scare=0         #2
        self.L3gE_BH_scare=0  #1
        self.L3gF_BH_scare=0  #1
  
    def bunny_print_no_hide(screen, bunny):
        background = pygame.image.load('Bunny_no_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def bunny_print_small_hide(screen, bunny,scare):
        background = pygame.image.load('Bunny_small_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))
    
    def level3_bunny_print_no_hide(screen, bunny):
        background = pygame.image.load('level3_Bunny_no_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def level3_bunny_print_small_hide(screen, bunny,scare):
        background = pygame.image.load('level3_Bunny_small_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def level3_bunny_print_big_hide(screen, bunny, scare_level):
        background = pygame.image.load('level3_Bunny_big_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def scare(self, cordinates_dog, level, powerup):
        x_cordinate,y_cordinate=cordinates_dog
       # if cordinates of dog  x=0 remove group a from 
        if level==1:
            if x_cordinate==0:
                self.L1gA_scare+=1
                print("L1gA")
            elif x_cordinate==266:
                self.L1gB_scare+=1
                print("L1gB")
            elif x_cordinate==532:
                self.L1gC_scare+=1
                print("L1gB")
            else:
                print("level 1 group not detected")
            print(self.L1gA_scare)
        if level==2:
            if x_cordinate==0:
                self.L2gA_NH_scare+=1
                if powerup==True:
                    self.L2gA_SH_scare+=2
                else:
                    self.L2gA_SH_scare+=1
                print("L2gA")
            elif x_cordinate==266:
                self.L2gB_NH_scare+=1
                if powerup==True:
                    self.L2gB_SH_scare+=2
                else:
                    self.L2gB_SH_scare+=1
                print("L2gB")
            elif x_cordinate==532:
                self.L2gC_NH_scare+=1
                if powerup==True:
                    self.L2gC_SH_scare+=2
                else:
                    self.L2gC_SH_scare+=1
                print("L2gC")
            else:
                print("level 2 group not detected")
            print(self.L2gC_SH_scare)


        if level==3:
            if x_cordinate==0:
                self.L3gA_NH_scare+=1
                if powerup==True:
                    self.L3gA_SH_scare+=2
                    self.L3gA_BH_scare+=3
                else:
                    self.L3gA_SH_scare+=1
                    self.L3gA_BH_scare+=1
                print("L3gA")
            elif x_cordinate==133:
                self.L3gB_NH_scare+=1
                if powerup==True:
                    self.L3gB_SH_scare+=2
                    self.L3gB_BH_scare+=3
                else:
                    self.L3gB_SH_scare+=1
                    self.L3gB_BH_scare+=1
                print("L3gB")
            elif x_cordinate==266:
                self.L3gC_NH_scare+=1
                if powerup==True:
                    self.L3gC_SH_scare+=2
                    self.L3gC_BH_scare+=3
                else:
                    self.L3gC_SH_scare+=1
                    self.L3gC_BH_scare+=1
                print("L3gC")
            elif x_cordinate==399:
                self.L3gD_NH_scare+=1
                if powerup==True:
                    self.L3gD_SH_scare+=2
                    self.L3gD_BH_scare+=3
                else:
                    self.L3gD_SH_scare+=1
                    self.L3gD_BH_scare+=1
                print("L3gD")
            elif x_cordinate==532:
                #self.L3gF_NH_scare=1
                if powerup==True:
                    self.L3gE_SH_scare+=2
                    self.L3gE_BH_scare+=3
                else:
                    self.L3gE_SH_scare+=1
                    self.L3gE_BH_scare+=1
                #if self.L3gE_SH_scare<=1:
                #    self.L3gE_SH_scare+=1
                #if self.L3gE_BH_scare<=2:
                #    self.L3gE_BH_scare+=1
                print("L3gE")
            elif x_cordinate==665:
                self.L3gF_NH_scare=1
                #if self.L3gF_SH_scare<=1:
                 #   self.L3gF_SH_scare+=1
                if powerup==True:
                    self.L3gF_SH_scare+=2
                    self.L3gF_BH_scare+=3
                else:
                    self.L3gF_SH_scare+=1
                    self.L3gF_BH_scare+=1
                
                #if self.L3gF_BH_scare<=2:
               #     self.L3gF_BH_scare+=1
               # print(self.L3gF_NH_scare)
               # print(self.L3gF_SH_scare)
               # print(self.L3gF_BH_scare)
            else:
                print("level 3 group not detected")
            print(self.L3gC_SH_scare)

    def level_3_small_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
        if scare_level_tracker==0:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_small_hide(screen,bunny,scare_level_tracker)
        elif scare_level_tracker==1:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_small_hide(screen,bunny,scare_level_tracker)

    def level_3_big_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
        
            if scare_level_tracker==0:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_big_hide(screen,bunny,scare_level_tracker)
            elif scare_level_tracker==1:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_big_hide(screen,bunny,scare_level_tracker)
            elif scare_level_tracker==2:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_big_hide(screen,bunny,scare_level_tracker)

    def level_1_2_no_hide_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
        if scare_level_tracker==False:
                for bunny in hide_type_group:
                    bunnies.bunny_print_no_hide(screen,bunny)

    def level_1_2_small_hide_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
            if scare_level_tracker==0:
                for bunny in hide_type_group:
                    bunnies.bunny_print_small_hide(screen,bunny,scare_level_tracker)
            elif scare_level_tracker==1:
                for bunny in hide_type_group:
                    bunnies.bunny_print_small_hide(screen,bunny,scare_level_tracker)

    def level_3_no_hide_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
            if scare_level_tracker==False:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_no_hide(screen,bunny)

    def Level_3_kill_system(self,screen):
            bunnies.level_3_no_hide_scare_tracker(self,self.L3gA_NH_scare,self.level3_bunny_no_hide_gA, screen)
            bunnies.level_3_no_hide_scare_tracker(self,self.L3gB_NH_scare,self.level3_bunny_no_hide_gB, screen)
            bunnies.level_3_no_hide_scare_tracker(self,self.L3gC_NH_scare,self.level3_bunny_no_hide_gC, screen)
            bunnies.level_3_no_hide_scare_tracker(self,self.L3gD_NH_scare,self.level3_bunny_no_hide_gD, screen)
            bunnies.level_3_no_hide_scare_tracker(self,self.L3gE_NH_scare,self.level3_bunny_no_hide_gE, screen)
            bunnies.level_3_no_hide_scare_tracker(self,self.L3gF_NH_scare,self.level3_bunny_no_hide_gF, screen)


            bunnies.level_3_small_scare_tracker(self,self.L3gA_SH_scare,self.level3_bunny_small_hide_gA, screen)
            bunnies.level_3_small_scare_tracker(self,self.L3gB_SH_scare,self.level3_bunny_small_hide_gB, screen)
            bunnies.level_3_small_scare_tracker(self,self.L3gC_SH_scare,self.level3_bunny_small_hide_gC, screen)
            bunnies.level_3_small_scare_tracker(self,self.L3gD_SH_scare,self.level3_bunny_small_hide_gD, screen)
            bunnies.level_3_small_scare_tracker(self,self.L3gE_SH_scare,self.level3_bunny_small_hide_gE, screen)
            bunnies.level_3_small_scare_tracker(self,self.L3gF_SH_scare,self.level3_bunny_small_hide_gF, screen)


            bunnies.level_3_big_scare_tracker(self,self.L3gA_BH_scare,self.level3_bunny_big_hide_gA, screen)
            bunnies.level_3_big_scare_tracker(self,self.L3gB_BH_scare,self.level3_bunny_big_hide_gB, screen)
            bunnies.level_3_big_scare_tracker(self,self.L3gC_BH_scare,self.level3_bunny_big_hide_gC, screen)
            bunnies.level_3_big_scare_tracker(self,self.L3gD_BH_scare,self.level3_bunny_big_hide_gD, screen)
            bunnies.level_3_big_scare_tracker(self,self.L3gE_BH_scare,self.level3_bunny_big_hide_gE, screen)
            bunnies.level_3_big_scare_tracker(self,self.L3gF_BH_scare,self.level3_bunny_big_hide_gF, screen)
           
    def Level_2_kill_system(self,screen):
            bunnies.level_1_2_no_hide_scare_tracker(self,self.L2gA_NH_scare,self.level2_bunny_no_hide_gA, screen)
            bunnies.level_1_2_no_hide_scare_tracker(self,self.L2gB_NH_scare,self.level2_bunny_no_hide_gB, screen)
            bunnies.level_1_2_no_hide_scare_tracker(self,self.L2gC_NH_scare,self.level2_bunny_no_hide_gC, screen)

            bunnies.level_1_2_small_hide_scare_tracker(self,self.L2gA_SH_scare,self.level2_bunny_small_hide_gA, screen)
            bunnies.level_1_2_small_hide_scare_tracker(self,self.L2gB_SH_scare,self.level2_bunny_small_hide_gB, screen)
            bunnies.level_1_2_small_hide_scare_tracker(self,self.L2gC_SH_scare,self.level2_bunny_small_hide_gC, screen)

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
            if self.L1gA_scare==False:
                for bunny in self.level1_bunny_no_hide_gA:
                    bunnies.bunny_print_no_hide(screen,bunny)
            if self.L1gB_scare==False:
                for bunny in self.level1_bunny_no_hide_gB:
                    bunnies.bunny_print_no_hide(screen,bunny)
            if self.L1gC_scare==False:
                for bunny in self.level1_bunny_no_hide_gC:
                    bunnies.bunny_print_no_hide(screen,bunny)
                 
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
            #self.level3_bunny_no_hide=[bunny_1a,bunny_1f,bunny_2f,bunny_3c]
            #for bunny in self.level3_bunny_no_hide:
            #    bunnies.level3_bunny_print_no_hide(screen,bunny)
            
            self.level3_bunny_small_hide_gA=[bunny_3a]
            self.level3_bunny_small_hide_gB=[bunny_1b, bunny_2b]
            self.level3_bunny_small_hide_gC=[bunny_1c]
            self.level3_bunny_small_hide_gD=[bunny_2d]
            self.level3_bunny_small_hide_gE=[bunny_1e, bunny_3e]
            self.level3_bunny_small_hide_gF=[]

            #self.level3_bunny_small_hide=(bunny_1b),(bunny_1c),(bunny_1e),(bunny_2b),(bunny_2d),(bunny_3a),(bunny_3e)


           # for bunny in self.level3_bunny_small_hide:
           #     bunnies.level3_bunny_print_small_hide(screen,bunny)

            self.level3_bunny_big_hide_gA=[bunny_2a]
            self.level3_bunny_big_hide_gB=[bunny_3b]
            self.level3_bunny_big_hide_gC=[bunny_2c]
            self.level3_bunny_big_hide_gD=[bunny_1d,bunny_3d]
            self.level3_bunny_big_hide_gE=[bunny_2e]
            self.level3_bunny_big_hide_gF=[bunny_3f]



            bunnies.Level_3_kill_system(self,screen)

           # self.level3_bunny_big_hide=[bunny_1d,bunny_2a,bunny_2c,bunny_2e,bunny_3b,bunny_3d,bunny_3f]
          #  for bunny in self.level3_bunny_big_hide:
             #   bunnies.level3_bunny_print_big_hide(screen,bunny)
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

                #for bunny in self.level2_bunny_small_hide:
                   # bunnies.bunny_print_small_hide(screen,bunny)
            bunnies.Level_2_kill_system(self,screen)



def bunny_test(screen):
    background = pygame.image.load('test_bunny_square.png').convert_alpha()

    NameTag=screen.blit(background, ((534), (380)))

def move_right(cordinates,level):
    x_cordinate, y_cordinate=cordinates
    if level==0:
        if x_cordinate>=665:
            new_cordinates=cordinates
        else:
            new_cordinates=((x_cordinate +133), (y_cordinate))
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
    if level==0:
        if x_cordinate<=0:
            new_cordinates=cordinates
        else:
            new_cordinates=(x_cordinate -133), (y_cordinate)
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
    if dt<=20000:
        level=0
        #print ("level 1")
    elif (dt>=20001 and dt<=40000):
        level=1
       # print ("level 2")
    elif dt>=40001 and dt<=60000:
        level=2
        #print ("level 3")
    elif dt>=60001 and dt<=80000:
        level=3
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
    Supper_Bunny=bunnies()
   # Supper_Pupppy=supper_puppy(fix_dog)
    running = True
    fullscreen=False
    #Level=level_determine(dt)
    Level=3
    powerup=False
    powerups=3
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
                    Supper_Bunny.scare(fix_dog, Level, powerup)
                    print("SCARE")
                    #scare=True
                if event.key == pygame.K_DOWN:
                    if powerups>0:
                        powerup=True
                        powerups-=1
                        print("Powerup")
                    Supper_Bunny.scare(fix_dog, Level,powerup)
                    
                    #scare=True
            #elif event.type == pygame.
        #Level=level_determine(Time)
        if Level==1:   
            Supper_Pupppy=supper_puppy(fix_dog)

        elif Level==2:
            Supper_Pupppy=supper_puppy(fix_dog)
        elif Level==3:
            Supper_Pupppy=Level3_supper_puppy(fix_dog)
        else:
            Supper_Pupppy=Level3_supper_puppy(fix_dog)

        Supper_Pupppy.update(dt)

        BLACK = pygame.Color(0, 0, 0)
        screen.fill(BLACK)
       # bunnies.draw(screen)
        
        map(screen,Level)
        
        Supper_Bunny.level_system(Level,screen)
        if scare==True:
            Supper_Bunny.grass_overwrite(screen,fix_dog,Level)
        #scare=False
        powerup=False
        Supper_Pupppy.image(screen)
        Supper_Pupppy.draw(screen)
        #Supper_Bunny.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(12)
        
    pygame.quit()

if __name__ == "__main__":
    main()