def on_button_pressed_a():
    Player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Player: game.LedSprite = None
Car_0 = game.create_sprite(0, 0)
Car_1 = game.create_sprite(1, 0)
Car_2 = game.create_sprite(2, 0)
Car_3 = game.create_sprite(3, 0)
Car_4 = game.create_sprite(4, 0)
score = 0
Player = game.create_sprite(2, 4)

def on_forever():
    global score
    score += 100
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    basic.pause(randint(0, 3000))
    Car_1.change(LedSpriteProperty.Y, 1)
    if Car_1.get(LedSpriteProperty.Y) == 4:
        if Car_1.is_touching(Player):
            game.game_over()
        Car_1.set(LedSpriteProperty.Y, 0)
        basic.pause(randint(0, 3000))
basic.forever(on_forever2)

def on_forever3():
    if game.is_game_over():
        basic.show_string("You got")
        basic.show_string("" + str((score)))
        basic.show_string("Points")
basic.forever(on_forever3)

def on_forever4():
    basic.pause(randint(0, 3000))
    Car_0.change(LedSpriteProperty.Y, 1)
    if Car_0.get(LedSpriteProperty.Y) == 4:
        if Car_0.is_touching(Player):
            game.game_over()
        Car_0.set(LedSpriteProperty.Y, 0)
        basic.pause(randint(0, 3000))
basic.forever(on_forever4)

def on_forever5():
    basic.pause(randint(0, 3000))
    Car_2.change(LedSpriteProperty.Y, 1)
    if Car_2.get(LedSpriteProperty.Y) == 4:
        if Car_2.is_touching(Player):
            game.game_over()
        Car_2.set(LedSpriteProperty.Y, 0)
        basic.pause(randint(0, 3000))
basic.forever(on_forever5)

def on_forever6():
    basic.pause(randint(0, 3000))
    Car_3.change(LedSpriteProperty.Y, 1)
    if Car_3.get(LedSpriteProperty.Y) == 4:
        if Car_3.is_touching(Player):
            game.game_over()
        Car_3.set(LedSpriteProperty.Y, 0)
        basic.pause(randint(0, 3000))
basic.forever(on_forever6)

def on_forever7():
    basic.pause(randint(0, 3000))
    Car_4.change(LedSpriteProperty.Y, 1)
    if Car_4.get(LedSpriteProperty.Y) == 4:
        if Car_4.is_touching(Player):
            game.game_over()
        Car_4.set(LedSpriteProperty.Y, 0)
        basic.pause(randint(0, 3000))
basic.forever(on_forever7)
