import ctypes
import urllib.request
import os
import shutil

# Variables
url = "https://github.com/wxWidgets/wxWidgets/releases/download/v3.2.1/wxWidgets-3.2.1.zip"
filename = "wxWidgets-3.2.1.zip"
finalpath = "C:\\wxWidgets-3.2.1"


def main():
    # Main
    downloadWxWidgets()
    extractWxWidgets()
    buildWxWidgets()
    setEnvironmentVariables()


def downloadWxWidgets():
    # Download wxWidgets
    print("[-] Downloading wxWidgets...")
    urllib.request.urlretrieve(url, filename)
    print("[-] Download complete!")


def extractWxWidgets():
    # Extract wxWidgets
    print("[-] Extracting wxWidgets...")
    shutil.unpack_archive(filename, finalpath)
    shutil.move(os.getcwd() + f"\\{filename}", f"{finalpath}.zip")
    print("[-] Extraction complete!")


def buildWxWidgets():
    # Build wxWidgets
    # This is a bit of a hack, but it works
    print("[-] Building wxWidgets...")
    os.chdir(f"{finalpath}\\build\\msw")
    print("[-] Building wxWidgets Debug (x64)...")
    os.system("msbuild wx_vc17.sln /p:Configuration=Debug /p:Platform=x64")
    print("[-] Building wxWidgets Release (x64)...")
    os.system("msbuild wx_vc17.sln /p:Configuration=Release /p:Platform=x64")
    print("[-] Building wxWidgets Debug (Win32)...")
    os.system("msbuild wx_vc17.sln /p:Configuration=Debug /p:Platform=Win32")
    print("[-] Building wxWidgets Release (Win32)...")
    os.system("msbuild wx_vc17.sln /p:Configuration=Release /p:Platform=Win32")
    print("[-] Build complete!")


def setEnvironmentVariables():
    # Set environment variables
    print("[-] Setting environment variables...")
    os.system(f"setx WXWIN \"{finalpath}\" /M")
    print("[-] Environment variables set!")


def checkAdmin():
    # Check if running as admin
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


if __name__ == "__main__":
    print("[-] Checking for admin privileges...")
    if checkAdmin():
        main()
    else:
        print("[!] Please run as admin")
        exit(0)
