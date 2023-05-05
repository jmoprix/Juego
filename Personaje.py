import pygame
from pygame import image

class Personaje(pygame.sprite.Sprite):        
    
    # -- CONSTRUCTOR

    def __init__(self):     
        super(Personaje, self).__init__()
 
        self.images = []
        self.images.append(pygame.image.load('imagenes\caminar_derecha\Walk (1).png'))
        self.images.append(pygame.image.load('imagenes\caminar_derecha\Walk (2).png'))
        self.images.append(pygame.image.load('imagenes\caminar_derecha\Walk (3).png'))
        self.images.append(pygame.image.load('imagenes\caminar_derecha\Walk (4).png'))
        self.images.append(pygame.image.load('imagenes\caminar_derecha\Walk (5).png'))
        self.images.append(pygame.image.load('imagenes\caminar_derecha\Walk (6).png'))
        self.images.append(pygame.image.load('imagenes\caminar_derecha\Walk (7).png'))
        self.images.append(pygame.image.load('imagenes\caminar_derecha\Walk (8).png'))
        self.images.append(pygame.image.load('imagenes\caminar_derecha\Walk (9).png'))
        self.images.append(pygame.image.load('imagenes\caminar_derecha\Walk (10).png'))
        self.images.append(pygame.image.load('imagenes\caminar_izquierda\Walk (1).png'))
        self.images.append(pygame.image.load('imagenes\caminar_izquierda\Walk (2).png'))
        self.images.append(pygame.image.load('imagenes\caminar_izquierda\Walk (3).png'))
        self.images.append(pygame.image.load('imagenes\caminar_izquierda\walk (4).png'))
        self.images.append(pygame.image.load('imagenes\caminar_izquierda\Walk (5).png'))
        self.images.append(pygame.image.load('imagenes\caminar_izquierda\Walk (6).png'))
        self.images.append(pygame.image.load('imagenes\caminar_izquierda\Walk (7).png'))
        self.images.append(pygame.image.load('imagenes\caminar_izquierda\Walk (8).png'))
        self.images.append(pygame.image.load('imagenes\caminar_izquierda\Walk (9).png'))
        self.images.append(pygame.image.load('imagenes\caminar_izquierda\Walk (10).png'))
        self.images.append(pygame.image.load('Princesa.png'))
        
        self.indexder = 0
        self.indexizq = 10
        self.indexw = 21
        self.vida = 500

        x = 0
        y = 0
        
        self.image = self.images[self.indexder]
 
        self.rect = pygame.Rect(x, y, 40, 40)
 
    
    def update(self):
        pass
    
    def  ava_der(self):

        #self.rect.x +=5
        self.indexder += 1
        if self.indexder >= 10:
            self.indexder = 0
        self.image = self.images[self.indexder]
    
    def  ava_izq(self):
        
        #self.rect.x -=5
        self.indexizq += 1
        if self.indexizq >= 20:
            self.indexizq = 10
        self.image = self.images[self.indexizq]
        
    
    def  ava_aba(self):

        #self.rect.y +=5
        self.indexder += 1
        if self.indexder >= 10:
            self.indexder = 0
        self.image = self.images[self.indexder]
    
    def  ava_arr(self):
        
        #self.rect.y -=5
        self.indexizq += 1
        if self.indexizq >= 20:
            self.indexizq = 10
        self.image = self.images[self.indexizq]
    
    def incrementar_vida(self):
        self.vida +=1

    def ganador(self):
        if self.indexw >= 21:
           self.indexw = 21
        self.image = self.images[self.indexw]
        self.rect.x = 720
        self.rect.y = 400

    
        
    
        
        
        