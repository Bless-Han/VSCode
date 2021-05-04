/**
 * @author : bless
 * @created : 2021-03-20
**/
import java.util.Scanner;

public class Main{
  public static int MAXN = 54;
  private String[] all = new String[MAXN];
  private int cishu = 0;
  private int rnd[] = new int[MAXN];
    
  public Main(){
    Scanner in = new Scanner(System.in);
    String s = "";
    for (int i = 0; i < 4; i++){
      switch (i) {
        case 0: s = "S"; break;
        case 1: s = "H"; break;
        case 2: s = "C"; break;
        case 3: s = "D"; break;
      }
      for (int j = 0; j < 13; j++)
        all[i * 13 + j] = s + (j + 1);
    }                                                    
    all[52] = "J1";
    all[53] = "J2";

    cishu = in.nextInt();
    for (int i = 0; i < MAXN; i++){
      rnd[i] = in.nextInt();
    }
  }

  public void showCards(){
    for (int i = 0; i < all.length; i++){
      if (i != 0)
        System.out.print(" ");
      System.out.print(all[i]);
    }
  }

  public void shuffling(){
    for (int i = 0; i < cishu; i++){
      String[] temp = new String[MAXN];
      for (int j = 0; j < MAXN; j++)
        temp[rnd[j] - 1] = all[j];
      all = temp;
    }
  }

  public static void main(String[] args){
    Main m = new Main();
    m.shuffling();
    m.showCards();
  }

}
