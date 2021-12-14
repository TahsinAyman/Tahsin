class MyException extends RuntimeException{}
public class Solution {

    public static void main(String[] args) {
       try{
           int a = 2;
           int b = 0;
           int ans = a / b;
       }catch (ArithmeticException e){
//           ans = 0;
       }catch (Exception exception){
           System.out.println(" inv . calc");
       }
//        System.out.println(ans);
    }
}