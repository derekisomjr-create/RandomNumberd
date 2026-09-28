import random
import keyboard
import time
import pygame


                                  

Running = True
Game = True

while Running:
    if keyboard.is_pressed("space"):
        RandomNumber = random.randint(12, 42,)
        print()
        # (12, 42)
        x = f"you got this number: {RandomNumber}!"
        
        print(x)
        while keyboard.is_pressed("space"):
            time.sleep(0.01)
        break
            
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()            
            
font = pygame.font.Font(None, 36)

text_surface = font.render(x, True, (255, 255, 255))  
    
text_rect = text_surface.get_rect(center=(200, 150))
            
            
while Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
    
    screen.fill((0, 0, 0)) # Clear screen
    
    screen.blit(text_surface, text_rect) # Draw text
    
    


pygame.quit()
            


            