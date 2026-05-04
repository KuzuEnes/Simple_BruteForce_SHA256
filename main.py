import hashlib

hedef_hash = input("Kırılacak SHA-256 hash: ")

# Basit wordlist
kelimeler = ["123456", "password", "admin", "qwerty", "enes", "1234"]

for kelime in kelimeler:
    hash_deger = hashlib.sha256(kelime.encode()).hexdigest()

    print(f"Deneniyor: {kelime}")

    if hash_deger == hedef_hash:
        print("Şifre bulundu:", kelime)
        break
else:
    print("Listede bulunamadı")