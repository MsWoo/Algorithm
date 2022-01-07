import java.util.*;

class test{    
    public static void main(String[] args){
        
        ArrayList<Integer> intArr = new ArrayList<Integer>();
        ArrayList<Integer> intArr2 = new ArrayList<Integer>();
        int[] test = new int[5];

        // for(int i=0;i<10;i++){
        //     intArr.add(i);
        // }

        // for(int i=0;i<intArr.size();i++){
        //     if(intArr.indexOf(3) >= 0){
        //         System.out.println("gg");
        //         intArr2.add(3);
        //     }
        // }


        // // for(int i=0;i<10;i++){
        // //     System.out.println(intArr.get(i));
        // // }
        // for(int i=0;i<intArr2.size();i++){
        //     System.out.println(intArr2.get(0));
        // }

        for(int i=0;i<5;i++){
            test[i] = i;
        }
        for(int i=0;i<test.length;i++){
            System.out.println(test[i]);
        }


    }
    
}