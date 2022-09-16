from random import *
from turtle import *
from freegames import path

car = path('car.gif')

#Hemos cambiado los númeor por letras aleatorias
tiles = ["D", "H", "S", "g", "J", "G", "p", "N", "t", "s", 
         "z", "C", "V", "F", "d", "a", "T", "y", "u", "o",
         "f", "R", "A", "Y", "E", "O", "c", "h", "e", "r", 
         "j", "U"] * 2

#Código que permite contar cuantos taps hay
state = {'mark': None, 'Taps': 1}
hide = [True] * 64

show = Turtle(visible=False)

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    show.undo()

    # Metodo para mostrar el contador de taps inicial en pantalla y sumarlos
    show.write(state['Taps'], font=('Arial', 30, 'normal'))
    state['Taps'] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Metodos para centrar y alinear los caracteres en las casillas
        goto(x + 25.5, y + 5)
        color('black')
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    #Método para detectar cuando todas las casillas han sido destapadas
    if not any(hide):
        print("Todos los cuadros han sido destapados!!")
    else:
        update()
        ontimer(draw, 100)

shuffle(tiles)
setup(420, 600, 370, 0)
addshape(car)
hideturtle()
tracer(False)

#Metodo para acomodar el contador de taps en panatalla 
show.goto(0, 200)
show.write(state['Taps'], font=('Arial', 20, 'normal')) 

onscreenclick(tap)
draw()
done()
