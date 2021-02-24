basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)

def on_forever():
    if input.sound_level() == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif input.sound_level() > 0 and input.sound_level() <= 51:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            """)
    elif input.sound_level() > 51 and input.sound_level() <= 102:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
    elif input.sound_level() > 102 and input.sound_level() <= 153:
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
    elif input.sound_level() > 153 and input.sound_level() <= 204:
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    else:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
basic.forever(on_forever)
