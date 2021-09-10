import pygame

pygame.init() #pygame을 호출하면 반드시 초기화를 해주어야 한다.

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/82107/Desktop/pythonworkspace/pygame_basic/background.png")

# 이벤트 루프 : 이벤트가 들어오는 지 check, 들어오면 그에 맞는 동장을 행하는 것

running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아니다
    
    screen.blit(background,(0, 0)) #배경 그리기

    #screen.fill((0,0,255))를 통해서 이미지를 불러오는 것이 아닌, 색깔만 불러오는 것도 가능하다.
    
    pygame.display.update() # 게임 화면을 다시 그리기! 반드시 계속 호출되어야 한다. 

# pygame 종료
pygame.quit()