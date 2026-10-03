from pathlib import Path
import pandas as pd

# Membaca dataset asli
folder = Path(__file__).resolve().parent
df = pd.read_csv(folder / "dataset_tugas1_preprocessing.csv")

# 1. Cek struktur dan tipe data
print("=== Struktur dan Tipe Data ===")
df.info()

# 2. Jumlah nilai hilang per kolom
print("\n=== Jumlah Nilai Hilang per Kolom ===")
print(df.isna().sum())

# 3. Statistik deskriptif numerik
print("\n=== Statistik Deskriptif Numerik ===")
print(df.describe(include="number").to_string())

# 4. Statistik deskriptif kategorikal
print("\n=== Statistik Deskriptif Kategorikal ===")
print(df.select_dtypes(include=["object", "str"]).describe().to_string())