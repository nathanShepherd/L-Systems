import turtle
import numpy as np

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

def adjusted_sigmoid(x):
    return 1 / (1 + np.exp(-.3 * (x ** 1/3)))

def tree(sequence, length, angle, decay):
    """ plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    decay is factor by which branch is shortened
    from level to level."""
    
    arr = []
    size = 25*(length/200)
    for aTurtle in sequence:
        aTurtle.pensize(size)
        alpha = np.random.normal(0, size)
        aTurtle.forward(length - alpha)
        next_turtle = aTurtle.clone()
        center_left = aTurtle.clone()
        center_right = aTurtle.clone()

        theta = np.random.normal(0, 30/size)
        aTurtle.left(angle + theta)
        next_turtle.right(angle - theta)
        
        center_left.left((angle/3) - theta)
        center_right.right((angle/3) + theta)
            
        arr.append(aTurtle)
        arr.append(next_turtle)
        arr.append(center_left)
        arr.append(center_right)

    delta = np.random.normal(0, 50)
    for branch in tree(arr,length*decay, angle-(decay + delta) + delta,decay):
        #compile sequence of branches to be drawn sequentially later
        yield None


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
    window.setup(width=800, height=800, startx=850, starty=0)
    window.bgcolor("gray")
    aTurtle.pensize(.5)
    aTurtle.speed(0)
    window.delay(0)
    aTurtle.up()
    aTurtle.back(0)# left
    aTurtle.right(90)
    aTurtle.back(-300)# up
    aTurtle.left(180)
    aTurtle.down()
    aTurtle.hideturtle()
    
    
    
def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    config_origin(t, screen)

    draw_tree = tree([t], 200, 45, 0.7)#magic decay rate: 0.6375
    for branch in draw_tree:
        pass

if __name__ == "__main__":
    main()
