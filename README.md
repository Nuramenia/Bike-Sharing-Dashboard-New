# 🚲 Dashboard Analisis Penyewaan Sepeda

Proyek ini merupakan dashboard interaktif untuk menganalisis tren penyewaan sepeda berdasarkan faktor cuaca, waktu (jam sibuk), dan pola penggunaan harian. Dashboard ini dibuat menggunakan Streamlit dan didasarkan pada dataset Bike Sharing Dataset.

## Pertanyaan Bisnis
1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda pada tahun 2012, dan seberapa besar perbedaannya antara cuaca cerah dan cuaca hujan (Light Rain/Snow)?
2. Pada jam berapa terjadi puncak penyewaan sepeda tertinggi dalam satu hari kerja (*workingday*) selama musim panas (*Summer*)?
   
## 📌 Fitur Utama
- **Ringkasan Metrik:** Menampilkan total penyewaan, rata-rata suhu, dan jumlah pengguna terdaftar secara real-time berdasarkan filter.
- **Analisis Cuaca:** Visualisasi pengaruh kondisi cuaca (Cerah, Berawan, Hujan Ringan) terhadap jumlah penyewa.
- **Pola Jam Sibuk:** Grafik tren penyewaan per jam pada hari kerja untuk mengidentifikasi waktu puncak (komuter).
- **Matriks Korelasi:** Analisis hubungan antara variabel lingkungan (suhu, kelembapan, kecepatan angin) dengan jumlah penyewaan.
# 🚲 Proyek Analisis Data: Bike Sharing Dataset


## 📂 Struktur Proyek
```text
Submission1/
├── dashboard.py       # File utama dashboard Streamlit
├── day.csv            # Dataset harian asli
├── hour.csv           # Dataset per jam asli
├── main_data.csv      # Dataset yang sudah dibersihkan dan digabungkan
├── Notebook.ipynb     # Notebook analisis data (EDA & Cleaning)
├── README.md          # Dokumentasi proyek
└── requirements.txt   # Daftar library Python yang dibutuhkan
```
### Alur Analisis
## Data Wrangling:
- Gathering Data: Memuat dataset hour.csv dan day.csv.
- Assessing Data: Memeriksa kelengkapan data (missing values) dan tipe data yang tidak sesuai.
- Cleaning Data: Mengonversi kolom dteday menjadi tipe data datetime, serta melakukan denormalisasi nilai suhu dan kelembapan.
## Exploratory Data Analysis (EDA):
- Memfilter data khusus tahun 2012 untuk membandingkan rata-rata penyewaan antara kondisi cuaca "Clear" dan "Light Rain/Snow".
- Melakukan filter data pada musim panas (Summer) dan hari kerja (Workingday) untuk melihat distribusi penyewaan per jam (hr).
- Visualization & Explanatory Analysis:
Bar Chart: Menampilkan perbandingan drastis antara cuaca cerah dan hujan.
Line Chart: Menunjukkan titik puncak (peak) penggunaan sepeda pada jam kerja di musim panas.

### 📊 Kesimpulan
- Analisis Cuaca: Terdapat penurunan signifikan (sering kali lebih dari 50%) pada jumlah penyewaan saat kondisi hujan/salju dibandingkan saat cuaca cerah.
- Puncak Jam Kerja: Di musim panas, penyewaan mencapai puncaknya pada jam 08:00 pagi dan 17:00 sore, yang menunjukkan pola penggunaan oleh kaum komuter.
