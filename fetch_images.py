from open_gopro import WirelessGoPro, Params

with WirelessGoPro(target="GoPro 9947", sudo_password="1qaz0plm") as gopro:
    resp = gopro.http_command.get_media_list()
    for file in resp.data.get("files", []):
        name = str(file["n"])
        if name.endswith(".JPG"):
            gopro.http_command.download_file(camera_file=name, ) 