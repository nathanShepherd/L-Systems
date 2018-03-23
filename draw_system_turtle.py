import turtle
import random

def apply_rules(char):
    '''
    Example 7: Fractal plant[edit]
    variables : X F
    constants : + − [ ]
    start  : X
    rules  : (X → F[−X][X]F[−X]+FX), (F → FF)
    angle  : 25°
    '''
    if char ==  "F":
        return 'F-F+B+F-F'
    elif char == "B":
        return 'F-F++F-F'
    else:
        return char

def generate(axiom, iters):
    delta = axiom
    for i in range(iters):
        new_str = ""
        for char in delta:
            new_str += apply_rules(char)
        delta = new_str
    return delta

def drawLsystem(aTurtle, instructions, angle, distance):
    for i, cmd in enumerate(instructions):
        scalar = random.randint(-1, 1)
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
            aTurtle.backward(distance)
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
            

def config_origin(aTurtle, window):
    window.setup(width=800, height=800, startx=900, starty=75)
    window.bgcolor("gray")
    aTurtle.pensize(.25)
    aTurtle.speed(0)
    window.delay(0)
    aTurtle.up()
    aTurtle.back(200)# Left
    aTurtle.right(150)
    aTurtle.back(25)# Up
    aTurtle.left(90)
    aTurtle.down()
    #aTurtle.hideturtle()
    
    
    
def main():
    dna_seq = generate('F', 3)
    print(dna_seq)
    t = turtle.Turtle()
    screen = turtle.Screen()
    config_origin(t, screen)

    ### (turtle, instruct, angle= 70 or 300, segment length= 25)
    theta = 143#120 == triangle, try 143
    for i in range(100):
        scalar = random.randint(-2, 2)
        drawLsystem(t, dna_seq, theta, 40)
        t.right(theta)
    #screen.exitonclick()

main()
