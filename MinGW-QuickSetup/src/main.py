# Python script
import os
from downloader import download_mingw
from installer import install_mingw

def main():
    print("Welcome to MinGW Quick Setup!")
    mingw_url = ""  # Replace with actual MinGW download link
    download_path = os.path.join(os.getcwd(), "mingw.zip")
    install_path = os.path.join(os.getcwd(), "MinGW")

    print("\nStep 1: Downloading MinGW...")
    download_mingw(mingw_url, download_path)

    print("\nStep 2: Installing MinGW...")
    install_mingw(download_path, install_path)

    print("\nMinGW setup completed successfully!")
    print(f"Make sure to add '{install_path}\\bin' to your PATH environment variable.")

if __name__ == "__main__":
    main()
