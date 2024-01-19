import ctypes
import urllib.request
import os
import shutil
import hashlib
import requests
import progressbar
import subprocess
import vswhere

# Variables
url = "https://github.com/wxWidgets/wxWidgets/releases/download/v3.2.3/wxWidgets-3.2.3.zip"
filename = "wxWidgets-3.2.3.zip"
finalpath = "C:\\wxWidgets-3.2.3"
checksum = "8ecc70034bf7d6ab8725114eb745404553cdf8dc"
pbar = None
configuration = [ "Debug", "Release" ]
platform = [ "x64", "Win32" ]

def main():
    # Main
    download_wxwidgets()
    extract_wxwidgets()
    build_wxwidgets()
    set_environment_variables()


def show_progress(block_num, block_size, total_size):
    # Progress bar
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

def fetch_releases():
    # Fetch releases
    print("[-] Fetching releases...")
    response = requests.get("https://api.github.com/repos/wxWidgets/wxWidgets/releases")
    data = response.json()
    print(data)


def download_wxwidgets():
    # Download wxWidgets
    print("[-] Downloading wxWidgets...")
    urllib.request.urlretrieve(url, filename, show_progress)
    print("[-] Download complete!")
    print("[-] Checking checksum...")
    if hashlib.sha1(open(filename, "rb").read()).hexdigest() == checksum:
        print("[-] Checksum matches!")
    else:
        print("[!] Checksum does not match!")
        exit(0)


def extract_wxwidgets():
    # Extract wxWidgets
    print("[-] Extracting wxWidgets...")
    shutil.unpack_archive(filename, finalpath)
    shutil.move(os.getcwd() + f"\\{filename}", f"{finalpath}.zip")
    print("[-] Extraction complete!")


def build_wxwidgets():
    # Build wxWidgets
    msbuild_path = find_msbuild()
    vsversion = determine_msbuild_vs_version()
    print(msbuild_path)
    print("[-] Building wxWidgets...")
    os.chdir(f"{finalpath}\\build\\msw")
    for config in configuration:
        for plat in platform:
            print(f"[-] Building wxWidgets {config} ({plat})...")
            subprocess.run([msbuild_path, f"wx_vc{vsversion}.sln", f"/p:Configuration={config}", f"/p:Platform={plat}"])
    print("[-] Build complete!")


def set_environment_variables():
    # Set environment variables
    print("[-] Setting environment variables...")
    os.system(f"setx WXWIN \"{finalpath}\" /M")
    print("[-] Environment variables set!")


def find_msbuild():
    # Find msbuild.exe
    print("[-] Finding msbuild.exe...")
    vspath = vswhere.get_latest_path()
    print(vspath)
    if vspath is not None:
        print("[-] Found msbuild.exe!")
        return vspath + "\\MSBuild\\Current\\Bin\\msbuild.exe"
    else:
        print("[!] Could not find msbuild.exe!")
        exit(0)

def determine_msbuild_vs_version():
    # Determine which version of Visual Studio is installed
    print("[-] Determining which version of Visual Studio is installed...")
    vsversion = vswhere.get_latest_major_version()
    if vsversion is not None:
        print(f"[-] Visual Studio {vsversion} is installed!")
        return vsversion
    else:
        print("[!] Could not determine which version of Visual Studio is installed!")
        exit(1)
    

def check_admin():
    # Check if running as admin
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


if __name__ == "__main__":
    print("[-] Checking for admin privileges...")
    if check_admin():
        main()
    else:
        print("[!] Please run as admin")
        exit(1)
