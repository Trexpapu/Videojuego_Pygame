import pygame #importamos pygame
import random as r
import time as t


class Mundo(pygame.sprite.Sprite):#clase mundo que nos servira para el diseño de cada nivel
    def __init__(self, piso, fondo1, fondo2, fondo3, fondo4, fondo5):
        super().__init__()
        self.piso = piso
        self.piso_grupo = pygame.sprite.Group()
        self.piso_grupo.add(self.piso)
        self.obstaculo_grupo = pygame.sprite.Group()
        self.grupo_enemigos = pygame.sprite.Group()
        self.imagen1 = pygame.image.load(fondo1).convert_alpha()
        self.imagen1=pygame.transform.scale(self.imagen1, (ancho_pantalla, alto_pantalla))#escalamos el fondo al ancho y alto de pantalla
        self.imagen2 = pygame.image.load(fondo2).convert_alpha()
        self.imagen2=pygame.transform.scale(self.imagen2, (ancho_pantalla, alto_pantalla))#escalamos el fondo al ancho y alto de pantalla
        self.imagen3 = pygame.image.load(fondo3).convert_alpha()
        self.imagen3=pygame.transform.scale(self.imagen3, (ancho_pantalla, alto_pantalla))#escalamos el fondo al ancho y alto de pantalla
        self.imagen4 = pygame.image.load(fondo4).convert_alpha()
        self.imagen4=pygame.transform.scale(self.imagen4, (ancho_pantalla, alto_pantalla))#escalamos el fondo al ancho y alto de pantalla
        self.imagen5 = pygame.image.load(fondo5).convert_alpha()
        self.imagen5=pygame.transform.scale(self.imagen5, (ancho_pantalla, alto_pantalla))#escalamos el fondo al ancho y alto de pantalla
        self.lista_fondos = [self.imagen1, self.imagen2, self.imagen3, self.imagen4, self.imagen5]
        #vidas
        self.grupo_vidas = pygame.sprite.Group()

        #gemas
        self.grupo_gemas = pygame.sprite.Group()

        #grupo dos de pisis
        self.cajas = pygame.sprite.Group()

        self.grupo_obstaculos2 = pygame.sprite.Group()

        self.champin = pygame.sprite.Group()

        self.poderes = pygame.sprite.Group()

        self.choco1 = False
        self.choco2 = False
        self.choco3 = False
        self.choco4 = False



        #grupo jefe final 
        self.jefe = pygame.sprite.Group()
        #mini jefes que lanza
        self.mini_jefes = pygame.sprite.Group()
        #piedras que levanta
        self.piedras_suelo = pygame.sprite.Group()
        #piedras del aire
        self.piedras_aire = pygame.sprite.Group()

        self.poderes = pygame.sprite.Group()

        self.proyectiles = pygame.sprite.Group()
    def agregar_proyectil(self, proyectil):
        self.proyectiles.add(proyectil)

    def agregar_miniboss(self, mini):
        self.mini_jefes.add(mini)

    def crear_piedra_suelo(self, piedra):
        self.piedras_suelo.add(piedra)

    def crear_piedra_aire(self, piedra):
        self.piedras_aire.add(piedra)    

    def crear_jefe(self, jefe):
        self.jefe.add(jefe)

    def agregar_champ(self, champ):
        self.champin.add(champ)

    def agregar_obstaculo2(self, obstaculo):
        self.grupo_obstaculos2.add(obstaculo)

    def agregar_caja(self, caja):
        self.cajas.add(caja)

    def agregar_gema(self, gema):
        self.grupo_gemas.add(gema)

    def agregar_poder(self, poder):
        self.poderes.add(poder)

    def agregar_vidas(self, vida):
        self.grupo_vidas.add(vida)

    def quitar_vidas(self):
        if jugador1.vidas > 0:
            vida_eliminada = self.grupo_vidas.sprites()[jugador1.vidas-1]
            self.grupo_vidas.remove(vida_eliminada)


    def dibujar_fondos(self):       
         for x in range(200):
            velocidad = 0.1
            for i in self.lista_fondos:
                pantalla.blit(i, ((x * ancho_pantalla) - jugador1.scroll * velocidad, 0))
                velocidad += 0.1
            

    def dibujar_pisos(self):
        for x in range(200):
            pantalla.blit(self.piso.image, ((x * self.piso.ancho_imagen) - jugador1.scroll * 1.1, alto_pantalla - self.piso.alto_imagen))


    def Generarenemigos(self, enemigo):
        self.grupo_enemigos.add(enemigo)

    def Generarobstaculos(self,obstaculo):
        self.obstaculo_grupo.add(obstaculo)

    def colision_jefe_proyectil(self):
        colision_jefe_p = pygame.sprite.spritecollide(jefe, self.proyectiles, False)
        for i in colision_jefe_p:
            if jefe.rect.left < i.rect.right < jefe.rect.right:
                i.kill()
                jefe.rectangulo_ancho -=50


    def colision_jefe(self):
        colision_jugador_jefe = pygame.sprite.spritecollide(jugador1, self.jefe, False)
        if colision_jugador_jefe:
            self.quitar_vidas()
            jugador1.vidas -= 1

    def colision_jugador_piedras_Aire(self):
        colision_jugador_piedras = pygame.sprite.spritecollide(jugador1, self.piedras_aire, False)
        for enemigo in colision_jugador_piedras:#recorrer toda la lista de los enemigos que han chocado con jugador
            if jugador1.rect.top < enemigo.rect.bottom < jugador1.rect.bottom:
                    enemigo.kill()#matar enemigo
                    self.quitar_vidas()
                    jugador1.vidas -= 1

    def colision_jugador_piedras_Suelo(self):
        colision_jugador_piedras = pygame.sprite.spritecollide(jugador1, self.piedras_suelo, False)
        for enemigo in colision_jugador_piedras:#recorrer toda la lista de los enemigos que han chocado con jugador
            if jugador1.rect.bottom > enemigo.rect.top > jugador1.rect.top:
                enemigo.kill()#matar enemigo
                self.quitar_vidas()
                jugador1.vidas -= 1


    def colision_jugador_mini_jefes(self):
        colision_jugador_enemigos = pygame.sprite.spritecollide(jugador1, self.mini_jefes, False)#lista que guarda los sprites del grupo enemigo que han chocado con jugador1
        for enemigo in colision_jugador_enemigos:#recorrer toda la lista de los enemigos que han chocado con jugador
            overlap_x = min(jugador1.rect.right - enemigo.rect.left, enemigo.rect.right - jugador1.rect.left)
            overlap_y = min(jugador1.rect.bottom - enemigo.rect.top, enemigo.rect.bottom - jugador1.rect.top)
               # print(overlap_x, overlap_y)

                # Ajusta la posición según la dirección de la superposición
            if overlap_x < overlap_y:
                enemigo.kill()#matar enemigo
                self.quitar_vidas()
                jugador1.vidas -= 1
                    
             
            else:
                    
                    if jugador1.rect.bottom > enemigo.rect.top > jugador1.rect.top:
                        enemigo.kill()
                    elif jugador1.rect.top < enemigo.rect.bottom < jugador1.rect.bottom:
                        enemigo.kill()#matar enemigo
                        self.quitar_vidas()
                        jugador1.vidas -= 1

            


    def colision_jugador_y_piso(self):
        colision_jugador_piso =  pygame.sprite.spritecollide(jugador1, self.piso_grupo, False)#lista que guarda sprites del grupo objetos nivel que han chocado con jugador1
        if colision_jugador_piso:#si la lista tiene algo dentro será verdad esta condición  
            jugador1.tocando_piso = True     
            jugador1.rect.bottom = self.piso.rect.top#asignar parte baja del rectangulo del jugador con lo alto del piso
        else:
            jugador1.tocando_piso = False

    def colision_enemigo_y_piso(self):
        for sprite in self.grupo_enemigos:
            colision_piso_enemigo =  pygame.sprite.spritecollide(sprite, self.piso_grupo, False)#lista que guarda sprites del grupo objetos nivel que han chocado con enemigo
            if colision_piso_enemigo:#si la lista tiene algo dentro será verdad esta condicion
                sprite.rect.bottom = self.piso.rect.top#asignar parte baja del rectangulo enemigo con alto piso

    def colision_jugador_y_enemigos(self):
        colision_jugador_enemigos = pygame.sprite.spritecollide(jugador1, self.grupo_enemigos, False)#lista que guarda los sprites del grupo enemigo que han chocado con jugador1
        for enemigo in colision_jugador_enemigos:#recorrer toda la lista de los enemigos que han chocado con jugador
            overlap_x = min(jugador1.rect.right - enemigo.rect.left, enemigo.rect.right - jugador1.rect.left)
            overlap_y = min(jugador1.rect.bottom - enemigo.rect.top, enemigo.rect.bottom - jugador1.rect.top)
               # print(overlap_x, overlap_y)

                # Ajusta la posición según la dirección de la superposición
            if overlap_x < overlap_y:
                enemigo.kill()#matar enemigo
                self.quitar_vidas()
                jugador1.vidas -= 1
                    
             
            else:
                    
                    if jugador1.rect.bottom > enemigo.rect.top > jugador1.rect.top:
                        enemigo.kill()
                    elif jugador1.rect.top < enemigo.rect.bottom < jugador1.rect.bottom:
                        enemigo.kill()#matar enemigo
                        self.quitar_vidas()
                        jugador1.vidas -= 1
            

    def colision_jugador_y_gemas(self):
        colision_jugador_gemas = pygame.sprite.spritecollide(jugador1, self.grupo_gemas, False)#lista que guarda los sprites del grupo enemigo que han chocado con jugador1
        for gemas in colision_jugador_gemas:#recorrer toda la lista de los gemass que han chocado con jugador
            gemas.kill()#matar enemigo
            jugador1.contador_gemas -= 1
            jugador1.sondio_toca_G.play()

    def colision_jugador_y_poder(self):
        colision_jugador_poder = pygame.sprite.spritecollide(jugador1, self.poderes, False)#lista que guarda los sprites del grupo enemigo que han chocado con jugador1
        for poder in colision_jugador_poder:#recorrer toda la lista de los gemass que han chocado con jugador
            poder.kill()
            jugador1.cont_poder += 1
            

    def colision_jugador_y_obstaculo(self):
        colision_jugador_obstaculo = pygame.sprite.spritecollide(jugador1, self.obstaculo_grupo, False)
        if colision_jugador_obstaculo:
            self.choco1 = True
        elif self.choco2 == False and self.choco3 == False and self.choco4 == False:
            jugador1.chocandoder = False
            jugador1.chocandoizq = False
            self.choco1 = False
        else:
            self.choco1 = False
        for obstaculo in colision_jugador_obstaculo:
                
                overlap_x = min(jugador1.rect.right - obstaculo.rect.left, obstaculo.rect.right - jugador1.rect.left)
                overlap_y = min(jugador1.rect.bottom - obstaculo.rect.top, obstaculo.rect.bottom - jugador1.rect.top)
               # print(overlap_x, overlap_y)

                # Ajusta la posición según la dirección de la superposición
                if overlap_x < overlap_y:
                    # Ajusta en el eje x
                    if jugador1.rect.right > obstaculo.rect.left > jugador1.rect.left:
                        #jugador1.rect.right = obstaculo.rect.left-40
                        jugador1.chocandoder = True
                        
                      

                    elif jugador1.rect.left < obstaculo.rect.right < jugador1.rect.right:
                        #jugador1.rect.left = obstaculo.rect.right
                        jugador1.chocandoizq = True
                    
             
                else:
                    # Ajusta en el eje y
                    jugador1.chocandoder = False
                    jugador1.chocandoizq = False
                    if jugador1.rect.bottom > obstaculo.rect.top > jugador1.rect.top:
                        jugador1.rect.bottom = obstaculo.rect.top
                        jugador1.tocando_piso = True
                    elif jugador1.rect.top < obstaculo.rect.bottom < jugador1.rect.bottom:
                        jugador1.rect.top = obstaculo.rect.bottom



    def colision_jugador_obstaculo2(self):
        colision_jugador_obstaculo2 = pygame.sprite.spritecollide(jugador1, self.grupo_obstaculos2, False)
        if colision_jugador_obstaculo2:
            self.choco2 = True
        elif self.choco1 == False and self.choco3 == False and self.choco4 == False:
            self.choco2 = False
            jugador1.chocandoder = False
            jugador1.chocandoizq = False
        else:
            self.choco2 = False
        for obstaculo in colision_jugador_obstaculo2:
                overlap_x = min(jugador1.rect.right - obstaculo.rect.left, obstaculo.rect.right - jugador1.rect.left)
                overlap_y = min(jugador1.rect.bottom - obstaculo.rect.top, obstaculo.rect.bottom - jugador1.rect.top)
                

                # Ajusta la posición según la dirección de la superposición
                if overlap_x < overlap_y:
                    # Ajusta en el eje x
                    if jugador1.rect.right > obstaculo.rect.left > jugador1.rect.left:
                        jugador1.chocandoder = True
                      
                      #  print(jugador1.chocandoder, jugador1.chocandoizq)
                    elif jugador1.rect.left < obstaculo.rect.right < jugador1.rect.right:
                        jugador1.chocandoizq = True
                       
                else:
                    # Ajusta en el eje y
                    if jugador1.rect.bottom > obstaculo.rect.top > jugador1.rect.top:
                        jugador1.rect.bottom = obstaculo.rect.top
                        jugador1.tocando_piso = True
                    elif jugador1.rect.top < obstaculo.rect.bottom < jugador1.rect.bottom:
                        jugador1.rect.top = obstaculo.rect.bottom
        
    def colision_jugador_champ(self):
        colision_jugador_obstaculo = pygame.sprite.spritecollide(jugador1, self.champin, False)
        if colision_jugador_obstaculo:
            self.choco3 = True
        elif self.choco1 == False and self.choco2 == False and self.choco4 == False:
            self.choco3 = False
            jugador1.chocandoder = False
            jugador1.chocandoizq = False
        else:
            self.choco3 = False

        for obstaculo in colision_jugador_obstaculo:

                overlap_x = min(jugador1.rect.right - obstaculo.rect.left, obstaculo.rect.right - jugador1.rect.left)
                overlap_y = min(jugador1.rect.bottom - obstaculo.rect.top, obstaculo.rect.bottom - jugador1.rect.top)

                # Ajusta la posición según la dirección de la superposición
                if overlap_x < overlap_y:
                    # Ajusta en el eje x
                    if jugador1.rect.right > obstaculo.rect.left > jugador1.rect.left:
                        jugador1.chocandoder = True
                      
                    elif jugador1.rect.left < obstaculo.rect.right < jugador1.rect.right:
                        jugador1.chocandoizq = True
                       
                else:
                    # Ajusta en el eje y
                    if jugador1.rect.bottom > obstaculo.rect.top > jugador1.rect.top:
                        jugador1.rect.bottom = obstaculo.rect.top
                        jugador1.tocando_piso = False ##########################
                        jugador1.saltando_champ = True
                    elif jugador1.rect.top < obstaculo.rect.bottom < jugador1.rect.bottom:
                        jugador1.rect.top = obstaculo.rect.bottom


            

    def colision_jugador_caja(self):
        colision_jugador_caja =pygame.sprite.spritecollide(jugador1, self.cajas, False)
        if colision_jugador_caja:
            self.choco4 = True
        elif self.choco1 == False and self.choco2 == False and self.choco3 == False:
            self.choco4 = False
            jugador1.chocandoder = False
            jugador1.chocandoizq = False
        else:
            self.choco4 = False

        for obstaculo in colision_jugador_caja:

                overlap_x = min(jugador1.rect.right - obstaculo.rect.left, obstaculo.rect.right - jugador1.rect.left)
                overlap_y = min(jugador1.rect.bottom - obstaculo.rect.top, obstaculo.rect.bottom - jugador1.rect.top)

                # Ajusta la posición según la dirección de la superposición
                if overlap_x < overlap_y:
                    # Ajusta en el eje x
                    if jugador1.rect.right > obstaculo.rect.left > jugador1.rect.left:
                        jugador1.chocandoder = True

                    elif jugador1.rect.left < obstaculo.rect.right < jugador1.rect.right:
                        jugador1.chocandoizq = True
                else:
                    # Ajusta en el eje y
                    if jugador1.rect.bottom > obstaculo.rect.top > jugador1.rect.top:
                        jugador1.rect.bottom = obstaculo.rect.top
                        jugador1.tocando_piso = True
                        obstaculo.caer()
                        if piso.rect.top <= obstaculo.rect.bottom:
                            obstaculo.kill()
                    elif jugador1.rect.top < obstaculo.rect.bottom < jugador1.rect.bottom:
                        jugador1.rect.top = obstaculo.rect.bottom
        













class Jugador(pygame.sprite.Sprite):
    def __init__(self,posicion_x, posicion_y, nuevo_ancho, nuevo_alto):
        super().__init__()
        self.idle0 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\idle\player-idle-1.png").convert_alpha()
        self.idle0 = pygame.transform.scale(self.idle0, (nuevo_ancho, nuevo_alto))
        self.idle1 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\idle\player-idle-2.png").convert_alpha()
        self.idle1 = pygame.transform.scale(self.idle1, (nuevo_ancho, nuevo_alto))
        self.idle2 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\idle\player-idle-3.png").convert_alpha()
        self.idle2 = pygame.transform.scale(self.idle2, (nuevo_ancho, nuevo_alto))
        self.lista_idle_derecha = [self.idle0, self.idle1, self.idle2]
        self.image = self.lista_idle_derecha[0]
        self.scroll = 600
        self.vidas = 3
        self.cont_poder = 0



        self.rect = self.image.get_rect(center = (posicion_x, posicion_y))
        self.rect.width = 50
        self.rect.height = 80
        self.rect.x = posicion_x
        self.rect.y = posicion_y
        self.velocidad = 10
        self.V_gravedad = 3
        self.altura_salto = 48
        self.velocidad_salto = self.altura_salto
        self.saltando = False
        self.tocando_piso = True
        self.derecha = True
        self.nuevo_ancho = nuevo_ancho
        self.nuevo_alto = nuevo_alto
        #imagenes salto
        self.salto_subida = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\jump\player-jump-1.png").convert_alpha()
        self.salto_subida = pygame.transform.scale(self.salto_subida, (nuevo_ancho, nuevo_alto))
        self.salto_bajada = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\jump\player-jump-2.png").convert_alpha()
        self.salto_bajada = pygame.transform.scale(self.salto_bajada, (nuevo_ancho, nuevo_alto))
        self.lista_salto = [self.salto_subida, self.salto_bajada]

        #imagenes caminando
        self.caminando0 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\\run\player-run-1.png").convert_alpha()
        self.caminando0 = pygame.transform.scale(self.caminando0, (nuevo_ancho, nuevo_alto))
        self.caminando1 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\\run\player-run-2.png").convert_alpha()
        self.caminando1 = pygame.transform.scale(self.caminando1, (nuevo_ancho, nuevo_alto))
        self.caminando2 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\\run\player-run-3.png").convert_alpha()
        self.caminando2 = pygame.transform.scale(self.caminando2, (nuevo_ancho, nuevo_alto))
        self.caminando3 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\\run\player-run-4.png").convert_alpha()
        self.caminando3 = pygame.transform.scale(self.caminando3, (nuevo_ancho, nuevo_alto))
        self.caminando4 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\\run\player-run-5.png").convert_alpha()
        self.caminando4 = pygame.transform.scale(self.caminando4, (nuevo_ancho, nuevo_alto))
        self.caminando5 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\player\\run\player-run-6.png").convert_alpha()
        self.caminando5 = pygame.transform.scale(self.caminando5, (nuevo_ancho, nuevo_alto))
        self.lista_caminando_derecha = [self.caminando0, self.caminando1, self.caminando2, self.caminando3, self.caminando4, self.caminando5]
        #sonido saltar
        self.sonido_saltar = pygame.mixer.Sound('Jump.wav')
        self.sondio_toca_G = pygame.mixer.Sound('toca_M.mp3')
        self.sonido_saltar_reproducido = False
        self.chocandoder = False
        self.chocandoizq = False
        self.saltando_champ = False

        #saltar champ
        self.altura_salto2 = 70
        self.velocidad_salto2 = self.altura_salto2
        
        self.nivel = 1

        self.contador_gemas = 8


        #imagen muerte
        self.muerte0 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\player\hurt\\player-hurt-1.png").convert_alpha()
        self.muerte0 = pygame.transform.scale(self.muerte0, (nuevo_ancho, nuevo_alto))
        self.muerte1 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\player\hurt\\player-hurt-2.png").convert_alpha()
        self.muerte1 = pygame.transform.scale(self.muerte1, (nuevo_ancho, nuevo_alto))
        self.lista_muerte = [self.muerte0, self.muerte1]

        


        

    def mover_derecha(self):
        if self.nivel == 1:
            self.scroll += self.velocidad
        if self.nivel == 2:
            self.rect.x += self.velocidad
        if self.saltando == False:
            tiempo_actual = pygame.time.get_ticks()
            duracion_frame = 100
            frame_index = (tiempo_actual // duracion_frame) % len(self.lista_caminando_derecha)
            self.image = self.lista_caminando_derecha[frame_index]
            

    def mover_izquierda(self):
        if self.nivel == 1:
            self.scroll -= self.velocidad
        if self.nivel == 2:
            self.rect.x -= self.velocidad
        if self.saltando == False:
            tiempo_actual = pygame.time.get_ticks()
            duracion_frame = 100
            frame_index = (tiempo_actual // duracion_frame) % len(self.lista_caminando_derecha)
            self.image = pygame.transform.flip(self.lista_caminando_derecha[frame_index], True, False).convert_alpha()

    

    def idle(self):
        if self.derecha:
            tiempo_acutal = pygame.time.get_ticks()
            duracion_frame = 300  
            frame_index = (tiempo_acutal // duracion_frame) % len(self.lista_idle_derecha)

            self.image = self.lista_idle_derecha[frame_index]
        else:
            tiempo_acutal = pygame.time.get_ticks()
            duracion_frame = 300  
            frame_index = (tiempo_acutal // duracion_frame) % len(self.lista_idle_derecha)

            self.image = pygame.transform.flip(self.lista_idle_derecha[frame_index], True, False)
    
    def muerte(self):
            tiempo_acutal = pygame.time.get_ticks()
            duracion_frame = 100  
            frame_index = (tiempo_acutal // duracion_frame) % len(self.lista_muerte)
            self.image = self.lista_muerte[frame_index]
            self.rect.y +=1
            


    def gravedad(self):#aplicamos gravedad a personaje
        self.rect.y += self.V_gravedad

    def saltar(self):  # Definición de la función para saltar
        self.rect.y -= self.velocidad_salto  # Se resta la velocidad de salto a la posición vertical del objeto
        self.velocidad_salto -= self.V_gravedad  # Se simula la influencia de la gravedad restando la velocidad de salto
        self.sonido_saltar_reproducido = True
        if self.velocidad_salto < -self.altura_salto:  # Verifica si se alcanzó la altura máxima del salto
            self.saltando = False  # Marca que el objeto ha dejado de saltar
            self.velocidad_salto = self.altura_salto  # Restablece la velocidad de salto a la altura máxima del salto
            self.sonido_saltar_reproducido = False
            
        if self.velocidad_salto > 0:
            if self.derecha == True: 
                self.image = self.lista_salto[0]
            else:
                self.image = pygame.transform.flip(self.lista_salto[0], True, False)
        else:
            if self.derecha == True: 
                self.image = self.lista_salto[1]
            else:
                self.image = pygame.transform.flip(self.lista_salto[1], True, False)

    def saltar_champ(self):  # Definición de la función para saltar
        self.rect.y -= self.velocidad_salto2  # Se resta la velocidad de salto a la posición vertical del objeto
        self.velocidad_salto2 -= self.V_gravedad  # Se simula la influencia de la gravedad restando la velocidad de salto
        self.sonido_saltar_reproducido = True
        if self.velocidad_salto2 < -self.altura_salto2:  # Verifica si se alcanzó la altura máxima del salto
            self.saltando_champ = False  # Marca que el objeto ha dejado de saltar
            self.velocidad_salto2 = self.altura_salto2  # Restablece la velocidad de salto a la altura máxima del salto
            self.sonido_saltar_reproducido = False
            
        if self.velocidad_salto2 > 0:
            if self.derecha == True: 
                self.image = self.lista_salto[0]
            else:
                self.image = pygame.transform.flip(self.lista_salto[0], True, False)
        else:
            if self.derecha == True: 
                self.image = self.lista_salto[1]
            else:
                self.image = pygame.transform.flip(self.lista_salto[1], True, False)

    def caer(self):
        if self.derecha == True: 
            self.image = self.lista_salto[1]
        else:
            self.image = pygame.transform.flip(self.lista_salto[1], True, False)

        self.rect.y += 20




    
    




class Piso(pygame.sprite.Sprite):#creamos clase piso que hereda de sprite
    def __init__(self, imagen, posx, posy):#creamos constructor
        super().__init__()#llamamos constructor de clase sprite
        self.image = pygame.image.load(imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, (ancho_pantalla*2, 150))#escalamos la imagen a lo ancho de la pantalla y alto 200
        self.ancho_imagen = self.image.get_width()
        self.alto_imagen = self.image.get_height()
        self.rect = self.image.get_rect()#obtenemos el rectangulo asociado al sprite
        self.rect.x = posx#manipulamos sus coordenadas en x
        self.rect.y = posy#manipulamos sus coordenadas en y


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, imagen, posx, posy, ancho, alto):#creamos constructor
        super().__init__()#llamamos constructor de clase sprite
        self.image = pygame.image.load(imagen).convert_alpha()#cargamos imagen
        self.image = pygame.transform.scale(self.image, (ancho, alto))#escalamos la imagen a lo ancho de la pantalla y alto 200
        self.rect = self.image.get_rect()#obtenemos el rectangulo asociado al sprite
        self.rect.x = posx#manipulamos sus coordenadas en x
        self.rect.y = posy#manipulamos sus coordenadas en y
        self.rect.width = 170
       

    def caer(self):
        self.rect.y += 10

class Obstaculo2(pygame.sprite.Sprite):
    def __init__(self, imagen, posx, posy, ancho, alto):#creamos constructor
        super().__init__()#llamamos constructor de clase sprite
        self.image = pygame.image.load(imagen).convert_alpha()#cargamos imagen
        self.image = pygame.transform.scale(self.image, (ancho, alto))#escalamos la imagen a lo ancho de la pantalla y alto 200
        self.rect = self.image.get_rect()#obtenemos el rectangulo asociado al sprite
        self.rect.x = posx#manipulamos sus coordenadas en x
        self.rect.y = posy#manipulamos sus coordenadas en y
        self.rect.width = 440
        self.rect.height = 425


class Poder(pygame.sprite.Sprite):
    def __init__(self, posx, posy):#creamos constructor
        super().__init__()#llamamos constructor de clase sprite
        ancho = 50
        alto = 50
        self.imagen1 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\item-feedback\\item-feedback-1.png").convert_alpha()#cargamos imagen
        self.imagen1 = pygame.transform.scale(self.imagen1, (ancho, alto))#escalamos la imagen a lo ancho de la pantalla y alto 200
        self.imagen2 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\item-feedback\\item-feedback-2.png").convert_alpha()#cargamos imagen
        self.imagen2 = pygame.transform.scale(self.imagen2, (ancho, alto))#escalamos la imagen a lo ancho de la pantalla y alto 200
        self.imagen3 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\item-feedback\\item-feedback-3.png").convert_alpha()#cargamos imagen
        self.imagen3 = pygame.transform.scale(self.imagen3, (ancho, alto))#escalamos la imagen a lo ancho de la pantalla y alto 200
        self.imagen4 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\item-feedback\\item-feedback-4.png").convert_alpha()#cargamos imagen
        self.imagen4 = pygame.transform.scale(self.imagen4, (ancho, alto))#escalamos la imagen a lo ancho de la pantalla y alto 200
        self.imagen_lista = [self.imagen1, self.imagen2, self.imagen3, self.imagen4]
        self.image = self.imagen_lista[0]
        self.rect = self.image.get_rect()#obtenemos el rectangulo asociado al sprite
        self.rect.x = posx#manipulamos sus coordenadas en x
        self.rect.y = posy#manipulamos sus coordenadas en y
       # self.rect.width = 440
       # self.rect.height = 425
    def idle(self):
        tiempo_acutal = pygame.time.get_ticks()
        duracion_frame = 100  
        frame_index = (tiempo_acutal // duracion_frame) % len(self.imagen_lista)

        self.image = self.imagen_lista[frame_index]


class Piedra(pygame.sprite.Sprite):
    def __init__(self, posx, posy):#creamos constructor
        super().__init__()#llamamos constructor de clase sprite
        ancho = 70
        alto = 70
        self.image = pygame.image.load("Sunny-land-files\\Graphical Assets\\environment\\Props\\face-block.png").convert_alpha()#cargamos imagen
        self.image = pygame.transform.scale(self.image, (ancho, alto))#escalamos la imagen a lo ancho de la pantalla y alto 200
        self.rect = self.image.get_rect()#obtenemos el rectangulo asociado al sprite
        self.rect.x = posx#manipulamos sus coordenadas en x
        self.rect.y = posy#manipulamos sus coordenadas en y
       # self.rect.width = 440
       # self.rect.height = 425
        
    def piedra_A(self):
        self.rect.y += 14

    def piedra_S(self):
        self.rect.y -= 6

class Champin(pygame.sprite.Sprite):
    def __init__(self, imagen, posx, posy, ancho, alto):#creamos constructor
        super().__init__()#llamamos constructor de clase sprite
        self.image = pygame.image.load(imagen).convert_alpha()#cargamos imagen
        self.image = pygame.transform.scale(self.image, (ancho*1.5, alto*1.5))#escalamos la imagen a lo ancho de la pantalla y alto 200
        self.rect = self.image.get_rect()#obtenemos el rectangulo asociado al sprite
        self.rect.x = posx#manipulamos sus coordenadas en x
        self.rect.y = posy#manipulamos sus coordenadas en y
        #self.rect.width = 90
       

       


       

class Gema(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.imagen1 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\gem\gem-1.png").convert_alpha()
        self.imagen1 = pygame.transform.scale(self.imagen1,(34,34))
        self.imagen2 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\gem\gem-2.png").convert_alpha()
        self.imagen2 = pygame.transform.scale(self.imagen2,(34,34))
        self.imagen3 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\gem\gem-3.png").convert_alpha()
        self.imagen3 = pygame.transform.scale(self.imagen3,(34,34))
        self.imagen4 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\gem\gem-4.png").convert_alpha()
        self.imagen4 = pygame.transform.scale(self.imagen4,(34,34))
        self.imagen5 = pygame.image.load("Sunny-land-files\Graphical Assets\sprites\gem\gem-5.png").convert_alpha()
        self.imagen5 = pygame.transform.scale(self.imagen5,(34,34))
        self.lista_gemas = [self.imagen1, self.imagen2, self.imagen3, self.imagen4, self.imagen5]
        self.image = self.lista_gemas[0]
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def idle(self):
        tiempo_acutal = pygame.time.get_ticks()
        duracion_frame = 200  
        frame_index = (tiempo_acutal // duracion_frame) % len(self.lista_gemas)

        self.image = self.lista_gemas[frame_index]

class EnemigoFinal(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        ancho = 864
        alto = 864
        self.vivo = True
        self.Nataque = 0
        self.crear = False
        self.rectangulo_ancho = 300
        self.tiempo_ataque = 8
        #imagenes caminar
        self.imagen_caminar1 = pygame.image.load("animacion_M\\caminar\\tile000.png").convert_alpha()
        self.imagen_caminar1 = pygame.transform.scale(self.imagen_caminar1, (ancho, alto))

        self.imagen_caminar2 = pygame.image.load("animacion_M\\caminar\\tile001.png").convert_alpha()
        self.imagen_caminar2 = pygame.transform.scale(self.imagen_caminar2, (ancho, alto))

        self.imagen_caminar3 = pygame.image.load("animacion_M\\caminar\\tile002.png").convert_alpha()
        self.imagen_caminar3 = pygame.transform.scale(self.imagen_caminar3, (ancho, alto))

        self.imagen_caminar4 = pygame.image.load("animacion_M\\caminar\\tile003.png").convert_alpha()
        self.imagen_caminar4 = pygame.transform.scale(self.imagen_caminar4, (ancho, alto))

        self.imagen_caminar5 = pygame.image.load("animacion_M\\caminar\\tile004.png").convert_alpha()
        self.imagen_caminar5 = pygame.transform.scale(self.imagen_caminar5, (ancho, alto))

        self.imagen_caminar6 = pygame.image.load("animacion_M\\caminar\\tile005.png").convert_alpha()
        self.imagen_caminar6 = pygame.transform.scale(self.imagen_caminar6, (ancho, alto))

        self.imagen_caminar7 = pygame.image.load("animacion_M\\caminar\\tile006.png").convert_alpha()
        self.imagen_caminar7 = pygame.transform.scale(self.imagen_caminar7, (ancho, alto))

        self.imagen_caminar8 = pygame.image.load("animacion_M\\caminar\\tile007.png").convert_alpha()
        self.imagen_caminar8 = pygame.transform.scale(self.imagen_caminar8, (ancho, alto))

        self.imagen_caminar9 = pygame.image.load("animacion_M\\caminar\\tile008.png").convert_alpha()
        self.imagen_caminar9 = pygame.transform.scale(self.imagen_caminar9, (ancho, alto))

        self.imagen_caminar10 = pygame.image.load("animacion_M\\caminar\\tile009.png").convert_alpha()
        self.imagen_caminar10 = pygame.transform.scale(self.imagen_caminar10, (ancho, alto))

        self.imagen_caminar11 = pygame.image.load("animacion_M\\caminar\\tile010.png").convert_alpha()
        self.imagen_caminar11 = pygame.transform.scale(self.imagen_caminar11, (ancho, alto))

        self.imagen_caminar12 = pygame.image.load("animacion_M\\caminar\\tile011.png").convert_alpha()
        self.imagen_caminar12 = pygame.transform.scale(self.imagen_caminar12, (ancho, alto))

        self.imagen_caminar13 = pygame.image.load("animacion_M\\caminar\\tile012.png").convert_alpha()
        self.imagen_caminar13 = pygame.transform.scale(self.imagen_caminar13, (ancho, alto))

        self.imagen_caminar14 = pygame.image.load("animacion_M\\caminar\\tile013.png").convert_alpha()
        self.imagen_caminar14 = pygame.transform.scale(self.imagen_caminar14, (ancho, alto))

        self.imagen_caminar15 = pygame.image.load("animacion_M\\caminar\\tile014.png").convert_alpha()
        self.imagen_caminar15 = pygame.transform.scale(self.imagen_caminar15, (ancho, alto))

        self.imagen_caminar16 = pygame.image.load("animacion_M\\caminar\\tile015.png").convert_alpha()
        self.imagen_caminar16 = pygame.transform.scale(self.imagen_caminar16, (ancho, alto))

        self.lista_caminar = [self.imagen_caminar1, self.imagen_caminar2, self.imagen_caminar3, self.imagen_caminar4,
                              self.imagen_caminar5, self.imagen_caminar6, self.imagen_caminar7, self.imagen_caminar8,
                              self.imagen_caminar9, self.imagen_caminar10, self.imagen_caminar11, self.imagen_caminar12,
                              self.imagen_caminar13, self.imagen_caminar14, self.imagen_caminar15, self.imagen_caminar16]
        
        self.image = self.lista_caminar[0]
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.rect.width = 300
        self.rect.height = 300



        self.idle1 = pygame.image.load("animacion_M\\idle\\tile000.png").convert_alpha()
        self.idle1 = pygame.transform.scale(self.idle1, (ancho, alto))

        self.idle2 = pygame.image.load("animacion_M\\idle\\tile001.png").convert_alpha()
        self.idle2 = pygame.transform.scale(self.idle2, (ancho, alto))

        self.idle3 = pygame.image.load("animacion_M\\idle\\tile002.png").convert_alpha()
        self.idle3 = pygame.transform.scale(self.idle3, (ancho, alto))

        self.idle4 = pygame.image.load("animacion_M\\idle\\tile003.png").convert_alpha()
        self.idle4 = pygame.transform.scale(self.idle4, (ancho, alto))

        self.idle5 = pygame.image.load("animacion_M\\idle\\tile004.png").convert_alpha()
        self.idle5 = pygame.transform.scale(self.idle5, (ancho, alto))

        self.idle6 = pygame.image.load("animacion_M\\idle\\tile005.png").convert_alpha()
        self.idle6 = pygame.transform.scale(self.idle6, (ancho, alto))

        self.idle7 = pygame.image.load("animacion_M\\idle\\tile006.png").convert_alpha()
        self.idle7 = pygame.transform.scale(self.idle7, (ancho, alto))

        self.idle8 = pygame.image.load("animacion_M\\idle\\tile007.png").convert_alpha()
        self.idle8 = pygame.transform.scale(self.idle8, (ancho, alto))

        self.idle9 = pygame.image.load("animacion_M\\idle\\tile008.png").convert_alpha()
        self.idle9 = pygame.transform.scale(self.idle9, (ancho, alto))

        self.idle10 = pygame.image.load("animacion_M\\idle\\tile009.png").convert_alpha()
        self.idle10 = pygame.transform.scale(self.idle10, (ancho, alto))

        self.idle11 = pygame.image.load("animacion_M\\idle\\tile010.png").convert_alpha()
        self.idle11 = pygame.transform.scale(self.idle11, (ancho, alto))

        self.idle12 = pygame.image.load("animacion_M\\idle\\tile011.png").convert_alpha()
        self.idle12 = pygame.transform.scale(self.idle12, (ancho, alto))

        self.idle13 = pygame.image.load("animacion_M\\idle\\tile012.png").convert_alpha()
        self.idle13 = pygame.transform.scale(self.idle13, (ancho, alto))

        self.idle14 = pygame.image.load("animacion_M\\idle\\tile013.png").convert_alpha()
        self.idle14 = pygame.transform.scale(self.idle14, (ancho, alto))

        self.idle15 = pygame.image.load("animacion_M\\idle\\tile014.png").convert_alpha()
        self.idle15 = pygame.transform.scale(self.idle15, (ancho, alto))

        self.idle16 = pygame.image.load("animacion_M\\idle\\tile015.png").convert_alpha()
        self.idle16 = pygame.transform.scale(self.idle16, (ancho, alto))

        self.lista_idle = [self.idle1, self.idle2, self.idle3, self.idle4, self.idle5, self.idle6, self.idle7, self.idle8, self.idle9,
                           self.idle10, self.idle11, self.idle12, self.idle13, self.idle14, self.idle15, self.idle16]
        

        #imagenes ataque1
        self.lista_ataque1 = [
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile000.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile001.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile002.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile003.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile004.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile005.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile006.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile007.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile008.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile009.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile010.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile011.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile012.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile013.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile014.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque1\\tile015.png").convert_alpha(), (ancho, alto)),
        ]

        #imagenes ataque2

        self.lista_ataque2 = [
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile000.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile001.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile002.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile003.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile004.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile005.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile006.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile007.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile008.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile009.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile010.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile011.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile012.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile013.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile014.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\ataque2\\tile015.png").convert_alpha(), (ancho, alto)),
        ]
        
        #imagenes ataque3

        

        self.lista_ataque3 = [
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile000.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile001.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile002.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile003.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile004.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile005.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile006.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile007.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile008.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile009.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile010.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile011.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile012.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile013.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile014.png").convert_alpha(), (ancho, alto)),
            pygame.transform.scale(pygame.image.load("animacion_M\\slap\\tile015.png").convert_alpha(), (ancho, alto)),
        ]




    def crear_ataque1(self):
        tiempo_acutal = pygame.time.get_ticks()
        duracion_frame = 100  
        total_frames = len(self.lista_ataque1)
        
        frame_index = (tiempo_acutal // duracion_frame) % total_frames

        self.image = pygame.transform.flip(self.lista_ataque1[frame_index], True, False).convert_alpha()
        return frame_index
    
    def crear_ataque2(self):

        tiempo_acutal = pygame.time.get_ticks()
        duracion_frame = 100  
        total_frames = len(self.lista_ataque2)
        
        frame_index = (tiempo_acutal // duracion_frame) % total_frames

        self.image = pygame.transform.flip(self.lista_ataque2[frame_index], True, False).convert_alpha()
        return frame_index
    

    
    def crear_ataque3(self):
        tiempo_acutal = pygame.time.get_ticks()
        duracion_frame = 100  
        total_frames = len(self.lista_ataque3)
        
        frame_index = (tiempo_acutal // duracion_frame) % total_frames

        self.image = pygame.transform.flip(self.lista_ataque3[frame_index], True, False).convert_alpha()
        return frame_index
    
         
            
       



    def idle(self):
        tiempo_acutal = pygame.time.get_ticks()
        duracion_frame = 100  
        frame_index = (tiempo_acutal // duracion_frame) % len(self.lista_idle)

        self.image = self.lista_idle[frame_index]
        self.image = pygame.transform.flip(self.lista_idle[frame_index], True, False).convert_alpha()

    def seleccionar_ataque(self):
        ataque = r.randint(1, 3)
        return ataque
        



    def caminar(self):
        self.rect.x -= 3
        tiempo_acutal = pygame.time.get_ticks()
        duracion_frame = 100  
        frame_index = (tiempo_acutal // duracion_frame) % len(self.lista_caminar)

        self.image = self.lista_caminar[frame_index]
        self.image = pygame.transform.flip(self.lista_caminar[frame_index], True, False).convert_alpha()



class Mini_jefe(pygame.sprite.Sprite):
    def __init__(self, posx, posy):#creamos constructor
        super().__init__()#llamamos contructor de clase sprite
        ancho = 364
        alto = 364
        self.velocidad = 9

        #imagenes caminar
        self.imagen_caminar1 = pygame.image.load("animacion_M\\caminar\\tile000.png").convert_alpha()
        self.imagen_caminar1 = pygame.transform.scale(self.imagen_caminar1, (ancho, alto))

        self.imagen_caminar2 = pygame.image.load("animacion_M\\caminar\\tile001.png").convert_alpha()
        self.imagen_caminar2 = pygame.transform.scale(self.imagen_caminar2, (ancho, alto))

        self.imagen_caminar3 = pygame.image.load("animacion_M\\caminar\\tile002.png").convert_alpha()
        self.imagen_caminar3 = pygame.transform.scale(self.imagen_caminar3, (ancho, alto))

        self.imagen_caminar4 = pygame.image.load("animacion_M\\caminar\\tile003.png").convert_alpha()
        self.imagen_caminar4 = pygame.transform.scale(self.imagen_caminar4, (ancho, alto))

        self.imagen_caminar5 = pygame.image.load("animacion_M\\caminar\\tile004.png").convert_alpha()
        self.imagen_caminar5 = pygame.transform.scale(self.imagen_caminar5, (ancho, alto))

        self.imagen_caminar6 = pygame.image.load("animacion_M\\caminar\\tile005.png").convert_alpha()
        self.imagen_caminar6 = pygame.transform.scale(self.imagen_caminar6, (ancho, alto))

        self.imagen_caminar7 = pygame.image.load("animacion_M\\caminar\\tile006.png").convert_alpha()
        self.imagen_caminar7 = pygame.transform.scale(self.imagen_caminar7, (ancho, alto))

        self.imagen_caminar8 = pygame.image.load("animacion_M\\caminar\\tile007.png").convert_alpha()
        self.imagen_caminar8 = pygame.transform.scale(self.imagen_caminar8, (ancho, alto))

        self.imagen_caminar9 = pygame.image.load("animacion_M\\caminar\\tile008.png").convert_alpha()
        self.imagen_caminar9 = pygame.transform.scale(self.imagen_caminar9, (ancho, alto))

        self.imagen_caminar10 = pygame.image.load("animacion_M\\caminar\\tile009.png").convert_alpha()
        self.imagen_caminar10 = pygame.transform.scale(self.imagen_caminar10, (ancho, alto))

        self.imagen_caminar11 = pygame.image.load("animacion_M\\caminar\\tile010.png").convert_alpha()
        self.imagen_caminar11 = pygame.transform.scale(self.imagen_caminar11, (ancho, alto))

        self.imagen_caminar12 = pygame.image.load("animacion_M\\caminar\\tile011.png").convert_alpha()
        self.imagen_caminar12 = pygame.transform.scale(self.imagen_caminar12, (ancho, alto))

        self.imagen_caminar13 = pygame.image.load("animacion_M\\caminar\\tile012.png").convert_alpha()
        self.imagen_caminar13 = pygame.transform.scale(self.imagen_caminar13, (ancho, alto))

        self.imagen_caminar14 = pygame.image.load("animacion_M\\caminar\\tile013.png").convert_alpha()
        self.imagen_caminar14 = pygame.transform.scale(self.imagen_caminar14, (ancho, alto))

        self.imagen_caminar15 = pygame.image.load("animacion_M\\caminar\\tile014.png").convert_alpha()
        self.imagen_caminar15 = pygame.transform.scale(self.imagen_caminar15, (ancho, alto))

        self.imagen_caminar16 = pygame.image.load("animacion_M\\caminar\\tile015.png").convert_alpha()
        self.imagen_caminar16 = pygame.transform.scale(self.imagen_caminar16, (ancho, alto))

        self.lista_caminar = [self.imagen_caminar1, self.imagen_caminar2, self.imagen_caminar3, self.imagen_caminar4,
                              self.imagen_caminar5, self.imagen_caminar6, self.imagen_caminar7, self.imagen_caminar8,
                              self.imagen_caminar9, self.imagen_caminar10, self.imagen_caminar11, self.imagen_caminar12,
                              self.imagen_caminar13, self.imagen_caminar14, self.imagen_caminar15, self.imagen_caminar16]
        
        self.image = self.lista_caminar[0]
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.rect.width = 90
        self.rect.height = 110

    def caminar(self):
        self.rect.x -= self.velocidad
        tiempo_acutal = pygame.time.get_ticks()
        duracion_frame = 100  
        frame_index = (tiempo_acutal // duracion_frame) % len(self.lista_caminar)

        self.image = self.lista_caminar[frame_index]
        self.image = pygame.transform.flip(self.lista_caminar[frame_index], True, False).convert_alpha()



class Enemigo1(pygame.sprite.Sprite):#creamos clase enemigo que hereda de sprite
    def __init__(self, posx, posy):#creamos constructor
        super().__init__()#llamamos contructor de clase sprite
        self.imagen1 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\opossum\\opossum-1.png").convert_alpha()#cargamos imagen
        self.imagen1= pygame.transform.scale(self.imagen1, (110, 110))#escalamos imagen
        self.imagen2 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\opossum\\opossum-2.png").convert_alpha()#cargamos imagen
        self.imagen2= pygame.transform.scale(self.imagen2, (110, 110))#escalamos imagen
        self.imagen3 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\opossum\\opossum-3.png").convert_alpha()#cargamos imagen
        self.imagen3= pygame.transform.scale(self.imagen3, (110, 110))#escalamos imagen
        self.imagen4 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\opossum\\opossum-4.png").convert_alpha()#cargamos imagen
        self.imagen4= pygame.transform.scale(self.imagen4, (110, 110))#escalamos imagen
        self.imagen5 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\opossum\\opossum-5.png").convert_alpha()#cargamos imagen
        self.imagen5= pygame.transform.scale(self.imagen5, (110, 110))#escalamos imagen
        self.imagen6 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\opossum\\opossum-6.png").convert_alpha()#cargamos imagen
        self.imagen6= pygame.transform.scale(self.imagen6, (110, 110))#escalamos imagen
        self.lista_caminar = [self.imagen1, self.imagen2, self.imagen3, self.imagen4, self.imagen5, self.imagen6]
        self.image = self.lista_caminar[0]
        self.rect = self.image.get_rect()#obtenemos rectangulo asociado a la imagen
        self.rect.x = posx#manipulamos sus coordenadas en x
        self.rect.y = posy#manipulamos sus coordenadas en y
        self.rect.width = 85
        self.rect.height = 65



    def mover(self):#movemos al enemigo a la izquierda
        self.rect.x -= 10
        tiempo_acutal = pygame.time.get_ticks()
        duracion_frame = 200  
        frame_index = (tiempo_acutal // duracion_frame) % len(self.lista_caminar)

        self.image = self.lista_caminar[frame_index]

class Enemigo2(pygame.sprite.Sprite):
    def __init__(self, posx, posy):#creamos constructor
        super().__init__()#llamamos contructor de clase sprite
        self.imagen1 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\eagle\\eagle-attack-1.png").convert_alpha()#cargamos imagen
        self.imagen1= pygame.transform.scale(self.imagen1, (110, 110))#escalamos imagen
        #self.imagen1 = pygame.transform.flip(self.imagen1, True, False)#volteamos imagen
        self.imagen2 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\eagle\\eagle-attack-2.png").convert_alpha()#cargamos imagen
        self.imagen2= pygame.transform.scale(self.imagen2, (110, 110))#escalamos imagen
       # self.imagen2 = pygame.transform.flip(self.imagen2, True, False)#volteamos imagen
        self.imagen3 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\eagle\\eagle-attack-3.png").convert_alpha()#cargamos imagen
        self.imagen3= pygame.transform.scale(self.imagen3, (110, 110))#escalamos imagen
        #self.imagen3 = pygame.transform.flip(self.imagen3, True, False)#volteamos imagen
        self.imagen4 = pygame.image.load("Sunny-land-files\\Graphical Assets\\sprites\\eagle\\eagle-attack-4.png").convert_alpha()#cargamos imagen
        self.imagen4= pygame.transform.scale(self.imagen4, (110, 110))#escalamos imagen
        self.lista_volar = [self.imagen1, self.imagen2, self.imagen3, self.imagen4]
        self.image = self.lista_volar[0]
        self.rect = self.image.get_rect()#obtenemos rectangulo asociado a la imagen
        self.rect.x = posx#manipulamos sus coordenadas en x
        self.rect.y = posy#manipulamos sus coordenadas en y
        self.rect.width = 85
        self.rect.height = 65
    def mover(self):#movemos al enemigo a la izquierda
        self.rect.x -= 14
        tiempo_acutal = pygame.time.get_ticks()
        duracion_frame = 200  
        frame_index = (tiempo_acutal // duracion_frame) % len(self.lista_volar)

        self.image = self.lista_volar[frame_index]



class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.image.load("bola.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def mover(self):
        self.rect.x +=10




class Vidas(pygame.sprite.Sprite):
    def __init__(self, imagen, posx):
        super().__init__()
        self.image = pygame.image.load(imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = 30

pygame.init()#iniciamos libreria pygame
reloj = pygame.time.Clock()#creamos objeto reloj
info = pygame.display.Info()#creamos objeto info (sirve para obtener informacion de pantalla)
ancho_pantalla = info.current_w#obtenemos la informacion del ancho de pantalla
alto_pantalla = info.current_h#obtenemos la informacion del alto de pantalla
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))#creamos pantalla con ancho y alto
jugador1 = Jugador(700, 700, 124, 124)#creamos objeto jugador
piso = Piso("ground.png", 0, alto_pantalla-150)#creamos objeto piso dentro del nivel
nivel1 = Mundo(piso, "plx-1.png", "plx-2.png", "plx-3.png", "plx-4.png", "plx-5.png")
teclas_jugador = {#diccionario de controles del jugador
        pygame.K_a: "izquierda",
        pygame.K_d: "derecha",
        pygame.K_SPACE: "saltar",
        pygame.K_f : "disparo",
    }

jefe = EnemigoFinal(ancho_pantalla +200, 420)
nivel1.crear_jefe(jefe)



def cargar_musica(cancion_actual):
        lista_canciones = [
            "Music by Ansimuz\\magic cliffs.ogg",
            "Music by Ansimuz\\dark-happy-world.ogg",
            "Music by Ansimuz\\summer nights.ogg",
            "Music by Ansimuz\\under the rainbow.ogg",
            "Music by Ansimuz\\up_and_right.ogg",
            "Music by Ansimuz\\happywalking.ogg"

        ]
        pygame.mixer.music.load(lista_canciones[cancion_actual])
        pygame.mixer.music.play()       

class Texto():
    def __init__(self, color_texto, size_font,texto, posx, posy):
        self.color_texto = color_texto
        self.texto_dado = texto
        self.fuente = pygame.font.Font(None, size_font)
        self.texto = self.fuente.render(self.texto_dado, True, self.color_texto)
        self.rect = self.texto.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def actualizar_color(self, nuevo_color):
        self.color_texto = nuevo_color
        self.texto = self.fuente.render(self.texto_dado, True, self.color_texto)

    def actualizar_texto(self):
        self.texto_dado = f"Gemas restantes {jugador1.contador_gemas}"
        self.texto = self.fuente.render(self.texto_dado, True, self.color_texto)
    
def transicion():
    pygame.display.set_caption("Transición")

    # Colores
    color_fondo = (0,0,0)
    color_rectangulo = (0, 255, 0)
    cargando = Texto((255, 255, 255), 106, "Cargando", ancho_pantalla / 2 - 150, alto_pantalla / 2 - 250)

    # Variables del rectángulo
    rectangulo_ancho = 0
    rectangulo_alto = 100
    rectangulo_velocidad = 5
    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False

        # Actualizar el ancho del rectángulo
        rectangulo_ancho += rectangulo_velocidad
        if rectangulo_ancho >= ancho_pantalla:
            juego()
            ejecutando = False

        # Dibujar en la pantalla
        pantalla.fill(color_fondo)
        pygame.draw.rect(pantalla, color_rectangulo, (0, alto_pantalla/2, rectangulo_ancho, rectangulo_alto))
        pantalla.blit(cargando.texto, (cargando.rect.x, cargando.rect.y))
        pantalla.set_alpha(0)


        # Actualizar la pantalla
        pygame.display.update()

        # Establecer la velocidad de actualización
        reloj.tick(60)
    


def menu():
    imagen = pygame.image.load("img/Background/mountain.png").convert_alpha()
    imagen = pygame.transform.scale(imagen, (ancho_pantalla*2, alto_pantalla))
    pygame.mixer.music.load("Music by Ansimuz/Hurt_and_heart.ogg")
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Menú")

    rectangulo = pygame.Rect(0, 100, ancho_pantalla*2, 100)
    rectangulo2 = pygame.Rect(ancho_pantalla*2, 100, ancho_pantalla*2, 100)

    boton_jugar = Texto((255, 255, 255), 106, "Jugar", ancho_pantalla / 2 - 150, alto_pantalla / 2 - 250)
    boton_salir = Texto((255, 255, 255), 106, "Salir", ancho_pantalla / 2 - 150, alto_pantalla / 2)

    menu_ejecutando = True
    print(menu_ejecutando)

    while menu_ejecutando:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_ejecutando = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        botones_raton = pygame.mouse.get_pressed()


        if boton_jugar.rect.collidepoint(mouse_x, mouse_y):
            boton_jugar.actualizar_color((0, 255, 0))
            if botones_raton[0]:
                pygame.mixer.music.stop()
                transicion()
               # menu_ejecutando = False
                
        else:
            boton_jugar.actualizar_color((255, 255, 255))

        if boton_salir.rect.collidepoint(mouse_x, mouse_y):
            boton_salir.actualizar_color((255, 0, 0))
            if botones_raton[0]:
                menu_ejecutando = False
        else:
            boton_salir.actualizar_color((255, 255, 255))

        # Manejar el desplazamiento del fondo
        pantalla.fill((135, 206, 235))
        pantalla.blit(imagen, (rectangulo.x, 0))
        pantalla.blit(imagen, (rectangulo2.x, 0))
        rectangulo.x -= 2
        rectangulo2.x -= 2
        if rectangulo.right <= 0:
            rectangulo.x = ancho_pantalla
        if rectangulo2.right <= 0:
            rectangulo2.x = ancho_pantalla

        pantalla.blit(boton_jugar.texto, (boton_jugar.rect.x, boton_jugar.rect.y))
        pantalla.blit(boton_salir.texto, (boton_salir.rect.x, boton_salir.rect.y))
       # pygame.draw.rect(pantalla, (255, 255, 255), rectangulo) #dibujando rectangulo
       # pygame.draw.rect(pantalla, (0, 255, 0), rectangulo2) # dibujando rectangulo
        reloj.tick(60)
        pygame.display.update()


def crear_enemigo1(x):
    posy = 700
    posx = jugador1.rect.x + x
    enemigo = Enemigo1(posx, posy)     
    return enemigo 

def crear_enemigo2(x,y):
    enemigo = Enemigo2(x+jugador1.rect.x, y)
    return enemigo

def crear_obstaculo(x, y):
    obstaculo = Obstaculo("piso.png", x, y, 120, 120)
    nivel1.Generarobstaculos(obstaculo)

def crear_caja(x, y):
    obstaculo = Obstaculo("Sunny-land-files\\Graphical Assets\\environment\\Props\\big-crate.png", x, y, 120, 120)
    nivel1.agregar_caja(obstaculo)

def crear_bloqueo(x,y):
    obstaculo = Obstaculo2("Sunny-land-files\\Graphical Assets\\environment\\Props\\face-block.png", x, y, 440, 440)
    nivel1.agregar_obstaculo2(obstaculo)
    
def crear_gema(x,y):
    gema = Gema(x, y)
    nivel1.agregar_gema(gema)

def crear_champ(x, y):
    champ = Champin("Hongo.png", x, y, 64, 64)
    nivel1.agregar_champ(champ)

def crear_minijefe(x,y):
    mini = Mini_jefe(x,y)
    nivel1.agregar_miniboss(mini)

def crear_piedra_S(x,y):
    piedra = Piedra(x,y)
    nivel1.crear_piedra_suelo(piedra)

def crear_piedra_A(x,y):
    piedra = Piedra(x,y)
    nivel1.crear_piedra_aire(piedra)

def crear_poder(x,y):
    poder = Poder(x,y)
    nivel1.agregar_poder(poder)

def crear_proyectil(x,y):
    pro = Proyectil(x,y)
    nivel1.agregar_proyectil(pro)

def juego():#funcion del nivel 1
    jugador1.rect.y = 700
    jugador1.rect.x = 700
    jugador1.scroll = 600
    rectangulo_alto = 60
    color_rectangulo = (0, 255, 0)
    
    movimiento = False
    ejecutando = True#booleano para saber cuando parar el loop del juego
    cancion = 0
    acder = False
    acizq = False
    pygame.display.set_caption("Nivel 1")#asignamos titulo a la pantalla
    pantalla.fill((0, 0, 0))
    vida1 = Vidas("Sunny-land-files\\Graphical Assets\\sprites\\cherry\\cherry-1.png", 0)
    vida2 = Vidas("Sunny-land-files\\Graphical Assets\\sprites\\cherry\\cherry-1.png", 80)
    vida3 = Vidas("Sunny-land-files\\Graphical Assets\\sprites\\cherry\\cherry-1.png", 160)
    crear_gema(1550, 420)
    crear_obstaculo(1500, 550)
    crear_obstaculo(2500, 500)
    crear_obstaculo(2720, 250)
    crear_gema(3065, 150)
    crear_obstaculo(3030, 250)
    crear_gema(5040, 480)
    crear_caja(5000, 480)
    crear_caja(4500, 480)
    crear_caja(4200, 480)
    crear_bloqueo(7000, 310)
    crear_champ(6840, 640)
    crear_champ(7520, 640)
    crear_gema(7200, 200)
    crear_obstaculo(9800, 330)
    crear_obstaculo(10100, 500)
    crear_obstaculo(9500, 330)
    crear_obstaculo(9200, 330)
    crear_champ(9180, 240)
    crear_obstaculo(8786, 330)
    crear_gema(8820, 290)
    crear_gema(13000, 550)
    crear_champ(15500, 640)
    crear_obstaculo(15790, 330)
    crear_bloqueo(16000, 310)
    crear_champ(16650, 640)
    crear_gema(16900, 200)

    crear_obstaculo(22000, 420)
    crear_obstaculo(22400, 330)
    crear_obstaculo(22800, 330)
    crear_obstaculo(23200, 330)
    crear_obstaculo(23600, 330)
    crear_bloqueo(24000, 310)
    crear_champ(24660, 640)


    crear_gema(27000, 500)

    nivel1.agregar_vidas(vida1)
    nivel1.agregar_vidas(vida2)
    nivel1.agregar_vidas(vida3)

    lista = []
    tiempo_inicial = t.time()
    tiempo2 = t.time()



    #nivel2
    
    
    
    
    gemas_obtenidas = Texto((255, 255, 255), 36, f"Gemas restantes {jugador1.contador_gemas}", ancho_pantalla -300, 30)
    instancia = True


    tiempo_ataque_e = t.time()
    tiempo_poder = t.time()
    eliminar_poder = t.time()


    while ejecutando:#loop o bucle del juego
       

        if jugador1.nivel == 1:
            gemas_obtenidas.actualizar_texto()
        
        if jugador1.nivel == 1:
            #logica de generacion de enemigos:
            tiempo_actual = t.time()
            if tiempo_actual - tiempo_inicial >= 9:   
                n_enemigos = r.randint(1, 6)
                for i in range(n_enemigos):
                    pos = r.randint(1000, 4200)
                    enemigo = crear_enemigo1(pos)
                    nivel1.Generarenemigos(enemigo)
                tiempo_inicial = tiempo_actual
            t2 = t.time()
            if t2 - tiempo2 >= 20:
                n_enemigos2 = r.randint(1, 3)
                for i in range(n_enemigos2):
                    posicionx = r.randint(1000, 4200)
                    posiciony =r.randint(60, 600)
                    enemigo = crear_enemigo2(posicionx, posiciony)
                    nivel1.Generarenemigos(enemigo)
                tiempo2 = t2

        




        for evento in pygame.event.get():#obtenemos todos los eventos del juego
            if evento.type == pygame.QUIT:#si cerramos la ventana con la equis de la esquina acabar el juego
                ejecutando = False
        for tecla, accion in teclas_jugador.items():#crear iterable clave, valor de nuestro diccionario

            if jugador1.vidas != 0:
                if pygame.key.get_pressed()[tecla]:#preguntamos si una de las teclas de nuestro diccionario a sido presionada
                    if accion == "derecha":
                        acder = True
                        acizq = False
                        lista.append("derecha")
                    elif accion == "izquierda":
                        acizq = True
                        acder = False
                        lista.append("izquierda")
                    else:
                        acder = False
                        acizq = False
                    if len(lista) != 1:
                        acizq = False
                        acder = False
                    if jugador1.nivel == 1:
                        if acder:
                            jugador1.derecha = True
                            if jugador1.chocandoder == False:
                                jugador1.mover_derecha()#mover a la derecha el jugador
                                movimiento = True
                            
                        if acizq:
                            if jugador1.scroll > 0:#condicion para no salir de la pantalla
                                jugador1.derecha = False
                                if jugador1.chocandoizq == False:
                                    jugador1.mover_izquierda()#mover a la derecha el izquierda
                                    movimiento = True
                                
                    if jugador1.nivel == 2:
                        if acder:
                            jugador1.derecha = True
                            if jugador1.rect.right <= ancho_pantalla:
                                if jugador1.chocandoder == False:
                                    jugador1.mover_derecha()#mover a la derecha el jugador
                                    movimiento = True
                                
                        elif acizq:
                            jugador1.derecha = False
                            if jugador1.rect.left >= 0:
                                if jugador1.chocandoizq == False:
                                    jugador1.mover_izquierda()#mover a la derecha el izquierda
                                    movimiento = True
                                    
                
                    if accion == "saltar":#si el valor devuelto es saltar
                        if jugador1.tocando_piso:
                            jugador1.saltando = True#asignar booleano saltando a verdad
                    if accion == "disparo" and jugador1.cont_poder >0:
                        crear_proyectil(jugador1.rect.x, jugador1.rect.y)
                        jugador1.cont_poder -=1


            teclas_presionadas = pygame.key.get_pressed()
            if not any(teclas_presionadas):
                jugador1.idle()
                
                    

        jugador1.gravedad()#llamar la funcion gravedad en cada iteracion para aplicarla siempre

        if jugador1.saltando:#si el booleano saltando es verdad
            if jugador1.sonido_saltar_reproducido==False:
                jugador1.sonido_saltar.play()
            jugador1.saltar()#llamar a la funcion saltar constantemente hasta que saltando sea falso
        if jugador1.saltando_champ:
            if jugador1.sonido_saltar_reproducido==False:
                jugador1.sonido_saltar.play()
            jugador1.saltar_champ()#llamar a la funcion saltar constantemente hasta que saltando sea falso
        





        #animacion de caida en el aire
        if jugador1.saltando == False and jugador1.tocando_piso == False and jugador1.saltando_champ == False:
            jugador1.caer()
        
        

        #cargar musica 
        if jugador1.nivel == 1 and jugador1.vidas != 0:
            if pygame.mixer.music.get_busy() == False:
                if cancion == 6:
                    cancion = 0
                cargar_musica(cancion)
                cancion +=1

        nivel1.dibujar_fondos()
        if jugador1.vidas != 0:
            nivel1.colision_jugador_y_piso()
            nivel1.colision_jugador_champ()
        nivel1.dibujar_pisos()
        nivel1.piso.update()
        if jugador1.nivel == 1 and jugador1.vidas != 0:
            nivel1.colision_enemigo_y_piso()
            nivel1.colision_jugador_y_enemigos()
            nivel1.colision_jugador_y_obstaculo()
            nivel1.colision_jugador_caja()
            nivel1.colision_jugador_obstaculo2()
            nivel1.colision_jugador_y_gemas()
            for e in nivel1.grupo_enemigos:#bucle para dibujar al enemigo dentro del rectangulo
                if jugador1.derecha:
                    pantalla.blit(e.image, ((e.rect.x-25) - jugador1.velocidad, e.rect.y-35))
                    nivel1.grupo_enemigos.update()
                   # pygame.draw.rect(pantalla, (255, 0, 0), e, 2) #dibujar rectangulo asociado 
                    if movimiento:
                        e.rect.x = e.rect.x - jugador1.velocidad

                elif jugador1.derecha == False:
                    pantalla.blit(e.image, ((e.rect.x-25) - (-1*jugador1.velocidad), e.rect.y-35))
                    nivel1.grupo_enemigos.update()
                  #  pygame.draw.rect(pantalla, (255, 0, 0), e, 2)
                    if movimiento:
                        e.rect.x = e.rect.x - (-1*jugador1.velocidad)

            for o in nivel1.obstaculo_grupo:
                if jugador1.derecha:
                    pantalla.blit(o.image, (o.rect.x + 19 -jugador1.velocidad, o.rect.y))
                    nivel1.obstaculo_grupo.update()
               #     pygame.draw.rect(pantalla, (255, 0, 0), o, 2)
                    if movimiento:
                        o.rect.x = o.rect.x - (jugador1.velocidad)

                elif jugador1.derecha == False:
                    pantalla.blit(o.image, (o.rect.x + 19 -(-1*jugador1.velocidad), o.rect.y))
                    nivel1.obstaculo_grupo.update()
                #    pygame.draw.rect(pantalla, (255, 0, 0), o, 2)
                    if movimiento:
                        o.rect.x = o.rect.x - (-1*jugador1.velocidad)

            for o in nivel1.grupo_obstaculos2:
                if jugador1.derecha:
                    pantalla.blit(o.image, (o.rect.x- jugador1.velocidad, o.rect.y))
                    nivel1.obstaculo_grupo.update()
                #    pygame.draw.rect(pantalla, (255, 0, 0), o, 2)
                    if movimiento:
                        o.rect.x = o.rect.x - jugador1.velocidad

                elif jugador1.derecha == False:
                    pantalla.blit(o.image, (o.rect.x - (-1*jugador1.velocidad), o.rect.y))
                    nivel1.obstaculo_grupo.update()
                  #  pygame.draw.rect(pantalla, (255, 0, 0), o, 2)
                    if movimiento:
                        o.rect.x = o.rect.x - (-1*jugador1.velocidad)


            for v in nivel1.grupo_vidas:
                pantalla.blit(v.image, (v.rect.x, v.rect.y))
                nivel1.grupo_vidas.update()

            for g in nivel1.grupo_gemas:
                if jugador1.derecha:
                    pantalla.blit(g.image, (g.rect.x - jugador1.velocidad, g.rect.y))
                    nivel1.obstaculo_grupo.update()
                 #   pygame.draw.rect(pantalla, (255, 0, 0), g, 2)
                    if movimiento:
                        g.rect.x = g.rect.x - jugador1.velocidad

                elif jugador1.derecha == False:
                    pantalla.blit(g.image, (g.rect.x - (-1*jugador1.velocidad), g.rect.y))
                    nivel1.obstaculo_grupo.update()
                  #  pygame.draw.rect(pantalla, (255, 0, 0), g, 2)
                    if movimiento:
                        g.rect.x = g.rect.x - (-1*jugador1.velocidad)

            for c in nivel1.cajas:
                if jugador1.derecha:
                    pantalla.blit(c.image, (c.rect.x - jugador1.velocidad, c.rect.y))
                    nivel1.obstaculo_grupo.update()
                   # pygame.draw.rect(pantalla, (255, 0, 0), c, 2)
                    if movimiento:
                        c.rect.x = c.rect.x - jugador1.velocidad

                elif jugador1.derecha == False:
                    pantalla.blit(c.image, (c.rect.x - (-1*jugador1.velocidad), c.rect.y))
                    nivel1.obstaculo_grupo.update()
                   # pygame.draw.rect(pantalla, (255, 0, 0), c, 2)
                    if movimiento:
                        c.rect.x = c.rect.x - (-1*jugador1.velocidad)

            for c in nivel1.champin:
                if jugador1.derecha:
                    pantalla.blit(c.image, (c.rect.x - jugador1.velocidad, c.rect.y))
                    nivel1.obstaculo_grupo.update()
                  #  pygame.draw.rect(pantalla, (255, 0, 0), c, 2)
                    if movimiento:
                        c.rect.x = c.rect.x - jugador1.velocidad

                elif jugador1.derecha == False:
                    pantalla.blit(c.image, (c.rect.x - (-1*jugador1.velocidad), c.rect.y))
                    nivel1.obstaculo_grupo.update()
                 #   pygame.draw.rect(pantalla, (255, 0, 0), c, 2)
                    if movimiento:
                        c.rect.x = c.rect.x - (-1*jugador1.velocidad)


            #movimiento de enemigos clase 1
            for e in nivel1.grupo_enemigos:
                e.mover()
                if e.rect.x <= 0:
                    e.kill()
            for g in nivel1.grupo_gemas:
                g.idle()
            movimiento = False

            pantalla.blit(gemas_obtenidas.texto, (gemas_obtenidas.rect.x, gemas_obtenidas.rect.y))
        if jugador1.contador_gemas == 0:
            jugador1.nivel = 2

        if jugador1.vidas <= 0:
            jugador1.muerte()
        if jugador1.rect.top >= alto_pantalla:
            ejecutando = False
        
        if jugador1.nivel == 2 and jugador1.vidas !=0:
            if instancia == True:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("musica.mp3")
                pygame.mixer.music.play(-1)
                instancia = False
            for v in nivel1.grupo_vidas:
                pantalla.blit(v.image, (v.rect.x, v.rect.y))
                nivel1.grupo_vidas.update()

            for enemigoF in nivel1.jefe:
                if enemigoF.rect.x >= ancho_pantalla -300:
                    enemigoF.caminar()
                   # print(enemigoF.rect.x)
                else:
                    
                    espera= t.time()
                    if jefe.Nataque == 0:
                        enemigoF.idle()
                    if espera - tiempo_ataque_e >= jefe.tiempo_ataque:
                        jefe.Nataque = jefe.seleccionar_ataque()
                        tiempo_ataque_e = espera
                        jefe.crear = False
                        
                    if jefe.Nataque == 1:
                        jefe.crear_ataque1()
                        frame = jefe.crear_ataque1()
                        if jefe.crear == False:
                            random = r.randint(1, 4)
                            for i in range(random):
                                posx = r.randint(1700, 2400)
                                crear_minijefe(posx, 610)
                                jefe.crear = True
                        if frame == 15:
                            jefe.Nataque = 0

                    if jefe.Nataque == 2:
                        jefe.crear_ataque2()
                        frame = jefe.crear_ataque2()
                        if jefe.crear == False:
                            random = r.randint(3, 9)
                            for i in range(random):
                                posx = r.randint(10, 900)
                                crear_piedra_A(posx, -400)
                                jefe.crear = True
                        if frame == 15:
                            jefe.Nataque = 0
                    if jefe.Nataque == 3:
                        jefe.crear_ataque3()
                        frame = jefe.crear_ataque3()
                        if jefe.crear == False:
                            random = r.randint(3, 8)
                            for i in range(random):
                                    posx = r.randint(10, 900)
                                    crear_piedra_S(posx, ancho_pantalla+200)
                                    jefe.crear = True
                        if frame == 15:
                            jefe.Nataque = 0
                
                



                 

                #dibujando enemigo
              #  pygame.draw.rect(pantalla, (255, 0, 0), enemigoF, 2)
                pantalla.blit(enemigoF.image, (enemigoF.rect.x-300, enemigoF.rect.y-300))
                nivel1.jefe.update()
            
            for e in nivel1.mini_jefes:#bucle para dibujar al enemigo dentro del rectangulo
                    e.caminar()
                    pantalla.blit(e.image, (e.rect.x-150 , e.rect.y-140))
                    nivel1.mini_jefes.update()
                  #  pygame.draw.rect(pantalla, (255, 0, 0), e, 2) #dibujar rectangulo asociado 

                    if e.rect.x <= 0:
                        e.kill()

            for e in nivel1.piedras_aire:#bucle para dibujar al enemigo dentro del rectangulo
                    e.piedra_A()
                    pantalla.blit(e.image, (e.rect.x , e.rect.y))
                    nivel1.piedras_aire.update()
                  #  pygame.draw.rect(pantalla, (255, 0, 0), e, 2) #dibujar rectangulo asociado 

                    if e.rect.y >= ancho_pantalla:
                        e.kill()

            for e in nivel1.piedras_suelo:#bucle para dibujar al enemigo dentro del rectangulo
                    e.piedra_S()
                    pantalla.blit(e.image, (e.rect.x , e.rect.y))
                    nivel1.piedras_suelo.update()
                   # pygame.draw.rect(pantalla, (255, 0, 0), e, 2) #dibujar rectangulo asociado 

                    if e.rect.y <= 0:
                        e.kill()

            for e in nivel1.proyectiles:#bucle para dibujar al enemigo dentro del rectangulo
                    e.mover()
                    pantalla.blit(e.image, (e.rect.x , e.rect.y))
                    nivel1.proyectiles.update()
                   # pygame.draw.rect(pantalla, (255, 0, 0), e, 2) #dibujar rectangulo asociado 

                    if e.rect.y >= ancho_pantalla:
                        e.kill()

            for e in nivel1.poderes:#bucle para dibujar al enemigo dentro del rectangulo
                    e.idle()
                    pantalla.blit(e.image, (e.rect.x , e.rect.y))
                    nivel1.proyectiles.update()
                    #pygame.draw.rect(pantalla, (255, 0, 0), e, 2) #dibujar rectangulo asociado 


            #logica de poderes
            espera2= t.time()
            if espera2 - tiempo_poder >= 4:
                randomx = r.randint(10, 800)
                crear_poder(randomx, 600)
                tiempo_poder = espera2
            destruir = t.time()
            if destruir - eliminar_poder >=8:
                nivel1.poderes.empty()
                eliminar_poder = destruir
            if jefe.rectangulo_ancho <= 200:
                jefe.tiempo_ataque = 5
            
            if jefe.rectangulo_ancho <= 0:
                ejecutando = False
            
            
            
            nivel1.colision_jugador_y_poder()        
            nivel1.colision_jefe_proyectil()
            nivel1.colision_jefe()
            nivel1.colision_jugador_mini_jefes()
            nivel1.colision_jugador_piedras_Aire()
            nivel1.colision_jugador_piedras_Suelo()
            #vida del boss
            #dibujando vida enemigo
            pygame.draw.rect(pantalla, color_rectangulo, (1000, 15, jefe.rectangulo_ancho, rectangulo_alto))

        
            





                
        pantalla.blit(jugador1.image, (jugador1.rect.x-35,jugador1.rect.y-40))
        jugador1.update()
       # pygame.draw.rect(pantalla, (255, 0, 0), jugador1.rect, 2) #dibujar rectangulo asociado al jugador1
       # pygame.draw.rect(pantalla, (255,0,0), (jugador1.scroll, jugador1.rect.y, 50, 50))
        reloj.tick(120)#120fps
        lista.clear()
        pygame.display.update()#actualizar pantalla

    pygame.mixer.music.stop()
    jugador1.vidas = 3
    pygame.mixer.music.load("Music by Ansimuz/Hurt_and_heart.ogg")
    pygame.mixer.music.play(-1)
    nivel1.grupo_enemigos.empty()
    nivel1.obstaculo_grupo.empty()
    nivel1.grupo_obstaculos2.empty()
    nivel1.grupo_gemas.empty()
    nivel1.cajas.empty()
    nivel1.grupo_vidas.empty()
    nivel1.champin.empty()
    nivel1.jefe.empty()
    nivel1.mini_jefes.empty()
    nivel1.piedras_aire.empty()
    nivel1.piedras_suelo.empty()
    nivel1.proyectiles.empty()
    nivel1.poderes.empty()
    jugador1.contador_gemas = 8
    jugador1.nivel = 1
    jefe.rectangulo_ancho = 300
    jefe.rect.x = ancho_pantalla +200
    jefe.rect.y = 420
    nivel1.crear_jefe(jefe)
    
#juego()
menu()

pygame.quit()#finalizar libreria pygame
