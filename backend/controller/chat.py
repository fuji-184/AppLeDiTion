from setup.postgresql import db

def ambilChat():
    hasil = db.query(query="SELECT chats.*, users.nama FROM chats JOIN users ON chats.id_user = users.id;")
    
    return {"hasil": hasil}