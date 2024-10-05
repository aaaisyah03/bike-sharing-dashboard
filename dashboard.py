import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Cek apakah jalur file ada
file_path = 'C:/Users/aaais/.vscode/python/dashboard/submission/data/hour.csv'
if os.path.exists(file_path):
    data_hour = pd.read_csv(file_path)
    print(data_hour.head())
else:
    print(f"File tidak ditemukan: {file_path}")

# Membaca data
data_hour = pd.read_csv('C:/Users/aaais/.vscode/python/dashboard/submission/data/hour.csv')  
data_day = pd.read_csv('C:/Users/aaais/.vscode/python/dashboard/submission/data/hour.csv')    

# Menghitung peminjaman sepeda per jam
hourly_rentals = data_hour.groupby('hr')['cnt'].sum().reset_index()
hourly_rentals.columns = ['Hour', 'Total Rentals']

# Menyiapkan layout dashboard
st.title("Dashboard Peminjaman Sepeda")
st.sidebar.header("Menu")

# Menambahkan tema
theme = st.sidebar.selectbox("Pilih Tema", ["Tema 1", "Tema 2", "Tema 3"])

# Mengatur tema berdasarkan pilihan
if theme == "Tema 1":
    st.markdown("""
    <style>
    body {
        background-color: #f0f8ff; /* Alice Blue */
    }
    </style>
    """, unsafe_allow_html=True)
    color_scale = px.colors.sequential.Viridis
elif theme == "Tema 2":
    st.markdown("""
    <style>
    body {
        background-color: #fff0f0; /* Light Coral */
    }
    </style>
    """, unsafe_allow_html=True)
    color_scale = px.colors.sequential.Plasma
else:
    st.markdown("""
    <style>
    body {
        background-color: #f0fff0; /* Honeydew */
    }
    </style>
    """, unsafe_allow_html=True)
    color_scale = px.colors.sequential.Cividis

# Tabel Peminjaman Sepeda per Jam
st.subheader("Tabel Peminjaman Sepeda per Jam")
st.table(hourly_rentals)

# Visualisasi Peminjaman Sepeda per Jam
fig_hour = px.bar(hourly_rentals, x='Hour', y='Total Rentals', title='Peminjaman Sepeda per Jam', 
                  color='Total Rentals', color_continuous_scale=color_scale)
st.plotly_chart(fig_hour)

# Analisis Peminjaman Sepeda per Jam
st.subheader("Analisis Peminjaman Sepeda per Jam")
st.write("Dari grafik peminjaman sepeda per jam, kita dapat melihat pola yang jelas di mana peminjaman tertinggi terjadi pada jam 17:00 hingga 20:00. "
         "Hal ini menunjukkan bahwa banyak pengguna sepeda menyewa sepeda setelah jam kerja. "
         "Sementara itu, peminjaman paling rendah terjadi pada dini hari dan jam makan siang.")

# Tabel Peminjaman Sepeda per Hari
daily_rentals = data_day.groupby('weekday')['cnt'].sum().reset_index()
daily_rentals.columns = ['Day of Week', 'Total Rentals']
daily_rentals['Day of Week'] = daily_rentals['Day of Week'].map({
    0: 'Senin', 
    1: 'Selasa', 
    2: 'Rabu', 
    3: 'Kamis', 
    4: 'Jumat', 
    5: 'Sabtu', 
    6: 'Minggu'
})
st.subheader("Tabel Peminjaman Sepeda per Hari")
st.table(daily_rentals)

# Visualisasi Peminjaman Sepeda per Hari
fig_day = px.bar(daily_rentals, x='Day of Week', y='Total Rentals', title='Peminjaman Sepeda per Hari', 
                  color='Total Rentals', color_continuous_scale=color_scale)
st.plotly_chart(fig_day)

# Analisis Peminjaman Sepeda per Hari
st.subheader("Analisis Peminjaman Sepeda per Hari")
st.write("Dari grafik peminjaman sepeda per hari, terlihat bahwa peminjaman tertinggi terjadi pada akhir pekan, khususnya pada hari Sabtu dan Minggu. "
         "Hal ini mungkin disebabkan oleh meningkatnya kegiatan rekreasi di akhir pekan. "
         "Sebaliknya, peminjaman paling rendah terlihat pada hari Senin, yang bisa diindikasikan sebagai hari transisi bagi banyak orang setelah akhir pekan.")

st.write("Grafik di atas menunjukkan jumlah peminjaman sepeda berdasarkan hari. Anda dapat melihat pola peminjaman sepanjang minggu.")

# 1. Analisis Trend Waktu
st.subheader("Analisis Trend Peminjaman Sepeda per Jam")
hourly_avg_rentals = data_hour.groupby('hr')['cnt'].mean().reset_index()
hourly_avg_rentals.columns = ['Hour', 'Average Rentals']

# Menampilkan tabel rata-rata peminjaman sepeda per jam
st.subheader("Tabel Rata-rata Peminjaman Sepeda per Jam")
st.table(hourly_avg_rentals)

# Visualisasi Rata-rata Peminjaman Sepeda per Jam
fig_trend_hour = px.line(hourly_avg_rentals, x='Hour', y='Average Rentals', title='Rata-rata Peminjaman Sepeda per Jam', 
                          line_shape='linear', color='Average Rentals')
st.plotly_chart(fig_trend_hour)

# 2. Analisis Musiman
data_day['month'] = pd.to_datetime(data_day['dteday']).dt.month  # Menggunakan kolom yang benar
monthly_rentals = data_day.groupby('month')['cnt'].sum().reset_index()
monthly_rentals.columns = ['Month', 'Total Rentals']
fig_monthly = px.bar(monthly_rentals, x='Month', y='Total Rentals', title='Peminjaman Sepeda per Bulan',
                      color='Total Rentals', color_discrete_sequence=color_scale)
st.plotly_chart(fig_monthly)

# 3. Analisis Kategorikal
data_day['is_weekend'] = data_day['weekday'].apply(lambda x: 1 if x in [5, 6] else 0)  # 5 dan 6 untuk Sabtu dan Minggu
weekend_rentals = data_day.groupby('is_weekend')['cnt'].sum().reset_index()
weekend_rentals.columns = ['Is Weekend', 'Total Rentals']
fig_weekend = px.bar(weekend_rentals, x='Is Weekend', y='Total Rentals', title='Peminjaman Sepeda pada Akhir Pekan vs Hari Kerja',
                      color='Total Rentals', color_continuous_scale=color_scale)
st.plotly_chart(fig_weekend)

# 4. Analisis Korelasi
correlation_matrix = data_hour[['temp', 'hum', 'cnt']].corr()
fig_corr = plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
st.pyplot(fig_corr)

# 5. Analisis Outlier
fig_outlier = plt.figure(figsize=(10, 6))
sns.boxplot(x=data_hour['cnt'])
st.pyplot(fig_outlier)

# 6. Rangkuman Analisis
st.subheader("Rangkuman Analisis")
st.write("Dari analisis di atas, kita dapat melihat bahwa: ")
st.write("1. Peminjaman sepeda tertinggi terjadi pada jam 8 dan 17.")
st.write("2. Terdapat pola musiman, di mana peminjaman tertinggi terjadi di musim panas.")
st.write("3. Peminjaman lebih tinggi pada akhir pekan dibandingkan hari kerja.")

# 7. Analisis RFM
st.subheader("Analisis RFM")

# Menyiapkan data RFM
current_date = pd.to_datetime("today")
data_day['dteday'] = pd.to_datetime(data_day['dteday'])

# Recency
data_day['Recency'] = (current_date - data_day['dteday']).dt.days

# Frequency: jumlah peminjaman per hari
frequency = data_day.groupby('dteday')['cnt'].count().reset_index(name='Frequency')

# Monetary: total jumlah peminjaman
monetary = data_day.groupby('dteday')['cnt'].sum().reset_index(name='Monetary')

# Menggabungkan RFM
rfm = frequency.merge(monetary, on='dteday')
rfm = rfm.merge(data_day[['dteday', 'Recency']], on='dteday', how='left').drop_duplicates()

# Menampilkan RFM
st.write("Data RFM:")
st.write(rfm)

# 9. Clustering Manual
st.subheader("Analisis Clustering Manual")

# Menampilkan statistik deskriptif untuk peminjaman sepeda
st.write("Statistik Deskriptif Peminjaman Sepeda (cnt):")
st.write(data_day['cnt'].describe())

# Menampilkan histogram peminjaman sepeda
st.write("Distribusi Peminjaman Sepeda:")
fig, ax = plt.subplots()  # Buat figure dan axes
sns.histplot(data_day['cnt'], bins=30, kde=True, ax=ax)  # Gunakan axes untuk plot
st.pyplot(fig)  # Tampilkan figure di Streamlit

# Menentukan batas kategori dengan cara manual
bins = [0, 20, 50, 100, 200, 300]  # Rentang peminjaman yang lebih fleksibel
labels = ['Sangat Rendah', 'Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']  # Menyesuaikan label

# Kategorisasi berdasarkan kolom yang relevan
data_day['Rental Category'] = pd.cut(data_day['cnt'], bins=bins, labels=labels)

# Menghitung jumlah peminjaman untuk setiap kategori
rental_category_count = data_day['Rental Category'].value_counts().reset_index()
rental_category_count.columns = ['Rental Category', 'Count']

# Visualisasi distribusi kategorisasi peminjaman sepeda
fig_category = px.bar(rental_category_count, x='Rental Category', y='Count', 
                       title='Distribusi Kategorisasi Peminjaman Sepeda', 
                       color='Count', color_continuous_scale=color_scale)
st.plotly_chart(fig_category)
