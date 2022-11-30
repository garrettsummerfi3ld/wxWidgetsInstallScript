import urllib.request
import os

def main():
    url = "https://github.com/wxWidgets/wxWidgets/releases/download/v3.2.1/wxWidgets-3.2.1.zip"
    filename = "wxWidgets-3.2.1.zip"
    urllib.request.urlretrieve(url, filename)

if __name__ == "__main__":
    main()