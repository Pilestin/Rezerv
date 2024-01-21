
package Odev_1_FactoryPattern;
/**
 *
 * @author Yasin
 */
public class PilotKalem extends Kalem {
    
    public PilotKalem(int fiyat){
        System.out.println("Pilot Kalem üretildi");
        this.fiyat = fiyat;
        
    }
    @Override
    public int getFiyat() {
        return this.fiyat;
    }
}












