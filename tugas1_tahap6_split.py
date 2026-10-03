from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

folder = Path(__file__).resolve().parent

# Membaca hasil Tahap 5
df = pd.read_pickle(folder / "tugas1_hasil_tahap5.pkl")

# Membagi data secara acak: 80% latih, 20% uji
data_latih, data_uji = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

print("=== Hasil Pembagian Data ===")
print("Jumlah seluruh data:", len(df))
print("Jumlah data latih:", len(data_latih))
print("Jumlah data uji:", len(data_uji))

print("\n=== Lima Baris Pertama Data Latih ===")
print(data_latih.head().to_string(index=False))

print("\n=== Lima Baris Pertama Data Uji ===")
print(data_uji.head().to_string(index=False))

# Memastikan tidak ada ID yang masuk ke kedua kelompok
id_beririsan = set(data_latih["ID"]) & set(data_uji["ID"])
assert not id_beririsan, "Ada ID yang masuk ke data latih dan uji."
assert len(data_latih) + len(data_uji) == len(df)

# Menyimpan hasil dengan tipe data tetap terjaga
data_latih.to_pickle(folder / "tugas1_data_latih.pkl")
data_uji.to_pickle(folder / "tugas1_data_uji.pkl")

# Versi CSV agar mudah diperiksa
data_latih.to_csv(folder / "tugas1_data_latih.csv", index=False)
data_uji.to_csv(folder / "tugas1_data_uji.csv", index=False)

print("\nData latih dan data uji berhasil disimpan.")