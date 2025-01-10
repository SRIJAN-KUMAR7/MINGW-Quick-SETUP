# Python script
import requests
from tqdm import tqdm  # For the progress bar to show on  terminal to visualize 

def download_mingw(url, dest_path):
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        with open(dest_path, 'wb') as file, tqdm(
            desc="Downloading MinGW",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                bar.update(len(data))
        print(f"Downloaded MinGW to {dest_path}")
    except Exception as e:
        print(f"Error while downloading MinGW: {e}")
        exit(1)
