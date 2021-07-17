import pygame

'''gvahim_python_book.pdf Line 154'''
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
WHITE = (255,255,255)
RED = (255,0,0)
PINK = (255, 174, 201)
REFRESH_RATE = 60
RADIUS = 8

LEFT = 1
SCROLL = 2
RIGHT = 3
#int screen
pygame.init()
#line 166
pygame.mouse.set_visible(False)#/we are using a new icon for curser
print(pygame)
size = (WINDOW_WIDTH,WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
IMAGE = 'devl.jpg'


#fills screen and show
screen.fill(WHITE)#Fill with white
img = pygame.image.load(IMAGE)
player_image = pygame.image.load('plane.png').convert()
player_image.set_colorkey(PINK)#ignore the pink background


mouse_pos_list = []
ball_x_pos = 1
ball_y_pos = 1
#line 159
finish = False
clock =  pygame.time.Clock()#line 161

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                  mouse_pos_list.append(pygame.mouse.get_pos())
                  print pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
                  if pygame.key == pygame.K_q:
                      finish = True
    ball_x_pos += 1
    ball_y_pos += 1
    screen.fill(WHITE)
    screen.blit(img, (200, 90))
    pygame.draw.line(screen, RED, [10, 100], [100, 500], 3)
    pygame.draw.circle(screen, RED,[ball_x_pos,ball_y_pos],RADIUS)
    #screen.blit(player_image, [ball_x_pos+12,ball_y_pos])
    mouse_point = pygame.mouse.get_pos()
    screen.blit(player_image, mouse_point)

    clock.tick(REFRESH_RATE)
    pygame.display.flip()  # Flip data in video memory with object data


pygame.quit()
