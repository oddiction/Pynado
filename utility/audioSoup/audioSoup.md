# 👨‍🍳 Audio Soup Line Cook 👨‍🍳

This script generates a random audio soup file by selecting and combining a specified number of audio files from a given directory. The resulting audio soup is saved as a .wav file in a folder named audioSoup on your desktop.

The concept behind this script is to generate highly randomized audio files for use in granular engines like the one in Phaseplant, or to load the file into Serum as a sample, allowing for the creation of intriguing glitch soup!

The greater the randomness of the samples within the folder, the more peculiar and intriguing your audio soup will become.

---

## Prequisities

Before running the script, make sure you have the following libraries installed:

- numpy
- scipy
- soundfile
- tqdm

You can install/upgrade them using the following commands:
```bash
pip install --upgrade numpy
pip install --upgrade scipy
pip install --upgrade soundfile
pip install --upgrade tqdm
```
---

## Usage

- Run the script in a terminal or command prompt.
```bash
    python audioSoup.py
```

- You will be prompted to enter the number of samples to pick (between 10 and 250).
- Copy & Paste, or enter the local folder path where the script needs to look for the sounds.
- The script will randomly select audio files and cook a random audio file in *.wav format*.
- It will create a folder called *audioSoup* on your desktop.
    - The script adds a timestamp to the generated audio file, and it will also create a text file with the used samples (in case you need or want to clear any of the used samples 😇).
    -   In certain scenarios, the script may produce an error log with the same timestamp as the generated audio and text files (it's located in the same folder).

---

## Notes from the Creator
- Using high values of samples to pick from, and large sample libraries will slow down the cooking of your soup! Please wait patiently until the prompt Chef tells you the soup is cooked.
- Best practice is to use  smaller folders containing samples, rather than letting the script rummage through the root folder of your sample library.
- On occasion, the script might churn out massive and lengthy files, typically when there are extensive audio files in a folder, such as field recordings, stems, or complete songs.
    - There isn't a failsafe for extremely long audio files because, on occasion, they can yield particularly fascinating results. Processing lengthy (field) recordings could take as much as 45 minutes, but the potential for unique outcomes makes it worthwhile.
    - There's also no proper conversion for audio files above 44.1 kHz; however, this will lead to intriguing outcomes for your audio soup. Yes, voices may sound like smurfs, but hey, embrace the chaos!
- *Support?* 🥳 Nope, none available. The script is what it is.

## Author
[Oddiction](https://linktr.ee/oddiction)

## License
This project is licensed under the [GNU General Public License v3.0 (GPL-3.0)](LICENSE).
