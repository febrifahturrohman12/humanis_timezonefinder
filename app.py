from fastapi import FastAPI
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime

app = FastAPI()

# Membuat objek TimezoneFinder
tf = TimezoneFinder()

@app.get("/")
async def root():
    return {"message": "Humanis Timezone API is running!"}

@app.get("/humanis_timezone")
async def get_current_time(lat: float, lon: float):
    """
    Mengambil waktu saat ini berdasarkan latitude dan longitude.
    
    :param lat: Latitude dari lokasi.
    :param lon: Longitude dari lokasi.
    :return: Zona waktu dan waktu saat ini sebagai string.
    """
    
    # Mendapatkan nama zona waktu berdasarkan koordinat
    timezone_name = tf.timezone_at(lat=lat, lng=lon)

    if not timezone_name:
        return {"error": "Timezone not found for the given coordinates."}

    # Menggunakan pytz untuk mendapatkan informasi zona waktu dan menghitung offset GMT saat ini
    tz = pytz.timezone(timezone_name)
    
    # Mendapatkan waktu saat ini dalam zona waktu tersebut 
    current_time = datetime.now(tz)

    # Mendapatkan offset GMT dalam jam 
    gmt_offset_hours = current_time.utcoffset().total_seconds() / 3600

    return {
        "timezone": timezone_name,
        "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        "gmt_offset": gmt_offset_hours,
    }
