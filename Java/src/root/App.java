package root;

import org.openqa.selenium.chrome.ChromeDriver;

public class App {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "E:\\Tutorial and Teaching\\Testing\\Software Testing using Selenium\\dvivers\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();

        // Launch website
        driver.navigate().to("http://www.google.com/");

        // Click on the search text box and send value
        driver.findElement(By.id("lst-ib")).sendKeys("javatpoint tutorials");

        // Click on the search button
        driver.findElement(By.name("btnK")).click();
    }
}