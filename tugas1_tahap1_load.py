from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Tahap 1: Membaca dataset dari folder tempat script disimpan
folder = Path(__file__).resolve().parent
df = pd.read_csv(folder / "dataset_tugas1_preprocessing.csv")

print("Lima baris pertama:")
print(df.head().to_string(index=False))

print("\nJumlah baris dan kolom:", df.shape)