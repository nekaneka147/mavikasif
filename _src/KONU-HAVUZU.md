# Blog / Journal — konu havuzu (mavikasif.com · TR + EN)

Sıradaki yazı = **listede `[ ]` olan en üstteki konu.** Yayınlanınca `[x]` işaretle + tarih yaz.
Kitle: Kapadokya'da **düğün / nişan / save-the-date** dış çekimi planlayan çiftler. Turist gezi çekimi değil — o cappadociaphotographer.com'un işi.

## Yayınlananlar
- [x] 2026-07-16 — **Neden Kapadokya'da Düğün Dış Çekimi Yaptırmalısınız?** (`neden-kapadokyada-dugun-dis-cekimi`)
- [x] 2026-07-16 — **Düğün Fotoğrafçısı Seçerken Nelere Dikkat Etmelisiniz?** (`dugun-fotografcisi-secerken-nelere-dikkat-etmeli`)
- [x] 2026-08-16 — ikisi de **İngilizceye çevrildi**, `/en/blog/` açıldı (yeni yazı değil, mevcutların EN sürümü)
- [x] 2026-09-11 — **Kapadokya'da Düğün Dış Çekimi İçin Hangi Mevsim? Ay Ay Rehber** (`kapadokyada-dugun-dis-cekimi-icin-en-iyi-mevsim`)
- [x] 2026-09-11 — **Gelinlikle Kapadokya Dış Çekimi: Pratikte Nasıl Oluyor?** (`gelinlikle-kapadokya-dis-cekimi-nasil-oluyor`)
- [x] 2026-09-11 — **Nişan ve Save-the-Date Çekimi: Ne Zaman, Nasıl, Ne Giyerek?** (`nisan-ve-save-the-date-cekimi-rehberi`)
- [x] 2026-09-22 — **Albümlü Hikâye Paketi Neden Var? Basılı Albüm ve Posterin Anlamı** (`albumlu-hikaye-paketi-neden-var`)

## Sırada
- [ ] **Çekim günü saat saat** — 04:30 otel alımı → hangi vadi → kaç lokasyon → kahvaltıya dönüş. Beklenti yönetimi, "bu kadar erken kalkmaya değer mi" itirazını kırar.
- [ ] **Kapadokya'ya nasıl gelinir, kaç gece kalınır?** — Kayseri/Nevşehir uçuşları, transfer, çekimi hangi güne koymalı. Planlama aşamasındaki çifti erken yakalar.
- [ ] **Yağmur/rüzgâr olursa ne oluyor?** — B planı: fener ve halı dükkânları, mağara otel terasları. Dürüstlük güven veriyor.
- [ ] **Evlilik teklifi çekimi: sürpriz nasıl bozulmadan çekilir** — gizli çekim kurgusu, lokasyon seçimi, partnerin fark etmemesi.
- [ ] **Yılkı atları: nerede, ne zaman, garanti var mı** — en çok sorulan sahne; "garanti edilemez" dürüstlüğüyle.
- [ ] **Mağara otelleri: hangi terasta hangi saatte iyi ışık var** — otellerle karşılıklı bağlantı potansiyeli.
- [ ] **Kaç fotoğraf teslim ediliyor, ne zaman?** — retuş sayısı, ham kareler, teslim süresi. Paket sayfasının cevaplamadığı asıl soru.
- [ ] **Yıl dönümü ve balayı çekimleri** — düğün dışı segment, sitede şu an zayıf temsil ediliyor.

## Yazarken uyulacaklar (her yazıda kontrol et)
1. **TR + EN zorunlu** — eksikse script durur. EN, TR'nin birebir çevirisi değil; aynı özü taşıyan doğal İngilizce metin olsun.
2. **Sadece gerçek hizmetler.** Var: otel alımı + tüm transferler, gün doğumu/batımı çekimi, **Albümlü Hikâye** (30×60 panoramik + 2×15×30 aile albümü + 50×75 poster + video klip), video & evlilik teklifi, uçan elbise, aksesuar, yılkı atları, fener & halı dükkânı, mağara otel terası, Instagram reels, poz sınırı yok, tüm fotoğraflar teslim + 20 retuş. **Yok (yazma):** drone, makyaj/saç, klasik araba, teklif-yemeği kurulumu.
3. **Fiyat yazma.** mavikasif fiyatsız çalışıyor (kullanıcı kararı) — WhatsApp'a yönlendir.
4. **Garanti verme.** Balon, hava, at sürüsü kimsenin elinde değil; bunu yazının kendisi söylesin.
5. Görsel `img/` içinden seçilir, `alt` iki dilde ve gerçeği anlatır.
6. Yazının sonunda ilgili dilin `#paketler` bağı olsun.
7. ⚠️ **cappadociaphotographer.com ile aynı metni kullanma.** İki site de bizim ama Google için ayrı yayınlar; aynı cümleler kopya içerik sayılır. Konu örtüşse bile metin sıfırdan yazılır, açı farklı olur (orada turist gezi çekimi, burada düğün).

## Nasıl yayınlanır
1. `_src/posts/<YYYY-AA-GG>-<slug>.json` aç (`i18n.tr` + `i18n.en` → `title, desc, alt, body`).
2. `python _src/mavi_build.py`
3. `gh auth switch --user nekaneka147` → commit + push → `gh auth switch --user wenaglobal`
