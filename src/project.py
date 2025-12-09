import random
import pygame



 
def pause_screen(screen):
    background = pygame.image.load('pause_screen.png').convert_alpha()
    screen.blit(background, ((0), (0)))

def reset_screen(screen):
    background = pygame.image.load('reset_screen.png').convert_alpha()
    screen.blit(background, ((0), (0)))

def map(screen, level, win, scroll):
    
        if level==0:
            background = pygame.image.load('introduction_to_supper_puppy.png').convert_alpha()
            screen.blit(background, ((0), (0)))
            #print("level 0 map")
        elif level>=1 and level<=3:
            background = pygame.image.load('big_scrollinngmap.png').convert_alpha()
            screen.blit(background, ((0),(scroll)))
        elif level==4:
            if win==True: 
                background = pygame.image.load('you_win.png').convert_alpha()
                screen.blit(background, ((0), (0)))
            elif win==False:
                background = pygame.image.load('you_lost.png').convert_alpha()
                screen.blit(background, ((0), (0)))

def Print_count_down(Count_down, screen):
        pygame.font.init()
        Title = pygame.font.SysFont('opensans', 75) 
        last_secs = pygame.font.SysFont('opensans', 100)
        if Count_down>3:
            count_down_surface = Title.render(f' {Count_down}', True, (59, 59, 59))
            screen.blit(count_down_surface, (630, 20))
        else:
            count_down_surface = last_secs.render(f' {Count_down}', True, (140, 25, 10)) 
            screen.blit(count_down_surface, (620, 15))        
            
def Print_gui(NH,SH,BH, screen, powerups):
        pygame.font.init()
        Title = pygame.font.SysFont('Arial', 25) 
        font = pygame.font.SysFont('Arial', 18)
        no_hide_surface = font.render(f'light bunnies: {NH}', True, (0, 0, 0)) 
        screen.blit(no_hide_surface, (10, 50)) 


        small_hide_surface = font.render(f'orange bunnies: {SH}', True, (0, 0, 0)) 
        screen.blit(small_hide_surface, (10, 75)) 


        big_hide_surface = font.render(f'yellow bunnies: {BH}', True, (0, 0, 0)) 
        screen.blit(big_hide_surface, (10, 100)) 

        Total_bunnies_scared=NH+SH+BH
        total_bunnies_text_surface = font.render(f'Total bunnies: {Total_bunnies_scared}', True, (0, 0, 0)) 
        screen.blit(total_bunnies_text_surface, (10, 125)) 

        total_bunnies_text_surface = Title.render(f'Bunnies scared', True, (0, 0, 0)) 
        screen.blit(total_bunnies_text_surface, (10, 5))

        powerups_surface = font.render(f'POWERUPS', True, (0, 0, 0))
        screen.blit(powerups_surface, (170, 40))

        Powerups_left_text_surface = Title.render(f' {powerups}', True, (0, 0, 0)) 
        screen.blit(Powerups_left_text_surface, (200, 55)) 

        powerups_surface = font.render(f'bunnies left till win', True, (0, 0, 0))
        screen.blit(powerups_surface, (170, 100))

        left_till_win_condition=28-Total_bunnies_scared
        Powerups_left_text_surface = Title.render(f' {left_till_win_condition}', True, (0, 0, 0)) 
        screen.blit(Powerups_left_text_surface, (210, 115)) 

class bunnies():
    def __init__(self):
        #these are the counter for the bunnies scared off
        #from level 1 to 3 tallies are added as each bunny is scared
        #Level 4 or the win/lose level adds the counters together to get the total bunnny count
        self.no_hide_bunny_count=0
        self.small_hide_bunny_count=0
        self.big_hide_bunny_count=0
        self.Total_bunny_count=0
               

               # theses lists store the bunnies and their location 
               # in total there are 3 differnt types of bunnies 
               # these lists are organized by level, bunny type, and group (groups are another name for columns as it is easier to remeber for me)
               # level1_bunny_no_hide_gA   =    Level:1   bunny type:no hide    group/column:A            
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

        # numbers indicate the amount of bunnies per group in level 3
        #
        # each of these groups indicate the amount of times that specfic row has been scared
        #      Level 3 group A no hide scare amount   =    L3gA_NH_scare=0 
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
  
    def win_condition(self):
        """
        calculates the final total bunny count
        checks if it is at least 28
            if at least 28 the win condition is met 
            if less than 28 the win condition is not met
        returns the win condition, which will detirmine the level 4 win/lose screen
        
        
        :param self: bunnies self
        """

        self.Total_bunny_count=(self.no_hide_bunny_count)+(self.small_hide_bunny_count)+(self.big_hide_bunny_count)

        if self.Total_bunny_count<=28:
              win=False
        elif self.Total_bunny_count>=28:
             win=True
        else:
             win=False
        return win

    def bunny_print_no_hide(screen, bunny):
        """
    
        :param screen: surface to blit onto 
        :param bunny: location of individual bunny from list
        """
        background = pygame.image.load('Bunny_no_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def bunny_print_small_hide(screen, bunny):
        """
        :param screen: surface to blit onto 
        :param bunny: location of individual bunny from list
        """
        background = pygame.image.load('Bunny_small_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))
    
    def level3_bunny_print_no_hide(screen, bunny):
        """
        
        
        :param screen: surface to blit onto 
        :param bunny: location of individual bunny from list
        """
        background = pygame.image.load('level3_Bunny_no_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def level3_bunny_print_small_hide(screen, bunny):
        """
        Docstring for level3_bunny_print_small_hide
        
        :param screen: surface to blit onto 
        :param bunny: location of individual bunny from list
        """
        background = pygame.image.load('level3_Bunny_small_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def level3_bunny_print_big_hide(screen, bunny):
        """
        Docstring for level3_bunny_print_big_hide
        
        :param screen: surface to blit onto 
        :param bunny: location of individual bunny from list
        """
        background = pygame.image.load('level3_Bunny_big_hide.png').convert_alpha()

        NameTag=screen.blit(background, (bunny))

    def scare_level_1(self, powerup, cordinates_dog, level):
        """
        Docstring for scare_level_1
        scare counter for level 1
        splits the cordinate of super puppy to determine if any bunnys share the same x_cordinates 
            if same x_cordinates the scare counter for that row increases
            if the max scare per type of bunny in row is reached 
                amount of type of bunnies in that row is added to counter

        :param self: bunnies self
        :param powerup: boolean determines how much bunny scare goes up
        :param cordinates_dog: location of super dog at moment of scare
        :param level: Description
        """
        x_cordinate,y_cordinate=cordinates_dog
        if level==1:
            if x_cordinate==0:
                self.L1gA_scare+=1
                if self.L1gA_scare==1:
                        self.no_hide_bunny_count+=2
            elif x_cordinate==266:
                self.L1gB_scare+=1
                if self.L1gB_scare==1:
                        self.no_hide_bunny_count+=2
            elif x_cordinate==532:
                self.L1gC_scare+=1
                if self.L1gC_scare==1:
                        self.no_hide_bunny_count+=3




    def scare_level_2(self, powerup, cordinates_dog, level):
        x_cordinate,y_cordinate=cordinates_dog
        if level==2:
            if x_cordinate==0:
                self.L2gA_NH_scare+=1
                if powerup==True:
                    self.L2gA_SH_scare+=2
                else:
                    if self.L2gA_SH_scare<3:
                        self.L2gA_SH_scare+=1
                if self.L2gA_NH_scare==1:
                        self.no_hide_bunny_count+=1
                if self.L2gA_SH_scare==2:
                            self.small_hide_bunny_count+=2

            elif x_cordinate==266:
                self.L2gB_NH_scare+=1
                if powerup==True:
                    self.L2gB_SH_scare+=2
                else:
                    if self.L2gB_SH_scare<3:
                        self.L2gB_SH_scare+=1   
                if self.L2gB_NH_scare==1:
                        self.no_hide_bunny_count+=1
                if self.L2gB_SH_scare==2:
                            self.small_hide_bunny_count+=2

            elif x_cordinate==532:
                self.L2gC_NH_scare+=1
                if powerup==True:
                    self.L2gC_SH_scare+=2
                else:
                    if self.L2gC_SH_scare<3:
                        self.L2gC_SH_scare+=1   
                if self.L2gC_NH_scare==1:
                        self.no_hide_bunny_count+=1
                if self.L2gC_SH_scare==2:
                            self.small_hide_bunny_count+=2

    def scare_level_3(self, powerup, cordinates_dog, level):
            x_cordinate,y_cordinate=cordinates_dog

            if x_cordinate==0:
                bunny=bunnies()
                self.L3gA_NH_scare+=1
                if powerup==True:
                    self.L3gA_SH_scare+=2
                    self.L3gA_BH_scare+=3
                else:
                    if self.L3gA_SH_scare<3:
                        self.L3gA_SH_scare+=1
                    if self.L3gA_BH_scare<4:
                        self.L3gA_BH_scare+=1
                if self.L3gA_NH_scare==1:
                        self.no_hide_bunny_count+=1
                if self.L3gA_SH_scare==2:
                            self.small_hide_bunny_count+=1
                if self.L3gA_BH_scare==3:
                            self.big_hide_bunny_count+=1
            elif x_cordinate==133:
                if powerup==True:
                    self.L3gB_SH_scare+=2
                    self.L3gB_BH_scare+=3
                else:
                    if self.L3gB_SH_scare<3:
                        self.L3gB_SH_scare+=1
                    if self.L3gB_BH_scare<4:
                        self.L3gB_BH_scare+=1
                if self.L3gB_NH_scare==1:
                        self.no_hide_bunny_count+=1
                if self.L3gB_SH_scare==2:
                            self.small_hide_bunny_count+=2
                if self.L3gB_BH_scare==3:
                            self.big_hide_bunny_count+=1
            elif x_cordinate==266:

                self.L3gC_NH_scare+=1
                if powerup==True:
                    self.L3gC_SH_scare+=2
                    self.L3gC_BH_scare+=3
                else:
                    if self.L3gC_SH_scare<3:
                        self.L3gC_SH_scare+=1
                    if self.L3gC_BH_scare<4:
                        self.L3gC_BH_scare+=1
                if self.L3gC_NH_scare==1:
                        self.no_hide_bunny_count+=1
                if self.L3gC_SH_scare==2:
                            self.small_hide_bunny_count+=1
                if self.L3gC_BH_scare==3:
                            self.big_hide_bunny_count+=1
            elif x_cordinate==399:

                if powerup==True:
                    self.L3gD_SH_scare+=2
                    self.L3gD_BH_scare+=3
                else:
                    if self.L3gD_SH_scare<3:
                        self.L3gD_SH_scare+=1
                    if self.L3gD_BH_scare<4:
                        self.L3gD_BH_scare+=1
                if self.L3gD_NH_scare==1:
                        self.no_hide_bunny_count+=1
                if self.L3gD_SH_scare==2:
                            self.small_hide_bunny_count+=1
                if self.L3gD_BH_scare==3:
                            self.big_hide_bunny_count+=2

            elif x_cordinate==532:
                if powerup==True:
                    self.L3gE_SH_scare+=2
                    self.L3gE_BH_scare+=3
                else:
                    if self.L3gE_SH_scare<3:
                        self.L3gE_SH_scare+=1
                    if self.L3gE_BH_scare<4:
                        self.L3gE_BH_scare+=1
                if self.L3gE_NH_scare==1:
                        self.no_hide_bunny_count+=1
                if self.L3gE_SH_scare==2:
                            self.small_hide_bunny_count+=2
                if self.L3gE_BH_scare==3:
                            self.big_hide_bunny_count+=1
            elif x_cordinate==665:
                self.L3gF_NH_scare+=1
                if powerup==True:
                    self.L3gF_BH_scare+=3
                else:
                    if self.L3gF_BH_scare<4:
                        self.L3gF_BH_scare+=1
                if self.L3gF_NH_scare==1:
                        self.no_hide_bunny_count+=2
                if self.L3gF_SH_scare==2:
                            self.small_hide_bunny_count+=1
                if self.L3gF_BH_scare==3:
                            self.big_hide_bunny_count+=1
            else:
                print("level 3 group not detected")
            
        
    def scare(self, cordinates_dog, level, powerup, screen):
        x_cordinate,y_cordinate=cordinates_dog
        if level==1:
            bunnies.scare_level_1(self, powerup, cordinates_dog, level)
        if level==2:
            bunnies.scare_level_2(self, powerup, cordinates_dog, level)
        if level==3:
            bunnies.scare_level_3(self, powerup, cordinates_dog, level)
        
    def level_3_small_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
        if scare_level_tracker==0:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_small_hide(screen,bunny)
        elif scare_level_tracker==1:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_small_hide(screen,bunny)

    def level_3_big_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
        
            if scare_level_tracker==0:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_big_hide(screen,bunny)
            elif scare_level_tracker==1:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_big_hide(screen,bunny)
            elif scare_level_tracker==2:
                for bunny in hide_type_group:
                    bunnies.level3_bunny_print_big_hide(screen,bunny)

    def level_1_2_no_hide_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
        if scare_level_tracker==False:
                for bunny in hide_type_group:
                    bunnies.bunny_print_no_hide(screen,bunny)

    def level_1_2_small_hide_scare_tracker(self,scare_level_tracker,hide_type_group, screen):
            if scare_level_tracker==0:
                for bunny in hide_type_group:
                    bunnies.bunny_print_small_hide(screen,bunny)
            elif scare_level_tracker==1:
                for bunny in hide_type_group:
                    bunnies.bunny_print_small_hide(screen,bunny)

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

    def Restart_Bunnies(self):
            """
            Resets all intial values of the __init__ as they were at game start
            allows 
                bunny respon after being killed in prievious play thorugh
                emptys lists that stored those bunnies           
            """
         
            self.no_hide_bunny_count=0
            self.small_hide_bunny_count=0
            self.big_hide_bunny_count=0
            self.Total_bunny_count=0





            self.L1gA_scare=False
            self.L1gB_scare=False
            self.L1gC_scare=False

            self.L2gA_NH_scare=0
            self.L2gB_NH_scare=0
            self.L2gC_NH_scare=0

            self.L2gA_SH_scare=0
            self.L2gB_SH_scare=0
            self.L2gC_SH_scare=0

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
                    

    def level_system(self,level,screen, time, powerups):
        level_count_down=level_timer(time, level)
        
        if level>0 and level<4:
            Print_gui(self.no_hide_bunny_count,self.small_hide_bunny_count,self.big_hide_bunny_count, screen,powerups)
        if level<4:
            Print_count_down(level_count_down, screen)

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
            bunnies.Level_3_kill_system(self,screen)

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
            bunnies.Level_2_kill_system(self,screen)
       



def move_right(cordinates,level):
    x_cordinate, y_cordinate=cordinates
    if level==0:
        if x_cordinate>=532:
            new_cordinates=cordinates
        else:
            new_cordinates=((x_cordinate +266), (y_cordinate))
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
        new_cordinates=(534),(490)


    result=new_cordinates
   
    return result

def move_left(cordinates,level):
    x_cordinate, y_cordinate=cordinates
    if level==0:
        if x_cordinate<=0:
            new_cordinates=cordinates
        else:
            new_cordinates=(x_cordinate -266), (y_cordinate)
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
        new_cordinates=(534),(490)

    result=new_cordinates
   
    return result

class supper_puppy():

    def __init__(self, position=(266, 490), size=30, life=1000):
        self.size = size
        self.location=position
        self.age = 0 
        self.life = life 
        self.dead = False
        self.alpha = 255
        self.surface = self.update_surface()

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
        self.age = 0 
        self.life = life 
        self.dead = False
        self.alpha = 255
        self.surface = self.update_surface()
      
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

def level_determine(pause,dt):
    if pause==False:
        if dt<=10000:
            level=0

        elif (dt>=10001 and dt<=15000):
            level=1
        elif dt>=15001 and dt<=25000:
            level=2
        elif dt>=25001 and dt<=30000:
            level=3
        elif dt>=30001:
            level=4

        else:
            level=4
            print("level error")
    return level

def scroll_determine(dt):

        if dt<=10000:
            scroll=(0)         
        elif (dt>=10001 and dt<=15000):
            scroll=(-1200)
        elif dt>=15001 and dt<=25000:
            if (dt>=15001 and dt<=15100):
                 scroll=(-1200)
            elif (dt>=15101 and dt<=15200):
                 scroll=(-1100)
            elif (dt>=15201 and dt<=15300):
                 scroll=(-1000) 
            elif (dt>=15301 and dt<=15400): 
                 scroll=(-900)
            elif (dt>=15401 and dt<=15500): 
                 scroll=(-600)
            
            if (dt>=15501 and dt<=24200):
                 scroll=(-600)

            elif (dt>=24201 and dt<=24300):
                 scroll=(-600)
            elif (dt>=24301 and dt<=24400):
                 scroll=(-500)
            elif (dt>=24401 and dt<=24500):
                 scroll=(-400) 
            elif (dt>=24501 and dt<=24600): 
                 scroll=(-300)
            elif (dt>=24601 and dt<=24700): 
                 scroll=(-200)
            elif (dt>=24701 and dt<=24800):
                 scroll=(-100)
            elif (dt>=24801 and dt<=24900):
                 scroll=(0)
            elif (dt>=24901 and dt<=25000):
                 scroll=(0)
        elif dt>=25001 and dt<=30000:
            scroll=(0)
        else:
            scroll=(0,0)
        return scroll

def level_timer(time, level):
    sec=time//1000
    if level==1:
        time_in_level=sec-10
        time_left_in_level=5-time_in_level
    elif level==2:
         time_in_level=sec-15
         time_left_in_level=10-time_in_level
    elif level==3:
         time_in_level=sec-25
         time_left_in_level=5-time_in_level
    elif level==0:
        time_in_level=sec
        time_left_in_level=10-time_in_level
    else:
         time_left_in_level=0

    result=time_left_in_level
    return result
  
def supper_puppy_class_determiner(Level, fix_dog):
        if Level==1:   
            Supper_Pupppy=supper_puppy(fix_dog)
        elif Level==2:
            Supper_Pupppy=supper_puppy(fix_dog)
        elif Level==3:
            Supper_Pupppy=Level3_supper_puppy(fix_dog)
        elif Level==4:
            Supper_Pupppy=supper_puppy(fix_dog)
        else:
            Supper_Pupppy=supper_puppy(fix_dog)
        return Supper_Pupppy

def main():
    pygame.init()
    pygame.display.set_caption("Supper Puppy")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    fix_dog = (266, 490)
    Supper_Bunny=bunnies()
    Pause=False
    running = True
    Level=level_determine(Pause, dt)
    powerups=3
    powerup=False
    start_time = 0
    win=False
    Pause_time=0
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
                    Supper_Bunny.scare(fix_dog, Level, powerup, screen)
                if event.key == pygame.K_DOWN:
                    if powerups>0:
                        powerup=True
                        powerups-=1
                        Supper_Bunny.scare(fix_dog, Level,powerup, screen)
                if event.key == pygame.K_p:
                    pause_screen(screen)
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    Pause_time+=3000
                if event.key == pygame.K_r:
                    reset_screen(screen)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    start_time = pygame.time.get_ticks()
                    Supper_Bunny.Restart_Bunnies()
                    powerups=3
                if event.key == pygame.K_q:
                    running = False  
        current_time=pygame.time.get_ticks()
        elapsed_milliseconds = current_time - (start_time+ Pause_time)
        Level=level_determine(Pause, elapsed_milliseconds)
        if Level==4:
            win=Supper_Bunny.win_condition()
        Supper_Pupppy=supper_puppy_class_determiner(Level, fix_dog)
        Supper_Pupppy.update(dt)
        BLACK = pygame.Color(87, 109, 97)
        screen.fill(BLACK)
        scroll=scroll_determine(elapsed_milliseconds)
        map(screen,Level, win,scroll)       
        Supper_Bunny.level_system(Level,screen, elapsed_milliseconds, powerups)
        powerup=False
        Supper_Pupppy.draw(screen)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
    main()