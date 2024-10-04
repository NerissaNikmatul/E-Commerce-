# Dicoding Collection Dashboard ✨
## E-Commerce Public Data Analysis with Python

![E-Commerce Data Dashboard](https://github.com/NerissaNikmatul/E-Commerce-/blob/main/Picture/Screenshot%202024-10-02%20204213.png)

[E-Commerce Data Dashboard Streamlit App](https://nerissanikma.streamlit.app/)

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data publik dari e-commerce menggunakan Python. Dashboard yang dibuat menampilkan visualisasi data untuk menjawab pertanyaan bisnis penting, seperti tren penjualan harian dan total pengeluaran pelanggan. Dengan menggunakan Streamlit, pengguna dapat berinteraksi dengan data secara dinamis.

## Fitur
- Pesanan Harian Terkirim: Grafik garis yang memvisualisasikan jumlah pesanan yang dikirim setiap hari.
- Pengeluaran Pelanggan: Grafik garis yang menampilkan total dan rata-rata pengeluaran pelanggan seiring waktu.
- Skor Ulasan: Grafik batang yang menunjukkan ulasan pelanggan.
- Penjualan Produk: Perbandingan kategori produk yang paling banyak terjual dan paling sedikit terjual.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup Environment](#setup-environment)
- [Run streamlit app](#run-streamlit-app)

## Project Structure
- Dasboard1.py: File utama yang berisi kode untuk dashboard Streamlit.
- df.csv: Dataset yang berisi data pesanan.
- geolocation.csv: (Opsional) Dataset untuk data geolokasi.
- func.py: File helper yang berisi class DataAnalyzer yang digunakan untuk pemrosesan data.
- README.md: File ini, yang menyediakan petunjuk untuk setup dan penggunaan.

## Setup Environment
Untuk menyiapkan lingkungan pengembangan, ikuti langkah-langkah berikut:

```bash
mkdir E-Commerce
cd E-Commerce
pipenv install
pipenv shell
pipenv install pandas matplotlib seaborn streamlit
```

## Run streamlit app
```
streamlit run Dasboard1.py
```
