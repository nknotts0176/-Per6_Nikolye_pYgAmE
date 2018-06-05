import pygame
import random

score = 0

#inputs for Window
Y_N_start = input("Begin game? Y/N ")
if Y_N_start == "Y":
        width_input = int(input("W? (Input must be above 599) "))
        height_input = int(input("H? (Input must be above 599) "))
else:
        quit
clock = pygame.time.Clock()

def Game_board(width_input, height_input):
        screen = pygame.display.set_mode((width_input, height_input))
        screen.fill((0, 50, 0))
        pygame.draw.aaline(screen, (225, 0, 0), (50, 50), (50, height_input - 50))
        pygame.draw.aaline(screen, (225, 0, 0), (50, 50), (width_input - 50, 50))
        pygame.draw.aaline(screen, (225, 0, 0), (width_input - 50, height_input - 50), (50, height_input - 50))
        pygame.draw.aaline(screen, (225, 0, 0), (width_input - 50, height_input - 50), (width_input - 50, 50))

def Game_Start(Y_N_start):
        if Y_N_start == "Y":
            screen = pygame.display.set_mode((width_input, height_input))
            print(Game_board(width_input, height_input))
            running = True
            while running:
                    x = random.randint(50, width_input - 50)
                    y = random.randint(50, height_input - 50)
                    screen.set_at((x, y), (0, 70, 225))

        # The Pixel design
                    food = [screen.set_at((x + 1, y), (0, 70, 225)),       #right
                    screen.set_at((x + 1, y + 1), (0, 70, 225)),   #top right
                    screen.set_at((x, y + 1), (0, 70, 225)),       #top
                    screen.set_at((x - 1, y + 1), (0, 70, 225)),   #top left
                    screen.set_at((x - 1, y), (0, 70, 225)),       #left
                    screen.set_at((x - 1, y - 1), (0, 70, 225)),   #bot left
                    screen.set_at((x, y - 1), (0, 70, 225)),       #bot
                    screen.set_at((x + 1, y - 1), (0, 70, 225)),   #bot right
                    screen.set_at((x + 2, y), (0, 70, 225)),       #right
                    screen.set_at((x + 2, y + 2), (0, 70, 225)),   #top right
                    screen.set_at((x, y + 2), (0, 70, 225)),       #top
                    screen.set_at((x - 2, y + 2), (0, 70, 225)),   #top left
                    screen.set_at((x - 2, y), (0, 70, 225)),       #left
                    screen.set_at((x - 2, y - 2), (0, 70, 225)),   #bot left
                    screen.set_at((x, y - 2), (0, 70, 225)),       #bot
                    screen.set_at((x + 2, y - 2), (0, 70, 225))]   #bot right

                    for event in pygame.event.get():    
                        if event.type == pygame.QUIT:
                            running = False
                            
                    snake_head = [screen.set_at((248, 248), (255, 0, 0)),
                                  screen.set_at((249, 248),(225, 0 , 0)),
                                  screen.set_at((250, 248), (255, 0, 0)),
                                  screen.set_at((251, 248), (255, 0, 0)),
                                  screen.set_at((252, 248),(225, 0 , 0)),
                            
                                  screen.set_at((248, 249), (255, 0, 0)),
                                  screen.set_at((249, 249),(225, 0 , 0)),
                                  screen.set_at((250, 249), (255, 0, 0)),
                                  screen.set_at((251, 249), (255, 0, 0)),
                                  screen.set_at((252, 249),(225, 0 , 0)), 

                                  screen.set_at((248, 250),(225, 0 , 0)),
                                  screen.set_at((249, 250), (255, 0, 0)),
                                  screen.set_at((250, 250), (255, 0, 0)),
                                  screen.set_at((251, 250), (255, 0, 0)),
                                  screen.set_at((252, 250), (255, 0, 0)),
                                  
                                  screen.set_at((248, 251),(225, 0 , 0)),
                                  screen.set_at((249, 251), (255, 0, 0)),
                                  screen.set_at((250, 251), (255, 0, 0)),
                                  screen.set_at((251, 251),(225, 0 , 0)),
                                  screen.set_at((252, 251), (255, 0, 0)),
                                  
                                  screen.set_at((248, 252), (255, 0, 0)),
                                  screen.set_at((249, 252),(225, 0 , 0)),
                                  screen.set_at((250, 252), (255, 0, 0)),
                                  screen.set_at((251, 252), (255, 0, 0)),
                                  screen.set_at((252, 252),(225, 0 , 0)),]
                    Snake = [snake_head]
                    if snake_head[0:] == food:
                            score += 1
                    #if snake_head[0] in snake_head[1:]:
                    #        break
                    
                    pygame.display.flip()
                    clock.tick(.2)





















print(Game_Start(Y_N_start))
