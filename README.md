# E-Commerce Public Data Analysis with Python - Dicoding

import streamlit as st

def tampilkan_gambar(url_gambar, caption=""):
    st.image(url_gambar, caption=caption)

# Contoh penggunaan
url = "https://github.com/NerissaNikmatul/E-Commerce-/tree/main/Picture" 
tampilkan_gambar(url, caption="Gambar E-Commerce Data Dashboard")

![E-Commerce Data Dashboard]

[E-Commerce Data Dashboard Streamlit App](https://nerissanikma.streamlit.app/)

## Project Structure
- `dashboard`: This directory contains dashboard.py which is used to create dashboards of data analysis results.
- `data`: Directory containing the raw CSV data files.
- `notebook.ipynb`: This file is used to perform data analysis.
- `README.md`: This documentation file.
