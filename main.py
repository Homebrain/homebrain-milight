import socket
from time import sleep

_ZONE_ARRAY = [0x42, 0x45, 0x47, 0x49, 0x4B]

def _get_zone(zone):
    return _ZONE_ARRAY[zone]

def _msg(b1, b2=0x00, b3=0x55):
    return bytes([b1, b2, b3])

def on(zone):
    msg = _msg(_get_zone(zone))
    return msg

def off(zone):
    if zone == 0:
        return _msg(0x41)
    else:
        return _msg(_get_zone(zone)+1)

def _print_cmd(cmd):
    print(list(map(hex, cmd)))

def send_cmd(cmd):
    _print_cmd(cmd)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(cmd, ('255.255.255.255', 8899))

def blink(loop=False):
    while True:
        ZONE = 0
        SLEEP_TIME = 1
        send_cmd(on(ZONE))
        sleep(SLEEP_TIME)
        send_cmd(off(ZONE))
        if not loop:
            break
        sleep(SLEEP_TIME)

if __name__ == "__main__":
    blink(loop=False)
