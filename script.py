import random
import turtle
import sys


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)

def func():
    print('ya pustaya funkciya')

x = random.randrange(1, 100)
#print (type(x))

print('sluchainoe chislo ', x) 
func()

def draw_circle(x, y, r):
    gotoxy(x, y)
    turtle.circle(r)


def draw_gibbet_element(step):
    if step == 1:
        draw_line(-160, -100, -160, 80)
    elif step == 2:
        draw_line(-160, 80, -80, 80)
    elif step == 3:    
        draw_line(-160, 40, -120, 80)
    elif step == 4:
        draw_line(-100, 80, -100, 40)
    elif step == 5:
        draw_circle(-100, 0, 20)
    elif step == 6:
        draw_line(-100, 0, -100, -50)
    elif step == 7:
        draw_line(-100, -10, -120, -20)
    elif step == 8:
        draw_line(-100, -10, -80, -20)
    elif step == 9:
        draw_line(-100, -50, -120, -60)
    elif step == 10:
        draw_line(-100, -50, -80, -60)

gotoxy(-200, 250)
turtle.write("Zagadano chislo ot 1 do 100. \n Poprobui ugadat!", \
             font=("Arial", 18, ))
ans = turtle.textinput("Hotite igrat?", "y/n")
if ans == 'n':
    sys.exit(13)

hints = False 
ans = turtle.textinput("Davat podskazki?", "y/n")
if ans == 'y':
  hints = True

try_count = 0

while True:
    number = turtle.numinput("Poprobui ugadat","Chislo", 0, 0, 100)

    if hints:
        gotoxy(230, 200 - try_count * 15)
        if number < x: 
            turtle.write(str(number) + 'Zagadannoe chislo bolshe')
        elif number > x:
            turtle.write(str(number) + 'Zagadannoe chislo menshe')

    if number == x:
        gotoxy(-150, -200)
        turtle.color('green')
        turtle.write("Vi ugadali", font=("Arial", 24, "normal"))
        break
    else:
        gotoxy(-150, 200)
        turtle.color('red')
        turtle.write("Neverno", font=("Arial", 20, "normal"))

        try_count += 1
        draw_gibbet_element(try_count)

        if try_count == 10:
            gotoxy(-150, 150)
            turtle.color('brown')
            turtle.write("Vi proigrali!", font=("Arial", 25, "normal"))
            break 

       
#input('Najmite Enter ')
