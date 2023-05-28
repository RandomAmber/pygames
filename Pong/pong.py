import pygame
from pygame.locals import *

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

#define game variiables

class Ball():
    def __init__ (self, x, y, velocity, radius):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.radius = radius
        
# class Paddle():
#     def __init__(self, x, y, size, velocity):
#         self.x = x
#         self.y = y
#         self.size = size
#         self.velocity = velocity
    
    
#ball = Ball(screen_width // 2, screen_height // 2, [1, 1])
ball_radius = 10
ball_pos = [screen_width // 2, screen_height // 2]
ball_vel = [0.5, 0.5]  # Initial velocity of the ball

def ball_pos_update():
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #border collision:
    if ball_pos[1] <= ball_radius or ball_pos[1] >= screen_height - ball_radius:
        ball_vel[1] *= -1
    
    #paddle collision:
    if (
        ball_pos[0] <= paddle_pos1[0] + paddle_width and
        paddle_pos1[1] <= ball_pos[1] <= paddle_pos1[1] + paddle_height
    ):
        ball_vel[0] *= -1
    elif (
        ball_pos[0] >= paddle_pos2[0] - ball_radius and
        paddle_pos2[1] <= ball_pos[1] <= paddle_pos2[1] + paddle_height
    ):
        ball_vel[0] *= -1
        


paddle_width = 10
paddle_height = 80
paddle_pos1 = [10, screen_height // 2 - paddle_height // 2]  # Left paddle position
paddle_pos2 = [screen_width - paddle_width - 10, screen_height // 2 - paddle_height // 2]  # Right paddle position
paddle_vel = 2  # Paddle velocity for movement

#game state
game_over = False



run = True
while run:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #paddle positions
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_pos1[1] > 0:
        paddle_pos1[1] -= paddle_vel
    if keys[pygame.K_s] and paddle_pos1[1] < screen_height - paddle_height:
        paddle_pos1[1] += paddle_vel
    if keys[pygame.K_UP] and paddle_pos2[1] > 0:
        paddle_pos2[1] -= paddle_vel
    if keys[pygame.K_DOWN] and paddle_pos2[1] < screen_height - paddle_height:
        paddle_pos2[1] += paddle_vel
        
    
    ball_pos_update()
    
    screen.fill((0,0,0)) # Clear the screen
    
    #paddles:
    pygame.draw.rect(screen, (255, 255, 255), (paddle_pos1[0], paddle_pos1[1], paddle_width, paddle_height))  # Draw left paddle
    pygame.draw.rect(screen, (255, 255, 255), (paddle_pos2[0], paddle_pos2[1], paddle_width, paddle_height))  # Draw right paddle
    
    #ball:
    pygame.draw.circle(screen, (255, 255, 255), (ball_pos[0], ball_pos[1]), ball_radius)  # Draw ball
    
    #borders:
    border_thickness = 5
    pygame.draw.rect(screen, (255,255,255), (0,0, screen_width, border_thickness)) #top border
    pygame.draw.rect(screen, (255, 255, 255), (0, screen_height - border_thickness, screen_width, border_thickness))  #bottom border
    
    
   
    
    if ball_pos[0] <= 0 or ball_pos[0] >= screen_width:
        game_over = True
        
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255,255,255))
        text_rect = text.get_rect(center =(screen_width//2, screen_height//2))
        screen.blit(text, text_rect)
        pygame.display.flip() #update the display
        pygame.time.wait(2000)
        break
    
    pygame.display.flip()
    
pygame.quit()
    
    