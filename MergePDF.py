import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfMerger

def gabung_pdf():
    # Buka dialog untuk pilih folder
    root = Tk()
    root.withdraw()  # sembunyikan jendela utama
    folder_path = filedialog.askdirectory(title="Pilih Folder yang berisi PDF")
    
    if not folder_path:
        print("Tidak ada folder yang dipilih.")
        return

    # Ambil semua file pdf di folder
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
    files.sort()  # urut berdasarkan nama file

    if not files:
        print("Tidak ada file PDF di folder yang dipilih.")
        return

    merger = PdfMerger()

    for pdf in files:
        filepath = os.path.join(folder_path, pdf)
        print(f"Menambahkan: {pdf}")
        merger.append(filepath)

    # Dialog untuk pilih lokasi & nama file output
    output_path = filedialog.asksaveasfilename(
        title="Simpan PDF Gabungan",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        initialfile="gabungan.pdf"
    )
    
    if not output_path:
        print("Proses dibatalkan, file tidak disimpan.")
        return

    merger.write(output_path)
    merger.close()
    
    print(f"PDF berhasil digabung! Hasil tersimpan di: {output_path}")


# Jalankan
gabung_pdf()
input("\nTekan Enter untuk keluar...")
