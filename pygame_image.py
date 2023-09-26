import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_reverse = pg.transform.flip(bg_img,True,False)
    kouka_img_3 = pg.image.load("fig/3.png")

    kouka_img_3 = pg.transform.flip(kouka_img_3,True,False)
    kouka_img_3_1 = pg.transform.rotozoom(kouka_img_3,10,1.0)

    tmr = 0
    x = 0
    koukaton_tmr = 0
    koukaton = [kouka_img_3,kouka_img_3_1]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        clock.tick()

        if x == 1599:
            x = 0

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_reverse, [1600-x, 0])

        if koukaton_tmr <= 50:
            screen.blit(koukaton[0],[300,200])
        elif 50 < koukaton_tmr <= 100: 
            screen.blit(koukaton[1],[300,200])
        else:
            koukaton_tmr = 0


        pg.display.update()
        tmr += 1     
        x += 1
        koukaton_tmr += 1 
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()