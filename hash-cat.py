import hashlib

def hash_cracker(hash_to_crack, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            for word in file:
                word = word.strip()  # satır sonu karakterlerini kaldır
                hashed_word = hashlib.sha256(word.encode()).hexdigest()

                if hashed_word == hash_to_crack:
                    print(f"✅ Şifre bulundu: {word}")
                    return word
        print("❌ Hiçbir eşleşme bulunamadı.")
    except FileNotFoundError:
        print("⚠️ Wordlist dosyası bulunamadı.")

if __name__ == "__main__":
    # SHA-256 ile şifrelenmiş parola örneği (örnek: "admin" için hash)
    hedef_hash = "8c6976e5b5410415bde908bd4dee15dfb16a7a60a3b144da0f8f9c3f8f6d7b88"

    # Wordlist dosyasının yolu (örnek bir wordlist oluşturabilirsin)
    wordlist_dosyasi = "wordlist.txt"

    print("🔍 Parola kırma işlemi başlatılıyor...")
    hash_cracker(hedef_hash, wordlist_dosyasi)
