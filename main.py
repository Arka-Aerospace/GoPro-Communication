from open_gopro import WirelessGoPro, Params
from time import sleep
import sys
import os
import signal
import subprocess

class TerminationSignal(Exception):
    pass

def termination_handler(signum, frame):
    raise TerminationSignal("Received SIGTERM")

# Get parent process id from arguments
parent_pid = int(sys.argv[1])
subprocess.call(["rfkill", "unblock", "bluetooth"])
signal.signal(signal.SIGTERM, termination_handler)

with WirelessGoPro(enable_wifi=False,sudo_password="7036841181") as gopro:
    print("Connected")
    os.kill(parent_pid, signal.SIGUSR1)
    print("Sent Connection Status")
    
    while True:
        try:
            sleep(1)
        except TerminationSignal:
            break
        except KeyboardInterrupt:
            exit()
    print("Shutter ON")
    gopro.ble_command.set_shutter(shutter=Params.Toggle.ENABLE)
    while True:
        try:
            sleep(1)
        except TerminationSignal:
            break
        except KeyboardInterrupt:
            exit()
    print("Shutter OFF")
    gopro.ble_command.set_shutter(shutter=Params.Toggle.DISABLE)

