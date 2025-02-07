import turtle
turtle.bgcolor("sky blue")


def draw_flagpole(x,y, width, height, color):
    """
    This function is used to draw a rectangle that represents the flag pole
    """
    turtle.up() #lifts the pen
    turtle.goto(x ,y) #goes to specified x and y coordinate 
    turtle.fillcolor(color) #uses the color that is passed through the parameter
    turtle.begin_fill() #starts the fill
    turtle.down() #puts the pen back down
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill() #ends the fills
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.up()
    turtle.forward(10)
    turtle.down()
    turtle.done


def draw_rectangle(x,y,width,height, color):
    """
    This function draws the rectangle that represents the flag
    """
    turtle.goto(x, y) #goes to specified x and y coordiantes
    turtle.fillcolor(color) #determines the fill color based on parameter
    turtle.begin_fill() #begins the fill
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.up()
    turtle.end_fill() #ends the fill
    return (x/2, y/2) #returns the center coordinates 


def draw_circle(x,y,radius,color): #call main function inorder for the circle to work
   """
   This function draws a circle representing the emblem 
   """
   turtle.up #lifts the pen
   turtle.goto(x,y - radius) 
   turtle.down #puts the pen back down
   turtle.fillcolor(color)
   turtle.begin_fill() #begins fill
   turtle.circle(radius) #draws the circle with specified 
   turtle.end_fill() #ends fill

def draw_flag(x,y, scale_factor):
    """
    Draws the 2nd flag using draw_flagpole, draw_rectangle, draw_circle and the scale factor
    """
    draw_flagpole(x,y,200 * scale_factor,5 * scale_factor, "black")
    turtle.up()
    turtle.goto(x + 5, y+ 50)
    turtle.down()
    draw_rectangle(x+ 5, y + 50, 100 * scale_factor, 200 * scale_factor, "red")
    draw_circle(x+55,y+ 105,15,"white")


def main():
    draw_flagpole(-100,0,5,200, "black") #correct coordinates
    draw_rectangle(-90, 200 ,200,100, "red") #correct coordinates
    draw_circle(50,185,35,"white")

    draw_flag(150, 0, 0.5)


main()