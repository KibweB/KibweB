import pygame, time, random
pygame.init()
snake_speed=30
window=pygame.display.set_mode((720, 480)) 
black=(0,0,0); red=(255, 0, 0); green=(0, 255, 0)
white=(255, 255, 255); gold=(255,215,0) 
pygame.display.set_caption("Snake in Python")
fPs=pygame.time.Clock(); snake_position=[100,50]

snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]

fruit_position = [random.randrange(3, (720//10)) * 10,
                  random.randrange(3, (480//10)) * 10]
fruit_spawn = True
direction='RIGHT'; change_to=direction; score=0

def show_score(choice,color,font,size):
    score_font=pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()#creates rectangle for text surface
    window.blit(score_surface, score_rect)#this  will display text
def game_Over():
    my_font=pygame.font.SysFont('biome',50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(1); pygame.quit(); quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change_to = 'UP'
            if event.key == pygame.K_s:
                change_to = 'DOWN'
            if event.key == pygame.K_a:
                change_to = 'LEFT'
            if event.key == pygame.K_d:
                change_to = 'RIGHT'
        #prevents snake from moving in 2 directions simultameously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        if direction == 'UP':#Snake controlas 
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10  
        #code for grwoing the snake,increase score by 10 once snake collides w/fruit
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (720//10)) * 10, 
            random.randrange(1, (480//10)) * 10]
        fruit_spawn = True
        window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(window, gold, pygame.Rect(pos[0], pos[1], 10, 10)) 
        pygame.draw.rect(window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))
        #conditions for ending the game
        if snake_position[0] < 0 or snake_position[0] > 720-10:
            game_Over()
        if snake_position[1] < 0 or snake_position[1] > 480-10:
            game_Over()
        
        #What'll happen when the snake body is touched
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_Over

        #continue to display score throughout the game
        show_score(1, white, 'jumble', 45)
        #refresh the game screen & FPS/ refresh rate
        pygame.display.update(); fPs.tick(snake_speed)


