function getNewDot() {
    
    tempDotX = randint(0, 4)
    tempDotY = randint(0, 4)
    while (led.point(tempDotX, tempDotY)) {
        tempDotX = randint(0, 4)
        tempDotY = randint(0, 4)
    }
    dotX = tempDotX
    dotY = tempDotY
    led.plot(dotX, dotY)
}

function dropTail() {
    led.unplot(snakePartsX.shift(), snakePartsY.shift())
}

function resetGame() {
    
    basic.clearScreen()
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
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (allowInput == 1) {
        if (gameRunning == 1) {
            currentDirection = (currentDirection + 3) % 4
        } else {
            gameRunning = 1
        }
        
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (allowInput == 1) {
        if (gameRunning == 1) {
            currentDirection = (currentDirection + 1) % 4
        } else {
            gameRunning = 1
        }
        
    }
    
})
function loseGame() {
    
    allowInput = 0
    gameRunning = 0
    basic.showIcon(IconNames.Ghost)
    basic.pause(200)
    basic.showIcon(IconNames.Skull)
    basic.pause(200)
    basic.showNumber(snakeScore)
    basic.pause(2000)
    resetGame()
}

let nextY = 0
let nextX = 0
let snakeScore = 0
let currentY = 0
let currentX = 0
let currentDirection = 0
let allowInput = 0
let gameRunning = 0
let gameSpeed = 0
let snakePartsY : number[] = []
let snakePartsX : number[] = []
let dotY = 0
let dotX = 0
let tempDotY = 0
let tempDotX = 0
resetGame()
basic.forever(function on_forever() {
    
    if (gameRunning == 1) {
        nextX = currentX
        nextY = currentY
        if (currentDirection == 0) {
            nextY += -1
        } else if (currentDirection == 1) {
            nextX += 1
        } else if (currentDirection == 2) {
            nextY += 1
        } else {
            nextX += -1
        }
        
        if (nextX < 0 || (nextX > 4 || (nextY < 0 || nextY > 4))) {
            loseGame()
        } else if ((nextX != dotX || nextY != dotY) && led.point(nextX, nextY)) {
            loseGame()
        } else {
            currentX = nextX
            currentY = nextY
            led.plot(currentX, currentY)
            snakePartsX.push(currentX)
            snakePartsY.push(currentY)
            if (nextX == dotX && nextY == dotY) {
                getNewDot()
                snakeScore += 1
                if (snakeScore % 2 == 0 && gameSpeed > 100) {
                    gameSpeed += -100
                } else {
                    dropTail()
                }
                
            } else {
                dropTail()
            }
            
        }
        
    }
    
    basic.pause(gameSpeed)
})
