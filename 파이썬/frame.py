import pygame

#####################기본 초기화#########################################
pygame.init() 

#화면 크기
screen_width=626
screen_height=383
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀
pygame.display.set_caption("Pang")

#FPS
clock = pygame.time.Clock()

#####################사용자 게임화면 초기화#########################################

#배경 이미지
background=pygame.image.load("C:/Users/pixels-007/Desktop/준표/파이썬/background.jpg")
# 플레이어 이미지
character=pygame.image.load("C:/Users/pixels-007/Desktop/준표/파이썬/character.png")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-character_width/2
character_y_pos = screen_height - character_height

#이동할 좌표
character_to_x_LEFT=0
character_to_x_RIGHT=0
to_y=0
character_speed=0.5

#악당 이미지
enemy=pygame.image.load("C:/Users/pixels-007/Desktop/준표/파이썬/enemy.png")
enemy_size=enemy.get_rect().size
enemy_width=enemy_size[0]
enemy_height=enemy_size[1]
enemy_x_pos=screen_width/2-enemy_width/2
enemy_y_pos = 20

#폰트
game_font=pygame.font.Font(None,40)

total_time=10
start_ticks=pygame.time.get_ticks()

#이벤트
running=True
while running:
    dt=clock.tick(50)
    print("fps = "+str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #창이 닫히는 이벤트
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x_LEFT-=character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT+=character_speed
            elif event.key == pygame.K_UP:
                to_y-=character_speed
            elif event.key == pygame.K_DOWN:
                to_y+=character_speed
        
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: # 이 부분은 모두 다 바뀜
                character_to_x_LEFT = 0
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y=0

    character_x_pos+=(character_to_x_LEFT + character_to_x_RIGHT)*dt
    character_y_pos+=to_y*dt

    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width

    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height

    #충돌처리
    character_rect=character.get_rect() 
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect=enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running=False

    #r그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    #경과시간을 1000으로 나눠 초단위로 표시
    elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000

    timer = game_font.render(str(int(total_time-elapsed_time)),True,(255,255,255))
    screen.blit(timer,(10,10))
    #시간이 0이하라면 게임 종료
    if total_time-elapsed_time<=0:
        print("타임아웃")
        running = False
    pygame.display.update()

pygame.time.delay(2000)
#ptgame 종료
pygame.quit()
