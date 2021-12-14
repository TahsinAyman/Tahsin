package lib;

public class Human {
    private String country;
    private String city;
    private String address;
    private String name;
    private String religion;
    private int age;
    private double height;
    private double weight;
    private String gender;

    public void setAddress(String address) {
        this.address = address;
    }
    public String getAddress() {
        return address;
    }
    public void setCity(String city) {
        this.city = city;
    }
    public String getCity() {
        return city;
    }
    public void setCountry(String country) {
        this.country = country;
    }
    public String getCountry() {
        return country;
    }
    public Human() {

    }
    public Human(String name, String religion, int age, double height, double weight, String gender) {
        this.name = name;
        this.religion = religion;
        this.age = age;
        this.height = height;
        this.weight = weight;
        this.gender = gender;
    }
    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getGender() {
        return gender;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public double getHeight() {
        return height;
    }
    public void setHeight(double height) {
        this.height = height;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getReligion() {
        return religion;
    }
    public void setReligion(String religion) {
        this.religion = religion;
    }
    public double getWeight() {
        return weight;
    }
    public void setWeight(double weight) {
        this.weight = weight;
    }

    @Override
    public String toString() {
         return "\nName: " + name + "\nReligion: " + religion
                + "\nAge: " + age + "\nGender: " + gender + "\nHeight: " + height + "\nWeight: " + weight
                + "\nAddress: " + country + ", " + city + ", " + address;
    }
}
