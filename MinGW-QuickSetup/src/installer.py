import zipfile
import os
import ctypes

def install_mingw(zip_path, install_dir):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(install_dir)
        print(f"Extracted MinGW to {install_dir}")
        bin_path = os.path.join(install_dir, "bin")
        add_to_path(bin_path)
    except Exception as e:
        print(f"Error while installing MinGW: {e}")
        exit(1)

def add_to_path(bin_path):
    try:
        key = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        reg = ctypes.windll.advapi32.RegOpenKeyExW
        if os.name == 'nt':  
            os.environ["PATH"] += f";{bin_path}"
            print(f"Added '{bin_path}' to PATH. Please restart your terminal.")
    except Exception as e:
        print(f"Error adding to PATH: {e}")
