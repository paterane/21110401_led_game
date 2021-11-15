def on_button_pressed_a():
    global T, X
    if X > 1 and Start == True:
        music.play_tone(740, music.beat(BeatFraction.SIXTEENTH))
        T = X
        X = X - 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global T, X
    if X < 3 and Start == True:
        music.play_tone(740, music.beat(BeatFraction.SIXTEENTH))
        T = X
        X = X + 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global BT_A
    if Start == False:
        BT_A = True
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

T1 = 0
D2 = 0
E1 = 0
T = 0
BT_A = False
Start = False
X = 0
music.start_melody(music.built_in_melody(Melodies.PRELUDE), MelodyOptions.ONCE)
D1 = 5
X = 2
Timer = 0
Time = 500
Start = False
basic.show_string("PRESS LOGO")
while not (BT_A):
    music.play_tone(698, music.beat(BeatFraction.SIXTEENTH))
    basic.show_icon(IconNames.DIAMOND)
    music.play_tone(784, music.beat(BeatFraction.SIXTEENTH))
    basic.show_icon(IconNames.SMALL_DIAMOND)
basic.clear_screen()
for index in range(5):
    led.plot(index, 0)
    music.play_tone(659, music.beat(BeatFraction.QUARTER))
for index2 in range(4):
    led.plot(4, index2 + 1)
    music.play_tone(698, music.beat(BeatFraction.QUARTER))
for index3 in range(4):
    led.plot(3 - index3, 4)
    music.play_tone(740, music.beat(BeatFraction.QUARTER))
for index4 in range(3):
    led.plot(0, 3 - index4)
    music.play_tone(784, music.beat(BeatFraction.QUARTER))
for index5 in range(3):
    led.plot(index5 + 1, 1)
    music.play_tone(831, music.beat(BeatFraction.QUARTER))
for index6 in range(2):
    led.plot(3, index6 + 2)
    music.play_tone(880, music.beat(BeatFraction.HALF))
for index7 in range(2):
    led.plot(2 - index7, 3)
    music.play_tone(932, music.beat(BeatFraction.HALF))
for index8 in range(2):
    led.plot(index8 + 1, 2)
    music.play_tone(988, music.beat(BeatFraction.WHOLE))
basic.pause(1000)
basic.clear_screen()
Start = True
music.start_melody(music.built_in_melody(Melodies.FUNK),
    MelodyOptions.FOREVER_IN_BACKGROUND)

def on_every_interval():
    global E1, D1, D2
    basic.pause(Time)
    if Start == True:
        if D1 > 4:
            led.unplot(E1, D1 - 1)
            E1 = randint(1, 3)
            D1 = 0
        led.plot(E1, D1)
        led.unplot(E1, D1 - 1)
        led.plot(0, D2)
        led.plot(4, D2)
        if D1 >= 0 and D1 < 5:
            D1 = D1 + 1
        if D2 >= 0 and D2 < 5:
            D2 = D2 + 1
        else:
            D2 = 0
loops.every_interval(1, on_every_interval)

def on_forever():
    global Start, T1, Timer, Time
    if X == E1 and D1 == 4:
        Start = False
        led.stop_animation()
        music.stop_all_sounds()
        music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
            MelodyOptions.ONCE)
        for index9 in range(2):
            basic.show_leds("""
                # . . . #
                                . # . # .
                                . . # . .
                                . # . # .
                                # . . . #
            """)
            basic.pause(300)
            basic.show_leds("""
                . # # # .
                                # . # . #
                                # # . # #
                                # . # . #
                                . # # # .
            """)
            basic.pause(300)
        basic.pause(200)
        control.reset()
    if Start == True:
        led.toggle(X, 3)
        if T1 != T:
            T1 = T
            led.unplot(T, 3)
        Timer = Timer + 1
        if Timer == 500:
            Timer = 0
            if Time >= 300:
                Time = Time - 100
basic.forever(on_forever)
