import pygame
import os
#####################기본 초기화#########################################
pygame.init() 

#화면 크기
screen_width=640
screen_height=480
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀
pygame.display.set_caption("Pang")

#FPS
clock = pygame.time.Clock()

#####################사용자 게임화면 초기화#########################################

current_path=os.path.dirname(__file__)
image_path=os.path.join(current_path,"images")

#배경
background=pygame.image.load(os.path.join(image_path,"background.png"))
#스테이지
stage=pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size=stage.get_rect().size
stage_height=stage_size[1]

#캐릭터
character=pygame.image.load(os.path.join(image_path,"character.png"))
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=(screen_width/2)-(character_width/2)
character_y_pos = screen_height - character_height-stage_height

#이벤트
running=True
while running:
    dt=clock.tick(50)
    print("fps = "+str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #창이 닫히는 이벤트
            running=False
    #r그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()

#ptgame 종료
pygame.quit()
