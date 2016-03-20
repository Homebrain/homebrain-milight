#!/usr/bin/env python3
from miactions import *
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("milight-cli")

cmd_to_f = {"on": on, "off": off, "whitemode": whitemode,
            "blink": blink,
            "hue": hue, "brightness": brightness,
            "fadein": fadein, "fadeout": fadeout, "strobe": strobe}

def printhelp():
    print(
    "\n"+
    "Milight Command Line Interface\n"+
    "==============================\n"+
    "\n"+
    "Usage: \n"+
    "   milight zone action [value] \n"+
    "\n"+
    "Actions: \n"+
    " - on \n"+
    " - off \n"+
    " - blink \n"+
    " - hue [0-255]\n"+
    " - brightness [0-19]\n"+
    " - whitemode \n"+
    " - fadein [0,1..]\n"+
    " - fadeout [0,1..]\n"+
    " - strobe [0,1..]\n"
    )

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        logger.error("No zone specified")
        printhelp()
        exit()
    elif len(sys.argv) <= 2:
        logger.error("No action specified")
        printhelp()
        exit()

    zone = int(sys.argv[1])
    cmd = sys.argv[2]

    if cmd in ["on", "off", "whitemode", "blink"]:
        cmd_to_f[cmd](zone)

    elif cmd in ["hue", "brightness", "whitemode", "fadein", "fadeout", "strobe"]:
        if len(sys.argv) <= 3:
            logger.error("Action needs value, and no value was specified")
            printhelp()
            exit()

        value = int(sys.argv[3])
        cmd_to_f[cmd](zone, value)
    else:
        logger.error("Unknown action")
        printhelp()
        exit()
