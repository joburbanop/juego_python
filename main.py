from pygame import *
from pygame.locals import *
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300

#rectangulos
rectanguloMenosVolumen = Rect(10,265, 30, 30)
rectanguloMasVolumen = Rect(50, 265, 30, 30)
personajes=[Rect(110,195,90,40 ),Rect(240,195,90,40 ),Rect(390,195,90,40 )]

#colores
RED = (184, 36, 39)
colorRec1=(153,168,176, 255)
colorRec2=(180,202,218, 255)
bordeRedondeado = 10

#variables de control
personajeSeleccionado=-1
animacion = False
velocidadAnimacion = 80
posicion =[250,90]
posicionPersonajes = [[240, 80], [120, 100], [380, 80]]
tamanioImagen=[[100,100],[70,80],[100,100]]
tamanioLetras=35
tamanioRecntangulosancho=0
iniciar=False
personaje_x = 200
personaje_y = 150
enemigo_y=0
enemigo_x=[10,110,210,310,410]
desplazamientoEnemigo=False
tecla_izquierda_presionada=False
tecla_derecha_presionada=False


def cargarVolumen():
    mixer.music.load('sonido/inicio.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.05)


def controlSonido():
       
        volumen_actual = mixer.music.get_volume()

        if volumen_actual==0.0:
            cargarImagen('imagenes/sinVolumen.svg',30,30)
        else:
            cargarImagen('imagenes/menosVolumen.svg',30,30)
            
        
        print(volumen_actual)
        if rectanguloMasVolumen.collidepoint(mouse.get_pos()) :
            nuevo_volumen = volumen_actual + 0.01
            mixer.music.set_volume(nuevo_volumen)
            print(volumen_actual)
        
        if  rectanguloMenosVolumen.collidepoint(mouse.get_pos()) :
            
            nuevo_volumen = volumen_actual - 0.01
            mixer.music.set_volume(nuevo_volumen)
            print(volumen_actual)
        

def mostrarTexto(texto, tamanio, color):
    
    fuente = font.SysFont(None,tamanio)
    texto_renderizado = fuente.render(texto, True, color)
    return texto_renderizado


def cargarImagen(ruta, ancho, alto):
    nuevaImagen = image.load(ruta)
    nuevaImagen = transform.scale(nuevaImagen, (ancho, alto))
    return nuevaImagen


def cambiarDimensiones():
    global tamanioLetras
    global personajes
    tamanioLetras=0
    for personaje in personajes:       
        personaje.width = 0
        personaje.height = 0


def main():
    init()
    cargarVolumen()
    global bordeRedondeado
    global personajeSeleccionado
    global animacion
    global personaje_x
    global personaje_y
    global iniciar
    global desplazamientoEnemigo
    global enemigo_x
    global enemigo_y
    global tecla_derecha_presionada
    global tecla_izquierda_presionada
    global RED

    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display.set_caption("Galactic")
   
    running = True
    while running:
        
        
        for e in event.get():
            if e.type == QUIT:
                running = False

            if e.type == MOUSEBUTTONDOWN and rectanguloMasVolumen.collidepoint(mouse.get_pos()):                
                controlSonido()
                print('subiendo volumen')

            if e.type == MOUSEBUTTONDOWN and rectanguloMenosVolumen.collidepoint(mouse.get_pos()):                
                controlSonido()
                print('bajando volumen')
            
            if e.type==MOUSEBUTTONDOWN and personajes[0].collidepoint(mouse.get_pos()):
                personajeSeleccionado=1
                animacion=True
                print('elccion alien')

            if e.type==MOUSEBUTTONDOWN and personajes[1].collidepoint(mouse.get_pos()):
                personajeSeleccionado=0
                animacion=True
                print('elccion atari')

            if e.type==MOUSEBUTTONDOWN and personajes[2].collidepoint(mouse.get_pos()):
                personajeSeleccionado=2
                animacion=True
                print('elccion robot')
            
            if e.type== KEYDOWN and personajeSeleccionado!=-1:
                if e.key == K_RETURN:  # Verificar si se ha presionado Enter
                    # Cambiar imagen, personaje seleccionado, música, etc.
                    personaje_enemigo=image.load('imagenes/blue.png')
                    mixer.music.set_volume(0.1)
                    iniciar=True
                    desplazamientoEnemigo=True
                    if personajeSeleccionado==0:
                        tamanioImagen[0][0]=0            
                        tamanioImagen[0][1]=0
                        personaje_imagen = image.load('jugadores/stand.png')
                    elif personajeSeleccionado==1:
                        tamanioImagen[1][0]=0            
                        tamanioImagen[1][1]=0
                        personaje_imagen = image.load('jugadores/standAlien.png')
                    elif personajeSeleccionado==2:
                        tamanioImagen[2][0]=0            
                        tamanioImagen[2][1]=0
                        personaje_imagen = image.load('jugadores/standrobot.png')
                        



            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    tecla_izquierda_presionada=True
                elif e.key == K_RIGHT:
                    tecla_derecha_presionada=True
                
                elif e.key == K_SPACE:
                    # Lógica para el disparo
                    print("holi")

            elif e.type == KEYUP:
                if e.key == K_LEFT:
                    tecla_izquierda_presionada = False
                
                elif e.key == K_RIGHT:
                    tecla_derecha_presionada = False

        #dibujando en pantalla
        if iniciar:
            screen.blit(cargarImagen('fondo/Background17.jpg',600,300), (0, 0))
            screen.blit(personaje_imagen, (personaje_x, personaje_y))
            screen.blit(personaje_enemigo,(enemigo_x[0],enemigo_y))
            screen.blit(personaje_enemigo,(enemigo_x[1],enemigo_y))
            
        else:
            
            screen.blit(cargarImagen('fondo/Background18.jpg',600,300), (0, 0))
            screen.blit(mostrarTexto("Escoje un personaje",50,RED),(120,30))

        
        screen.blit(cargarImagen('jugadores/stand.png',tamanioImagen[0][0],tamanioImagen[0][1]),posicionPersonajes[0])
        screen.blit(cargarImagen('jugadores/standAlien.png',tamanioImagen[1][0],tamanioImagen[1][1]),posicionPersonajes[1])
        screen.blit(cargarImagen('jugadores/standrobot.png',tamanioImagen[2][0],tamanioImagen[2][1]),posicionPersonajes[2])
        screen.blit(cargarImagen('imagenes/masVolumen.svg',30,30),(50,265))
        

        if mixer.music.get_volume()==0.0:
            screen.blit(cargarImagen('imagenes/sinVolumen.svg',30,30),(10,265))
        else:
            screen.blit(cargarImagen('imagenes/menosVolumen.svg',30,30),(10,265))
       
        if personajes[0].collidepoint(mouse.get_pos()):
            draw.rect(screen,colorRec2,personajes[0],border_radius=bordeRedondeado)   
        else:
            draw.rect(screen,colorRec1,personajes[0],border_radius=bordeRedondeado)

        if personajes[1].collidepoint(mouse.get_pos()):
            draw.rect(screen,colorRec2,personajes[1],border_radius=bordeRedondeado)   
        else:
            draw.rect(screen,colorRec1,personajes[1],border_radius=bordeRedondeado)
        
        if personajes[2].collidepoint(mouse.get_pos()):
            draw.rect(screen,colorRec2,personajes[2],border_radius=bordeRedondeado)   
        else:
            draw.rect(screen,colorRec1,personajes[2],border_radius=bordeRedondeado)

        
        
        screen.blit(mostrarTexto("Alien", tamanioLetras,RED), (120, 202))
        screen.blit(mostrarTexto("Atari", tamanioLetras,RED), (255, 202))
        screen.blit(mostrarTexto("Robot", tamanioLetras,RED), (395, 202)) 

        if desplazamientoEnemigo:
            movimiento =random.uniform(0.5, 0.9)
            if enemigo_y<320:
                enemigo_y+=movimiento
            else:
                enemigo_y=0

     
        if animacion:
            
            desplazamiento=[0,0]
            if posicionPersonajes[personajeSeleccionado][0] != posicion[0] and posicionPersonajes[personajeSeleccionado][1] != posicion[1]:
                desplazamiento[0] = (posicion[0] - posicionPersonajes[personajeSeleccionado][0])/velocidadAnimacion
                desplazamiento[1] = (posicion[1]-posicionPersonajes[personajeSeleccionado][1])/velocidadAnimacion
                posicionPersonajes[personajeSeleccionado][0] +=  desplazamiento[0]
                posicionPersonajes[personajeSeleccionado][1] += desplazamiento[1] 
                
                
                if posicionPersonajes[personajeSeleccionado][0] >= 249 and posicionPersonajes[personajeSeleccionado][1] >= 89:
                    posicionPersonajes[personajeSeleccionado][0] = 250
                    posicionPersonajes[personajeSeleccionado][1] = 90
                    animacion = False
            else:
                animacion = False

            if personajeSeleccionado==0:
                tamanioImagen[1][0]=0            
                tamanioImagen[1][1]=0
                tamanioImagen[2][0]=0            
                tamanioImagen[2][1]=0
                cambiarDimensiones()
                screen.blit(mostrarTexto("Presiona enter para iniciar",50,colorRec2),(100,223))

            if personajeSeleccionado==1:
                tamanioImagen[0][0]=0            
                tamanioImagen[0][1]=0
                tamanioImagen[2][0]=0            
                tamanioImagen[2][1]=0
                personaje_imagen = image.load('jugadores/standAlien.png')
                cambiarDimensiones()
                screen.blit(mostrarTexto("Presiona enter para iniciar",50,colorRec2),(100,223))

            if personajeSeleccionado==2:
                tamanioImagen[0][0]=0            
                tamanioImagen[0][1]=0
                tamanioImagen[1][0]=0            
                tamanioImagen[1][1]=0
                personaje_imagen = image.load('jugadores/standrobot.png')
                cambiarDimensiones()
                screen.blit(mostrarTexto("Presiona enter para iniciar",50,colorRec2),(100,223))
        
        # Actualizar la posición del personaje según las teclas presionadas
        if tecla_izquierda_presionada:
            personaje_x -= 0.5
        if tecla_derecha_presionada:
            personaje_x += 0.5
        
        
        #print(personajeSeleccionado)
        #print(mouse.get_pos())
        display.update()

    quit()

if __name__ == '__main__':
    main()