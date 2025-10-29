# cepGPT (pocketGPT)
```
Veri içinde boğuluyoruz, ama bilgiye açız.

-John Naisbitt
```
Yukarıdaki ifade, bu depoda yapmak istediğim şeyi tam olarak anlatıyor. Bu proje serisiyle hem doğal dil işleme tekniklerini, Türkçe dil istatistiklerini hem de tamamen Türkçe için geliştirilmiş bir dil modeli oluşturma fikrini hayata geçirmeye çalışıyorum.  

Süreç boyunca Andrej Karpathy’nin [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) deposundan ilham aldım ve onun ötesine geçmeye çalıştım.

---

## 🚀 Veri Setleri

1. **Nutuk:** Atatürk'ün Nutuk kitabının modern Türkçe'ye uyarlanmış halinin işlenerek saf metin olacak şekilde ayarlandığı veri seti. Dosyanın kaynağını Google'a Nutuk PDF yazdığınızda çıkan resmi websayfalarında paylaşılan dosyalardan bulabilirsiniz.

2. **Türkçe isimler:** Bu veri seti, internet üzerinde açıkça paylaşılan seçmen, öğrenci, bebek (TÜİK), YSK ve benzeri kaynaklarda geçen gerçek insan isimlerinden (gizlilik nedeniyle yalnızca ad kısmı kullanılmıştır) derlenmiş 2,315 özgün ismi içermektedir. Veri seti karakter düzeyinde LLM uygulamaları için hazırlanmıştır.
Not: Yabancı ve nadir isimler filtrelenmiştir.