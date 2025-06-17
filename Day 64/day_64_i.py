# Using Python for Merging PDFs

from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()

# Example usage 
merge_pdfs(["p1.pdf","p2.pdf"], "merged.pdf")
print("PDFs merged successfully!")