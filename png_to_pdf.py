from PIL import Image
from fpdf import FPDF
import os
from PyPDF2 import PdfMerger

def convert_png_to_pdf(png_file, pdf_file):
    image = Image.open(png_file)
    # Save the image as a PDF with a high resolution
    image.save(pdf_file, "PDF", resolution=300.0)

# Path to the folder containing the PNG files
folder_path = 'pngs10'
output_pdf_path = '10.pdf'

# Temporary file to store individual PDF pages
temp_pdf_files = []

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        # Open the PNG file
        image_path = os.path.join(folder_path, filename)
        
        # Temporary PDF file for the current image
        temp_pdf_file = os.path.join(folder_path, f"{filename}.pdf")
        temp_pdf_files.append(temp_pdf_file)
        
        # Convert the image to a high-resolution PDF
        convert_png_to_pdf(image_path, temp_pdf_file)

# Merge all temporary PDF files into a single PDF
merger = PdfMerger()
for temp_pdf_file in temp_pdf_files:
    merger.append(temp_pdf_file)

# Save the final PDF document
merger.write(output_pdf_path)
merger.close()

# Clean up temporary PDF files
for temp_pdf_file in temp_pdf_files:
    os.remove(temp_pdf_file)