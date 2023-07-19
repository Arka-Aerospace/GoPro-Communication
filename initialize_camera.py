import subprocess
import os
from time import sleep
import signal

SUDO_PASSWORD = "animesh"

class ChildStartedSignal(Exception):
    pass

def child_started_handler(signum, frame):
    raise ChildStartedSignal("Child process has started")


def disable_bluetooth():
    os.system(f'echo "{SUDO_PASSWORD}\n" | sudo -S rfkill block bluetooth')

def enable_bluetooth():
    os.system(f'echo "{SUDO_PASSWORD}\n" | sudo -S rfkill unblock bluetooth')

def initialize_camera():
    enable_bluetooth()
    handler = signal.signal(signal.SIGUSR1, child_started_handler)
    p = subprocess.Popen(["python3.9", "/home/animesh/GoPro-Communication/main.py", str(os.getpid())])
    while True:
        try:
            sleep(1)
        except ChildStartedSignal:
            return p.pid
        except KeyboardInterrupt:
            exit()

def start_recording(p: int):
    os.kill(p, signal.SIGTERM)
    while True:
        try:
            sleep(1)
        except ChildStartedSignal:
            print("Started Recording")
            break
        except KeyboardInterrupt:
            exit()

def kill_camera(p: int):
    os.kill(p, signal.SIGTERM)
    while True:
        try:
            sleep(1)
        except ChildStartedSignal:
            print("End Recording")
            signal.signal(signal.SIGUSR1, signal.SIG_DFL)  # Unregister the signal handler
            break
        except KeyboardInterrupt:
            exit()
    disable_bluetooth()

if __name__ == "__main__":
    print("Initializing Camera")
    pid = initialize_camera()
    print("initialized camera")
    sleep(1)
    start_recording(pid)
    for i in range(5):
        sleep(1)
        print(i+1)
    kill_camera(pid)