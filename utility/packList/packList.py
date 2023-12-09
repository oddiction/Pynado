# Audio Metadata Analysis Script

import os
import wave
import xlsxwriter
import math
from tqdm import tqdm  # Import tqdm for the progress bar

def convert_sample_length(sample_length):
    seconds = sample_length / 1000
    minutes = math.floor(seconds / 60)
    seconds = math.floor(seconds % 60)
    return minutes, seconds

def get_audio_metadata(file_path):
    try:
        with wave.open(file_path, 'rb') as wave_file:
            n_channels, sampwidth, framerate, n_frames, _, _ = wave_file.getparams()
            bit_depth = sampwidth * 8
            sample_length = n_frames / framerate * 1000
            minutes, seconds = convert_sample_length(sample_length)
            return os.path.basename(file_path), bit_depth, n_channels, framerate, minutes, seconds
    except:
        return os.path.basename(file_path), None, None, None, None, None

# Function to update progress bar
def update_progress_bar():
    progress_bar.update(1)

folder_path = input("Please paste the folder path and press enter: ")

if not os.path.exists(folder_path):
    print("The given folder path does not exist. Please try again.")
else:
    # Create an .xlsx file in the given folder
    output_file_path = os.path.join(folder_path, os.path.basename(folder_path) + '.xlsx')
    workbook = xlsxwriter.Workbook(output_file_path)
    worksheet = workbook.add_worksheet()

    # Define the worksheet format
    bold = workbook.add_format({'bold': True})
    center = workbook.add_format({'align': 'center'})

    # Write the folder name to the first row
    worksheet.write('A1', 'File Name:', bold)
    worksheet.write('B1', os.path.basename(folder_path))

    # Define the worksheet column width
    worksheet.set_column('A:A', 20)  # Column for "File Name"
    worksheet.set_column('B:B', 50)  # Increase column width for file names
    worksheet.set_column('C:C', 10)
    worksheet.set_column('D:D', 10)
    worksheet.set_column('E:E', 15)  # Add column for Sample Rate
    worksheet.set_column('F:F', 10)  # Add column for Bit Depth
    worksheet.set_column('G:G', 10)  # Add column for Channels
    worksheet.set_column('H:H', 10)  # Add column for Minutes
    worksheet.set_column('I:I', 10)  # Add column for Seconds

    # Define the page size
    worksheet.set_paper(9)  # Use 'set_paper()' instead of 'set_page_size()'

    # Set up the progress bar
    total_files = sum(len(files) for _, _, files in os.walk(folder_path))
    progress_bar = tqdm(total=total_files, desc="Processing", position=0)

    # Write headers to the Excel file
    headers = ['File Name', 'Bit Depth', 'Channels', 'Sample Rate', 'Minutes', 'Seconds']
    for col_num, header in enumerate(headers, start=2):
        worksheet.write(1, col_num, header, bold)

    # Initialize variables for folder handling
    current_row = 2
    current_folder = ""

    # Iterate through all files (including subdirectories)
    for root, _, files in os.walk(folder_path):
        folder_name = os.path.basename(root)
        if folder_name != current_folder:
            # Add an empty row when a new folder starts
            current_row += 1
            current_folder = folder_name

        # Sort files alphabetically
        sorted_files = sorted(files)

        for audio_file in sorted_files:
            file_path = os.path.join(root, audio_file)
            metadata = get_audio_metadata(file_path)

            if metadata[1] is not None:  # Check if metadata is available
                worksheet.write(current_row, 1, "")
                for col_num, data in enumerate(metadata, start=2):
                    worksheet.write(current_row, col_num, data)
                current_row += 1

            # Update the progress bar
            update_progress_bar()

    # Write total file count and total size at the end
    worksheet.write(current_row, 1, f'Total Files: {current_row - 2}', bold)
    worksheet.write(current_row + 1, 1, f'Total Size: {sum(os.path.getsize(os.path.join(root, file)) for root, _, files in os.walk(folder_path) for file in files) / (1024 ** 2):.2f} MB', bold)

    # Close the progress bar

    # Save the Excel file
    workbook.close()

    print(f"Excel file created successfully at: {output_file_path}")
