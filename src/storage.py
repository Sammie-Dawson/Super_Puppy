                if event.key == pygame.K_UP:
                    bunnies.scare(fix_dog, Level,screen)
                    print("scare")    



    def scare(cordinates,level,screen):
        bunny_counter=0
        if level==1:
            x_cordinate, y_cordinate=cordinates
            bunny_row_4a=(0),(490)
            bunny_row_4b=(266),(490)
            bunny_row_4c=(534),(490)
            if x_cordinate==0:
                bunnies.map_piece_row1_12(level,x_cordinate,screen)
                bunny_counter=bunny_counter+2
            elif x_cordinate==266:
                bunnies.map_piece_row1_12(level,x_cordinate,screen)
                bunny_counter=bunny_counter+2
            elif x_cordinate==534:
                bunnies.map_piece_row1_12(level,x_cordinate,screen)
                bunny_counter=bunny_counter+3
        if level==2:
            x_cordinate, y_cordinate=cordinates
            row1=0
            row2=0
            row3=0
            bunny_row_4a=(0),(490)
            bunny_row_4b=(266),(490)
            bunny_row_4c=(534),(490)
            if x_cordinate==0:
                if row1==0: #and power up == false
                    row1=row1+1
                    bunny_counter=bunny_counter+1
                elif row1==1:
                    row1=row1+1
                    bunny_counter=bunny_counter+4
                else:
                    bunny_counter=bunny_counter

                bunnies.map_piece_row1_12(level,x_cordinate,screen)
                
            elif x_cordinate==266 and row2<2:
                if row2==0: #and power up == false
                    row2=row2+1
                    bunny_counter=bunny_counter+1
                elif row2==1:
                    row2=row2+1
                    bunny_counter=bunny_counter+4
                else:
                    bunny_counter=bunny_counter

                bunnies.map_piece_row1_12(level,x_cordinate,screen)

            elif x_cordinate==534 and row3<2:
                if row3==0: #and power up == false
                    row3=row3+1
                    bunny_counter=bunny_counter+1
                elif row3==1:
                    row3=row3+1
                    bunny_counter=bunny_counter+4
                else:
                    bunny_counter=bunny_counter
                bunnies.map_piece_row1_12(level,x_cordinate,screen)







    def map_piece_row1_12(level,x_cordinate,screen):
        while level==1: 
            if x_cordinate==0:
                background = pygame.image.load('grass.png').convert_alpha()
                screen.blit(background, (0,0))
            elif x_cordinate==266:
                background = pygame.image.load('grass.png').convert_alpha()
                screen.blit(background, (266,0))
            elif x_cordinate==534:
                background = pygame.image.load('grass.png').convert_alpha()
                screen.blit(background, (534,0))


       # if level==3:
        #    if x_cordinate==0:
       #     open image level 2 collom1

        #    if x_cordinate==133:
        #    open image level 2 collom 2

        #    if x_cordinate==266:
          #  open image level 2 collom 3
     
          #  if x_cordinate==399:
           # open image level 2 collom 4

           # if x_cordinate==534:
            #open image level 2 collom 5
#
           # if x_cordinate==665:
           # open image level 2 collom 6
