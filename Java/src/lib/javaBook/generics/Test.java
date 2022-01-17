package lib.javaBook.generics;

public class Test <T, V>{
    T code;
    V vote;
    public Test(T code, V vote){
        this.code = code;
        this.vote = vote;
    }

    public void print(){
        System.out.println(code);
    }

    @Override
    public String toString() {
        return "Test{" + "code=" + code + '}';
    }
}
