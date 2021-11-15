input.onButtonPressed(Button.A, function () {
    if (X > 1 && Start == true) {
        music.playTone(740, music.beat(BeatFraction.Sixteenth))
        T = X
        X = X - 1
    }
})
input.onButtonPressed(Button.B, function () {
    if (X < 3 && Start == true) {
        music.playTone(740, music.beat(BeatFraction.Sixteenth))
        T = X
        X = X + 1
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (Start == false) {
        BT_A = true
    }
})
let T1 = 0
let D2 = 0
let E1 = 0
let T = 0
let BT_A = false
let Start = false
let X = 0
music.startMelody(music.builtInMelody(Melodies.Prelude), MelodyOptions.Once)
let D1 = 5
X = 2
let Timer = 0
let Time = 500
Start = false
basic.showString("PRESS LOGO")
while (!(BT_A)) {
    music.playTone(698, music.beat(BeatFraction.Sixteenth))
    basic.showIcon(IconNames.Diamond)
    music.playTone(784, music.beat(BeatFraction.Sixteenth))
    basic.showIcon(IconNames.SmallDiamond)
}
basic.clearScreen()
for (let index = 0; index <= 4; index++) {
    led.plot(index, 0)
    music.playTone(659, music.beat(BeatFraction.Quarter))
}
for (let index = 0; index <= 3; index++) {
    led.plot(4, index + 1)
    music.playTone(698, music.beat(BeatFraction.Quarter))
}
for (let index = 0; index <= 3; index++) {
    led.plot(3 - index, 4)
    music.playTone(740, music.beat(BeatFraction.Quarter))
}
for (let index = 0; index <= 2; index++) {
    led.plot(0, 3 - index)
    music.playTone(784, music.beat(BeatFraction.Quarter))
}
for (let index = 0; index <= 2; index++) {
    led.plot(index + 1, 1)
    music.playTone(831, music.beat(BeatFraction.Quarter))
}
for (let index = 0; index <= 1; index++) {
    led.plot(3, index + 2)
    music.playTone(880, music.beat(BeatFraction.Half))
}
for (let index = 0; index <= 1; index++) {
    led.plot(2 - index, 3)
    music.playTone(932, music.beat(BeatFraction.Half))
}
for (let index = 0; index <= 1; index++) {
    led.plot(index + 1, 2)
    music.playTone(988, music.beat(BeatFraction.Whole))
}
basic.pause(1000)
basic.clearScreen()
Start = true
music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.ForeverInBackground)
loops.everyInterval(1, function () {
    basic.pause(Time)
    if (Start == true) {
        if (D1 > 4) {
            led.unplot(E1, D1 - 1)
            E1 = randint(1, 3)
            D1 = 0
        }
        led.plot(E1, D1)
        led.unplot(E1, D1 - 1)
        led.plot(0, D2)
        led.plot(4, D2)
        if (D1 >= 0 && D1 < 5) {
            D1 = D1 + 1
        }
        if (D2 >= 0 && D2 < 5) {
            D2 = D2 + 1
        } else {
            D2 = 0
        }
    }
})
basic.forever(function () {
    if (X == E1 && D1 == 4) {
        Start = false
        led.stopAnimation()
        music.stopAllSounds()
        music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
        for (let index = 0; index <= 1; index++) {
            basic.showLeds(`
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                `)
            basic.pause(300)
            basic.showLeds(`
                . # # # .
                # . # . #
                # # . # #
                # . # . #
                . # # # .
                `)
            basic.pause(300)
        }
        basic.pause(200)
        control.reset()
    }
    if (Start == true) {
        led.toggle(X, 3)
        if (T1 != T) {
            T1 = T
            led.unplot(T, 3)
        }
        Timer = Timer + 1
        if (Timer == 500) {
            Timer = 0
            if (Time >= 300) {
                Time = Time - 100
            }
        }
    }
})
