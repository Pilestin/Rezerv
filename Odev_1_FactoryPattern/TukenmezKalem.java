
package Odev_1_FactoryPattern;

/**
 *
 * @author Yasin
 */
public class TukenmezKalem extends Kalem {
       
    public TukenmezKalem(int fiyat) {
        System.out.println("Tükenmez kalem üretildi.");
        this.fiyat = fiyat;
    }
    
    @Override
    public int getFiyat() {
        return this.fiyat;
    }
}
