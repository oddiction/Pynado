import subprocess
import random
import soundfile as sf
import os
import numpy as np
from tqdm import tqdm
from datetime import datetime

# Install and upgrade necessary libraries
subprocess.run(['pip', 'install', '--upgrade', 'numpy'])
subprocess.run(['pip', 'install', '--upgrade', 'scipy'])
subprocess.run(['pip', 'install', '--upgrade', 'soundfile'])
subprocess.run(['pip', 'install', '--upgrade', 'tqdm'])

# Import required libraries
import numpy as np
import os

# Set parameters
duration = 10 * 60  # 10 minutes in seconds
sample_rate = 44100  # Sample rate in Hz
num_channels = 2  # Stereo

# Prompt the user to input the desired number of samples
num_samples = input("Please enter the number of samples to pick (between 10 and 250): ")
try:
    num_samples = int(num_samples)
    if num_samples < 10 or num_samples > 250:
        print("Invalid input. Please enter a number between 10 and 250.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Ask the user to paste the local folder path where the script needs to look for the sounds
print("Please paste the local folder path where the script needs to look for the sounds:")
folder_path = input()

# Check if the folder path is valid
if not os.path.isdir(folder_path):
    print("The provided folder path is not valid. Please try again.")
else:
    # Create a list of all audio files in the current directory and subdirectories
    audio_files = []
    for root, dirs, files in tqdm(os.walk(folder_path), desc="Searching for audio files"):
        for file in files:
            if file.endswith('.wav'):
                audio_files.append(os.path.join(root, file))
    
    # Check if there are any audio files in the provided folder and subdirectories
    if not audio_files:
        print("No audio files found in the provided folder and subdirectories. Please add some .wav files to the folder or its subdirectories.")
    else:
        # Randomly select a list of audio files
        selected_files = random.sample(audio_files, min(num_samples, len(audio_files)))
        
        # Find the longest audio file
        max_duration = 0
        error_log = []  # Initialize error log list
        for file in selected_files:
            try:
                audio_data, sample_rate = sf.read(file)
                max_duration = max(max_duration, audio_data.shape[0])
            except sf.SoundFileError as e:
                error_log.append(f"Error reading audio file '{file}': {e}")
        
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Get the desktop directory
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        
        # Create the audioSoup folder on the desktop if it doesn't exist
        audio_soup_folder = os.path.join(desktop_path, 'audioSoup')
        if not os.path.exists(audio_soup_folder):
            os.makedirs(audio_soup_folder)
        
        # Write error log to a file with timestamp
        error_log_file = f"error_log_{timestamp}.txt"
        error_log_path = os.path.join(audio_soup_folder, error_log_file)
        with open(error_log_path, "w", encoding="utf-8") as f:  # Specify encoding as UTF-8
            for error in error_log:
                f.write(error + "\n")
        
        # Combine the selected audio files
        combined_audio = np.zeros((max_duration, num_channels))
        for file in tqdm(selected_files, desc="Creating your sound soup!"):
            try:
                audio_data, sample_rate = sf.read(file)
                if audio_data.shape:
                    if len(audio_data.shape) > 1 and audio_data.shape[1] == num_channels:
                        # Scale the audio data to fit in the range [-1, 1]
                        audio_data /= np.max(np.abs(audio_data))
                        # Randomly select the start position for this audio clip
                        start_position = random.randint(0, max_duration - audio_data.shape[0])
                        # Pad the audio data with zeros to match the duration of the longest audio file and place it randomly
                        combined_audio[start_position:start_position+audio_data.shape[0], :] += audio_data
                    else:
                        continue  # Skip processing files that are not stereo
                else:
                    error_log.append(f"Failed to read audio file '{file}'. It may be empty or corrupted.")
            except sf.SoundFileError as e:
                error_log.append(f"Error reading audio file '{file}': {e}")
        
        # Scale the combined audio data to fit in the range [-1, 1]
        combined_audio /= np.max(np.abs(combined_audio))
        
        # Write combined audio data to a .wav file with timestamp
        output_wav_file = f"audioSoup_{timestamp}.wav"
        output_wav_path = os.path.join(audio_soup_folder, output_wav_file)
        sf.write(output_wav_path, combined_audio, sample_rate)
        
        # Write used files to a .txt file with timestamp
        output_txt_file = f"used_files_{timestamp}.txt"
        output_txt_path = os.path.join(audio_soup_folder, output_txt_file)
        with open(output_txt_path, "w", encoding="utf-8") as f:  # Specify encoding as UTF-8
            f.write("Used audio files:\n")
            for file in selected_files:
                f.write(file + "\n")
        
        print(f"Your random audio soup '{output_wav_file}' cooked successfully. Used files are listed in '{output_txt_file}'.")
