# scan the page for links and if the link is a .swg file, download it into the /swfs folder


import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

LINK = "http://moldan.hu/doc/nemzeti/12_e/publication/pages/"
FOLDER = "swfs12"

# Create a folder to store the SWF files
os.makedirs(FOLDER , exist_ok=True)

# Send a GET request to the URL
response = requests.get(LINK)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links on the page
links = soup.find_all("a")

# Loop through the links
for link in links:
    href = link.get("href")
    if href and href.endswith(".swf"):
        # Construct the full URL of the SWF file
        swf_url = urljoin(LINK, href)
        # Extract the filename from the URL
        filename = os.path.basename(swf_url)
        # Download the SWF file
        response = requests.get(swf_url)
        with open(os.path.join(FOLDER , filename), "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")