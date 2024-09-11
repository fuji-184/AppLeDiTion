from setup.postgresql import db
from flask import request
import traceback
import pandas as pd

class Histori_Deteksi():
    def __init__(self) -> None:
        pass
    
    # @jwt_required()
    def get_all(self):
        try:
            hasil = db.query(query="select hd.*, h.nama as hasil, k.nama as kebun, k.alamat as alamat_kebun from histori_deteksi as hd join hasil as h on hd.id_hasil = h.id join kebun as k on hd.id_kebun = k.id")
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get all data histori deteksi")
            traceback.print_exc()
            return "Error", 500
        
    def get_all_by_user_id(self, user_id):
        try:
            print(f"id: {user_id}")
            hasil = db.query(query="select hd.*, h.nama as hasil, k.nama as kebun, k.alamat as alamat_kebun from histori_deteksi as hd join hasil as h on hd.id_hasil = h.id join kebun as k on hd.id_kebun = k.id where hd.id_user = %s", params=(user_id,))
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get all data histori deteksi by user id")
            traceback.print_exc()
            return "Error", 500
        
    def get_all_by_id_user_dan_kebun(self, id_user, id_kebun):
        try:
            print(f"id: {id_kebun}")
            hasil = db.query(query="select hd.*, h.nama as hasil, k.nama as kebun, k.alamat as alamat_kebun from histori_deteksi as hd join hasil as h on hd.id_hasil = h.id join kebun as k on hd.id_kebun = k.id where hd.id_user = %s and hd.id_kebun = %s", params=(id_user, id_kebun,))
            
            print(hasil)
            
            df = pd.DataFrame(hasil)
            
            print(df.columns)

            
            df['tgl'] = pd.to_datetime(df['tanggal'], format='%d %m %y').dt.to_period('D')
            
            hasil = df.groupby(['tgl', 'id_kebun', 'hasil']).size().reset_index(name='jumlah')
            
            max_freq = hasil.groupby(['tgl', 'id_kebun', 'hasil'])['jumlah'].transform('max')
            
            hasil = hasil
            
            [hasil['jumlah'] == max_freq]
            
            hasil = hasil.groupby(['tgl', 'id_kebun', 'hasil'])['jumlah'].sum().reset_index()
            
            hasil['tgl'] = hasil['tgl'].astype(str)
            
            hasil = hasil.to_dict(orient='records')
            
            # print(hasil)
            
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get all data histori deteksi by user id")
            traceback.print_exc()
            return "Error", 500
    
    def get_one(self, id):
        try:
            hasil = db.query(query="select * from histori_deteksi where id = %s", params=(id,))
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get one data histori deteksi by id")
            traceback.print_exc()
            return "Error", 500
        
    def add(self):
        try:
            data = request.json
            print(data)
            hasil = db.query(query="insert into histori_deteksi(id_user, id_kebun, id_hasil, skor) values(%s, %s, %s, %s) returning *", params=(
                data.get("id_user"),
                data.get("id_kebun"),
                data.get("id_hasil"),
                data.get("skor"),
            ))
            return {
                "berhasil": True,
                "hasil": hasil
            }
        except Exception as e:
            print(f"Error di add histori deteksi")
            traceback.print_exc()
            return "Error internal server", 500
            
    def delete(self, id):
        try:
            db.query(query="delete from histori_deteksi where id = %s", params=(id,))
            return {
                "berhasil": True
            }
        except Exception as e:
            print(f"Error di delete histori deteksi")
            traceback.print_exc()
            return {
                "pesan": "Error internal server"    
            }, 500
            
    def get_by_bulan(self):
        try:
            hasil = db.query(query="select hd.id_kebun, to_char(hd.tanggal, 'dd mm yyyy') as tanggal, hs.nama from histori_deteksi as hd join hasil as hs on hd.id_hasil = hs.id")
            
            # Membaca data ke dalam DataFrame
            df = pd.DataFrame(hasil)

            # Mengonversi kolom tanggal
            df['bulan'] = pd.to_datetime(df['tanggal'], format='%d %m %Y').dt.to_period('M')

            # Menghitung frekuensi setiap kombinasi bulan, id_kebun, dan nama
            hasil = df.groupby(['bulan', 'id_kebun', 'nama']).size().reset_index(name='jumlah')

            # Menentukan frekuensi maksimum untuk setiap kombinasi bulan dan id_kebun
            max_freq = hasil.groupby(['bulan', 'id_kebun'])['jumlah'].transform('max')

            # Memilih baris yang memiliki frekuensi maksimum
            hasil = hasil[hasil['jumlah'] == max_freq]

            hasil = hasil.groupby(['bulan', 'nama'])['jumlah'].sum().reset_index()

            # Mengonversi 'bulan' ke string agar bisa di-serialize ke JSON
            hasil['bulan'] = hasil['bulan'].astype(str)

            # Mengonversi DataFrame ke list of dictionaries
            hasil = hasil.to_dict(orient='records')


            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get all data histori_ eteksi")
            traceback.print_exc()
            return "Error", 500
        
    def get_terbaru_by_user_id(self, user_id):
        try:
            print(f"id: {user_id}")
            hasil = db.query(query="select hd.*, h.nama as hasil, k.nama as kebun, k.alamat as alamat_kebun from histori_deteksi as hd join hasil as h on hd.id_hasil = h.id join kebun as k on hd.id_kebun = k.id where hd.id_user = %s", params=(user_id,))
            
            df = pd.DataFrame(hasil)
            df['tanggal'] = pd.to_datetime(df['tanggal'])

            # Mengubah format tanggal menjadi "Hari, tanggal bulan tahun"
            df['tanggal'] = df['tanggal'].dt.strftime('%d %b %Y')

            # Group by 'id_kebun' dan pilih baris dengan tanggal terbaru untuk setiap 'id_kebun'
            df_latest = df.sort_values('tanggal', ascending=False).groupby('id_kebun').first().reset_index()

            # Temukan `id_hasil` yang paling sering muncul di data terbaru
            most_frequent_id_hasil = df_latest['id_hasil'].mode()[0]

            # Filter data berdasarkan `id_hasil` yang paling sering muncul
            filtered_result = df_latest[df_latest['id_hasil'] == most_frequent_id_hasil]

            # Konversi hasil ke dictionary untuk output
            hasil = filtered_result.to_dict(orient="records")

            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get all data terbaru by user id")
            traceback.print_exc()
            return "Error", 500
        
    def get_perkembangan_kebun_by_user_id(self, user_id):
        try:
            print(f"id: {user_id}")
            hasil = db.query(query="select hd.*, h.nama as hasil, k.nama as kebun, k.alamat as alamat_kebun from histori_deteksi as hd join hasil as h on hd.id_hasil = h.id join kebun as k on hd.id_kebun = k.id where hd.id_user = %s", params=(user_id,))
            
            df = pd.DataFrame(hasil)

            # Konversi kolom 'tanggal' ke tipe datetime dan ambil tanggalnya
            df['tanggal'] = pd.to_datetime(df['tanggal']).dt.date

            # Fungsi untuk mendapatkan id_hasil yang paling sering muncul
            def get_most_frequent_id_hasil(group):
                most_frequent_id_hasil = group['id_hasil'].mode()[0]
                # Ambil nilai kebun, hasil, dan informasi lain untuk id_hasil yang paling sering muncul
                sample_row = group[group['id_hasil'] == most_frequent_id_hasil].iloc[0]
                return pd.Series({
                    # 'id_hasil': most_frequent_id_hasil,
                    'alamat_kebun': sample_row['alamat_kebun'],
                    'hasil': sample_row['hasil'],
                    # 'id': sample_row['id'],
                    # 'id_kebun': sample_row['id_kebun'],
                    # 'id_user': sample_row['id_user'],
                    'kebun': sample_row['kebun'],
                    # 'skor': sample_row['skor'],
                    'tanggal': sample_row['tanggal']
                })

            # Group by 'id_kebun' dan 'tanggal', lalu terapkan fungsi
            df_filtered = df.groupby(['id_kebun', 'tanggal']).apply(get_most_frequent_id_hasil).reset_index(drop=True)

            # Konversi DataFrame ke format dictionary
            hasil = df_filtered.to_dict(orient="records")
            
            return {
                "data": hasil
            }
        except Exception as e:
            print(f"Error di get all data terbaru by user id")
            traceback.print_exc()
            return "Error", 500
  
histori_deteksi = Histori_Deteksi()