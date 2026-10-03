from pathlib import Path
import pandas as pd

folder = Path(__file__).resolve().parent
df = pd.read_csv(folder / "dataset_tugas1_preprocessing.csv")

print("=== Missing Values Sebelum Imputasi ===")
print(df.isna().sum())

# Menentukan nilai pengisi
modus_nilai = df["Nilai_Akhir"].mode().iloc[0]
median_umur = df["Umur"].median()

print("\nNilai pengisi Nilai_Akhir (modus):", modus_nilai)
print("Nilai pengisi Umur (median):", median_umur)

# Mengisi nilai kosong
df["Nilai_Akhir"] = df["Nilai_Akhir"].fillna(modus_nilai)
df["Umur"] = df["Umur"].fillna(median_umur)

print("\n=== Missing Values Setelah Imputasi ===")
print(df.isna().sum())

print("\n=== Lima Baris Pertama Setelah Imputasi ===")
print(df.head().to_string(index=False))

# Menyimpan hasil untuk digunakan pada Tahap 4
file_hasil = folder / "tugas1_hasil_tahap3.pkl"
df.to_pickle(file_hasil)

print("\nHasil disimpan:", file_hasil.name)