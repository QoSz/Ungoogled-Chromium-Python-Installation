
# Ungoogled Chromium Windows Downloader and Installer (`chrome.py`)

## Overview
This Python script, `chrome.py`, automates the process of downloading and installing the latest build of Ungoogled Chromium for Windows x86 systems. Ungoogled Chromium is a modification of Google's Chromium web browser with an emphasis on privacy and the minimization of Google's tracking.

## Prerequisites
- **Python 3.x**: Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Required Libraries**: The script requires several Python libraries listed in `requirements.txt`.

## Installation
1. **Clone or Download the Repository**:
   Download the script `chrome.py` and the `requirements.txt` file to your local machine.

2. **Install Dependencies**:
   Open your command line or terminal, navigate to the directory containing the downloaded files, and install the required Python libraries using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Script**:
   In your command line or terminal, execute the script with Python:
   ```bash
   python chrome.py
   ```

2. **Downloading the Browser**:
   The script will automatically find the latest Ungoogled Chromium build and prompt you to confirm the download. Type `y` (yes) to start downloading.

3. **Installation Process**:
   Once downloaded, the script will execute the installer. Follow the installation instructions provided by the installer.

4. **Post-Installation**:
   After installation, the script will ask if you want to delete the downloaded `.exe` file. Enter `y` (yes) to delete it, or `n` (no) to keep it.


## License
This script is provided "as is", without any warranty. Use at your own risk.
