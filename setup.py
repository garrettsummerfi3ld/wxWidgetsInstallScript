import ctypes
import urllib.request
import os
import shutil
import hashlib
import progressbar
import subprocess
import vswhere

# Variables
url = "https://github.com/wxWidgets/wxWidgets/releases/download/v3.2.3/wxWidgets-3.2.3.zip"
filename = "wxWidgets-3.2.3.zip"
finalpath = "C:\\wxWidgets-3.2.3"
checksum = "8ecc70034bf7d6ab8725114eb745404553cdf8dc"
pbar = None


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
    # It is a bit of a hack, but it works
    msbuild_path = find_msbuild()
    print(msbuild_path)
    print("[-] Building wxWidgets...")
    os.chdir(f"{finalpath}\\build\\msw")
    print("[-] Building wxWidgets Debug (x64)...")
    subprocess.run([msbuild_path, "wx_vc17.sln", "/p:Configuration=Debug", "/p:Platform=x64"])
    print("[-] Building wxWidgets Release (x64)...")
    subprocess.run([msbuild_path, "wx_vc17.sln", "/p:Configuration=Release", "/p:Platform=x64"])
    print("[-] Building wxWidgets Debug (Win32)...")
    subprocess.run([msbuild_path, "wx_vc17.sln", "/p:Configuration=Debug", "/p:Platform=Win32"])
    print("[-] Building wxWidgets Release (Win32)...")
    subprocess.run([msbuild_path, "wx_vc17.sln", "/p:Configuration=Release", "/p:Platform=Win32"])
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
