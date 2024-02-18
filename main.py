import turtle
import time
import random

score = 0
lastScoringTime = time.time()
remainingTime = 10
count = 1

# our screen
screen = turtle.Screen()
screen.bgcolor("light gray")
screen.title("Catch The Turtle")
screen.setup(width=1200, height=1200)
screenHeight = screen.window_height()
yOfScoreLabel = screenHeight / 2 * 0.91
yOfTimeLabel = screenHeight / 2 * 0.84


# score label's turtle
scoreTurtle = turtle.Turtle()
scoreTurtle.hideturtle()
scoreTurtle.color("dark blue")
scoreTurtle.penup()
scoreTurtle.right(90)
#scoreTurtle.setposition(0, (int(screen.window_height() / 2) - 50))
scoreTurtle.setposition(0, yOfScoreLabel)
scoreTurtle.write("Score: 0", align="center", font=("Arial", 36, "normal"))

# the turtle that we'll try to catch
t = turtle.Turtle()
t.shape("turtle")
t.shapesize(4)
t.color("black", "green")


# time label's turtle
timeTurtle = turtle.Turtle()
timeTurtle.hideturtle()
timeTurtle.penup()
timeTurtle.right(90)
#timeTurtle.setposition(0, (int(screen.window_height() / 2) - 90))
timeTurtle.setposition(0, yOfTimeLabel)
def update_countdown():
    global remainingTime
    timeTurtle.clear()

    if remainingTime > 0:
        timeTurtle.write(f"Time: {remainingTime}", align="center", font=("Arial", 24, "normal"))
        remainingTime -= 1
        screen.ontimer(update_countdown, 1000)  # Schedule the function to be called after 1000 milliseconds (1 second)
    else:
        timeTurtle.write("Time's off!", align="center", font=("Arial", 28, "normal"))

def changeTurtleLocation():
    while True:
        t.hideturtle()
        t.penup()
        t.speed(0)
        randomX = random.randint(-(int(screen.window_width() / 2) - 100), int(screen.window_height() / 2) - 100)
        randomY = random.randint(-(int(screen.window_width() / 2) - 100), int(screen.window_height() / 2) - 100)
        t.setposition(randomX, randomY)
        t.showturtle()
        time.sleep(0.7)
        if remainingTime == 0:
            break
    t.home()

def isClickedOnTurtle(x, y):
    distanceToTurtle = t.distance(x,y)
    global score, lastScoringTime, count
    if distanceToTurtle < 50:
        currentTime = time.time()
        if currentTime - lastScoringTime >= 0.7 and remainingTime != 0:
            print(f"clicked on turtle {count}")
            score += 1
            scoreTurtle.clear()
            scoreTurtle.write(f"Score: {score}", align="center", font=("Arial", 32, "normal"))
            lastScoringTime = currentTime
            count += 1


screen.onscreenclick(isClickedOnTurtle)
update_countdown()
changeTurtleLocation()

turtle.mainloop()