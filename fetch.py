from open_gopro import WirelessGoPro

def fetch(device_name: str):
    with WirelessGoPro(target=device_name, sudo_password="1qaz0plm") as gopro:
        resp = gopro.http_command.get_media_list()
        for file in resp.data.get("files", []):
            name = str(file["n"])
            if not name.endswith(".MP4"):
                continue
            gopro.http_command.download_file(camera_file=name)

fetch("GoPro 9947")