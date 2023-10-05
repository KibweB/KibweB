
import pygame 
pygame.init() 
screen = pygame.display.set_mode((960, 600)) 
pygame.display.set_caption('Drawing with changeable cursor') 
clock = pygame.time.Clock() 

OGcursor=pygame.cursors.diamond
cursor2=pygame.SYSTEM_CURSOR_CROSSHAIR
surf = pygame.Surface((30, 25), pygame.SRCALPHA) 
pygame.draw.rect(surf, (253,143,143), [0, 0, 10, 10]) 
pygame.draw.rect(surf, (253,143,143), [20, 0, 10, 10]) 
pygame.draw.rect(surf, (89,186,251), [5, 5, 20, 20]) 
cursor3 = pygame.cursors.Cursor((15, 5), surf) 

cursors = [OGcursor, cursor2, cursor3] 
cursor_index = 0

loop = True
while loop: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cursor_index += 1
            cursor_index %= len(cursors) 
            pygame.mouse.set_cursor(cursors[cursor_index]) 
        elif event.type==pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    pos = pygame.mouse.get_pos() 
    pygame.draw.circle(screen, (233,105,44),pos, 15, 1) 
    pygame.display.update() 
    pygame.display.flip()
    clock.tick(60) 

pygame.quit() 