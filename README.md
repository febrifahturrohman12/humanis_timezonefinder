Berikut adalah dokumen `README.md` yang siap untuk digunakan di GitHub. Anda dapat menyalin dan menempelkannya ke dalam file `README.md` di repositori Anda:

```markdown
# Proyek Python Humanis

## Tujuan Proyek
Proyek Python Humanis bertujuan untuk mencari timezone berdasarkan latitude dan longitude menggunakan data yang diberikan. Aplikasi ini menyediakan dua endpoint:
1. Endpoint `/` yang mengembalikan pesan bahwa API sedang berjalan.
2. Endpoint `/humanis_timezone` yang mengembalikan informasi timezone, waktu saat ini, dan offset GMT berdasarkan parameter latitude dan longitude.

## Requirements
Berikut adalah daftar library yang diperlukan untuk menjalankan proyek ini:
- `timezonefinder`
- `fastapi`
- `uvicorn`
- `datetime`
- `pytz` atau `zoneinfo` (tergantung pada versi Python)

## Cara Menjalankan Proyek

### 1. Instalasi Dependencies
Sebelum menjalankan proyek, pastikan Anda telah menginstal semua dependencies yang diperlukan. Anda dapat menginstalnya menggunakan `pip` dengan menjalankan perintah berikut di terminal:

```bash
pip install timezonefinder fastapi uvicorn pytz datetime
```

Atau jika Anda menggunakan Python 3.9 atau lebih tinggi, Anda dapat menggunakan `zoneinfo` yang sudah termasuk dalam standar library:

```bash
pip install timezonefinder fastapi uvicorn datetime
```

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

Dengan README ini, pengguna dapat dengan mudah memahami tujuan proyek, menginstal dependencies yang diperlukan, dan menjalankan aplikasinya. Jika ada tambahan atau modifikasi lain pada README ini, silakan beritahu saya! 😊

```

Silakan simpan dokumen ini sebagai `README.md` di repositori GitHub Anda. Jika Anda memerlukan bantuan lebih lanjut, jangan ragu untuk bertanya!
```