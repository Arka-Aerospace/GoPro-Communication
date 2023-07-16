from open_gopro import WirelessGoPro, Params
from time import sleep


with WirelessGoPro(sudo_password="1qaz0plm") as gopro:
    print("connected")
    gopro.ble_command.load_preset_group(group=Params.PresetGroup.VIDEO)
    gopro.ble_setting.fps.set(Params.FPS.FPS_24)
    gopro.ble_setting.resolution.set(Params.Resolution.RES_5K)
    gopro.ble_setting.video_field_of_view.set(Params.VideoFOV.LINEAR)
    gopro.ble_command.set_shutter(shutter=Params.Toggle.ENABLE)
    sleep(10)
    gopro.ble_command.set_shutter(shutter=Params.Toggle.DISABLE)

    while True:
        pass