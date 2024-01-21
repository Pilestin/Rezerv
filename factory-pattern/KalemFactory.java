package Odev_1_FactoryPattern;
/**
 *
 * @author Yasin
 */
public class KalemFactory {
    
    public Kalem kalemUret(KalemType tip, int kalemFiyati){
   
        // kalem tipi string yapılabilirdi. Fakat burada enum kullanmak(KalemType) daha iyi bir yol.
        // Enum ile tip kontrolünü string'e göre daha kolay bir şekilde yapabiliriz.
        if(tip == KalemType.kursun){
            return new KursunKalem(kalemFiyati);
        }
        else if(tip == KalemType.pilot){
            return new PilotKalem(kalemFiyati);
        }
        else if(tip == KalemType.tukenmez){
            return new TukenmezKalem(kalemFiyati);
        }
        else{
            System.out.println("Hatalı tür girildi.");
            return null;
        }
    }
}


