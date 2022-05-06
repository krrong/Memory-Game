import pygame

# 초기화
pygame.init()
screen_width = 1280 # 가로 크기
screen_height = 720 # 가로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
# 

# 게임 루프
running = True # 게임이 실행중인지 체크하는 변수
while running:
    # 이벤트 루프 : 사용자의 동작 확인
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가를 확인
        if event.type == pygame.QUIT: # 창을 닫히는 이벤트인가?
            running = False # 게임이 더 이상 실행중이 아님을 체크
            
# 게임 종료
pygame.quit()