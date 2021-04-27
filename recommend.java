package bk;

import java.util.ArrayList;
import java.util.Random;

public class recommend {
    public void recommend(ArrayList<Book> arr){
        int randomNumber = new Random().nextInt(arr.size());
        System.out.println("id\t\t书名");
        Book b = arr.get(randomNumber);
        System.out.println(b.getId()+"\t\t"+b.getName());
    }
}
