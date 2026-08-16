# -*- coding: utf-8 -*-
"""mavikasif.com — Kapadokya düğün fotoğrafçısı, TR+EN statik site üretici

Kullanim:  python _src/mavi_build.py            -> repo kokune uretir
           python _src/mavi_build.py <klasor>   -> baska klasore uretir (onizleme)

Yeni blog yazisi = _src/posts/ altina bir .json dosyasi (tr + en) + bu script.
"""
import os, json, sys, glob

_HERE = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(_HERE, "posts")
LANG_DIR = {"tr": "", "en": "en"}
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(_HERE)
DOMAIN = "https://mavikasif.com"
WA_NUM = "905537175240"
EMAIL = "kasifmavi@gmail.com"
IG = "https://www.instagram.com/mavikasif/"
FB = "https://www.facebook.com/mavikasif/"
PIN = "https://tr.pinterest.com/mavikasif/"

T = {
"tr": {
 "meta_title": "Kapadokya Düğün Fotoğrafçısı — Mavi Kaşif | Karı-Koca Dış Çekim Ekibi",
 "meta_desc": "Kapadokya'da düğün, nişan ve save-the-date dış çekimi. Karı-koca fotoğrafçı ekibi, balonlu gün doğumu çekimleri, albümlü paketler. Tüm fotoğraflar teslim — WhatsApp'tan yazın.",
 "wa_text": "Merhaba! Kapadokya'da dış çekim için bilgi almak istiyorum.",
 "nav": ["Paketler","Neler Yaşarsınız","Galeri","Yorumlar","Biz Kimiz","S.S.S."],
 "nav_cta": "Tarih Sor",
 "lang_link": ("/en/", "EN"),
 "hero_loc": "Kapadokya Düğün & Nişan Dış Çekimi · Göreme",
 "hero_title": 'Aşkınızın hikâyesi, <em>peribacaları</em> arasında',
 "hero_sub": "Karı-koca fotoğrafçı ekibiyiz. 2016'dan beri düğün, nişan ve save-the-date çekimlerini Kapadokya'nın altın ışığında, balonların altında ölümsüzleştiriyoruz.",
 "hero_cta1": "WhatsApp'tan Yazın",
 "hero_cta2": "Paketleri Görün",
 "hero_scroll": "kaydırın",
 "pk_kicker": "Dış Çekim Paketleri",
 "pk_title": 'Işığınızı <em>seçin</em>',
 "pk_intro": "Her pakette otel transferi, Kapadokya'nın en iyi çekim noktaları ve çekilen TÜM fotoğrafların dijital teslimi var. Poz sınırı yok. Tarihinizi yazın, size özel teklifle dönelim.",
 "pk_popular": "En Çok Tercih Edilen",
 "pk_cta": "Fiyat Al",
 "packs": [
  {"time":"Gün Doğumu · 2–2,5 saat","name":"Gün Doğumu Çekimi","tag":"Başınızın üstünde yüzlerce balon",
   "feats":["Otel alımı ve tüm transferler dahil","Balonlarla gün doğumu çekimi","En iyi 3 gün doğumu lokasyonu","Poz sınırı yok — tüm fotoğraflar teslim","Seçilen 20 fotoğrafa profesyonel retuş","Instagram reel videosu dahil","Sınırsız kıyafet değişimi"]},
  {"time":"Gün Batımı · 2–2,5 saat","name":"Gün Batımı Çekimi","tag":"Vadilerin üzerinde altın saat",
   "feats":["Otel alımı ve tüm transferler dahil","En iyi 3 gün batımı lokasyonu","Opsiyonel: 200–300 yılkı atı","Poz sınırı yok — tüm fotoğraflar teslim","Seçilen 20 fotoğrafa profesyonel retuş","Instagram reel videosu dahil","Sınırsız kıyafet değişimi"]},
  {"time":"Albümlü","name":"Albümlü Hikâye","tag":"Elinizde tutacağınız anılar",
   "feats":["Gün doğumu veya gün batımı çekimi","Tüm fotoğraflar + 35 profesyonel retuş","1 adet 30×60 panoramik albüm","2 adet 15×30 aile albümü","1 adet 50×75 poster","1–2 dakikalık video klip","Instagram reel videosu dahil"]},
  {"time":"Sinematik","name":"Video & Evlilik Teklifi","tag":"Hayatta bir kez yaşanan anlar için",
   "feats":["Evlilik teklifi planlaması","Sinematik video klip","Sürpriz için gizli çekim","Kalabalıksız en iyi noktalar","Tüm görüntüler teslim","Her fotoğraf paketiyle birleşir"]},
 ],
 "ex_kicker": "Neler Yaşayacaksınız",
 "ex_title": 'Sadece <em>burada</em> mümkün',
 "ex_intro": "Kapadokya dünyanın en masalsı fonu — ve biz her köşesini biliyoruz. Çiftlerin dünyanın öbür ucundan gelme sebebi bu kareler.",
 "exps": [
  {"img":"cappadocia-hot-air-balloons-sunrise.jpg","alt":"Gün doğumunda Kapadokya semalarını dolduran onlarca sıcak hava balonunu izleyen gezgin",
   "t":"Balonlu Gün Doğumu","p":"Her açık sabah yüzlerce balon peribacalarının üzerinde yükselir. Sizi bildiğimiz sakin seyir noktalarına konumlandırırız; tüm o masal arkanızda kalır. Herkesin hayalindeki o kare — doğru çekilmiş hali."},
  {"img":"cave-hotel-photoshoot-cappadocia.jpg","alt":"Taş sütunlar arasında kırmızı uçan elbisesiyle poz veren misafir, arkada yükselen balonlar",
   "t":"Uçan Elbise & Gelinlik","p":"Vadilere karşı savrulan etekler... Ünlü uçan elbise karelerimiz için elbiseleri biz getiririz, pozu biz kurarız, kumaşın en güzel savrulduğu anı biz yakalarız. Gelinlikle de, elbiseyle de."},
  {"img":"cappadocia-valley-photoshoot.jpg","alt":"Gün batımında yılkı atlarına doğru el ele koşan çift",
   "t":"Gün Batımında Yılkı Atları","p":"Altın saatte 200–300 yılkı atı vadilerden geçer. Güneş Erciyes'in ardına inerken atların arasında durmak — Kapadokya'nın en sinematik karesi."},
  {"img":"lantern-shop-photoshoot-cappadocia.jpg","alt":"Kapadokya'da yüzlerce mozaik fenerin altında duran misafir",
   "t":"Fener & Halı Dükkânları","p":"Mozaik fenerlerle aydınlanan asırlık halı dükkânları — Kapadokya'nın en büyülü kapalı mekân sahnesi. Yağmurlu günler için birebir; favori karenizi almadan çıkamazsınız."},
  {"img":"couple-photoshoot-goreme.jpg","alt":"Mağara otelin havuzlu terasında, gökyüzü balonlarla doluyken öpüşen çift",
   "t":"Mağara Otel Terasları","p":"Taş terasta kahvaltı, yanınızdan süzülen balonlar... Çekimi konakladığınız otelde başlatıp ışık değiştikçe vadilere ineriz."},
 ],
 "st_kicker": "Nasıl Çalışır",
 "st_title": 'Rezervasyon <em>çok kolay</em>',
 "steps": [
  {"t":"Paketinizi seçin","p":"Yukarıdaki detayları inceleyin, seyahat planınıza uyanı seçin — ya da tarihinizi söyleyin, size en uygununu biz önerelim."},
  {"t":"WhatsApp'tan yazın","p":"Birkaç saat içinde döneriz: müsait tarihler, güncel fiyatlar ve merak ettiğiniz her şey."},
  {"t":"Tarihinizi kilitleyin","p":"Küçük bir kapora ile gün doğumu veya gün batımı saatiniz size ayrılır. Kalanı çekim günü ödersiniz."},
  {"t":"Çekimin tadını çıkarın","p":"Sizi otelinizden alırız, her pozda yönlendiririz ve tüm fotoğraflarınızı teslim ederiz — en güzel 20'si elle retuşlu."},
 ],
 "ga_kicker": "Galeri",
 "ga_title": 'Vadilerden <em>kareler</em>',
 "gallery": [
  {"img":"hot-air-balloons-goreme-valley.jpg","alt":"Göreme vadisinin kayalıkları üzerinde süzülen balonlar","cap":"Göreme, ilk ışık"},
  {"img":"carpet-shop-photoshoot-cappadocia.jpg","alt":"Kapadokya halı dükkânında rengârenk kilimlerin arasında","cap":"Halı dükkânı çekimi"},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"Altın saatte vadide karşılıklı duran gelin ve damat","cap":"Altın saat yeminleri"},
  {"img":"bridal-photoshoot-cappadocia.jpg","alt":"Vadiye karşı salıncakta gelin, arkada balonlar","cap":"Vadiye karşı salıncak"},
  {"img":"wedding-couple-cappadocia.jpg","alt":"Yumuşak ışıkta poz veren gelin ve damat","cap":"Evlendik!"},
  {"img":"cappadocia-valley-photoshoot.jpg","alt":"Gün batımında yılkı atlarına koşan çift","cap":"Yılkı atları"},
  {"img":"engagement-photoshoot-cappadocia.jpg","alt":"Kapadokya'da gün batımında gelinin yanağına kondurulan öpücük","cap":"Altın öpücük"},
  {"img":"anniversary-photoshoot-cappadocia.jpg","alt":"Pastel balonlu gökyüzünün altında el ele yürüyen çift","cap":"Yıl dönümü ışığı"},
  {"img":"photographer-cappadocia-at-work.jpg","alt":"Kapadokya'da çekim sırasında fotoğrafçı","cap":"Objektifin arkası"},
 ],
 "rv_kicker": "Misafir Yorumları",
 "rv_title": 'Dünyanın dört yanından <em>çiftler</em>',
 "reviews": [
  {"txt":"Nişanımızın o güzel anlarını ölümsüzleştirdiğiniz için çok teşekkürler. Siz en tatlı fotoğrafçı çiftsiniz — balonların kurulumuna yardım ettiniz, esnek davrandınız, bizi muhteşem noktalara götürdünüz. Hâlâ büyülenmiş durumdayım. Kapadokya'daki her anınız için bu ikiliyi şiddetle tavsiye ederim!","name":"Tim & Linh","type":"Nişan Çekimi"},
  {"txt":"Kapadokya'nın balonlarını görmek ve fotoğraflamak hep hayalimizdi. Hava şartları balonların uçmasına izin vermedi ama yine de harika vakit geçirdik — çekim eğlenceli ve doğaldı, fotoğraflar tam beklediğimiz gibi çıktı. İkisine de bravo!","name":"Willius & Qinghui","type":"Çift Çekimi"},
  {"txt":"Çekimi yönetme şekillerine bayıldık. Yanımızda bebeğimiz vardı; baştan sona sabırlı ve anlayışlıydılar. Hem çekimden hem lokasyonlardan çok keyif aldık — kesinlikle yapılması gereken bir deneyim!","name":"Aayushi & Aakash","type":"Aile Çekimi"},
 ],
 "ab_kicker": "Biz Kimiz",
 "ab_title": 'Objektifin arkasında <em>bir karı-koca</em>',
 "ab_p1": "Fotoğrafa —ve aşkı fotoğraflamaya— gönül vermiş yerli bir çiftiz. On yıla yakındır çiftleri gün doğumu vadilerinde, kimsenin bilmediği seyir noktalarında ve fener ışığıyla yıkanan dükkânlarda gezdiriyor, Kapadokya yolculuklarını ömür boyu saklanacak karelere dönüştürüyoruz.",
 "ab_p2": "Burada yaşadığımız için sabah 6'da ışığın nereye düştüğünü, atların akşamüstü hangi vadiden geçtiğini, balonları arkanıza nasıl alacağımızı biliriz. İki kişi olduğumuz içinse biri pozunuzu kurarken diğeri aradaki en doğal anları yakalar — en çok seveceğiniz kareler onlar olur.",
 "ab_sign": "— Kaşif & Bahar",
 "stats": [["2016","'dan beri"],["1000+","mutlu misafir"],["4 saat","yanıt süresi"]],
 "ab_alt": "Kapadokya vadilerinde çekim yapan karı-koca fotoğrafçı ekibi",
 "fq_kicker": "Merak Edilenler",
 "fq_title": 'Sormadan <em>önce</em>',
 "faqs": [
  {"q":"Kapadokya'da dış çekim için en iyi zaman hangisi?","a":"Yılın her mevsimi gün doğumu: balonlar o saatte uçar ve ışık en yumuşak hâlindedir. İkinci sırada gün batımı gelir — sıcak altın ışık, çok daha az kalabalık. Nisan–Haziran ve Eylül–Kasım hava açısından en istikrarlı dönemlerdir; kar altındaki kış çekimleri ise bambaşka güzeldir."},
  {"q":"Balonlar garanti mi?","a":"Balonlar açık sabahların çoğunda uçar; ancak uçuşlar hava durumuna ve sivil havacılık iznine bağlıdır. Tarihinizde uçuş iptal olursa çekimi vadilere ve aksesuarlara göre yeniden kurgularız — fotoğraflar yine büyüleyici olur, misafirlerimizin yorumları ortada."},
  {"q":"Kaç fotoğraf alıyoruz?","a":"Hepsini. Çekimdeki tüm başarılı kareler dijital olarak sizindir; üzerine seçtiğiniz 20 kare (Albümlü Hikâye'de 35) profesyonelce retuşlanır. Teslimat birkaç gün içinde online galeriyle yapılır."},
  {"q":"Ne giymeliyiz? Gelinlik olur mu?","a":"Vadilere karşı uzun ve uçuşan elbiseler harika görünür — meşhur uçan elbiselerimizi ve aksesuarları biz getiririz. Gelinlik-damatlıkla da çekiyoruz; yanınıza ikinci bir kıyafet alın, değişim sınırsız. Rezervasyondan sonra size stil rehberi göndeririz."},
  {"q":"Rezervasyon ve ödeme nasıl işliyor?","a":"Tarihlerinizi WhatsApp'tan yazın. Küçük bir kapora ile saatiniz kilitlenir; kalan ödemeyi çekim günü nakit veya havaleyle yaparsınız."},
  {"q":"Albümler ne zaman teslim edilir?","a":"Albümlü Hikâye paketinde retuşlarınızı onayladıktan sonra panoramik albüm, aile albümleri ve posteriniz baskıya girer; kargoyla adresinize gönderilir. Dijital teslim ise her pakette birkaç gün içindedir."},
 ],
 "ct_kicker": "Siz hazırsanız biz hazırız",
 "ct_title": '<em>Kapadokya</em> çekiminizi planlayalım',
 "ct_sub": "Seyahat tarihlerinizi yazın; gerisi bizde — lokasyonlar, aksesuarlar, zamanlama ve ışık.",
 "ct_wa": "WhatsApp'tan Yazın",
 "ct_ig": "Instagram'dan DM",
 "ct_or": "ya da yazın:",
 "ft_rights": "Tüm fotoğraflar © Mavi Kaşif Fotoğrafçılık",
 "blog_kicker": "Blog",
},
"en": {
 "meta_title": "Cappadocia Wedding Photographer — Mavi Kaşif | Wife & Husband Elopement Team",
 "meta_desc": "Wedding, elopement and pre-wedding photography in Cappadocia by a local wife & husband team. Sunrise balloon sessions, printed album packages, all photos delivered. Message us on WhatsApp.",
 "wa_text": "Hello! I would like to ask about a wedding photoshoot in Cappadocia.",
 "nav": ["Packages","Experiences","Gallery","Reviews","About","FAQ"],
 "nav_cta": "Check Dates",
 "lang_link": ("/", "TR"),
 "hero_loc": "Cappadocia Wedding Photographer · Göreme",
 "hero_title": 'Your love story, among the <em>fairy chimneys</em>',
 "hero_sub": "We are a local wife & husband team photographing weddings, elopements and pre-wedding sessions in Cappadocia's golden light — since 2016.",
 "hero_cta1": "Message on WhatsApp",
 "hero_cta2": "See Packages",
 "hero_scroll": "scroll",
 "pk_kicker": "Wedding Photoshoot Packages",
 "pk_title": 'Choose your <em>light</em>',
 "pk_intro": "Every package includes hotel pick-up, Cappadocia's best photo spots and ALL of your digital photos — no pose limits. Tell us your date and we'll reply with a tailored quote.",
 "pk_popular": "Most Popular",
 "pk_cta": "Get a Quote",
 "packs": [
  {"time":"Sunrise · 2–2.5 h","name":"Sunrise Session","tag":"Hundreds of balloons above you",
   "feats":["Hotel pick-up & all transfers included","Shoot with hot-air balloons at dawn","3 best sunrise locations","No pose limit — all photos delivered","20 professionally retouched picks","Instagram reel video included","Unlimited outfit changes"]},
  {"time":"Sunset · 2–2.5 h","name":"Sunset Session","tag":"Golden hour over the valleys",
   "feats":["Hotel pick-up & all transfers included","3 best sunset locations","Optional: 200–300 wild horses","No pose limit — all photos delivered","20 professionally retouched picks","Instagram reel video included","Unlimited outfit changes"]},
  {"time":"With Albums","name":"Album Story","tag":"Memories you can hold",
   "feats":["Sunrise or sunset session","All photos + 35 fine retouches","1 panoramic album (30×60 cm)","2 family albums (15×30 cm)","1 poster print (50×75 cm)","1–2 minute video clip","Instagram reel video included"]},
  {"time":"Cinematic","name":"Video & Proposal","tag":"For once-in-a-lifetime moments",
   "feats":["Marriage proposal planning","Cinematic video clip","Discreet shooting for surprises","Best viewpoints, zero crowds","All footage delivered","Combine with any photo package"]},
 ],
 "ex_kicker": "Signature Experiences",
 "ex_title": 'Only possible <em>here</em>',
 "ex_intro": "Cappadocia is the world's dreamiest wedding backdrop — and we know every corner of it. These are the scenes couples cross the world for.",
 "exps": [
  {"img":"cappadocia-hot-air-balloons-sunrise.jpg","alt":"Traveler watching dozens of hot-air balloons rise over Cappadocia at sunrise",
   "t":"Hot-Air Balloon Sunrise","p":"Every clear morning, a hundred balloons rise over the fairy chimneys. We place you on quiet viewpoints we know well — the whole spectacle unfolds behind you."},
  {"img":"cave-hotel-photoshoot-cappadocia.jpg","alt":"Guest in a flowing red dress between stone columns as balloons rise behind",
   "t":"Flying Dress & Bridal","p":"Skirts billowing against the sunrise valleys — we bring the dresses, build the pose and catch the fabric at its most beautiful. In a wedding gown or a flying dress alike."},
  {"img":"cappadocia-valley-photoshoot.jpg","alt":"Couple running hand in hand toward a herd of wild horses at sunset near Cappadocia",
   "t":"Wild Horses at Sunset","p":"At golden hour, a herd of 200–300 wild horses crosses the valleys. Standing among them as the sun drops behind Mount Erciyes — Cappadocia's most cinematic frame."},
  {"img":"lantern-shop-photoshoot-cappadocia.jpg","alt":"Guest standing under hundreds of glowing mosaic lanterns in a Cappadocia shop",
   "t":"Lantern & Carpet Shops","p":"Century-old carpet shops glowing with mosaic lanterns — Cappadocia's most magical indoor scene. Perfect for rainy days; impossible to leave without a favorite photo."},
  {"img":"couple-photoshoot-goreme.jpg","alt":"Couple kissing on a cave hotel pool terrace as balloons fill the sky",
   "t":"Cave Hotel Terraces","p":"Breakfast on a stone terrace while balloons drift past — we can start your session right at your hotel, then follow the light into the valleys."},
 ],
 "st_kicker": "How It Works",
 "st_title": 'Booking is <em>simple</em>',
 "steps": [
  {"t":"Pick your package","p":"Browse the details above and choose what fits your plan — or tell us your dates and we'll recommend."},
  {"t":"Message us on WhatsApp","p":"We reply within hours with availability, current prices and everything you want to know."},
  {"t":"Lock your date","p":"A small booking payment reserves your sunrise or sunset. The rest is paid on the day of your shoot."},
  {"t":"Enjoy your session","p":"We pick you up, guide every pose and deliver all your photos — the finest, hand-retouched."},
 ],
 "ga_kicker": "Gallery",
 "ga_title": 'Frames from the <em>valleys</em>',
 "gallery": [
  {"img":"hot-air-balloons-goreme-valley.jpg","alt":"Hot-air balloons floating close to the rock formations of Göreme valley","cap":"Göreme, first light"},
  {"img":"carpet-shop-photoshoot-cappadocia.jpg","alt":"Guest among colorful kilims in a Cappadocia carpet shop","cap":"Carpet shop session"},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"Bride and groom facing each other at golden hour in a Cappadocia valley","cap":"Golden hour vows"},
  {"img":"bridal-photoshoot-cappadocia.jpg","alt":"Bride on a swing overlooking the Cappadocia valleys, balloons behind","cap":"Swing over the valley"},
  {"img":"wedding-couple-cappadocia.jpg","alt":"Bride and groom posing in soft light","cap":"Just married"},
  {"img":"cappadocia-valley-photoshoot.jpg","alt":"Couple running toward wild horses at sunset","cap":"The wild horses"},
  {"img":"engagement-photoshoot-cappadocia.jpg","alt":"Groom kissing bride at golden hour in Cappadocia","cap":"Golden kiss"},
  {"img":"anniversary-photoshoot-cappadocia.jpg","alt":"Couple walking hand in hand under a balloon-filled pastel sky","cap":"Anniversary light"},
  {"img":"photographer-cappadocia-at-work.jpg","alt":"Photographer at work during a session in Cappadocia","cap":"Behind the lens"},
 ],
 "rv_kicker": "Guest Words",
 "rv_title": 'Loved by couples <em>worldwide</em>',
 "reviews": [
  {"txt":"Thank you so much for capturing the beautiful moments of our engagement. You guys are the sweetest couple photographers — assisting with the balloon setup, staying flexible, taking us to beautiful and cool spots. Still in awe. Highly recommend this duo for any Cappadocia moment you want to capture!","name":"Tim & Linh","type":"Engagement"},
  {"txt":"We always dreamt about seeing the hot-air balloons at Cappadocia and documenting it. The weather didn't let the balloons fly, but we still had an amazing time — the photoshoot was fun and natural, and the pictures turned out exactly how we hoped!","name":"Willius & Qinghui","type":"Couple"},
  {"txt":"Really loved the way these two handled our shoot. We had an infant with us and they were accommodating and patient throughout. We enjoyed the shoot and the locations a lot — a must-do activity!","name":"Aayushi & Aakash","type":"Family"},
 ],
 "ab_kicker": "About Us",
 "ab_title": 'A wife & husband <em>behind the lens</em>',
 "ab_p1": "We are a local couple in love with photography — and with photographing love. For nearly a decade we've guided couples through sunrise valleys, secret viewpoints and lantern-lit shops, turning their Cappadocia journey into images they keep forever.",
 "ab_p2": "Because we live here, we know where the light lands at 6 a.m., which valley the horses cross at dusk, and how to time the balloons behind you. And because we are two, one of us builds your pose while the other catches the candid in-between moments — the ones you'll love most.",
 "ab_sign": "— Kaşif & Bahar",
 "stats": [["2016","working since"],["1000+","happy guests"],["4 h","reply time"]],
 "ab_alt": "Cappadocia wedding photographer couple at work in the valleys",
 "fq_kicker": "Questions",
 "fq_title": 'Before you <em>ask</em>',
 "faqs": [
  {"q":"When is the best time for a wedding photoshoot in Cappadocia?","a":"Sunrise, all year round — that's when the balloons fly and the light is softest. Sunset comes a close second with warm golden light and far fewer people. April–June and September–November are the most stable months; winter snow sessions are breathtaking too."},
  {"q":"Are the hot-air balloons guaranteed?","a":"Balloons fly on most clear mornings, but flights depend on the weather and aviation authority. If they don't fly on your date, we rebuild the session around the valleys and props — the photos are still magical, as our guests will tell you."},
  {"q":"How many photos do we receive?","a":"All of them. Every good frame from your session is yours digitally, plus 20 professionally retouched picks (35 in the Album Story package). Delivery via online gallery within days."},
  {"q":"What should we wear? Can we shoot in a wedding gown?","a":"Long, flowing dresses look stunning against the valleys — we bring our famous flying dresses and props. We absolutely shoot in wedding gowns too. Bring a second outfit; changes are unlimited. A style guide is sent after booking."},
  {"q":"How do we book and pay?","a":"Message us on WhatsApp with your dates. A small booking payment locks your slot; the remainder is paid in cash or transfer on the day of the shoot."},
  {"q":"When are the printed albums delivered?","a":"In the Album Story package, once you approve your retouched picks, the panoramic album, family albums and poster go to print and are shipped to your address. Digital delivery happens within days on every package."},
 ],
 "ct_kicker": "Ready when you are",
 "ct_title": 'Let’s plan your <em>Cappadocia</em> wedding session',
 "ct_sub": "Tell us your travel dates and we'll take care of the rest — locations, props, timing and the light.",
 "ct_wa": "Message on WhatsApp",
 "ct_ig": "DM on Instagram",
 "ct_or": "or write to",
 "ft_rights": "All photographs © Mavi Kaşif Photography",
 "blog_kicker": "Journal",
},
}

def load_posts():
    """_src/posts/*.json -> yeniden eskiye sirali liste. tr+en zorunlu."""
    posts = []
    for path in sorted(glob.glob(os.path.join(POSTS_DIR, "*.json"))):
        with open(path, encoding="utf-8") as f:
            pj = json.load(f)
        eksik = [c for c in LANG_DIR if c not in pj.get("i18n", {})]
        if eksik:
            raise SystemExit(f"HATA {os.path.basename(path)}: eksik dil {eksik} — tr+en zorunlu")
        posts.append(pj)
    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts

POSTS = load_posts()

WA_SVG = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2a10 10 0 0 0-8.66 15L2 22l5.2-1.3A10 10 0 1 0 12 2zm5.47 14.13c-.23.65-1.35 1.24-1.86 1.28-.5.05-.97.23-3.27-.68-2.77-1.09-4.53-3.9-4.67-4.08-.13-.18-1.11-1.48-1.11-2.82 0-1.34.7-2 .95-2.27.25-.28.55-.35.73-.35.18 0 .37 0 .53.01.17.01.4-.06.62.48.23.55.78 1.9.85 2.04.07.14.11.3.02.48-.09.18-.13.29-.27.45-.13.16-.28.35-.4.47-.13.13-.27.28-.12.54.16.27.7 1.16 1.5 1.87 1.03.92 1.9 1.2 2.17 1.34.27.13.42.11.58-.07.16-.18.67-.78.85-1.05.18-.27.36-.22.6-.13.25.09 1.57.74 1.84.88.27.13.45.2.51.31.07.11.07.65-.16 1.3z"/></svg>'

def head_common(title, desc, canonical, lang, extra=""):
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="tr" href="{DOMAIN}/">
<link rel="alternate" hreflang="en" href="{DOMAIN}/en/">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}/">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}/img/og-cover.jpg">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E💙%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Manrope:wght@400;500;700&display=swap" rel="stylesheet">
{extra}'''

def schema(t, lang):
    biz = {
      "@context":"https://schema.org","@type":["LocalBusiness","Photograph"],
      "@id": DOMAIN+"/#business",
      "name":"Mavi Kaşif Fotoğrafçılık" if lang=="tr" else "Mavi Kaşif Photography",
      "url":DOMAIN,"image":DOMAIN+"/img/og-cover.jpg","description":t["meta_desc"],
      "telephone":"+90 553 717 52 40","email":EMAIL,"priceRange":"$$",
      "address":{"@type":"PostalAddress","addressLocality":"Göreme","addressRegion":"Nevşehir","addressCountry":"TR"},
      "geo":{"@type":"GeoCoordinates","latitude":38.6431,"longitude":34.8289},
      "sameAs":[IG,FB,PIN],
    }
    faq = {"@context":"https://schema.org","@type":"FAQPage",
      "mainEntity":[{"@type":"Question","name":f["q"],"acceptedAnswer":{"@type":"Answer","text":f["a"]}} for f in t["faqs"]]}
    return (f'<script type="application/ld+json">{json.dumps(biz,ensure_ascii=False)}</script>\n'
            f'<script type="application/ld+json">{json.dumps(faq,ensure_ascii=False)}</script>')

JS = '''<script>
const nav=document.querySelector('.nav');
addEventListener('scroll',()=>nav.classList.toggle('scrolled',scrollY>40),{passive:true});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
const burger=document.getElementById('burger'),links=document.getElementById('navlinks');
if(burger){burger.addEventListener('click',()=>links.classList.toggle('open'));
links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>links.classList.remove('open')));}
</script>'''

# ============================================================
#  BLOG — TR + EN. Yeni yazi: _src/posts/<YYYY-AA-GG>-<slug>.json
#  Kurallar ve konu sirasi: _src/KONU-HAVUZU.md
# ============================================================
BLOG_T = {
"tr": {"nav":"Blog","kicker":"Blog","title":'Kapadokya <em>rehberi</em>',
 "intro":"Dış çekim planlayan çiftler için yazdık: doğru zaman, doğru fotoğrafçı, doğru hazırlık.",
 "index_title":"Kapadokya Dış Çekim Rehberi — Mavi Kaşif Blog",
 "index_desc":"Kapadokya'da düğün, nişan ve save-the-date dış çekimi planlayan çiftler için rehberler: hangi mevsim, ne giyilir, fotoğrafçı nasıl seçilir.",
 "read":"Yazıyı okuyun","back":"← Blog'a dön","home":"Ana sayfa","published":"Yayın",
 "more":"Blog'dan diğer yazılar",
 "cta_title":"Tarihinizi konuşalım mı?",
 "cta_sub":"Seyahat tarihlerinizi yazın; o günler için gerçekçi olarak ne mümkün, açıkça söyleyelim.",
 "cta_btn":"WhatsApp'tan Yazın"},
"en": {"nav":"Journal","kicker":"Journal","title":'The Cappadocia <em>guide</em>',
 "intro":"Written for couples planning a shoot here: when to come, what to wear, and how to choose the people who will photograph your day.",
 "index_title":"Cappadocia Wedding Photoshoot Guide — Mavi Kaşif Journal",
 "index_desc":"Guides for couples planning a wedding, elopement or engagement shoot in Cappadocia: seasons, what to wear, and how to choose your photographer.",
 "read":"Read the guide","back":"← Back to the Journal","home":"Home","published":"Published",
 "more":"More from the Journal",
 "cta_title":"Shall we talk about your dates?",
 "cta_sub":"Send us the dates you already have and we'll tell you honestly what those mornings usually allow.",
 "cta_btn":"Message us on WhatsApp"},
}

def lang_base(lang):
    return "/" if lang == "tr" else f"/{LANG_DIR[lang]}/"

def blog_index_url(lang):
    return f"{DOMAIN}{lang_base(lang)}blog/"

def post_url(lang, slug):
    return f"{DOMAIN}{lang_base(lang)}blog/{slug}.html"

def blog_depth(lang):
    return "../" if lang == "tr" else "../../"

def blog_hreflangs(slug=None):
    def u(c):
        return post_url(c, slug) if slug else blog_index_url(c)
    return "\n".join(
        [f'<link rel="alternate" hreflang="x-default" href="{u("tr")}">'] +
        [f'<link rel="alternate" hreflang="{c}" href="{u(c)}">' for c in LANG_DIR])

def blog_head(lang, title, desc, canonical, image, hreflang_block, extra_ld=""):
    root = blog_depth(lang)
    head = head_common(title, desc, canonical, lang,
                       f'<link rel="stylesheet" href="{root}css/style.css">\n'
                       f'<link rel="stylesheet" href="{root}css/blog.css">\n{extra_ld}')
    # ana sayfanin sabit tr/en hreflang'lerini yazininkiyle degistir
    head = head.replace(
        f'<link rel="alternate" hreflang="tr" href="{DOMAIN}/">\n'
        f'<link rel="alternate" hreflang="en" href="{DOMAIN}/en/">\n'
        f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/">', hreflang_block)
    return head.replace(f'<meta property="og:image" content="{DOMAIN}/img/og-cover.jpg">',
                        f'<meta property="og:image" content="{DOMAIN}/img/{image}">')

def blog_chrome(lang):
    t, b = T[lang], BLOG_T[lang]
    wa = f"https://wa.me/{WA_NUM}?text=" + t["wa_text"].replace(" ", "%20")
    other = "en" if lang == "tr" else "tr"
    return f'''<header class="nav scrolled" id="top">
  <a class="brand" href="{lang_base(lang)}"><b>Mavi</b><span>Kaşif</span></a>
  <ul class="nav-links" id="navlinks">
    <li><a href="{lang_base(lang)}#paketler">{t["nav"][0]}</a></li>
    <li><a href="{lang_base(lang)}#galeri">{t["nav"][2]}</a></li>
    <li><a href="{lang_base(lang)}blog/">{b["nav"]}</a></li>
    <li><a class="nav-cta" href="{wa}" target="_blank" rel="noopener">{t["nav_cta"]}</a></li></ul>
  <div style="display:flex;gap:12px;align-items:center">
    <nav class="lang"><a href="{blog_index_url(other).replace(DOMAIN,"")}">{"EN" if lang=="tr" else "TR"}</a></nav>
    <button class="burger" id="burger" aria-label="Menu">☰</button>
  </div>
</header>'''

def blog_foot(lang):
    t, b = T[lang], BLOG_T[lang]
    wa = f"https://wa.me/{WA_NUM}?text=" + t["wa_text"].replace(" ", "%20")
    return f'''<section class="contact"><div class="wrap">
  <h2 class="contact-title">{b["cta_title"]}</h2>
  <p class="contact-sub">{b["cta_sub"]}</p>
  <div class="contact-ctas">
    <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{b["cta_btn"]}</a>
  </div>
</div></section>

<footer class="site">
  <div>{t["ft_rights"]} · Göreme, Kapadokya</div>
  <div class="foot-social"><a href="{IG}" target="_blank" rel="noopener">Instagram</a>
  <a href="{FB}" target="_blank" rel="noopener">Facebook</a></div>
</footer>

<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>
{JS}'''

def post_cards(lang, posts):
    b = BLOG_T[lang]
    return "".join(f'''<a class="blog-card reveal" href="{lang_base(lang)}blog/{p["slug"]}.html">
      <div class="blog-card-meta">{p["date"]}</div>
      <h3>{p["i18n"][lang]["title"]}</h3><p>{p["i18n"][lang]["desc"]}</p>
      <span class="blog-card-more">{b["read"]} →</span></a>''' for p in posts)

def blog_section(lang):
    """ana sayfadaki blog vitrini — artik TR ve EN ikisinde de var."""
    if not POSTS:
        return ""
    b = BLOG_T[lang]
    return f'''<section id="blog" class="reviews"><div class="wrap">
  <div class="kicker reveal">{b["kicker"]}</div>
  <h2 class="sec-title reveal">{b["title"]}</h2>
  <p class="sec-intro reveal">{b["intro"]}</p>
  <div class="blog-grid">{post_cards(lang, POSTS[:3])}</div>
</div></section>'''

def blog_index(lang):
    b = BLOG_T[lang]
    canonical = blog_index_url(lang)
    ld = {"@context":"https://schema.org","@type":"Blog","@id":canonical,
          "name":b["index_title"],"description":b["index_desc"],"inLanguage":lang,
          "publisher":{"@id":DOMAIN+"/#business"},
          "blogPost":[{"@type":"BlogPosting","headline":p["i18n"][lang]["title"],
                       "datePublished":p["date"],"url":post_url(lang,p["slug"])} for p in POSTS]}
    head = blog_head(lang, b["index_title"], b["index_desc"], canonical, "og-cover.jpg",
                     blog_hreflangs(),
                     f'<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>')
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
{head}
</head>
<body class="blog-page">
{blog_chrome(lang)}
<section class="blog-hero"><div class="wrap">
  <div class="kicker reveal">{b["kicker"]}</div>
  <h1 class="sec-title reveal">{b["title"]}</h1>
  <p class="sec-intro reveal">{b["intro"]}</p>
  <div class="blog-grid">{post_cards(lang, POSTS)}</div>
</div></section>
{blog_foot(lang)}
</body>
</html>'''

def page(lang):
    t = T[lang]
    canonical = DOMAIN + ("/" if lang == "tr" else "/en/")
    root = "" if lang == "tr" else "../"
    wa = f"https://wa.me/{WA_NUM}?text=" + t["wa_text"].replace(" ", "%20")
    nav_ids = ["paketler","deneyimler","galeri","yorumlar","hakkimizda","sss"]
    nav_html = "".join(f'<li><a href="#{i}">{n}</a></li>' for i, n in zip(nav_ids, t["nav"]))
    if POSTS:
        nav_html += f'<li><a href="{lang_base(lang)}blog/">{BLOG_T[lang]["nav"]}</a></li>'
    lhref, llabel = t["lang_link"]

    packs = []
    for i, p in enumerate(t["packs"]):
        pop = ' popular' if i == 0 else ''
        badge = f'<span class="pack-badge">{t["pk_popular"]}</span>' if i == 0 else ''
        feats = "".join(f"<li>{f}</li>" for f in p["feats"])
        packs.append(f'''<article class="pack{pop} reveal">{badge}
          <div class="pack-time">{p["time"]}</div><h3>{p["name"]}</h3>
          <div class="pack-tag">{p["tag"]}</div><ul>{feats}</ul>
          <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{t["pk_cta"]}</a></article>''')

    exps = []
    for i, e in enumerate(t["exps"]):
        exps.append(f'''<div class="exp-row reveal">
          <div class="exp-img"><img src="{root}img/{e["img"]}" alt="{e["alt"]}" loading="lazy" width="800" height="1000"></div>
          <div class="exp-body"><div class="exp-num">0{i+1}</div><h3>{e["t"]}</h3><p>{e["p"]}</p></div></div>''')

    steps = "".join(f'<div class="step reveal"><h3>{s["t"]}</h3><p>{s["p"]}</p></div>' for s in t["steps"])
    gal = "".join(f'''<figure class="gitem reveal"><img src="{root}img/{g["img"]}" alt="{g["alt"]}" loading="lazy">
      <figcaption>{g["cap"]}</figcaption></figure>''' for g in t["gallery"])
    revs = "".join(f'''<article class="rev reveal"><div class="rev-stars">★★★★★</div>
          <p>{r["txt"]}</p><footer><div class="rev-avatar">{r["name"][0]}</div>
          <div><div class="rev-name">{r["name"]}</div><div class="rev-type">{r["type"]}</div></div></footer></article>''' for r in t["reviews"])
    faqs = "".join(f'<details class="faq reveal"><summary>{f["q"]}</summary><div>{f["a"]}</div></details>' for f in t["faqs"])
    stats = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in t["stats"])

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
{head_common(t["meta_title"], t["meta_desc"], canonical, lang, f'<link rel="stylesheet" href="{root}css/style.css">')}
{schema(t, lang)}
</head>
<body>
<header class="nav" id="top">
  <a class="brand" href="{canonical}"><b>Mavi</b><span>Kaşif</span></a>
  <ul class="nav-links" id="navlinks">{nav_html}
    <li><a class="nav-cta" href="{wa}" target="_blank" rel="noopener">{t["nav_cta"]}</a></li></ul>
  <div style="display:flex;gap:14px;align-items:center">
    <nav class="lang"><a href="{lhref}">{llabel}</a></nav>
    <button class="burger" id="burger" aria-label="Menü">☰</button>
  </div>
</header>

<section class="hero">
  <div class="hero-bg"><img src="{root}img/cappadocia-valley-photoshoot.jpg" alt="{t["exps"][2]["alt"]}" fetchpriority="high"></div>
  <div class="hero-inner">
    <div class="hero-loc">{t["hero_loc"]}</div>
    <h1>{t["hero_title"]}</h1>
    <p class="hero-sub">{t["hero_sub"]}</p>
    <div class="hero-ctas">
      <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{t["hero_cta1"]}</a>
      <a class="btn btn-ghost" href="#paketler">{t["hero_cta2"]}</a>
    </div>
  </div>
  <div class="hero-scroll">{t["hero_scroll"]}</div>
</section>

<section class="packages" id="paketler"><div class="wrap">
  <div class="kicker reveal">{t["pk_kicker"]}</div>
  <h2 class="sec-title reveal">{t["pk_title"]}</h2>
  <p class="sec-intro reveal">{t["pk_intro"]}</p>
  <div class="pack-grid">{"".join(packs)}</div>
</div></section>

<section id="deneyimler"><div class="wrap">
  <div class="kicker reveal">{t["ex_kicker"]}</div>
  <h2 class="sec-title reveal">{t["ex_title"]}</h2>
  <p class="sec-intro reveal">{t["ex_intro"]}</p>
  {"".join(exps)}
</div></section>

<section class="steps"><div class="wrap">
  <div class="kicker reveal">{t["st_kicker"]}</div>
  <h2 class="sec-title reveal">{t["st_title"]}</h2>
  <div class="step-grid">{steps}</div>
</div></section>

<section id="galeri"><div class="wrap">
  <div class="kicker reveal">{t["ga_kicker"]}</div>
  <h2 class="sec-title reveal">{t["ga_title"]}</h2>
  <div class="gallery-grid">{gal}</div>
</div></section>

<section class="reviews" id="yorumlar"><div class="wrap">
  <div class="kicker reveal">{t["rv_kicker"]}</div>
  <h2 class="sec-title reveal">{t["rv_title"]}</h2>
  <div class="rev-grid">{revs}</div>
</div></section>

<section id="hakkimizda"><div class="wrap about-grid">
  <div class="about-img reveal"><img src="{root}img/photographer-cappadocia-at-work.jpg" alt="{t["ab_alt"]}" loading="lazy"></div>
  <div class="about reveal">
    <div class="kicker">{t["ab_kicker"]}</div>
    <h2 class="sec-title">{t["ab_title"]}</h2>
    <p>{t["ab_p1"]}</p><p>{t["ab_p2"]}</p>
    <div class="about-sign">{t["ab_sign"]}</div>
    <div class="stats">{stats}</div>
  </div>
</div></section>

<section id="sss"><div class="wrap">
  <div class="kicker reveal">{t["fq_kicker"]}</div>
  <h2 class="sec-title reveal">{t["fq_title"]}</h2>
  <div class="faq-list">{faqs}</div>
</div></section>

{blog_section(lang)}

<section class="contact" id="iletisim"><div class="wrap">
  <div class="kicker reveal">{t["ct_kicker"]}</div>
  <h2 class="contact-title reveal">{t["ct_title"]}</h2>
  <p class="contact-sub reveal">{t["ct_sub"]}</p>
  <div class="contact-ctas reveal">
    <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{t["ct_wa"]}</a>
    <a class="btn btn-ghost" href="{IG}" target="_blank" rel="noopener">{t["ct_ig"]}</a>
  </div>
  <div class="contact-alt reveal"><span>{t["ct_or"]}</span> <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:+{WA_NUM}">+90 553 717 52 40</a></div>
</div></section>

<footer class="site">
  <div>{t["ft_rights"]} · Göreme, Kapadokya</div>
  <div class="foot-social">
    <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
    <a href="{FB}" target="_blank" rel="noopener">Facebook</a>
    <a href="{PIN}" target="_blank" rel="noopener">Pinterest</a>
  </div>
</footer>

<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>
{JS}
</body>
</html>'''

def blog_post(lang, p):
    t, b = T[lang], BLOG_T[lang]
    i = p["i18n"][lang]
    root = blog_depth(lang)
    canonical = post_url(lang, p["slug"])
    art = {"@context":"https://schema.org","@type":"BlogPosting",
           "headline":i["title"],"description":i["desc"],
           "datePublished":p["date"],"dateModified":p.get("modified", p["date"]),
           "inLanguage":lang,"mainEntityOfPage":canonical,
           "image":f"{DOMAIN}/img/{p['image']}",
           "author":{"@type":"Organization",
                     "name":"Mavi Kaşif Fotoğrafçılık" if lang=="tr" else "Mavi Kaşif Photography"},
           "publisher":{"@id":DOMAIN+"/#business"}}
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":b["home"],"item":DOMAIN+lang_base(lang)},
        {"@type":"ListItem","position":2,"name":b["nav"],"item":blog_index_url(lang)},
        {"@type":"ListItem","position":3,"name":i["title"],"item":canonical}]}
    ld = ('<script type="application/ld+json">' + json.dumps(art, ensure_ascii=False) + '</script>\n'
          '<script type="application/ld+json">' + json.dumps(crumbs, ensure_ascii=False) + '</script>')
    head = blog_head(lang, i["title"] + " | Mavi Kaşif", i["desc"], canonical,
                     p["image"], blog_hreflangs(p["slug"]), ld)
    others = [q for q in POSTS if q["slug"] != p["slug"]][:3]
    more = (f'''<section class="blog-more"><div class="wrap">
  <div class="kicker reveal">{b["more"]}</div>
  <div class="blog-grid">{post_cards(lang, others)}</div>
</div></section>''' if others else "")
    wa = f"https://wa.me/{WA_NUM}?text=" + t["wa_text"].replace(" ", "%20")
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
{head}
</head>
<body class="blog-page">
{blog_chrome(lang)}
<article class="blog-body">
  <nav class="crumbs"><a href="{lang_base(lang)}">{b["home"]}</a> · <a href="{lang_base(lang)}blog/">{b["nav"]}</a></nav>
  <h1>{i["title"]}</h1>
  <div class="blog-meta">{b["published"]} {p["date"]}</div>
  <figure class="post-hero"><img src="{root}img/{p["image"]}" alt="{i["alt"]}" fetchpriority="high"></figure>
{i["body"]}
  <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{b["cta_btn"]}</a>
  <div><a class="post-back" href="{lang_base(lang)}blog/">{b["back"]}</a></div>
</article>
{more}
{blog_foot(lang)}
</body>
</html>'''

BLOG_CSS = """/* Blog indeksi + yazi sayfasi — mavi_build.py uretir, elle duzenleme.
   Kart/govde stilleri style.css'te zaten var; burasi yalnizca EKLER. */
.blog-page{padding-top:76px}
.blog-hero .wrap{padding-bottom:clamp(40px,6vh,72px)}
.blog-hero .sec-title{margin-bottom:14px}

/* kirinti + geri donus */
.crumbs{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-faint);
  font-weight:700;margin-bottom:18px}
.crumbs a{color:var(--ink-faint);text-decoration:none}
.crumbs a:hover{color:var(--mavi)}
.post-back{display:inline-block;margin-top:26px;color:var(--mavi);font-weight:700;
  font-size:14px;letter-spacing:.04em;text-decoration:none}
.post-back:hover{text-decoration:underline}

/* yazi basi gorseli */
.post-hero{margin:26px 0 34px;border-radius:6px;overflow:hidden;
  box-shadow:0 18px 40px rgba(35,41,70,.10)}
.post-hero img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block}

/* yazi govdesinde style.css'te olmayan ogeler */
.blog-body h3{font-size:21px;margin:26px 0 8px}
.blog-body ul,.blog-body ol{margin:0 0 18px 22px;color:var(--ink-soft)}
.blog-body li{margin-bottom:8px}
.blog-body strong{color:var(--ink);font-weight:700}
.blog-body em{font-style:italic}
.blog-body a{color:var(--mavi);border-bottom:1px solid rgba(45,74,158,.35);text-decoration:none}
.blog-body blockquote{border-left:3px solid var(--gold);padding:4px 0 4px 20px;margin:24px 0;
  font-family:var(--serif);font-style:italic;font-size:21px;color:var(--ink)}
.blog-body table{width:100%;border-collapse:collapse;margin:24px 0;font-size:15px}
.blog-body th,.blog-body td{padding:11px 12px;border-bottom:1px solid rgba(35,41,70,.12);
  text-align:left;color:var(--ink-soft)}
.blog-body th{color:var(--gold);font-weight:700;letter-spacing:.08em;
  text-transform:uppercase;font-size:12px}

.blog-more .wrap{padding-top:clamp(48px,7vh,80px)}

@media(max-width:700px){
  .blog-page{padding-top:64px}
  .blog-body{padding-top:104px}
  /* dar ekranda tablo sayfayi degil kendini kaydirsin */
  .blog-body table{display:block;overflow-x:auto;white-space:nowrap}
  .blog-body td,.blog-body th{white-space:normal;min-width:120px}
}
"""

# --- uret ---
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(page("tr"))
os.makedirs(os.path.join(OUT, "en"), exist_ok=True)
with open(os.path.join(OUT, "en", "index.html"), "w", encoding="utf-8") as f:
    f.write(page("en"))
if POSTS:
    os.makedirs(os.path.join(OUT, "css"), exist_ok=True)
    with open(os.path.join(OUT, "css", "blog.css"), "w", encoding="utf-8") as f:
        f.write(BLOG_CSS)
    for lang, d in LANG_DIR.items():
        bd = os.path.join(OUT, "blog") if lang == "tr" else os.path.join(OUT, d, "blog")
        os.makedirs(bd, exist_ok=True)
        with open(os.path.join(bd, "index.html"), "w", encoding="utf-8") as f:
            f.write(blog_index(lang))
        for p in POSTS:
            with open(os.path.join(bd, p["slug"] + ".html"), "w", encoding="utf-8") as f:
                f.write(blog_post(lang, p))
    print(f"OK sayfalar: tr, en · blog {len(POSTS)} yazi x 2 dil + 2 indeks")
else:
    print("UYARI: _src/posts/ bos — blog uretilmedi")

REDIR = '''<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={url}"><link rel="canonical" href="{url}">
<title>Yönlendiriliyor…</title></head><body><a href="{url}">Yönlendiriliyor…</a></body></html>'''
for old, new in [
    ("page1.html", DOMAIN+"/#paketler"),
    ("page2.html", DOMAIN+"/blog/dugun-fotografcisi-secerken-nelere-dikkat-etmeli.html"),
    ("page3.html", DOMAIN+"/blog/neden-kapadokyada-dugun-dis-cekimi.html")]:
    with open(os.path.join(OUT, old), "w", encoding="utf-8") as f:
        f.write(REDIR.format(url=new))
with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
    f.write(REDIR.format(url=DOMAIN+"/"))
print("OK yonlendirmeler")

alts = (f'<xhtml:link rel="alternate" hreflang="tr" href="{DOMAIN}/"/>'
        f'<xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}/en/"/>')
rows = [f"<url><loc>{DOMAIN}/</loc>{alts}<changefreq>monthly</changefreq></url>",
        f"<url><loc>{DOMAIN}/en/</loc>{alts}<changefreq>monthly</changefreq></url>"]
# blog indeksi + yazilar (tr+en, karsilikli hreflang)
for lang in LANG_DIR:
    a = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{blog_index_url(c)}"/>' for c in LANG_DIR)
    rows.append(f"<url><loc>{blog_index_url(lang)}</loc>{a}<changefreq>weekly</changefreq></url>")
for p in POSTS:
    for lang in LANG_DIR:
        a = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{post_url(c, p["slug"])}"/>' for c in LANG_DIR)
        rows.append(f'<url><loc>{post_url(lang, p["slug"])}</loc>{a}'
                    f'<lastmod>{p.get("modified", p["date"])}</lastmod><changefreq>yearly</changefreq></url>')
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>")
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print("OK sitemap+robots")
print("BITTI")
