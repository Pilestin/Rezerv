package Odev_1_FactoryPattern;
/**
 *
 * @author Yasin
 */
/* 
 *   Main java uygulamayı yönettiğimiz kısım diyebiliriz. 
 *   Buradan factory tipinde bir nesne üreteceğiz ve bu nesneye üretim yaptıracağız.
 *   Nesneye verdiğimiz bilgi doğrultusunda hangi türden yapı üreteceğine karar verilecek.
 *   Burada hatayı azaltmak ve iyi kod yazmak için tür bilgisini STRİNG değil , ENUM olarak vereceğiz.
 *   (Kaynak : Wikipedi:Factory_method_pattern sayfasından yararlanıldı.)
 */

// Kalem türlerini tutacak olan Enum yapısı
enum KalemType {
    kursun,
    pilot,
    tukenmez
}

public class Main {
    public static void main(String[] args) {
        KalemFactory factory = new KalemFactory();
        Kalem k1 = factory.kalemUret(KalemType.pilot    , 40 );
        Kalem k2 = factory.kalemUret(KalemType.kursun   , 5  );
        Kalem k3 = factory.kalemUret(KalemType.tukenmez , 14 );
        
        System.out.println( "Pilot: "  + k1.fiyat + 
                            "\nKurşun:"  + k2.fiyat + 
                            "\nTükenmez" + k3.fiyat);
              
    }
}
