# 🔐 SHA-256 Brute Force Demo (Python)

Bu proje, verilen bir SHA-256 hash değerinden orijinal metni bulmak için basit bir brute force (deneme-yanılma) yaklaşımını göstermektedir.

## 📌 Açıklama

Script, kullanıcıdan bir SHA-256 hash alır ve önceden tanımlanmış bir kelime listesi (wordlist) ile karşılaştırma yapar. Eğer eşleşme bulunursa, hash’in karşılık geldiği gerçek metin ekrana yazdırılır.

> ⚠️ Bu proje sadece eğitim amaçlıdır. Gerçek sistemlerde şifre kırmak için kullanılmamalıdır.

## 🚀 Nasıl Çalışır?

1. Kullanıcı hedef hash değerini girer
2. Script, kelime listesindeki her bir değeri tek tek dener
3. Her kelime SHA-256 ile hash’lenir
4. Oluşan hash ile hedef hash karşılaştırılır
5. Eşleşme bulunursa → şifre bulunur

## 🧪 Örnek Kelime Listesi

```python id="9r4l3v"
["123456", "password", "admin", "qwerty", "enes", "1234"]
```

## ▶️ Kullanım

```bash id="2zj9wx"
python script.py
```

Çalıştırdıktan sonra hedef hash değerini girmeniz yeterlidir.

## 🛠 Gereksinimler

* Python 3.x
* Dahili hashlib kütüphanesi (ek kurulum gerekmez)

## ⚠️ Uyarı

* Brute force işlemleri çok zaman alabilir
* SHA-256 güçlü bir algoritmadır ve kırılması zordur
* Gerçek sistemlerde:

  * Salt kullanılır
  * Rate limiting uygulanır

## 📚 Amaç

Bu proje sayesinde:

* Hash fonksiyonlarının nasıl çalıştığını
* Hash’lerin neden tek yönlü olduğunu
* Brute force mantığını

öğrenebilirsiniz.

---

💡 Geliştirme fikirleri:

* Daha büyük wordlist kullanımı
* Dosyadan veri okuma
* Çoklu işlem (multi-threading) ile hızlandırma

---
