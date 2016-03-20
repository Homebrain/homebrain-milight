"""
A small library for controlling Milights.


Usage:

 - Call the on(zone) function with the zone of choice
 - Use any of the other commands to control the lamp turned on with on(zone)

"""

import socket
from time import sleep
import logging

# Zones used for selecting and turning on lamps,
# the array used for turning lamps off is similar (see `off()` function)
_ZONE_ARRAY = [0x42, 0x45, 0x47, 0x49, 0x4B]

# The values below 0x02 do nothing, values above 0x1B also do nothing
_BRIGHTNESS_ARRAY = list(range(0x02, 0x1C))
BRIGHTNESS_LEVELS = len(_BRIGHTNESS_ARRAY)

HUE_RED = 174;
HUE_BLUE = 240;

logger = logging.getLogger("milight")

def _get_zone(zone):
    return _ZONE_ARRAY[zone]

def _msg(b1, b2=0x00, b3=0x55):
    return bytes([b1, b2, b3])

def _print_cmd(cmd):
    logger.debug("Bytes sent to WiFi hub: " + str(list(map(hex, cmd))))

def on(zone):
    msg = _msg(_get_zone(zone))
    return msg

def off(zone):
    if zone == 0:
        return _msg(0x41)
    else:
        return _msg(_get_zone(zone)+1)

def hue(h):
    """h should be a value in the range 0-255"""
    return _msg(0x40, h)

def brightness(b):
    """b should be in range 0-19"""
    return _msg(0x4E, _BRIGHTNESS_ARRAY[b])

def whitemode():
    return _msg(0xC2)

def send_cmd(cmd):
    _print_cmd(cmd)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(cmd, ('255.255.255.255', 8899))

    # Ensures that the call is respected, calling repeatedly without this may cause package loss
    sleep(0.05)
