import re
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import subprocess

# URL of the web page to scrape
url = "https://chromium.woolyss.com/"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, "html.parser")

# Find the first <a> tag with a "title" attribute
a_tag = soup.find("a", title=re.compile(r"_ungoogled_mini_installer\.exe"))

# Extract the link from the <a> tag
link = a_tag["href"]

# Extract the filename from the link
filename = link.split("/")[-1]

# Check if the file already exists
if os.path.exists(filename):
    print(f"Removing existing file: {filename}")
    os.remove(filename)

# Get the total file size from the response headers
total_size = int(requests.head(link).headers.get("content-length", 0))

# Display file information and ask for user confirmation
print("File Name:", filename)
choice = input("Do you want to download this file? (y/n): ")

if choice.lower() in ['y', 'yes']:
    # Send a GET request to the link
    file_response = requests.get(link, stream=True)

    # Initialize the progress bar
    progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)

    # Save the file in the current directory
    with open(filename, "wb") as file:
        for chunk in file_response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
                progress_bar.update(len(chunk))

    # Close the progress bar
    progress_bar.close()

    print(f"\nDownloaded: {filename}")

    # Code to execute the downloaded file
    try:
        print(f"Executing file: {filename}")
        subprocess.run([filename], shell=True)
    except Exception as e:
        print(f"An error occurred while executing the file: {e}")

    # Ask if the user wants to delete the file
    delete_choice = input(f"Do you want to delete the file '{filename}'? (y/n): ")
    if delete_choice.lower() in ['y', 'yes']:
        try:
            os.remove(filename)
            print(f"File '{filename}' has been deleted.")
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")
else:
    print("Download canceled.")
