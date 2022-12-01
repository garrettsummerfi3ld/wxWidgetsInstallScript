# wxWidgetsInstallScript

A small Python script to install wxWidgets 3.2.1 and build automatically.

Tested on Windows 10/11 with Visual Studio 2022 (17)

## Requirements

- Visual Studio with Desktop C++ installed
- Python 3
- Internet connection

## What does this script do?

This script downloads a specific release of wxWidgets and builds from that source and sets environment variables on the whole system.

Current configurations and architectures built are:

- Debug x64
- Debug Win32
- Release x64
- Release Win32

## Steps to run

- Clone or download `setup.py`
- Open an **administrative** Visual Studio PowerShell or Command Prompt
  - You may need to go to the Start Menu > Visual Studio (`Version`) > Developer ... > Right-click and Run as Administrator
- `cd` to your downloaded `setup.py` file
- `python .\setup.py`
