import pygame
from fruta import Fruta


#CRIANDO TELA
pygame.init()
LARGURA = 733
ALTURA = 478
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
FPS = 30
sair = False
pontos = 0
fonte = pygame.font.SysFont("comicsansms", 30)
fonte2 = pygame.font.SysFont("comicsansms", 70)
tela = pygame.display.set_mode([LARGURA, ALTURA])
mouse = pygame.mouse     # encurta o nome
mouse.set_visible(False) # esconde o pontei
texto = fonte.render("Pontos: " + str(pontos), True, (BRANCO))

frutas = pygame.sprite.Group()
uva = Fruta("uva.png")
morango = Fruta("morango.png")
laranja = Fruta("laranja.png")
melancia = Fruta("melancia.png")
kiwi = Fruta("kiwi.png")
maca = Fruta("maca.png")
pera = Fruta("pera.png")
pessego = Fruta("pessego.png")
limao = Fruta("limao.png")
abacaxi = Fruta("abacaxi.png")
goiaba = Fruta("goiaba.png")
bomba = Fruta("bomba.png")
cesta = Fruta("cesta.png")

frutas.add(uva)
frutas.add(abacaxi)
frutas.add(morango)
frutas.add(laranja)
frutas.add(melancia)
frutas.add(kiwi)
frutas.add(pera)
frutas.add(pessego)
frutas.add(limao)
frutas.add(bomba)
frutas.add(cesta)

pygame.display.set_caption("FruitNinja")
fundo = pygame.image.load("yinyang.jpg").convert_alpha()
sprites = pygame.sprite.Group()
sprites.add(frutas)

tela.blit(fundo, (0,0))   # põe o objeto na tela na posição especificada

while sair == False:

    frutas.add(cesta)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        if event.type == pygame.KEYDOWN:
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_F1]:
                print("F1")
        if event.type == pygame.MOUSEMOTION:
            pos = mouse.get_pos()
            if pos[0] <= 733 and pos[1] <= 478:
                cesta.mover(pos[0], pos[1])
                if pos[0] >= uva.x1 and pos[0] <= (uva.x1+100) and pos[1] >= uva.y1 and pos[1] <= (uva.y1+100):
                    uva.morrer()
                    sprites.remove(uva)
                    pontos += 1
                if pos[0] >= morango.x1 and pos[0] <= (morango.x1+100) and pos[1] >= morango.y1 and pos[1] <= (morango.y1+100):
                    morango.morrer()
                    sprites.remove(morango)
                    pontos += 1
                if pos[0] >= laranja.x1 and pos[0] <= (laranja.x1+100) and pos[1] >= laranja.y1 and pos[1] <= (laranja.y1+100):
                    laranja.morrer()
                    sprites.remove(laranja)
                    pontos += 1
                if pos[0] >= melancia.x1 and pos[0] <= (melancia.x1+100) and pos[1] >= melancia.y1 and pos[1] <= (melancia.y1+100):
                    melancia.morrer()
                    sprites.remove(melancia)
                    pontos += 1
                if pos[0] >= kiwi.x1 and pos[0] <= (kiwi.x1+100) and pos[1] >= kiwi.y1 and pos[1] <= (kiwi.y1+100):
                    kiwi.morrer()
                    sprites.remove(kiwi)
                    pontos += 1
                if pos[0] >= maca.x1 and pos[0] <= (maca.x1+100) and pos[1] >= maca.y1 and pos[1] <= (maca.y1+100):
                    maca.morrer()
                    sprites.remove(maca)
                    pontos += 1
                if pos[0] >= pera.x1 and pos[0] <= (pera.x1+100) and pos[1] >= pera.y1 and pos[1] <= (pera.y1+100):
                    pera.morrer()
                    sprites.remove(pera)
                    pontos += 1
                if pos[0] >= pessego.x1 and pos[0] <= (pessego.x1+100) and pos[1] >= pessego.y1 and pos[1] <= (pessego.y1+100):
                    pessego.morrer()
                    sprites.remove(pessego)
                    pontos += 1
                if pos[0] >= abacaxi.x1 and pos[0] <= (abacaxi.x1+100) and pos[1] >= abacaxi.y1 and pos[1] <= (abacaxi.y1+100):
                    abacaxi.morrer()
                    sprites.remove(abacaxi)
                    pontos += 1
                if pos[0] >= goiaba.x1 and pos[0] <= (goiaba.x1+100) and pos[1] >= goiaba.y1 and pos[1] <= (goiaba.y1+100):
                    goiaba.morrer()
                    sprites.remove(goiaba)
                    pontos += 1
                if pos[0] >= bomba.x1 and pos[0] <= (bomba.x1+100) and pos[1] >= bomba.y1 and pos[1] <= (bomba.y1+100):
                    bomba.morrer()
                    uva.morrer()
                    sprites.remove(uva)
                    morango.morrer()
                    sprites.remove(morango)
                    laranja.morrer()
                    sprites.remove(laranja)
                    melancia.morrer()
                    sprites.remove(melancia)
                    kiwi.morrer()
                    sprites.remove(kiwi)
                    maca.morrer()
                    sprites.remove(maca)
                    pera.morrer()
                    sprites.remove(pera)
                    pessego.morrer()
                    sprites.remove(pessego)
                    abacaxi.morrer()
                    sprites.remove(abacaxi)
                    goiaba.morrer()
                    sprites.remove(goiaba)
                    sprites.remove(bomba)
                    cesta.kill()
                    sprites.remove(cesta)
                    sair = True

                # texto, antialias, cor, fundo (opcional)


    uva.cair()
    morango.cair()
    laranja.cair()
    melancia.cair()
    kiwi.cair()
    maca.cair()
    pera.cair()
    pessego.cair()
    abacaxi.cair()
    goiaba.cair()
    bomba.cair()

    if uva.y1 >= 500:
        uva.kill()
        uva = Fruta("uva.png")
        frutas.add(uva)
    if morango.y1 >= 500:
        morango.kill()
        morango = Fruta("morango.png")
        frutas.add(morango)
    if laranja.y1 >= 500:
        laranja.kill()
        laranja = Fruta("laranja.png")
        frutas.add(laranja)
    if melancia.y1 >= 500:
        melancia.kill()
        melancia = Fruta("melancia.png")
        frutas.add(melancia)
    if kiwi.y1 >= 500:
        kiwi.kill()
        kiwi = Fruta("kiwi.png")
        frutas.add(kiwi)
    if maca.y1 >= 500:
        maca.kill()
        maca = Fruta("maca.png")
    if pera.y1 >= 500:
        pera.kill()
        pera = Fruta("pera.png")
        frutas.add(pera)
    if pessego.y1 >= 500:
        pessego.kill()
        pessego = Fruta("pessego.png")
        frutas.add(pessego)
    if limao.y1 >= 500:
        limao.kill()
        limao = Fruta("limao.png")
        frutas.add(limao)
    if abacaxi.y1 >= 500:
        abacaxi.kill()
        abacaxi = Fruta("abacaxi.png")
        frutas.add(abacaxi)
    if goiaba.y1 >= 500:
        goiaba.kill()
        goiaba = Fruta("goiaba.png")
    if bomba.y1 >= 500:
        bomba.kill()
        bomba = Fruta("bomba.png")
        frutas.add(bomba)

    sprites.add(frutas)
    tela.blit(fundo, (0,0))    # põe o objeto na tela na posição especificada
    tela.blit(fonte.render("Pontos: " + str(pontos), True, (255,255,255)), (0, 0))
    frutas.draw(tela)         # desenha demais objetos
    pygame.display.update()

fim = False

while not fim:
    tela.blit(fundo, (0,0))
    tela.blit(fonte2.render("Morreu", True, (0, 0, 0)), (240, 70))
    tela.blit(fonte2.render("Pontos: " + str(pontos), True, (0, 0, 0)), (200, 200))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fim = True
            pygame.quit()
