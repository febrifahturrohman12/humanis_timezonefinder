## Project Python Humanis Timezone

Project Python Humanis bertujuan untuk mencari timezone berdasarkan latitude dan longitude menggunakan data yang diberikan. Aplikasi ini menyediakan dua endpoint:

**1. Endpoint** `/` yang mengembalikan pesan bahwa API sedang berjalan.

**2. Endpoint** `/humanis_timezone` yang mengembalikan informasi timezone, waktu saat ini, dan offset GMT berdasarkan parameter latitude dan longitude.

## Persyaratan (Requirements)

Berikut adalah daftar library yang diperlukan untuk menjalankan project ini:
- `timezonefinder`
- `fastapi`
- `uvicorn`
- `datetime`
- `pytz` atau `zoneinfo` (tergantung pada versi Python)

## Cara Menjalankan Project Lokal

### 1. Instalasi Dependencies

Untuk menjalankan dan menggunakan project ini, Anda memerlukan beberapa library Python.  Library-library ini dapat diinstal secara manual satu per satu, atau lebih efisien dengan menggunakan file `requirements.txt`.

**Metode 1: Instalasi Manual**

Anda dapat menginstal setiap library yang dibutuhkan secara individual menggunakan pip:

Sebelum menjalankan project, pastikan Anda telah menginstal semua dependencies yang diperlukan. Anda dapat menginstalnya menggunakan `pip` dengan menjalankan perintah berikut di terminal:

```bash
pip install timezonefinder fastapi uvicorn pytz datetime
```

Atau jika Anda menggunakan Python 3.9 atau lebih tinggi, Anda dapat menggunakan `zoneinfo` yang sudah termasuk dalam standar library:

```bash
pip install timezonefinder fastapi uvicorn datetime
```
**Metode 2: Instalasi Menggunakan `requirements.txt`**

Cara yang lebih direkomendasikan adalah dengan menggunakan file `requirements.txt`. File ini mencantumkan semua dependensi yang dibutuhkan oleh project. Anda dapat menginstal semua dependensi sekaligus dengan menjalankan perintah berikut:

```bash
pip install -r requirements.txt
```
File `requirements.txt` terletak di direktori root project dan berisi daftar library dan versi spesifiknya. Ini memastikan konsistensi lingkungan pengembangan dan menghindari konflik versi.

Anda dapat menginstal semua dependensi sekaligus dengan menjalankan perintah berikut:


### 2. Menjalankan Aplikasi

Setelah semua dependencies terinstal, Anda dapat menjalankan aplikasi menggunakan `uvicorn`. Jalankan perintah berikut di terminal:

```bash
uvicorn app:app --reload
```

Perintah di atas akan menjalankan server FastAPI dengan fitur auto-reload yang memungkinkan aplikasi secara otomatis merefresh ketika ada perubahan kode.

### 3. Mengakses Aplikasi

Setelah server berjalan, Anda dapat mengakses aplikasi melalui browser web dengan membuka alamat berikut:

```
http://127.0.0.1:8000
```

Anda juga dapat mengakses dokumentasi API yang disediakan oleh FastAPI dengan membuka alamat berikut:

```
http://127.0.0.1:8000/docs
```

## Contoh Penggunaan

### Endpoint `/`

Ketika mengakses URL `/`, aplikasi akan mengembalikan pesan berikut:

#### Request

```
GET /
```

#### Response

```json
{
  "message": "Humanis Timezone API is running!"
}
```

### Endpoint `/humanis_timezone`

Ketika mengakses URL `/humanis_timezone` dengan parameter latitude dan longitude, aplikasi akan mengembalikan informasi timezone, waktu saat ini, dan offset GMT.

#### Request

```
GET /humanis_timezone?lat=-8.5115987&lon=140.4165321
```

#### Response

```json
{
  "timezone": "Asia/Jayapura",
  "current_time": "2025-04-15 12:10:12",
  "gmt_offset": 9
}
```
---
## Cara Menjalankan Project Menggunakan Heroku / Railway.app
Project ini sudah disiapkan agar dapat dijalankan di platform cloud seperti Heroku atau Railway menggunakan file Procfile. Berikut panduan singkatnya:

**1. Pastikan File Procfile Ada**
File Procfile harus berada di root direktori project dan berisi perintah berikut:
```bash
web: uvicorn app:app --host=0.0.0.0 --port=${PORT:-8000}
```
* ```web``` : menandakan proses utama web server.
* Perintah menjalankan aplikasi FastAPI menggunakan Uvicorn.
* ```${PORT:-8000}``` memungkinkan platform menentukan port secara dinamis.

**2.Buat File requirements.txt**

Pastikan semua dependencies tercantum dalam file `requirements.txt`, misalnya:
```bash
fastapi
uvicorn
timezonefinder
pytz
datetime
```
Platform akan menginstal dependencies ini secara otomatis saat deploy.

**3.Deploy ke Heroku / Railway**

Contoh Deploy ke Heroku:
```bash
heroku create nama-aplikasi-anda
git push heroku main
heroku ps:scale web=1
heroku open
```
Contoh Deploy ke Railway:

* Login dan buat project baru di `Railway`.
* Hubungkan repository GitHub Anda.
* Platform akan otomatis mendeteksi Procfile dan menjalankan perintah yang ada.

**4. Akses Aplikasi**

Setelah deploy berhasil, aplikasi dapat diakses melalui URL yang diberikan oleh platform hosting.

---
## Cara Menjalankan Project Menggunakan Docker
Proyek ini juga dapat dijalankan menggunakan Docker untuk kemudahan deployment dan isolasi lingkungan.

**1. Buat File Dockerfile**

Pastikan Anda memiliki file Dockerfile di root proyek dengan isi seperti berikut:
```bash
# Gunakan image Python resmi sebagai base image
FROM python:3.10-slim

# Set working directory di dalam container
WORKDIR /app

# Salin file requirements.txt ke working directory
COPY requirements.txt .

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode sumber ke working directory
COPY . .

# Expose port yang digunakan aplikasi (8000)
EXPOSE 8000

# Jalankan aplikasi menggunakan uvicorn saat container dijalankan
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**2. Build Image Docker**

Jalankan perintah berikut di terminal pada direktori proyek untuk membangun image Docker:
```
docker build -t humanis-timezone-api .
```

**3. Jalankan Container dari Image yang Dibuat**

Setelah proses build selesai, jalankan container dengan perintah:
```
docker run -d -p 8000:8000 --name humanis-api-container humanis-timezone-api
```
* Opsi -d menjalankan container secara background (detached).
* Opsi -p 8000:8000 memetakan port host ke port container.
* Nama container bisa disesuaikan (humanis-api-container).

**4. Akses Aplikasi**

Buka browser dan akses URL berikut untuk melihat API berjalan:
```
http://localhost:8000/
```

Anda juga dapat mengakses dokumentasi API FastAPI di:
```
http://localhost:8000/docs
```

---

#### Sekian dan Terima Kasih😊