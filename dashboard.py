import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Bike Sharing Dashboard 🚲", layout="wide")

# 1. Load Data
@st.cache_data
def load_data():
    # Pastikan file ini ada di folder yang sama
    df = pd.read_csv("hour.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    
    # Mapping untuk keterbacaan
    df['yr'] = df['yr'].map({0: '2011', 1: '2012'})
    df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    df['weather_label'] = df['weathersit'].map({
        1: 'Clear', 2: 'Misty/Cloudy', 
        3: 'Light Rain/Snow', 4: 'Heavy Rain'
    })
    return df

df = load_data()

# --- SIDEBAR ---
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun", options=['2011', '2012'], index=1)
selected_season = st.sidebar.multiselect("Pilih Musim", options=df['season'].unique(), default=df['season'].unique())

# Filter DataFrame
main_df = df[(df['yr'] == selected_year) & (df['season'].isin(selected_season))]

# --- HEADER ---
st.title("🚲 Dashboard Analisis Penyewaan Sepeda")
st.markdown(f"Menampilkan data untuk tahun **{selected_year}**")

# --- METRICS ---
col1, col2, col3 = st.columns(3)
with col1:
    total_rentals = main_df['cnt'].sum()
    st.metric("Total Penyewaan", value=f"{total_rentals:,}")
with col2:
    avg_temp = round(main_df['temp'].mean() * 41, 1) # Denormalisasi temp
    st.metric("Rata-rata Suhu", value=f"{avg_temp}°C")
with col3:
    registered_ratio = round((main_df['registered'].sum() / total_rentals) * 100, 1)
    st.metric("Pengguna Terdaftar", value=f"{registered_ratio}%")

st.divider()

# --- VISUALISASI 1: CUACA ---
st.subheader("1. Pengaruh Cuaca terhadap Jumlah Penyewaan")
weather_res = main_df.groupby('weather_label')['cnt'].mean().reset_index().sort_values('cnt', ascending=False)

fig_weather = px.bar(
    weather_res, 
    x='weather_label', 
    y='cnt', 
    color='weather_label',
    labels={'cnt': 'Rata-rata Penyewaan', 'weather_label': 'Kondisi Cuaca'},
    template="plotly_white"
)
st.plotly_chart(fig_weather, use_container_width=True)

# --- VISUALISASI 2: JAM SIBUK ---
st.subheader("2. Pola Penyewaan Berdasarkan Jam (Hari Kerja)")
workingday_df = main_df[main_df['workingday'] == 1]
hourly_res = workingday_df.groupby('hr')['cnt'].mean().reset_index()

fig_hour = px.line(
    hourly_res, 
    x='hr', 
    y='cnt', 
    markers=True,
    labels={'hr': 'Jam (0-23)', 'cnt': 'Rata-rata Penyewaan'},
    title="Tren Jam Sibuk di Hari Kerja"
)
fig_hour.add_vrect(x0=7, x1=9, fillcolor="green", opacity=0.2, annotation_text="Pagi")
fig_hour.add_vrect(x0=16, x1=19, fillcolor="orange", opacity=0.2, annotation_text="Sore")

st.plotly_chart(fig_hour, use_container_width=True)

# --- ANALISIS LANJUTAN: KORELASI ---
with st.expander("Lihat Analisis Korelasi (Heatmap)"):
    st.write("Hubungan antara variabel numerik (Temp, Hum, Windspeed vs Rental)")
    corr = main_df[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
    fig_corr, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig_corr)

st.caption("Copyright © 2026 | Proyek Analisis Data Bike Sharing")