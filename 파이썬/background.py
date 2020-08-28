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
#이벤트
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #창이 닫히는 이벤트
            running=False

    screen.blit(background,(0,0))
    pygame.display.update()

#ptgame 종료
pygame.quit()
