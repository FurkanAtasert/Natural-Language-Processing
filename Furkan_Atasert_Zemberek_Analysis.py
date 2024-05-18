from typing import List
from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishTokenizer,
    TurkishMorphology,
    TurkishSentenceExtractor,
)
## İşlemlerden önce " pip install zemberek-python " ile kütüphaneyi importlayınız.
## Programı Çalıştırmak için python Furkan_Atasert_Zemberek_Analysis.py kısayolunu kullanabilirsiniz.


# Fonksiyon başlangıcı
def preprocess_text(text: str) -> str:
    # Metni küçük harfe çevir
    text = text.lower()
    
    # Metin içerisinde bulunan noktalama ve özel karakterleri kaldırma işlemi. Kelime köklerine odaklanmak için verinin temizlenmesi için gerklidir.
    text = ''.join([char for char in text if char.isalpha() or char.isspace()])
    
    return text

# İki metin arasındaki benzerliği hesaplayan fonksiyon
def calculate_similarity(text1: str, text2: str, morphology: TurkishMorphology) -> float:
    # Metinleri analiz edip kelime listelerini elde etme işlem kısmı
    tokens1 = [token.word_analysis for token in morphology.analyze_and_disambiguate(text1)]
    tokens2 = [token.word_analysis for token in morphology.analyze_and_disambiguate(text2)]
    
    # Ortak kelimeleri bul
    common_tokens = set(tokens1).intersection(set(tokens2))
    
    # Benzerlik oranını hesapla
    similarity = len(common_tokens) / (len(set(tokens1)) + len(set(tokens2)) - len(common_tokens))
    
    return similarity

# Hedef metnin en benzer metni bulan fonksiyon
def find_most_similar_text(target_text: str, texts: List[str]) -> (int, List[float]):
    # Türkçe morfoloji analizi için varsayılan ayarlarla bir morfoloji nesnesi oluşturma işlem kısmı
    morphology = TurkishMorphology.create_with_defaults()
    
    # Hedef metni ön işleme
    target_text = preprocess_text(target_text)
    
    # Tüm metinlerle benzerlikleri hesapla
    similarities = [calculate_similarity(target_text, preprocess_text(text), morphology) for text in texts]
    
    # En benzer metnin indeksini bul
    most_similar_index = similarities.index(max(similarities))
    
    return most_similar_index, similarities

########################### Aşağıda bulunan kısımda içeriği değiştirebilir ve farklı köşe yazarlarına ait eğitim verisi ekleyebilirsiniz.

# Köşe yazıları için eğitim verisi
corner_texts = [
    ("""Pandemi sonrası konut piyasası hareketli bir dönem geçirdi. Türkiye’de enflasyonun da etkisiyle ev fiyatlarında yüksek artışlar oldu. Ukrayna-Rusya savaşı ve Ortadoğu’daki huzursuzluklar da gayrimenkul sektöründe değişim yarattı. 2023 yılında Türkiye’de 35 bin 268 yabancıya konut satıldı. Bu satışların yüzde 29.94’ü Rusya vatandaşlarına yapıldı. Yabancılara yapılan konut satışının payı yüzde 2.9 oldu. 2023 yılında yabancılara yapılan konut satışlarında ilk sırayı 12 bin 702 konut satışı ile Antalya aldı.""", "Deniz Sipahi"),
    
    ("""İşçi ile işveren arasındaki iş sözleşmesinin karşılıklı anlaşarak ikale (sonlandırma sözleşmesi) ile sona erdirilmesi, işçinin işvereni ibra ettiği anlamına gelmez. İşçinin ikaleden önce doğmuş hak ve alacaklarını ortadan kaldırmaz. İkale tazminatı alan işçi eksik ödenen alacakları için talepte bulunabilir.""", "Ahmet Kıvanç"),
    
    ("""Uzun yıllardır kirliliğiyle gündeme gelen Ergene Nehri için kritik bir uyarı geldi. Su Politikaları Derneği Başkanı Dursun Yıldız, nehirdeki kirliliğin arıtma tesisleri tamamlanmasına rağmen ortadan kalkmadığını, nehre bazı noktasal kirlilik kaynaklarından deşarj yapıldığını söyledi.""", "Esra Toptaş"),
    
    ("""Zaman zaman yurtdışından örnekler veriyorum. Barselona gibi 30 yıl önce stratejik bir plan hazırlayıp uygulayan bir şehir, bugün turizmde açık ara önde koşuyor. Türkiye’de de iyi örnekler var, ancak sayıları az. O eleştirdiğiniz Barselona, Gaudi gibi önemli bir mimarın ve Picasso, Dali gibi olağanüstü sanatçıların imzalarını attığı bir şehirdi. Geçen yıllarda iyi projeler gerçekleştirdi ve bugün başarılı bir turizm destinasyonu haline geldi.""", "Rahim Ak"),
    
    ("""Ülkelerin demografik yapısı, ekonomi üzerinde oldukça belirleyicidir. Gençlerin ağırlıkta olduğu ülkelerde talep canlıdır. İç talepteki hareketlilik, şirketleri dinamik tutar. Yeni mal ve hizmet geliştirmeye dönük motivasyon artar. Gençlerin risk alma ve yeniliklere kafa yorma eğilimleri daha yüksektir. Genç toplumlardan daha fazla girişimci çıkar. Genç nüfus, işgücüne katılımı besleyerek de üretime katkı verir.""", "Nurullah Gür")
]

########################### Aşağıda bulunan kısımda içeriği değiştirebilir ve test verisini değiştirebilirsiniz.

# Test edilecek hedef metin (İçerik 5 adet yazardan farklı bir köşe yazarından gelmektedir.)
# Kök kelimelere odaklanılarak hangi yazar ile bu hedef köşe yazısının daha çok benzerlik gösterdiğini bulmak için bu tercihi yaptım.
# Aynı yazarlara ait içerikleri de test ettim fakat kişilerin köşe yazılarının içerikleri farklı olduğundan ötürü benzerlik oranında sapmalar mevcuttur.
# Bir üstte belirttiğim hatanın çözüm önerisi olarak daha uzun köşe yazıları tanımlanarak daha yakın oranlar bulabiliriz ve daha doğru sonuçlar elde edebileceğimizi düşünüyorum.

target_text = """Günümüzde çevre sorunları giderek artıyor. 
    Sürdürülebilir bir yaşam için herkesin üzerine düşeni yapması gerekmektedir."""


# En benzer metni ve benzerlik oranlarını bulma
most_similar_index, similarities = find_most_similar_text(target_text, [text[0] for text in corner_texts])
most_similar_author = corner_texts[most_similar_index][1]

# Benzerlik oranlarını ekrana yazdırma
for idx, sim in enumerate(similarities):
    print(f"{idx + 1}. köşe yazısına %{sim * 100:.2f} oranında benziyor.")

# En benzer yazarı ve metni ekrana yazdırma
print(f"\nTest edilen köşe yazısı, {most_similar_author} tarafından yazılan {most_similar_index + 1}. köşe yazısına daha fazla benzemektedir.")
