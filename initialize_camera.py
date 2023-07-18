import subprocess
import os
from time import sleep
import signal

class ChildStartedSignal(Exception):
    pass

def child_started_handler(signum, frame):
    raise ChildStartedSignal("Child process has started")


def initialize_camera():
    subprocess.call(["rfkill", "unblock", "bluetooth"])
    handler = signal.signal(signal.SIGUSR1, child_started_handler)
    p = subprocess.Popen(["python3.9", "main.py", str(os.getpid())])
    while True:
        try:
            pass
        except ChildStartedSignal:
            print("registered")
            signal.signal(signal.SIGUSR1, signal.SIG_DFL)  # Unregister the signal handler
            return p.pid
        except KeyboardInterrupt:
            exit()

def start_recording(p: int):
    os.kill(p, signal.SIGTERM)

def kill_camera(p: int):
    os.kill(p, signal.SIGTERM)
    subprocess.call(["rfkill", "block", "bluetooth"])

if __name__ == "__main__":
    print("Initializing Camera")
    pid = initialize_camera()
    print("initialized camera")
    start_recording(pid)
    for i in range(5):
        sleep(1)
        print(i+1)
    kill_camera(pid)