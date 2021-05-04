import java.util.*;
 
class RunoobTest extends GregorianCalendar {
    public static void main(String[] args) {
        try {
            // 创建 RunoobTest 对象
            RunoobTest cal = new RunoobTest();
 
            // 输出当前时间
            System.out.println("" + cal.getTime());
 
            // finalize cal
            System.out.println("Finalizing...");
            cal.finalize();
            System.out.println("Finalized.");
 
        } catch (Throwable ex) {
            ex.printStackTrace();
        }
    }
}
