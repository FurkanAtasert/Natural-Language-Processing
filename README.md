                                    --DESCRIPTION--
Main Functions:

Text Preprocessing:
Texts are converted to lowercase and unnecessary characters such as punctuation marks are removed. This step allows for a better comparison by focusing on the root words of the texts.


Similarity Calculation:
The Zemberek library is used to perform morphological analysis of the texts and obtain lists of words.
The similarity ratio between two texts is calculated by the ratio of the number of common words to the total number of unique words.


Finding the Most Similar Author:
The target text is compared with predefined column texts, and the author with the highest similarity ratio is determined.


Usage Instructions:
Installation of Required Library:
pip install zemberek-python


Running the Project:
python Furkan_Atasert_Zemberek_Analysis.py


Evaluating the Results:
The similarity percentage of each column text to the target text is displayed.
The most similar author and text results are printed to the screen.
This project forms a foundation for Turkish text analysis and demonstrates the usage of the Zemberek library. The similarity analysis between texts can be extended for tasks such as text classification, sentiment analysis, and other natural language processing tasks.


------------------------------------------------------------------------------------------------------------------------------


                                            --TURKISH DESCRIPTION--
                                            
Bu proje, Türkçe metinler arasındaki benzerliği analiz etmek için Zemberek Doğal Dil İşleme kütüphanesini kullanır. Metinleri ön işleme ve normalleştirme adımlarından geçirerek, bir hedef metni önceden belirlenmiş köşe yazılarıyla karşılaştırır ve en benzer yazarı belirler. Benzerlik hesaplaması için Türkçe morfolojik analiz kullanılır.


Ana İşlevler:
Metin Ön İşleme:
Metinler küçük harfe dönüştürülür ve noktalama işaretleri gibi gereksiz karakterler kaldırılır. Bu adım, metinlerin kök kelimelerine odaklanarak daha iyi bir karşılaştırma yapılmasını sağlar.


Benzerlik Hesaplama:
Zemberek kütüphanesi kullanılarak metinlerin morfolojik analizi yapılır ve kelime listeleri elde edilir.
İki metin arasındaki benzerlik oranı, ortak kelime sayısının toplam benzersiz kelime sayısına oranıyla hesaplanır.


En Benzer Yazarı Bulma:
Hedef metin, önceden tanımlanmış köşe yazılarıyla karşılaştırılır ve en yüksek benzerlik oranına sahip yazar belirlenir.


Kullanım Talimatları:
Gerekli Kütüphanenin Yüklenmesi:
pip install zemberek-python


Projenin Çalıştırılması:
python Furkan_Atasert_Zemberek_Analysis.py


Sonuçların Değerlendirilmesi:
Her köşe yazısının hedef metne olan benzerlik oranı yüzdesiyle görüntülenir.
En benzer yazar ve metin sonuçları ekrana yazdırılır.
Bu proje, Türkçe metin analizi için bir temel oluşturur ve Zemberek kütüphanesinin kullanımını gösterir. Metinler arasındaki benzerlik analizi, metin sınıflandırma, duygu analizi ve diğer doğal dil işleme görevleri için genişletilebilir.
