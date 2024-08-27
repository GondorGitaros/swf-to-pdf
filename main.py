import os
import subprocess

swf_folder = "swfs9"
png_folder = "pngs9"

# Ensure the output folder exists
os.makedirs(png_folder, exist_ok=True)

# Scan the swf_folder for SWF files
for swf_file in os.listdir(swf_folder):
    if swf_file.endswith(".swf"):
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