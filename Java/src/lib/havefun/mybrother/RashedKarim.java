package lib.havefun.mybrother;

public class RashedKarim {
    protected boolean house;
    protected String houseName;
    protected boolean family;
    private static boolean damage;

    public RashedKarim() {

    }

    public RashedKarim(boolean house, String houseName, boolean family) {
        this.house = house;
        this.houseName = houseName;
        this.family = family;
    }

    public static void Action() {
        damage = true;
        System.out.println("\nRashed Karim: *Damage\n");
    }

    protected void setDamage(boolean damage) {
        RashedKarim.damage = damage;
    }
    protected boolean getDamage() {
        return RashedKarim.damage;
    }
    public void setHouse(boolean house) {
        this.house = house;
    }
    public boolean getHouse() {
        return house;
    }
    public void setHouseName(String houseName) {
        this.houseName = houseName;
    }
    public String getHouseName() {
        return houseName;
    }
    public void setFamily(boolean family) {
        this.family = family;
    }
    public boolean getFamily() {
        return family;
    }

    @Override
    public String toString() {
        return "[Rashed Karim]\n[Family = " + family + "]\n[House = " + house + 
        "]\n[House Name = " + houseName + "]\n" + "[Damage = " + damage + "]\n";
    }
}
