from pathlib import Path
import pandas as pd

folder = Path(__file__).resolve().parent

# Membaca hasil Tahap 3
df = pd.read_pickle(folder / "tugas1_hasil_tahap3.pkl")
tanggal_awal = df["Tanggal_Ujian"].copy()

# Konversi dua format tanggal secara eksplisit
tanggal_slash = pd.to_datetime(
    tanggal_awal, format="%Y/%m/%d", errors="coerce"
)

tanggal_strip = pd.to_datetime(
    tanggal_awal, format="%d-%m-%Y", errors="coerce"
)

df["Tanggal_Ujian"] = tanggal_slash.fillna(tanggal_strip)

# Memastikan seluruh tanggal berhasil dikonversi
gagal = df["Tanggal_Ujian"].isna()

if gagal.any():
    print("Tanggal yang gagal dikonversi:")
    print(tanggal_awal[gagal].to_string())
    raise ValueError("Ada tanggal yang perlu diperiksa.")

# Menampilkan perbandingan sebelum dan sesudah
perbandingan = pd.DataFrame({
    "Sebelum": tanggal_awal,
    "Sesudah": df["Tanggal_Ujian"]
})

print("=== Perbandingan Format Tanggal ===")
print(perbandingan.head(10).to_string(index=False))

print("\nTipe data:", df["Tanggal_Ujian"].dtype)
print("Jumlah tanggal gagal:", int(gagal.sum()))

# Menyimpan hasil untuk Tahap 5
file_hasil = folder / "tugas1_hasil_tahap4.pkl"
df.to_pickle(file_hasil)

print("\nHasil disimpan:", file_hasil.name)