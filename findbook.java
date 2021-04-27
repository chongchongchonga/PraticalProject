package bk;

import java.util.ArrayList;

public class findbook {
    public void findbook(ArrayList<Book> arr){
        System.out.println("id\t\t书名");
        for(int i=0 ; i<arr.size();i++){
            Book b = arr.get(i);
            System.out.println(b.getId()+"\t\t"+b.getName());

        }
    }
}
