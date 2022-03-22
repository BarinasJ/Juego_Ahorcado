import turtle
import time
import random
retrasar=0.05

puntaje=0
maximo_puntaje=0
#bordes
ventana=turtle.Screen()
ventana.bgcolor("black")
ventana.title("juego snake")
ventana.setup(width=600 , height=600)
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.penup()
cabeza.shape("circle")
cabeza.color("white")
cabeza.direction="stop"
#comida
comida = turtle.Turtle()
comida.speed(0)
comida.penup()
comida.shape("square")
comida.color("green")
comida.goto(0,100)

cuerpo=[]

#puntos
puntos=turtle.Turtle()
puntos.speed(0)
puntos.color("white")
puntos.penup()
puntos.hideturtle()
puntos.goto(0,260)
puntos.write("puntaje: 0    Maximo puntaje: 0", align="center", font=("courier", 24, "normal"))
#Movimientos
def arriba():
    cabeza.direction="up"

def abajo():
    cabeza.direction="down"

def derecha():
    cabeza.direction="right"

def izquierda():
    cabeza.direction="left"
            
def movi():
    if cabeza.direction=="up":
        y=cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction=="down":
        y=cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction=="right":
        x=cabeza.xcor()
        cabeza.setx(x + 20)
    if cabeza.direction=="left":
        x=cabeza.xcor()
        cabeza.setx(x - 20)   
#movimmientos teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(izquierda, "Left")
while True:
    #choque bordes
    ventana.update()

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        #limpiar cuerpo
        for i in cuerpo:
            i.hideturtle()
        cuerpo.clear() 

        #reiniciar maracdor
        puntaje=0
        puntos.clear()    
        puntos.write("puntaje: {}   Maximo puntaje: {}".format(puntaje, maximo_puntaje), align="center", font=("courier", 24, "normal"))   
        #recoger comida
    if cabeza.distance(comida)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.speed(0)
        nuevo_cuerpo.penup()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("red")
        cuerpo.append(nuevo_cuerpo)
        #marcador
        puntaje+=5
        if puntaje >maximo_puntaje:
            maximo_puntaje=puntaje
        puntos.clear()    
        puntos.write("puntaje: {}   Maximo puntaje: {}".format(puntaje, maximo_puntaje), align="center", font=("courier", 24, "normal"))
    totalcpo=len(cuerpo)
    for i in range (totalcpo -1, 0, -1):
        x=cuerpo [i-1].xcor()
        y=cuerpo [i-1].ycor()
        cuerpo[i].goto(x,y)

    if totalcpo >0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        cuerpo[0].goto(x,y)    
    movi()
    #choque con el cuerpo
    for i in cuerpo:
        if i.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction= "stop"
            for i in cuerpo:
                i.hideturtle()
            cuerpo.clear()
            #reiniciar marcador
            puntaje=0
            puntos.clear()    
            puntos.write("puntaje: {}   Maximo puntaje: {}".format(puntaje, maximo_puntaje), align="center", font=("courier", 24, "normal"))           
    time.sleep(0.05)
