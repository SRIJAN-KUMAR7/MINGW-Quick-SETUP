# Python script
from downloader import download_mingw

def test_download_mingw():
    url = ""  #testing url 
    dest_path = "test_mingw.zip"
    download_mingw(url, dest_path)
    assert os.path.exists(dest_path)
