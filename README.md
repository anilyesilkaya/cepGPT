# cepGPT (pocketGPT)
**Sıfırdan Türkçe için özel olarak tasarlanmış en basit ve en hızlı GPT serisi.**  
[karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)'den ilham alan, **Türkçe** veri, tokenizasyon ve değerlendirme için ilk ilkelerden yeniden oluşturulmuş temiz, minimal, araştırma dostu bir yeniden uygulama.

---

## 🚀 Öne Çıkanlar
- **Sıfırdan**: Küçük, okunabilir kod tabanı—öğrenmek ve geliştirmek için harika.
- **Türkçe öncelikli**: **İ/ı, Ç/ç, Ğ/ğ, Ö/ö, Ş/ş, Ü/ü**, apostroflar, klitikler ve üç nokta işaretlerinin düzgün işlenmesi.
- **Tak-çalıştır tokenizasyon**: Karakter, kelime veya BPE düzeyinde (kendi tokenizer'ınız veya [turktoken](https://github.com/anilyesilkaya/turktoken) ile çalışır).
- **Küçük model profilleri**: Hızlı iterasyonlar için `minik` (çok küçük), `mini` (küçük), `small` (kompakt).
- **Tekrarlanabilir**: Deterministik çalıştırmalar, yapılandırma dosyaları ve tohum kontrolü.
- **Hızlı**: Didaktik deneyler için tek bir GPU veya CPU üzerinde eğitim.

---

## 🚀 Veri Setleri

1. Nutuk: Atatürk'ün Nutuk kitabının modern Türkçe'ye uyarlanmış halinin işlenerek saf metin olacak şekilde ayarlandığı veri seti. Dosyanın kaynağını Google'a Nutuk PDF yazdığınızda çıkan resmi websayfalarında paylaşılan dosyalardan bulabilirsiniz.

2. Türkçe isimler: Bu veri setinde internet üzerinde açıkça paylaşılan seçmen, öğrenci, bebek (TÜİK) gerçek insan isimlerinden derlenmiş 1144 özgün isim karakter düzeyinde LLM uygulamaları için hazırlanmıştır.
