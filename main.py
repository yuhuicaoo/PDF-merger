from PyPDF2 import PdfMerger
import os
import tkinter as tk
from tkinter import filedialog, messagebox

os.environ["TK_SILENCE_DEPRECATION"] = "1"


def merge_pdfs(folder_path):
    merger = PdfMerger()

    # Assuming all the pdfs u want to merge are in the folder_path and are ordered already
    pdf_files = [
        f for f in os.listdir(folder_path) if f.endswith(".pdf") and f != "merged.pdf"
    ]
    pdf_files.sort()

    for filename in pdf_files:
        merger.append(os.path.join(folder_path, filename))

    output_filename = os.path.join(folder_path, "merged.pdf")
    merger.write(output_filename)
    merger.close()

    messagebox.showinfo(
        "Merge Complete", f"PDFs merged successfully into {output_filename}"
    )


def main():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    if folder_path:
        merge_pdfs(folder_path)


if __name__ == "__main__":
    main()
