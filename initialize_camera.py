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
    p = subprocess.Popen(["python", "burst.py", str(os.getpid())])
    while True:
        try:
            sleep(1)
        except ChildStartedSignal:
            signal.signal(signal.SIGUSR1, signal.SIG_DFL)  # Unregister the signal handler
            return p.pid

def kill_camera(p: int):
    os.kill(p, signal.SIGTERM)
    subprocess.call(["rfkill", "block", "bluetooth"])

if __name__ == "__main__":
    pid = initialize_camera()
    print("initialized camera")
    for i in range(5):
        sleep(1)
        print(i+1)
    kill_camera(pid)