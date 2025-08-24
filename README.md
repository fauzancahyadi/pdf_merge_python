# 📚 PDF Merger Python

Skrip Python sederhana untuk **menggabungkan beberapa file PDF** dalam satu folder menjadi satu file PDF.  
Mendukung pemilihan folder dan lokasi file output menggunakan GUI (Tkinter).

---

## ✨ Fitur
- Pilih folder berisi file PDF dengan dialog
- Mengurutkan file berdasarkan nama (alfabetis)
- Pilih nama & lokasi file hasil gabungan
- Output dalam format PDF tunggal

---

## 🚀 Instalasi
1. Clone repo ini:
   ```bash
   git clone https://github.com/username/pdf-merger-python.git
   cd pdf-merger-python


2. Install dependencies:
    pip install PyPDF2

Catatan: Tkinter biasanya sudah ter-install otomatis di Python (Windows/Linux).
Jika error, cek dokumentasi Python sesuai OS kamu.

🛠️ Cara Pakai

Jalankan script:
python gabung_pdf.py

* Akan muncul dialog untuk memilih folder berisi PDF.
* Setelah itu, pilih lokasi & nama file hasil gabungan.
* Hasil akan berupa file gabungan.pdf (atau nama yang kamu pilih).

📂 Contoh Struktur Folder
📁 PDF_Folder
 ├── dokumen1.pdf
 ├── dokumen2.pdf
 ├── dokumen3.pdf

 Output:

gabungan.pdf
