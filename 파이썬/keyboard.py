import pygame

pygame.init() #초기화

#화면 크기
screen_width=626
screen_height=383
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀
pygame.display.set_caption("Pang")

#배경 이미지
background=pygame.image.load("C:/Users/pixels-007/Desktop/준표/파이썬/background.jpg")
character=pygame.image.load("C:/Users/pixels-007/Desktop/준표/파이썬/character.png")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-character_width/2
character_y_pos = screen_height - character_height

#이동할 좌표
to_x=0
to_y=0

#이벤트
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #창이 닫히는 이벤트
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x-=5
            elif event.key == pygame.K_RIGHT:
                to_x+=5
            elif event.key == pygame.K_UP:
                to_y-=5
            elif event.key == pygame.K_DOWN:
                to_y+=5
        
        
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y=0

    character_x_pos+=to_x
    character_y_pos+=to_y

    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width

    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()

#ptgame 종료
pygame.quit()
