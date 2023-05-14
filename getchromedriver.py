# will get and install the latest chrome driver
# https://gist.github.com/y3rsh/b55d5c8daaac7fb1632cc5a3380aec93

import requests
import zipfile
import io
import re
import subprocess
from sys import platform

class GetChromedriver:
    LATEST_URL = "http://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    BASE_URL = "http://chromedriver.storage.googleapis.com/"
    MAC_FILENAME = "chromedriver_mac64.zip"
    LINUX_FILENAME = "chromedriver_linux64.zip"
    TARGET_DIR = "/usr/bin/chromedriver"  # change me; this is the path on the raspberry pi

    def __init__(self):
        self.latest = self._get_latest_version()
        self.installed = self._get_installed_version()
        self.download_url = self._build_download_url()

    def _get_latest_version(self):
        response = requests.get(self.LATEST_URL)
        text = response.text
        print(f"latest version is {text}")
        return text

    def _get_installed_version(self):
        try:
            installed = str(
                subprocess.run(["chromedriver", "-v"], stdout=subprocess.PIPE).stdout
            )
        except:
            installed = (
                "0.0.0.0"
            )  # this is the pattern of the versioning chromedriver is following.
        version = re.findall("\d+\.\d+\.\d+\.\d+", installed)[0]
        print(f"installed version is {installed}")
        print(f"extracted version number is {version}")
        return version

    def _build_download_url(self):
        filename = self.MAC_FILENAME if platform == "darwin" else self.LINUX_FILENAME
        url = f"{self.BASE_URL}{self.latest}/{filename}"
        print(f"download url is {url}")
        return url

    def download_extract(self):
        if self.latest != self.installed:
            print("downloading latest chromedriver")
            response = requests.get(self.download_url, stream=True)
            zip_file = zipfile.ZipFile(io.BytesIO(response.content))
            zip_file.extractall(self.TARGET_DIR)
            subprocess.run(["chmod", "0777", f"{self.TARGET_DIR}/chromedriver"])
        else:
            print("latest version is installed")


if __name__ == "__main__":
    """
    decide what you want to be the TARGET_DIR
    add the TARGET_DIR to your path
    run the below command
    sudo python getchromedriver.py
    """
    get_chromedriver = GetChromedriver()
    get_chromedriver.download_extract()