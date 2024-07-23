from setup.postgresql import db

def obat(penyakit):
	if penyakit is not None:
		if penyakit == "apple_scab":
			penyakit = ("Apple Scab",)
		elif penyakit == "cedar_apple_rust":
			penyakit = ("Cedar Apple Rust",)
		elif penyakit == "black_root":
			penyakit = ("Black Root",)
		elif penyakit == "healthy":
			penyakit = ("Healthy",)
		hasil = db.query("select * from hasil where nama = %s;", penyakit)
		return {"hasil": hasil}