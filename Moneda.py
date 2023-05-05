import pygame

class Moneda(pygame.sprite.Sprite):

    def __init__(self):
        super(Moneda, self).__init__()
        
        self.images = []
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 1.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 1.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 1.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 1.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 2.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 2.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 2.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 2.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 3.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 3.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 3.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 3.png'))       
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 4.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 4.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 4.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 4.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 5.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 5.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 5.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 5.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 6.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 6.png'))        
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 6.png'))
        self.images.append(pygame.image.load('imagenes\monedas\Moneda 6.png'))
        
        
        self.index = 0
        self.index1 = 0
        self.index2 = 0
        self.index3 = 0
        self.index4 = 0
        self.index5 = 0
        self.index6 = 0
        self.index7 = 0
        self.index8 = 0
        
        x = - 40
        y = - 40
        
        self.image = self.images[self.index]
        self.image1 = self.images[self.index1]
        self.image2 = self.images[self.index2]
        self.image3 = self.images[self.index3]
        self.image4 = self.images[self.index4]
        self.image5 = self.images[self.index5]
        self.image6 = self.images[self.index6]
        self.image7 = self.images[self.index7]
        self.image8 = self.images[self.index8]
 
        self.rect = pygame.Rect(x, y, 40, 40)
 
    
    def update(self):
        pass
    
    def monedas_mov(self):
        self.index += 1
        if self.index >= 24:
            self.index = 0
        self.image = self.images[self.index]
        self.rect.x = 1040
        self.rect.y = 400

    def monedas_mov1(self):
        self.index1 += 1
        if self.index1 >= 24:
            self.index1 = 0
        self.image = self.images[self.index1]
        #self.rect.x +=1
        self.rect.x = 1040
        self.rect.y = 40
        
    def monedas_mov2(self):
        
        self.index2 += 1
        if self.index2 >= 24:
            self.index2 = 0
        self.image = self.images[self.index2]        
        self.rect.x =40
        self.rect.y =40
    
    def monedas_mov3(self):
        
        self.index3 += 1
        if self.index3 >= 24:
            self.index3 = 0
        self.image = self.images[self.index3]
        self.rect.x =640
        self.rect.y =320

    def monedas_mov4(self):
        
        self.index4 += 1
        if self.index4 >= 24:
            self.index4 = 0
        self.image = self.images[self.index4]
        self.rect.x =200
        self.rect.y =560


    def monedas_mov5(self):
        
        self.index5 += 1
        if self.index5 >= 24:
            self.index5 = 0
        self.image = self.images[self.index5]
        self.rect.x =70
        self.rect.y =80   

    def monedas_mov6(self):
        
        self.index6 += 1
        if self.index6 >= 24:
            self.index6 = 0
        self.image = self.images[self.index6]
        self.rect.x =50
        self.rect.y =60 

    def monedas_mov7(self):
        
        self.index7 += 1
        if self.index7 >= 24:
            self.index7 = 0
        self.image = self.images[self.index7]
        self.rect.x =0
        self.rect.y =60             
    
    def monedas_mov8(self):
        
        self.index8 += 1
        if self.index8 >= 24:
            self.index8 = 0
        self.image = self.images[self.index8]
        self.rect.x =100
        self.rect.y =160     