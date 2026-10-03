from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

folder = Path(__file__).resolve().parent

# Data setelah imputasi, sebelum kategori diubah menjadi angka
df = pd.read_pickle(folder / "tugas1_hasil_tahap4.pkl")

# 1. Histogram Umur
fig, ax = plt.subplots(figsize=(8, 5))

# Setiap interval mewakili satu tahun
bins = range(
    int(df["Umur"].min()) - 1,
    int(df["Umur"].max()) + 2
)
batas_bins = [nilai + 0.5 for nilai in bins]

ax.hist(
    df["Umur"],
    bins=batas_bins,
    color="skyblue",
    edgecolor="black"
)

ax.set_title("Distribusi Umur Mahasiswa")
ax.set_xlabel("Umur (tahun)")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks(range(
    int(df["Umur"].min()),
    int(df["Umur"].max()) + 1
))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

fig.tight_layout()
fig.savefig(folder / "tugas1_histogram_umur.png", dpi=300)

# 2. Grafik batang jumlah mahasiswa per Prodi
jumlah_prodi = df["Prodi"].value_counts().sort_index()

print("=== Jumlah Mahasiswa per Prodi ===")
print(jumlah_prodi)

fig, ax = plt.subplots(figsize=(9, 5))
batang = ax.bar(
    jumlah_prodi.index,
    jumlah_prodi.values,
    color="steelblue",
    edgecolor="black"
)

ax.set_title("Jumlah Mahasiswa per Program Studi")
ax.set_xlabel("Program Studi")
ax.set_ylabel("Jumlah Mahasiswa")
ax.bar_label(batang, padding=3)
ax.tick_params(axis="x", labelrotation=15)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_ylim(0, jumlah_prodi.max() + 5)

fig.tight_layout()
fig.savefig(folder / "tugas1_jumlah_mahasiswa_prodi.png", dpi=300)

print("\nKedua grafik berhasil disimpan sebagai PNG.")

# Menampilkan kedua grafik
plt.show()