import pygame #Nhập các mô đun pygame
import random #Nhập mô đun ngẫu nhiên

pygame.init()

pygame.mixer.init()

#Màu sắc và ảnh trong game
blue = (0,0,255)
red = (255,0,0)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)
grass = pygame.image.load('Images/grass.jpg')

#Kích thước màn hình
hienThi_doDai = 640
hienThi_doCao = 480

hienThi=pygame.display.set_mode((hienThi_doDai,hienThi_doCao))
pygame.display.set_caption('Tro choi ran') #Hiện chữ trên cửa sổ

clock = pygame.time.Clock()

#kích thước rắn và tốc độ rắn
co_ran = 10
toc_do_ran = int(input())

#phông chữ
kieu_font = pygame.font.SysFont('impact', 25)
diem_font = pygame.font.SysFont('arial', 25)

def diem_cua_ban(diem):
    giatri = diem_font.render("Diem cua ban: " + str(diem), True, blue)
    hienThi.blit(giatri, [0, 0])

def ran_ta(co_ran, than_ran):
    for x in than_ran:
        pygame.draw.rect(hienThi, black, [x[0], x[1], co_ran, co_ran])

def tin_nhan(msg, mau_sac):
    mesg = kieu_font.render(msg, True, mau_sac)
    hienThi.blit(mesg, [hienThi_doDai / 6, hienThi_doCao / 3])

def vong_lap():
    game_over = False
    game_close = False

    x1 = hienThi_doDai / 2  # tọa độ x bắt đầu của rắn
    y1 = hienThi_doCao / 2  # tọa độ y bắt đầu của rắn

    # biến thay đổi tọa độ
    x1_change = 0
    y1_change = 0

    # thân rắn và độ dài thân rắn
    bo_ran = []
    do_dai_ran = 1

    do_an_x = round(random.randrange(0, hienThi_doDai - co_ran) / 10.0) * 10.0
    do_an_y = round(random.randrange(0, hienThi_doCao - co_ran) / 10.0) * 10.0

    huong = 'NULL'
    chuyen = huong

    while not game_close:

        while game_over == True:
            hienThi.fill(white)
            hienThi.blit(grass, [0, 0])
            tin_nhan("Ban da thua! An Q đe đong hay R đe chay lai", blue)
            diem_cua_ban(do_dai_ran - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                    if event.key == pygame.K_r:
                        vong_lap()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Ấn nút đóng màn hình
                game_close = True
            if event.type == pygame.KEYDOWN: # Ấn nút
                if event.key == pygame.K_LEFT: # Ấn nút trái
                    chuyen = 'LEFT'
                elif event.key == pygame.K_RIGHT: # Ấn nút phải
                    chuyen = 'RIGHT'
                elif event.key == pygame.K_UP: # Ấn nút lên
                    chuyen = 'UP'
                elif event.key == pygame.K_DOWN: # Ấn nút xuống
                    chuyen = 'DOWN'

        if chuyen == 'UP' and huong != 'DOWN':
            huong = 'UP'
        if chuyen == 'DOWN' and huong != 'UP':
            huong = 'DOWN'
        if chuyen == 'LEFT' and huong != 'RIGHT':
            huong = 'LEFT'
        if chuyen == 'RIGHT' and huong != 'LEFT':
            huong = 'RIGHT'

        if huong == 'UP':
            x1_change = 0
            y1_change = -co_ran
        if huong == 'DOWN':
            x1_change = 0
            y1_change = co_ran
        if huong == 'LEFT':
            x1_change = -co_ran
            y1_change = 0
        if huong == 'RIGHT':
            x1_change = co_ran
            y1_change = 0

        if x1 >= hienThi_doDai:
            x1 = 0 - co_ran
        elif x1 < 0:
            x1 = hienThi_doDai
        elif y1 >= hienThi_doCao:
            y1 = 0 - co_ran
        elif y1 < 0:
            y1 = hienThi_doCao


        x1 += x1_change
        y1 += y1_change

        hienThi.fill(white)
        hienThi.blit(grass, (0, 0))
        pygame.draw.rect(hienThi, orange, [do_an_x, do_an_y, co_ran, co_ran])# vẽ đồ ăn
        dau_ran = []
        dau_ran.append(x1)
        dau_ran.append(y1)
        bo_ran.append((dau_ran))
        if len(bo_ran) > do_dai_ran:
            del bo_ran[0]

        for x in bo_ran[:-1]:
            if x == dau_ran:
                game_over = True

        ran_ta(co_ran, bo_ran)
        diem_cua_ban(do_dai_ran - 1)

        pygame.display.update()

        if x1 == do_an_x and y1 == do_an_y:
            do_an_x = round(random.randrange(0, hienThi_doDai - co_ran) / 10.0) * 10.0
            do_an_y = round(random.randrange(0, hienThi_doCao - co_ran) / 10.0) * 10.0
            do_dai_ran += 1
            sound = pygame.mixer.Sound("Sounds/Ding.wav")
            pygame.mixer.Sound.play(sound)

        clock.tick(toc_do_ran)

    pygame.quit()
    quit()

vong_lap()