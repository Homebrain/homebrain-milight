"""

A set of example actions for the homebrain-milight python library

"""

import milight
from time import sleep

def on(zone):
    msg = milight.on(zone)
    milight.send_cmd(msg)

def off(zone):
    msg = milight.off(zone)
    milight.send_cmd(msg)

def whitemode(zone):
    # Select zone
    msg = milight.on(zone)
    milight.send_cmd(msg)
    # Send brightness message
    msg = milight.whitemode()
    milight.send_cmd(msg)

def brightness(zone, brightness):
    # Select zone
    msg = milight.on(zone)
    milight.send_cmd(msg)
    # Send brightness message
    msg = milight.brightness(brightness)
    milight.send_cmd(msg)

def hue(zone, hue):
    # Select zone
    msg = milight.on(zone)
    milight.send_cmd(msg)
    # Send brightness message
    msg = milight.hue(hue)
    milight.send_cmd(msg)

def blink(zone=0, loop=False, sleeptime=1):
    while True:
        ZONE = 0
        send_cmd(on(zone))
        sleep(sleeptime)
        send_cmd(off(zone))
        if not loop:
            break
        sleep(sleeptime)

def strobe(zone, time):
    blink(zone, time)

def fade_brightness(zone, time, fadein=True):
    """
    Fades in from lowest to highest during a total of the passed argument time.
    If argument fadein is set to False it will instead fade out from the highest to lowest.
    """
    # Select zone
    msg = milight.on(zone)
    milight.send_cmd(msg)
    # Loop brightness levels
    step = time/BRIGHTNESS_LEVELS
    for i in range(BRIGHTNESS_LEVELS):
        if not fadein:
            i = (BRIGHTNESS_LEVELS-1) - i
        send_cmd(brightness(i))
        sleep(step)


def fadein(zone, time):
    fade_brightness(zone, time, True)

def fadeout(zone, time):
    fade_brightness(zone, time, False)
