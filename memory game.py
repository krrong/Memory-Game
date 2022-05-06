from asyncio import format_helpers
import pygame
from random import *

# 레벨에 맞게 설정
def setup(level):
    # 얼마나 많은 숫자를 보여줄 것인가?
    number_cnt = (level // 3) + 5
    number_cnt = min(number_cnt, 20)
    
    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_cnt)
    
# 숫자 섞기
def shuffle_grid(number_cnt):
    rows = 5
    columns = 9
    
    cell_size = 130             # 각 grid cell의 가로, 세로 크기
    button_size = 110           # grid cell내에 실제로 그려질 버튼의 크기
    screen_left_margin = 50     # 전체 스크린 왼쪽 여백
    screen_top_margin = 20      # 전체 스크린 위쪽 여백
    
    # 5 x 9 grid(list) 생성
    grid = [[0 for column in range(columns)] for row in range(rows)]
    
    # 시작 숫자
    number = 1
    while number <= number_cnt:
        row_index = randrange(0, rows) # 0 <= row_index < rows (0~4)
        col_index = randrange(0, columns) # 0 <= col_index < columns (0~8)
        
        # 빈 값이면 값을 넣어주고 number 증가
        if grid[row_index][col_index] == 0:
            grid[row_index][col_index] = number
            number = number + 1
            
            # 현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + (col_index * cell_size) + cell_size // 2
            center_y = screen_top_margin + (row_index * cell_size) + cell_size // 2
            
            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)
            
            number_buttons.append(button)


# 시작 화면 보여주는 함수
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 원을 그리고, 중심 좌표는 start_button의 중심좌표 사용
    # 반지름은 60, 두께는 5

# 게임 화면 보여주는 함수
def display_game_screen():
    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            # 버튼 사각형 그리기
            pygame.draw.rect(screen, WHITE, rect)
        else:        
            # 실제 숫자 텍스트
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)
        

# position에 해당하는 버튼 확인
def check_buttons(position):
    # 전역 변수로 사용하기 위함
    global start
    
    # 게임이 시작했다면
    if start:
        check_number_buttons(position)
        
    # start 버튼에 position이 포함되면
    elif start_button.collidepoint(position):
        start = True
    
def check_number_buttons(position):
    global hidden
    
    for button in number_buttons:
        # 클릭한 위치가 버튼에 포함되면
        if button.collidepoint(position):
            # 첫 번째 숫자가 맞다면
            if button == number_buttons[0]:
                print("correct")
                del number_buttons[0]   # 리스트에서 첫 번째 숫자 삭제
                
                if not hidden:
                    hidden = True  # 숫자 숨김 처리
            # 잘못된 숫자 클릭 시
            else:
                print("wrong")
    
# 초기화
pygame.init()
screen_width = 1280 # 가로 크기
screen_height = 720 # 가로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120) # 폰트 정의

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)          # 사각형의 크기가 120x120
start_button.center = (120, screen_height - 120)    # 사각형 중심좌표 설정

# 색상
BLACK = (0, 0, 0) # RGC
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

# 플레이어가 눌러야 하는 버튼을 관리하는 리스트
number_buttons = [] 

start = False   # 게임 시작 여부 
hidden = False  # 숫자 숨김 여부(사용자가 1을 클릭하거나, 일정 시간이 지났을 때)

# 게임 시작 전에 게임 설정 함수 수행
setup(1)

# 게임 루프
running = True  # 게임이 실행중인지 체크
while running:
    click_position = None
    
    # 이벤트 루프 : 사용자의 동작 확인
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가를 확인
        # 창을 닫는 이벤트일 때
        if event.type == pygame.QUIT: 
            running = False # 게임이 더 이상 실행중이 아님을 체크
            
        # 사용자가 마우스를 클릭했을 때
        elif event.type == pygame.MOUSEBUTTONUP: 
            click_position = pygame.mouse.get_pos()
            print(click_position)
            
    # 화면을 검정색으로 설정
    screen.fill(BLACK)
            
    if start:
        display_game_screen() # 게임 화면 표시
    else:
        display_start_screen() # 시작 화면 표시
    
    # 사용자가 클릭한 좌표값이 있다면(클릭했다면)
    if click_position:
        check_buttons(click_position)
    
    # 화면 업데이트
    pygame.display.update()
    
# 게임 종료
pygame.quit()