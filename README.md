# windows-set-static-ip-gui

![Platform](https://img.shields.io/badge/platform-Windows-0078D6?style=for-the-badge)
![Language](https://img.shields.io/badge/language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/gui-PyQt6-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![Tool](https://img.shields.io/badge/tool-netsh-F97316?style=for-the-badge)
![Protocol](https://img.shields.io/badge/protocol-IPv4-22C55E?style=for-the-badge)
![Mode](https://img.shields.io/badge/mode-Static%20%26%20DHCP-EF4444?style=for-the-badge)
![Runs In](https://img.shields.io/badge/runs%20in-GUI-8B5CF6?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-22C55E?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

## About

**windows-set-static-ip-gui** is a lightweight Windows graphical tool that lets you configure IPv4 settings without opening Control Panel.
The tool is built with Python and PyQt6, and uses `netsh` to apply network changes directly, so no installation, dependencies, or backend are required.

> [!NOTE]
> **The tool provides three main actions:**
> - **View Current IP Configuration** — Display the current IPv4 settings of all adapters.
> - **Set Static IP Address** — Assign a static IPv4 address, subnet mask, and optional gateway.
> - **Set IP to DHCP** — Revert the adapter back to automatic (DHCP) mode.

The tool automatically requests administrator privileges on launch, so users can simply double-click and follow the interface.

## Screenshots

<p align="center">
  <img width="32%" alt="View Current IP" src="https://github.com/user-attachments/assets/96b0cf53-f884-48a5-a292-1b777ab5bb63" />
  <img width="32%" alt="Set Static IP" src="https://github.com/user-attachments/assets/cb6c5db6-2d09-4374-9f06-9819297c8d28" />
  <img width="32%" alt="Set DHCP" src="https://github.com/user-attachments/assets/4a62691c-d3be-4c90-9877-e59d94a9f1da" />
</p>

## Download

> [!TIP]
> **Ready-to-run executable:**
> [Download WindowsSetStaticIPGUI.exe](https://github.com/fouad-salehi/windows-set-static-ip-gui/releases/latest/download/WindowsSetStaticIPGUI.exe)
>
> No Python installation required. Just download, run, and start configuring.

## Technologies

- Python 3.10+
- PyQt6
- `netsh` command-line utility
- Windows UAC (User Account Control)
- PyInstaller
- GitHub

## Features

- Browser-free, install-free GUI tool
- Automatic administrator privilege request
- View current IP configuration
- Set static IPv4 address with subnet mask and gateway
- Revert to DHCP (automatic)
- Clean tabbed interface
- Lightweight and portable (single `.exe`)

## Installation

### Option 1 — Clone the repository

```bash
git clone https://github.com/fouad-salehi/windows-set-static-ip-gui.git
cd windows-set-static-ip-gui
pip install -r requirements.txt
```

Then run `python main.py`.

### Option 2 — Download directly

> [!TIP]
> **Direct download:**
> [WindowsSetStaticIPGUI.exe](https://github.com/fouad-salehi/windows-set-static-ip-gui/releases/latest/download/WindowsSetStaticIPGUI.exe)

Download the file and double-click it — no installation required.

## Usage

1. Run `WindowsSetStaticIPGUI.exe` (or `python main.py`). It will automatically request administrator privileges.
2. Choose a tab from the interface:
   - **View Current IP** — View current IP configuration
   - **Set Static IP** — Set a static IPv4 address
   - **Set DHCP** — Revert to DHCP (automatic)
3. Fill in the fields and click Apply.

## Build

```bash
cd build
pyinstaller build.spec
```

The output binary will appear in `build/dist/WindowsSetStaticIPGUI.exe`.

## Project

A small utility for IT administrators and everyday users who need to switch between static and DHCP IPv4 configurations quickly, without navigating through Windows Control Panel.

> [!NOTE]
> This is the GUI counterpart of the CLI tool [windows-set-static-ip](https://github.com/fouad-salehi/windows-set-static-ip).

## Author

[**Fouad Salehi**](https://github.com/fouad-salehi)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
