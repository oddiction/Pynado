# Audio Metadata Analysis Script

## Overview
This script analyzes audio files in a specified folder, extracts metadata, and generates an Excel spreadsheet with the results.

## Prerequisites
- **Python:** Ensure that you have Python 3 installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

- **Required Python Libraries:**
  - `os`: Built-in library (available by default).
  - `wave`: Built-in library for working with WAV files (available by default).
  - `xlsxwriter`: External library for creating Excel files. Install it using:
    ```bash
    pip install XlsxWriter
    ```
  - `tqdm`: External library for displaying progress bars. Install it using:
    ```bash
    pip install tqdm
    ```

## Usage
1. Clone or download the script from this repository.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the script.

4. Run the script by entering the following command:
    ```bash
    python packList.py
    ```

5. Follow the on-screen instructions to provide the path to the folder containing your audio files.

6. The script will generate a simple Excel file with metadata analysis results in the same folder as the script.

## Notes
- The script assumes that the audio files are in WAV format.

- The script assumes the audio files are in sub folders.

- Make sure to provide the correct path to the folder containing your audio files when prompted.

- The Excel file will include metadata such as file name, bit depth, channels, sample rate, minutes, and seconds.

- The Excel file is a bit crude, and will need some additional styling, but the heavy lifting is done. ;-)

- The last two rows in the Excel file display the total number of files and the total size of the analyzed folder (it counts the Excel file too).

## Author
Oddiction

## License
This project is licensed under the [GNU General Public License v3.0 (GPL-3.0)](LICENSE).
