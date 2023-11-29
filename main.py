basic.show_icon(IconNames.HAPPY)

def on_forever():
    basic.show_icon(IconNames.HAPPY)
    cuteBot.forward()
    basic.pause(500)
    cuteBot.motors(100, 40)
    basic.pause(100)
    cuteBot.forward()
    basic.pause(100)
    cuteBot.forward()
    basic.pause(100)
    cuteBot.motors(40, 100)
    basic.pause(500)
    cuteBot.forward()
    basic.pause(100)
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
