# Setup for Raspberry Pi

### Install `python3.9`

```bash
sudo apt install python3.9
```

### Install BlueZ
```bash
sudo apt install bluez*
```


### Install OpenGoPro

```bash
git clone https://github.com/gopro/OpenGoPro
```

```bash
cd OpenGoPro/demos/python/sdk_wireless_camera_control
```

```bash
python3.9 -m pip install .
```

### Upgrade protobuf
```bash
python3.9 -m pip install --upgrade protobuf
```
