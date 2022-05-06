import pygame

# 시작 화면 보여주는 함수
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 원을 그리고, 중심 좌표는 start_button의 중심좌표 사용
    # 반지름은 60, 두께는 5

# 초기화
pygame.init()
screen_width = 1280 # 가로 크기
screen_height = 720 # 가로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)          # 사각형의 크기가 120x120
start_button.center = (120, screen_height - 120)    # 사각형 중심좌표 설정

# 색상
BLACK = (0, 0, 0) # RGC
WHITE = (255, 255, 255)

# 게임 루프
running = True  # 게임이 실행중인지 체크
while running:
    # 이벤트 루프 : 사용자의 동작 확인
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가를 확인
        if event.type == pygame.QUIT: # 창을 닫히는 이벤트인가?
            running = False # 게임이 더 이상 실행중이 아님을 체크
            
    # 화면을 검정색으로 설정
    screen.fill(BLACK)
            
    # 시작 화면 구성
    display_start_screen()
    
    # 화면 업데이트
    pygame.display.update()
    
# 게임 종료
pygame.quit()