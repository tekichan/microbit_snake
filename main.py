"""
Microbit Snake
A snake game in Microbit

Author: Teki Chan
"""

# Initialize variables

# Next position (nextX, nextY)
nextY = 0
nextX = 0

# Current position (currentX, currentY) and direction
currentY = 0
currentX = 0
currentDirection = 0

# Position of Fruit (dotX, dotY)
dotY = 0
dotX = 0

# Temporary position of Fruit (tempDotX, tempDotY)
tempDotY = 0
tempDotX = 0

snakeScore = 0      # Snake game score
allowInput = 0      # Whether it allows to input
gameRunning = 0     # Whether the game is running
gameSpeed = 0       # Game speed
snakePartsY: List[number] = []      # List of snake's parts' Y
snakePartsX: List[number] = []  # List of snake's parts' X

# Function: Get New Dot
def getNewDot():
    global tempDotX, tempDotY, dotX, dotY
    tempDotX = randint(0, 4)
    tempDotY = randint(0, 4)
    while led.point(tempDotX, tempDotY):
        tempDotX = randint(0, 4)
        tempDotY = randint(0, 4)
    dotX = tempDotX
    dotY = tempDotY
    led.plot(dotX, dotY)

# Function: Drop off the tail during moving    
def dropTail():
    led.unplot(snakePartsX.shift(), snakePartsY.shift())

# Function: Reset and start a new game    
def resetGame():
    global gameSpeed, gameRunning, allowInput, currentDirection, currentX, currentY, dotX, dotY, snakePartsX, snakePartsY, snakeScore
    basic.clear_screen()
    gameSpeed = 1000
    gameRunning = 0
    allowInput = 1
    currentDirection = 1
    currentX = 0
    currentY = 2
    dotX = 0
    dotY = 0
    snakePartsX = [currentX]
    snakePartsY = [currentY]
    snakeScore = 0
    led.plot(currentX, currentY)
    getNewDot()

# Event handler: When Button A is pressed
def on_button_pressed_a():
    global currentDirection, gameRunning
    if allowInput == 1:
        if gameRunning == 1:
            currentDirection = (currentDirection + 3) % 4
        else:
            gameRunning = 1
# Add the event handler to the listener           
input.on_button_pressed(Button.A, on_button_pressed_a)

# Event handler: When Button B is pressed
def on_button_pressed_b():
    global currentDirection, gameRunning
    if allowInput == 1:
        if gameRunning == 1:
            currentDirection = (currentDirection + 1) % 4
        else:
            gameRunning = 1
# Add the event handler to the listener            
input.on_button_pressed(Button.B, on_button_pressed_b)

# Function: When the game loses
def loseGame():
    global allowInput, gameRunning
    allowInput = 0
    gameRunning = 0
    basic.show_icon(IconNames.GHOST)
    basic.pause(200)
    basic.show_icon(IconNames.SKULL)
    basic.pause(200)
    basic.show_number(snakeScore)
    basic.pause(2000)
    resetGame()

# Event handler: What the game does in forever loop
def on_forever():
    global nextX, nextY, currentX, currentY, snakeScore, gameSpeed
    if gameRunning == 1:
        nextX = currentX
        nextY = currentY
        if currentDirection == 0:
            nextY += -1
        elif currentDirection == 1:
            nextX += 1
        elif currentDirection == 2:
            nextY += 1
        else:
            nextX += -1
        if nextX < 0 or (nextX > 4 or (nextY < 0 or nextY > 4)):
            loseGame()
        elif (nextX != dotX or nextY != dotY) and led.point(nextX, nextY):
            loseGame()
        else:
            currentX = nextX
            currentY = nextY
            led.plot(currentX, currentY)
            snakePartsX.append(currentX)
            snakePartsY.append(currentY)
            if nextX == dotX and nextY == dotY:
                getNewDot()
                snakeScore += 1
                if snakeScore % 2 == 0 and gameSpeed > 100:
                    gameSpeed += -100
                else:
                    dropTail()
            else:
                dropTail()
    basic.pause(gameSpeed)

# Start the game by re-setting game
resetGame()

# Add the event handler to the forever manager
basic.forever(on_forever)
