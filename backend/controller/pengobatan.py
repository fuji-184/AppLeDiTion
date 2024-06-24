from setup.postgresql import db

def obat(penyakit):
  if penyakit == "apple_scab":
    penyakit = "Apple Scab"
  
    hasil = db.query("select * from penyakit where nama = $1", penyakit)
    return {"hasil": hasil}