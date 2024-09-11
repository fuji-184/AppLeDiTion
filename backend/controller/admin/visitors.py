import traceback
from setup.postgresql import db
from flask import request
from datetime import datetime
import pytz

def convert_to_wib(dt_obj):
    return dt_obj.astimezone(pytz.timezone('Asia/Jakarta'))\
        .strftime("%H:%M WIB, %a, %d %b %Y")

class Visitors():
    def __init__(self) -> None:
        pass
    
    def get_all(self):
        try:
            hasil = db.query(query="SELECT DATE_TRUNC('day', tanggal) AS tanggal, COUNT(*) AS pengunjung FROM visitors GROUP BY DATE_TRUNC('day', tanggal) ORDER BY tanggal DESC;")
            for item in hasil:
                item['tanggal'] = convert_to_wib(item['tanggal'])
            return {
                "hasil": hasil
            }
        except Exception as e:
            print(f"Error di get all visitors")
            traceback.print_exc()
            return "Error", 500
        
    def add(self):
        try:
            db.query(query="insert into visitors(tanggal, ip) values(%s, %s)", params=(datetime.now(), request.remote_addr,), fetch=False)
            return {
                "berhasil": True
            }
        except Exception as e:
            print(f"Error di add visitors")
            traceback.print_exc()
            return "Error", 500
        
visitors = Visitors()