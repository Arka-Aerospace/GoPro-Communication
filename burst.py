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
with WirelessGoPro(enable_wifi=False, target="GoPro 9947",sudo_password="1qaz0plm") as gopro:
    # gopro.ble_command.load_preset_group(group=Params.PresetGroup.PHOTO)
    # preset_groups = gopro.ble_command.get_preset_status()["preset_group_array"]
    # preset = parse_preset_groups(preset_groups)
    # if preset is None:
    #     print("preset burst not found")
    # print(preset)

    # gopro.ble_command.load_preset(preset=int(preset["id"]))
    # gopro.ble_setting.fps.set(Params.FPS.FPS_24)
    gopro.ble_setting.resolution.set(Params.Resolution.RES_5_3_K)
    # gopro.ble_setting.video_field_of_view.set(Params.VideoFOV.LINEAR)
    gopro.ble_command.set_shutter(shutter=Params.Toggle.ENABLE)
    os.kill(parent_pid, signal.SIGUSR1)
    while True:
        try:
            gopro.ble_command.set_shutter(shutter=Params.Toggle.ENABLE)
        except TerminationSignal:
            break
    # sleep(10)
    # gopro.ble_command.set_shutter(shutter=Params.Toggle.DISABLE)

    # while True:
    #     pass

