#komentar
import random
import pygame as pg

pg.init()
pg.display.set_caption('Apple game')
(sirina, visina) = (500, 300)
prozor = pg.display.set_mode((sirina, visina))

pg.key.set_repeat(10, 10)

korpa = pg.image.load("korpa.png")
jabuka = pg.image.load("jabuka.png")
zivot = jabuka

maks_jabuke = 3
jabuke = []
poeni = 0
zivoti = 3
(korpa_x, korpa_y) = (0, visina - korpa.get_height())

def dodaj_jabuku():
    x = random.randint(0, sirina - jabuka.get_width())
    jabuke.append([x, 10])

def dodaj_jabuke():
    if len(jabuke) == 0 or (len(jabuke) < maks_jabuke):
        dodaj_jabuku()

def pomeri_jabuke():
    for jabuka in jabuke:
        jabuka[1] += 5

def pokupi_jabuke():
    global jabuke, poeni, zivoti
    nove_jabuke = []
    for [x, y] in jabuke:
        if y > visina - korpa.get_height() and\
                korpa_x <= x and x <= korpa_x + korpa.get_width():
            poeni += 1
        elif y > visina:
            zivoti -= 1
        else:
            nove_jabuke.append([x, y])
    jabuke = nove_jabuke

def crtaj():
    prozor.fill(pg.Color('white'))
    font = pg.font.SysFont('Arial', 20)
    tekst = font.render('Poeni: ' + str(poeni), True, pg.Color('black'))
    prozor.blit(tekst, (5, 5))

    for i in range(1, zivoti + 1):
        prozor.blit(zivot, (sirina - 5 - i * zivot.get_width(),5))
    for [x, y] in jabuke:
        prozor.blit(jabuka, (x, y))
    prozor.blit(korpa, (korpa_x, korpa_y))

def obradi_dogadjaj(dogadjaj):
    global korpa_x
    if dogadjaj.type == pg.KEYDOWN:
        if dogadjaj.key == pg.K_LEFT:
            korpa_x -= 5
        elif dogadjaj.key == pg.K_RIGHT:
            korpa_x += 5

def novi_frejm():
    global kraj
    dodaj_jabuke()
    pomeri_jabuke()
    pokupi_jabuke()
    if zivoti <= 0:
        kraj = True
        print('Poeni: ', poeni)

sat = pg.time.Clock()
kraj = False
while not kraj:
    crtaj()
    pg.display.update()
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            kraj = True
            print('Poeni: ',poeni)
        else:
            obradi_dogadjaj(dogadjaj)
    sat.tick(20)
    novi_frejm()
pg.quit()
