from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Color al azar de la comida y la serpiente
colors=['gold','green','purple', 'aqua','blue'] #Lista con los colores posibles de la comida y serpiente
colorSnake=random.choice(colors)
colorFood=random.choice(colors) 
while(colorSnake==colorFood): 
    colorFood=random.choice(colors)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Función para regresar la comida al centro si se sale del tablero
def foodReturn(x, y):
    food.x = x
    food.y = y

#Función para que la comida se mueva al azar
def moveFood():
    if inside(food):
        food.x += randrange(-1, 2) *10
        food.y += randrange(-1, 2) *10
    else:
        foodReturn(0,0)



def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    moveFood()

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
