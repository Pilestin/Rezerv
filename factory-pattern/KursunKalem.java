
package Odev_1_FactoryPattern;
/**
 *
 * @author Yasin
 */
public class KursunKalem extends Kalem {
    
    public KursunKalem(int fiyat){
        System.out.println("Kursun kalem üretildi.");
        this.fiyat = fiyat;
        // sonra düzelt
    }
    
    @Override
    public int getFiyat() {
        return this.fiyat;
    }   
}
