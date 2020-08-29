input.onButtonPressed(Button.A, function () {
    Player.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    Player.change(LedSpriteProperty.X, 1)
})
let Player: game.LedSprite = null
let Car_0 = game.createSprite(0, 0)
let Car_1 = game.createSprite(1, 0)
let Car_2 = game.createSprite(2, 0)
let Car_3 = game.createSprite(3, 0)
let Car_4 = game.createSprite(4, 0)
let score = 0
Player = game.createSprite(2, 4)
basic.forever(function () {
    score += 100
    basic.pause(1000)
})
basic.forever(function () {
    basic.pause(randint(0, 3000))
    Car_1.change(LedSpriteProperty.Y, 1)
    if (Car_1.get(LedSpriteProperty.Y) == 4) {
        if (Car_1.isTouching(Player)) {
            game.gameOver()
        }
        Car_1.set(LedSpriteProperty.Y, 0)
        basic.pause(randint(0, 3000))
    }
})
basic.forever(function () {
    if (game.isGameOver()) {
        basic.showString("You got")
        basic.showString("" + (score))
        basic.showString("Points")
    }
})
basic.forever(function () {
    basic.pause(randint(0, 3000))
    Car_0.change(LedSpriteProperty.Y, 1)
    if (Car_0.get(LedSpriteProperty.Y) == 4) {
        if (Car_0.isTouching(Player)) {
            game.gameOver()
        }
        Car_0.set(LedSpriteProperty.Y, 0)
        basic.pause(randint(0, 3000))
    }
})
basic.forever(function () {
    basic.pause(randint(0, 3000))
    Car_2.change(LedSpriteProperty.Y, 1)
    if (Car_2.get(LedSpriteProperty.Y) == 4) {
        if (Car_2.isTouching(Player)) {
            game.gameOver()
        }
        Car_2.set(LedSpriteProperty.Y, 0)
        basic.pause(randint(0, 3000))
    }
})
basic.forever(function () {
    basic.pause(randint(0, 3000))
    Car_3.change(LedSpriteProperty.Y, 1)
    if (Car_3.get(LedSpriteProperty.Y) == 4) {
        if (Car_3.isTouching(Player)) {
            game.gameOver()
        }
        Car_3.set(LedSpriteProperty.Y, 0)
        basic.pause(randint(0, 3000))
    }
})
basic.forever(function () {
    basic.pause(randint(0, 3000))
    Car_4.change(LedSpriteProperty.Y, 1)
    if (Car_4.get(LedSpriteProperty.Y) == 4) {
        if (Car_4.isTouching(Player)) {
            game.gameOver()
        }
        Car_4.set(LedSpriteProperty.Y, 0)
        basic.pause(randint(0, 3000))
    }
})
