# windows-set-static-ip-gui

A simple Windows GUI tool to set static IPv4 addresses and switch back to DHCP.
Built with Python and PyQt6. GUI counterpart of [windows-set-static-ip](https://github.com/fouad-salehi/windows-set-static-ip).

## Features

- View current IPv4 configuration of all adapters
- Set a static IPv4 address, subnet mask and gateway
- Revert adapter back to DHCP
- Automatic UAC elevation
- Clean, lightweight Qt interface

## Requirements

- Windows 10 or 11
- Python 3.10+
- Administrator privileges

## Install

```
pip install -r requirements.txt
```

## Run

```
python main.py
```

## Build a single executable

```
cd build
pyinstaller build.spec
```

The output binary will appear in `build/dist/StaticIPConfig.exe`.

## Project layout

```
windows-set-static-ip-gui/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── ui/
│   ├── main_window.py
│   ├── view_tab.py
│   ├── setip_tab.py
│   ├── dhcp_tab.py
│   └── theme.py
├── core/
│   ├── admin.py
│   ├── network.py
│   └── validators.py
├── assets/
└── build/
    └── build.spec
```

## License

MIT
