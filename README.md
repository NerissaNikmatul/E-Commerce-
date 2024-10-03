# Dicoding Collection Dashboard ✨
## E-Commerce Public Data Analysis with Python

![E-Commerce Data Dashboard](https://github.com/NerissaNikmatul/E-Commerce-/blob/main/Picture/Screenshot%202024-10-02%20204213.png)

[E-Commerce Data Dashboard Streamlit App](https://nerissanikma.streamlit.app/)

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data publik dari e-commerce menggunakan Python. Dashboard yang dibuat menampilkan visualisasi data untuk menjawab pertanyaan bisnis penting, seperti tren penjualan harian dan total pengeluaran pelanggan. Dengan menggunakan Streamlit, pengguna dapat berinteraksi dengan data secara dinamis.

## Table of Contents
- [Project Structure](#project-structure)
- [Run Streamlit App](#run-streamlit-app)
- [Setup Environment](#setup-environment)

## Project Structure
- `dashboard`: Direktori ini berisi `dashboard.py` yang digunakan untuk membuat dashboard dari hasil analisis data.
- `data`: Direktori yang berisi file CSV data mentah.
- `notebook.ipynb`: File ini digunakan untuk melakukan analisis data.
- `README.md`: File dokumentasi ini.

## Setup Environment
Untuk menyiapkan lingkungan pengembangan, ikuti langkah-langkah berikut:

```bash
mkdir E-Commerce
cd E-Commerce
pipenv install
pipenv shell
pipenv install pandas matplotlib seaborn streamlit

