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