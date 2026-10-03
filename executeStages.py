from pathlib import Path
import subprocess
import sys

folder = Path(__file__).resolve().parent

daftar_tahap = [
    "tugas1_tahap1_load.py",
    "tugas1_tahap2_eda.py",
    "tugas1_tahap3_missing.py",
    "tugas1_tahap4_tanggal.py",
    "tugas1_tahap5_encoding.py",
    "tugas1_tahap6_split.py",
    "tugas1_tahap7_visualisasi.py",
]


def main():
    for nama_file in daftar_tahap:
        if not (folder / nama_file).is_file():
            print(f"File tidak ditemukan: {nama_file}", flush=True)
            return 1

    for nomor, nama_file in enumerate(daftar_tahap, start=1):
        print(
            f"\n{'=' * 60}\n"
            f"Menjalankan Tahap {nomor}: {nama_file}\n"
            f"{'=' * 60}",
            flush=True
        )

        hasil = subprocess.run(
            [sys.executable, "-u", str(folder / nama_file)],
            cwd=folder
        )

        if hasil.returncode != 0:
            print(
                f"\nTahap {nomor} gagal. Periksa error di atas.",
                flush=True
            )
            return hasil.returncode

    print("\nSemua 7 tahap berhasil diselesaikan!", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

    
# ini digunakan untuk RUN atau Execute semua step atau tahapan
# caranya cukup tulis ini di Terminal : python ExecuteStages.py