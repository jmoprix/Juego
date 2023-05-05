from pygame.mixer import Sound
from Moneda import Moneda
import pygame
from Personaje import Personaje
from pygame.locals import *

# -- CREAMOS UN SPRITE 

class Pared(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Princesa.png')
        self.rect=self.image.get_rect()

# -- INICIALIZAR

pygame.init()

#Sonido

pygame.mixer.music.load("street-fighter.wav")
pygame.mixer.music.play(10)


# -- MEDIDAS

ancho = 1280
alto = 720

# -- COLORES

negro =  (0,0,0)
blanco = (255,255,255)
azul = (0,0,255)
verde = (0,255,0)
rojo = (255,0,0)
naranja = (255,128,0)
griss = (30,30,30)

# -- VARIABLES

Princesa = pygame.image.load('Princesa.png')
pr_rect = Princesa.get_rect()
movil = pygame.Rect(0,0,40,40)
x = 0
y = 0
alt = 0
vel = 0

# -- LISTA PARED

listaPared = pygame.sprite.Group()
pared=Pared()
listaPared.add(pared) 

# -- MAPA
mapa = [
    '  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    '               X        XX     X',
    'X XXX XXXXXXX    XXXXXX  X X XXX',
    'X X   X       XXXX      XX X   X',
    'X XX XXXXX XX  X X XX XXX  XXX X',
    'X             XX X  XXX   XXX  X',
    'XXXXX XX XXXX  X     X  XXX   XX',
    'X   XXX       XXXXX    XX      X',
    'X X     XXX XXX   XXXX     XXX X',
    'XXXXX  XX X X XX XX     XXXX X X',
    'X           X  X X  XXX X      X',
    'X XXX XXXXXXXX      X X XX  XXXX',
    'X X   X        XXX             X',
    'X XXXXX XXXXXXXX X XXXXXXXXXXX X',
    'X  X  X    X   X X X      X    X',
    'X XX XXX XXXXX X X X X XXXXXXXXX',
    'X            X   X   X          ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ',
]

# -- CREAMOS LISTA DE RECTANGULOS

def construir_mapa(mapa):
    listaMuros=[]
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro == 'X':
                listaMuros.append(pygame.Rect(x,y,30,30))
            x+=40
        x=0
        y+=40
    return listaMuros

listaMuros = construir_mapa(mapa)

# -- DIBUJAMJOS UN RECTANGULO

def dibujar_muro(superficie,rectangulo):
    pygame.draw.rect(superficie, griss, rectangulo)

def dibujar_mapa(superficie, listaMuros):
    for muro in listaMuros:
        dibujar_muro(superficie, muro)

# -- AQUI INICIA 

if __name__ == '__main__':

# -- VENTANA
    pygame.display.set_caption('Laberinto by JHB')
    ventana = pygame.display.set_mode((ancho,alto))
    reloj = pygame.time.Clock()
    FPS = 60

# -- DATOS

    g_monedas= pygame.sprite.Group()
    moneda = Moneda()
    moneda1 = Moneda()
    moneda2 = Moneda()
    moneda3 = Moneda()
    moneda4 = Moneda()
    moneda5=Moneda()
    moneda6 =Moneda()
    moneda7 =Moneda()
    moneda8=Moneda()
    
    g_monedas.add(moneda,moneda1,moneda2,moneda3,moneda4,moneda5,moneda6,moneda7,moneda8)

    g_jugador= pygame.sprite.Group()
    jugador1 = Personaje()
    #--jugador2=Personaje()
    g_jugador.add(jugador1)

# -- TEXTO

    pygame.font.init()
    Text = str(jugador1.vida)
    font = pygame.font.SysFont(None, 30)

    # -- BUCLE PRINCIPAL

    jugando = True

    while jugando:
        
        # -- EVENTOS

        img = font.render(str(jugador1.vida), True,blanco)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass

                if event.key == pygame.K_r:
                    jugador1.incrementar_vida()
                    


                if event.key == pygame.K_RIGHT:
                                        
                    
                    g_jugador.update()
                    jugador1.ava_der()
                    #movil.x +=5
                    des_i_d +=5
                    jugador1.vida-=1
                    

                                        

                if event.key == pygame.K_LEFT:
                    g_jugador.update()                    
                    jugador1.ava_izq()
                    #movil.x -=5
                    des_i_d -=5
                    jugador1.vida-=1
                    

                    

                if event.key == pygame.K_UP:
                    g_jugador.update()                    
                    jugador1.ava_arr()
                    #movil.y -=5
                    des_a_a -=5
                    jugador1.vida-=1
              

                    
                if event.key == pygame.K_DOWN:
                    g_jugador.update()                    
                    jugador1.ava_aba()
                    #movil.y +=5
                    des_a_a +=5
                    jugador1.vida-=1
                    

                if jugador1.vida == 0:
                        jugando = False

            else:

                des_i_d = 0
                des_a_a = 0
            
        # -- LOGICA

        
            
            movil.x +=des_i_d
            movil.y +=des_a_a


            jugador1.rect.x = movil.x
            jugador1.rect.y = movil.y

            for muro in listaMuros:
                if movil.colliderect(muro):
                    movil.x -=des_i_d
                    movil.y -=des_a_a
        
        x=0
        y=0

        for fila in mapa:
            for muro in fila:
                if muro=="X":
                    pared.rect.x=x
                    pared.rect.y=y
                    listaPared.add(pared)
                    listaPared.draw(ventana)
                x+=40
            x=0
            y=+40
        
        #for moneda in g_monedas:
            if movil.colliderect(moneda):
               jugador1.vida +=50

        # --DIBUJO

        ventana.fill(negro)

        g_monedas.update()
        moneda.monedas_mov()
        moneda1.monedas_mov1()
        moneda2.monedas_mov2()
        moneda3.monedas_mov3()
        moneda4.monedas_mov4()
        
        g_monedas.draw(ventana)
        g_jugador.draw(ventana)
        dibujar_mapa(ventana,listaMuros)
        ventana.blit(img,(1200,10))
        ventana.blit(Princesa,(1220,670))
        
        # -- ACTUALIZA
        
        reloj.tick(60)
        pygame.display.update()
        pygame.display.flip()
        

    # -- SALIR

pygame.quit()