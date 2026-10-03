from pathlib import Path
import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder

folder = Path(__file__).resolve().parent

# Membaca hasil Tahap 4
df = pd.read_pickle(folder / "tugas1_hasil_tahap4.pkl")

kolom_kategori = [
    "Nama",
    "Jenis_Kelamin",
    "Prodi",
    "Status",
    "Nilai_Akhir"
]

mapping_semua = {}

# Encoding masing-masing kolom secara terpisah
for kolom in kolom_kategori:
    encoder = LabelEncoder()
    df[kolom] = encoder.fit_transform(df[kolom])

    mapping = {
        str(kategori): int(kode)
        for kode, kategori in enumerate(encoder.classes_)
    }
    mapping_semua[kolom] = mapping

    print(f"\n=== Mapping {kolom} ===")
    for kategori, kode in mapping.items():
        print(f"{kategori} -> {kode}")

print("\n=== Lima Baris Pertama Setelah Encoding ===")
print(df.head().to_string(index=False))

print("\n=== Tipe Data Setelah Encoding ===")
print(df.dtypes)

# Menyimpan dataset untuk Tahap 6
df.to_pickle(folder / "tugas1_hasil_tahap5.pkl")

# Menyimpan mapping agar arti kode angka tetap diketahui
with open(
    folder / "tugas1_mapping_encoding.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(mapping_semua, file, ensure_ascii=False, indent=4)

print("\nHasil disimpan: tugas1_hasil_tahap5.pkl")
print("Mapping disimpan: tugas1_mapping_encoding.json")