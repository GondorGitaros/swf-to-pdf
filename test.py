import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

swf_folder = "swfs12"
png_folder = "pngs12"

# Ensure the output folder exists
os.makedirs(png_folder, exist_ok=True)

def convert_swf_to_png(swf_file):
    swf_path = os.path.join(swf_folder, swf_file)
    png_file = os.path.splitext(swf_file)[0] + ".png"
    png_path = os.path.join(png_folder, png_file)

    # Convert SWF to PNG using swfrender with maximum quality
    command = f"swfrender {swf_path} -o {png_path} -r 300"
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Converting {swf_file} to {png_file}")
        print("swfrender output:", result.stdout)
        print("swfrender errors:", result.stderr)
        
        # Check if the output PNG file was created
        if not os.path.exists(png_path):
            print(f"Error: The output PNG file {png_file} was not created.")
        else:
            # Check the size of the output PNG file
            file_size = os.path.getsize(png_path)
            if file_size == 0:
                print(f"Error: The output PNG file {png_file} is empty.")
            else:
                print(f"Success: The file {png_file} was created with size {file_size} bytes.")
    except subprocess.CalledProcessError as e:
        print(f"Error: swfrender command failed for {swf_file} with error: {e.stderr}")

# Scan the swf_folder for SWF files
swf_files = [f for f in os.listdir(swf_folder) if f.endswith(".swf")]

# Use ThreadPoolExecutor to run conversions in parallel
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(convert_swf_to_png, swf_file) for swf_file in swf_files]
    for future in as_completed(futures):
        future.result()  # This will raise any exceptions caught during execution