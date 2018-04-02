
import turtle

# Create a screen on which we draw
screen = turtle.Screen()

# Configure a default size
dimX = 400
dimY = 400
screen.setup(dimX, dimY)

def drawTree(ttl,length,generations):
    if(generations == 0):
        ttl.forward(length)
        ttl.backward(length)
        
        return
        
    ttl.forward(length)
    ttl.left(45)
    drawTree(ttl,length/2,generations-1)
    ttl.right(90)
    drawTree(ttl,length/2,generations-1)
    ttl.left(45)
    ttl.backward(length)

    return

# Reset the screen
turtle.clearscreen()
screen.reset()
screen.screensize(dimX, dimY)
turtle.tracer(10)

# Create a turtle
ttl = turtle.Turtle()

ttl.resizemode("user")
ttl.speed(5)
ttl.penup()
ttl.setposition(0, -dimY/2 + 50)
ttl.pendown()

ttl.left(90)
drawTree(ttl, 150, 8)

