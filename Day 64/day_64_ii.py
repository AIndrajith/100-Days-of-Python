# Adding File Order options

from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()

def get_pdf_order():
    pdf_list = input("Enter PDF file names in the desired order(comma-separated): ").split(",")
    return [pdf.strip() for pdf in pdf_list]

def validate_files(pdf_list):
    for pdf in pdf_list:
        if not os.path.exists(pdf):
            print(f"Error: {pdf} does not exist.")
            return False
    return True

# Example usage 
pdf_order = get_pdf_order()
merge_pdfs(pdf_order, "merged_output.pdf")