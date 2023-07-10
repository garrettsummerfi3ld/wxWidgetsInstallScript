# wxWidgetsInstallScript

A small Python script to install wxWidgets 3.2.1 and build automatically.

Tested on Windows 10/11 with Visual Studio 2022 (17)

GitHub Actions runs successfully on Windows 10/11 with Visual Studio 2019 (16) and 2022 (17). You can verify with the "Validate install" workflow running on a matrix of Python versions and Windows versions.

| Workflow           | Status                                                                                                                                                                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Validate install   | [![Validate install](https://github.com/garrettsummerfi3ld/wxWidgetsInstallScript/actions/workflows/validate-win.yml/badge.svg)](https://github.com/garrettsummerfi3ld/wxWidgetsInstallScript/actions/workflows/validate-win.yml)             |
| Pytest with flake8 | [![Pytest with flake8](https://github.com/garrettsummerfi3ld/wxWidgetsInstallScript/actions/workflows/test.yml/badge.svg)](https://github.com/garrettsummerfi3ld/wxWidgetsInstallScript/actions/workflows/test.yml)                           |
| Pylint             | [![Pylint](https://github.com/garrettsummerfi3ld/wxWidgetsInstallScript/actions/workflows/pylint.yml/badge.svg)](https://github.com/garrettsummerfi3ld/wxWidgetsInstallScript/actions/workflows/pylint.yml)                                   |
| CodeQL             | [![CodeQL](https://github.com/garrettsummerfi3ld/wxWidgetsInstallScript/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/garrettsummerfi3ld/wxWidgetsInstallScript/actions/workflows/github-code-scanning/codeql) |
| Qodana             | [![Qodana](https://github.com/garrettsummerfi3ld/wxWidgetsInstallScript/actions/workflows/qodana.yml/badge.svg)](https://github.com/garrettsummerfi3ld/wxWidgetsInstallScript/actions/workflows/qodana.yml)                                   |

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

- Clone repository
- Run `pip install -r requirements.txt`
- Open an **administrative** PowerShell or Command Prompt
  - You may need to go to the Start Menu > Visual Studio (`Version`) > Developer ... > Right-click and Run as Administrator
- `cd` to your downloaded `setup.py` file
- `python .\setup.py`
